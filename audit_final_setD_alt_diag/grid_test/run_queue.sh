#!/usr/bin/env bash
# Run-queue script for Grid5/FinalGrid6 sensitivity test on cu2i2_veratrole_methoxyO_startA.
# Executes ORCA jobs sequentially; logs to /workspace/grid_test/run_queue.log.
set -uo pipefail
exec >>/workspace/grid_test/run_queue.log 2>&1

export ORCA_DIR=/workspace/orca_6_1_1
export PATH=$ORCA_DIR:$PATH
export LD_LIBRARY_PATH=$ORCA_DIR:${LD_LIBRARY_PATH:-}
export OMPI_ALLOW_RUN_AS_ROOT=1
export OMPI_ALLOW_RUN_AS_ROOT_CONFIRM=1

cd /workspace/grid_test
mkdir -p outputs scratch

run_orca() {
  local name=$1
  local inp="$name.inp"
  local out="outputs/$name.out"
  local scr="scratch/$name"
  echo
  echo "[`date -u +%H:%M:%S`] START $name"
  rm -rf "$scr"; mkdir -p "$scr"
  cp -L "$inp" "$scr/"
  for ref in $(grep -oP '\* xyzfile \S+ \S+ \K\S+' "$inp"); do
    cp -L "$ref" "$scr/"
  done
  local t0=$(date +%s)
  ( cd "$scr" && "$ORCA_DIR/orca" "$inp" > "../../$out" 2>&1 )
  local rc=$?
  local t1=$(date +%s)
  local dt=$((t1-t0))
  if grep -q 'ORCA TERMINATED NORMALLY' "$out"; then
    local fe=$(grep 'FINAL SINGLE POINT ENERGY' "$out" | tail -1 | awk '{print $NF}')
    echo "[`date -u +%H:%M:%S`] OK    $name (${dt}s) FINAL_E=$fe"
    rm -rf "$scr"
  else
    echo "[`date -u +%H:%M:%S`] FAIL  $name (${dt}s rc=$rc)"
    tail -25 "$out" | sed 's/^/    /'
    return 1
  fi
}

echo "==================================================="
echo "[`date -u +%H:%M:%S`] run_queue.sh STARTED"
echo "==================================================="

# Stage 1: optimize free veratrole at DefGrid3 (provides reference geom)
run_orca veratrole_free_opt_freq_dg3 || { echo "STAGE1_FAIL"; exit 1; }

# Extract converged veratrole geometry from output
python3 <<'PYEXTRACT'
import re, os
out = open('outputs/veratrole_free_opt_freq_dg3.out').read()
blocks = list(re.finditer(r'CARTESIAN COORDINATES \(ANGSTROEM\)\s*\n-+\s*\n((?:\s*[A-Z][a-z]?\s+-?\d+\.\d+\s+-?\d+\.\d+\s+-?\d+\.\d+\s*\n)+)', out))
block = blocks[-1].group(1)
atoms = []
for line in block.strip().split('\n'):
    parts = line.split()
    atoms.append((parts[0], float(parts[1]), float(parts[2]), float(parts[3])))
with open('veratrole_free.xyz', 'w') as f:
    f.write(f"{len(atoms)}\nveratrole_free DefGrid3-relaxed (from opt above)\n")
    for el, x, y, z in atoms:
        f.write(f"{el:>2s}  {x:>14.8f}  {y:>14.8f}  {z:>14.8f}\n")
print(f"wrote veratrole_free.xyz ({len(atoms)} atoms)")
PYEXTRACT

# Build veratrole free SP inputs at Grid5/FinalGrid6 (gas + SMD)
cat > veratrole_free_grid5_gas_sp.inp <<'INP'
! B3LYP D3BJ def2-TZVP RIJCOSX def2/J TightSCF Grid5 FinalGrid6
%pal nprocs 16 end
%maxcore 4000
* xyzfile 0 1 veratrole_free.xyz
INP
cat > veratrole_free_grid5_smd_sp.inp <<'INP'
! B3LYP D3BJ def2-TZVP RIJCOSX def2/J TightSCF Grid5 FinalGrid6 CPCM(WATER)
%pal nprocs 16 end
%maxcore 4000
%cpcm
   smd true
   SMDsolvent "water"
end
* xyzfile 0 1 veratrole_free.xyz
INP

# Stage 2: 6 SPs at Grid5/FinalGrid6
for j in cu2i2_veratrole_methoxyO_startA_grid5_gas_sp \
         cu2i2_veratrole_methoxyO_startA_grid5_smd_sp \
         cu2i2_rhombic_grid5_gas_sp \
         cu2i2_rhombic_grid5_smd_sp \
         veratrole_free_grid5_gas_sp \
         veratrole_free_grid5_smd_sp; do
  run_orca "$j" || { echo "STAGE2_FAIL_$j"; exit 1; }
done

echo
echo "==================================================="
echo "[`date -u +%H:%M:%S`] run_queue.sh COMPLETE"
echo "==================================================="
