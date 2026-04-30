"""
Build all ORCA inputs for Grid5/FinalGrid6 sensitivity test on
cu2i2_veratrole_methoxyO_startA (V2 bidentate kappa-2-O,O complex).

Geometries:
  - complex: from setD_alt_v2_analysis.json (V2 DefGrid3-relaxed)
  - cu2i2_rhombic: from local results/tier_b/cu2i2_rhombic_opt_freq.out (DefGrid3-relaxed)
  - veratrole_free: must be re-optimized first at DefGrid3 (no local copy survives)

Outputs:
  Stage 1 (run first): veratrole_free_opt_freq_dg3.inp  (~5-10 min)
  Stage 2 (after stage 1, can run in parallel):
    cu2i2_veratrole_methoxyO_startA_grid5_gas_sp.inp
    cu2i2_veratrole_methoxyO_startA_grid5_smd_sp.inp
    cu2i2_rhombic_grid5_gas_sp.inp
    cu2i2_rhombic_grid5_smd_sp.inp
    veratrole_free_grid5_gas_sp.inp        (built after stage 1)
    veratrole_free_grid5_smd_sp.inp        (built after stage 1)
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
INP = os.path.join(ROOT, 'inputs')
os.makedirs(INP, exist_ok=True)

def write_xyz(path, atoms, comment=""):
    with open(path, 'w') as f:
        f.write(f"{len(atoms)}\n{comment}\n")
        for el, x, y, z in atoms:
            f.write(f"{el:>2s}  {x:>14.8f}  {y:>14.8f}  {z:>14.8f}\n")

def extract_final_xyz_from_orca_out(path):
    """Parse converged geometry from an ORCA opt output (last CARTESIAN COORDINATES (ANGSTROEM) block)."""
    with open(path) as f:
        text = f.read()
    blocks = list(re.finditer(r'CARTESIAN COORDINATES \(ANGSTROEM\)\s*\n-+\s*\n((?:\s*[A-Z][a-z]?\s+-?\d+\.\d+\s+-?\d+\.\d+\s+-?\d+\.\d+\s*\n)+)', text))
    if not blocks:
        raise RuntimeError(f"No coord block in {path}")
    block = blocks[-1].group(1)
    atoms = []
    for line in block.strip().split('\n'):
        parts = line.split()
        atoms.append((parts[0], float(parts[1]), float(parts[2]), float(parts[3])))
    return atoms

# ------------------ Complex ------------------
v2 = json.load(open(os.path.join(os.path.dirname(ROOT), 'setD_alt_v2_analysis.json')))
sa = next(s for s in v2['species'] if s['species']=='cu2i2_veratrole_methoxyO_startA')
complex_atoms = [(el, float(x), float(y), float(z)) for el, x, y, z in sa['final_xyz']]
print(f"complex: {len(complex_atoms)} atoms")
write_xyz(os.path.join(INP, 'cu2i2_veratrole_methoxyO_startA.xyz'), complex_atoms,
          "V2 DefGrid3-relaxed (from setD_alt_v2_analysis.json)")

# ------------------ cu2i2_rhombic ------------------
RHOMBIC = '../../results/tier_b/cu2i2_rhombic_opt_freq.out'
RHOMBIC_FULL = os.path.normpath(os.path.join(ROOT, RHOMBIC))
print(f"rhombic source: {RHOMBIC_FULL} (exists={os.path.exists(RHOMBIC_FULL)})")
rhombic_atoms = extract_final_xyz_from_orca_out(RHOMBIC_FULL)
print(f"rhombic: {len(rhombic_atoms)} atoms")
write_xyz(os.path.join(INP, 'cu2i2_rhombic.xyz'), rhombic_atoms,
          "DefGrid3-relaxed (from results/tier_b/cu2i2_rhombic_opt_freq.out)")

# ------------------ veratrole_free seed (rough planar 1,2-dimethoxybenzene) ------------------
# Build a chemically sensible seed (planar ring + sp3 OMe groups). Bond lengths/angles approximate;
# DefGrid3 opt will relax to true minimum.
# Ring atoms (z=0): standard benzene with two OMe substituents at 1,2 positions.
# Coords roughly correct; we only need a starting geometry for opt.
vf_seed = [
    ('C',  1.40000,  0.00000, 0.00000),  # C1 (bears OMe)
    ('C',  0.70000,  1.21244, 0.00000),  # C2 (bears OMe)
    ('C', -0.70000,  1.21244, 0.00000),  # C3 - H
    ('C', -1.40000,  0.00000, 0.00000),  # C4 - H
    ('C', -0.70000, -1.21244, 0.00000),  # C5 - H
    ('C',  0.70000, -1.21244, 0.00000),  # C6 - H
    ('H', -1.24000,  2.16244, 0.00000),  # C3-H
    ('H', -2.48000,  0.00000, 0.00000),  # C4-H
    ('H', -1.24000, -2.16244, 0.00000),  # C5-H
    ('H',  1.24000, -2.16244, 0.00000),  # C6-H
    ('O',  2.78000,  0.00000, 0.00000),  # O1
    ('O',  1.39000,  2.41244, 0.00000),  # O2
    ('C',  3.50000,  1.20000, 0.00000),  # OMe-C on O1
    ('C',  2.50000,  3.40000, 0.00000),  # OMe-C on O2
    ('H',  3.30000,  1.78000, 0.90000),
    ('H',  3.30000,  1.78000,-0.90000),
    ('H',  4.55000,  0.95000, 0.00000),
    ('H',  2.30000,  3.98000, 0.90000),
    ('H',  2.30000,  3.98000,-0.90000),
    ('H',  3.55000,  3.18000, 0.00000),
]
print(f"veratrole seed: {len(vf_seed)} atoms (expect 20: C8H10O2)")
write_xyz(os.path.join(INP, 'veratrole_free_seed.xyz'), vf_seed,
          "veratrole (1,2-dimethoxybenzene) seed - planar ring approx, requires opt")

# ------------------ ORCA inputs ------------------
HEADER_OPT_DG3 = """! B3LYP D3BJ def2-TZVP RIJCOSX def2/J TightSCF Opt Freq
%pal nprocs 16 end
%maxcore 4000
* xyzfile {chrg} {mult} {xyzfile}
"""

HEADER_SP_GRID5 = """! B3LYP D3BJ def2-TZVP RIJCOSX def2/J TightSCF Grid5 FinalGrid6
%pal nprocs 16 end
%maxcore 4000
* xyzfile {chrg} {mult} {xyzfile}
"""

HEADER_SP_SMD = """! B3LYP D3BJ def2-TZVP RIJCOSX def2/J TightSCF Grid5 FinalGrid6 CPCM(WATER)
%pal nprocs 16 end
%maxcore 4000
%cpcm
   smd true
   SMDsolvent "water"
end
* xyzfile {chrg} {mult} {xyzfile}
"""

JOBS = [
    # Stage 1 (must run first to get free veratrole geometry)
    ('veratrole_free_opt_freq_dg3', HEADER_OPT_DG3, 0, 1, 'veratrole_free_seed.xyz'),
    # Stage 2 (run in parallel after Stage 1 OR right away for non-veratrole-free SPs)
    ('cu2i2_veratrole_methoxyO_startA_grid5_gas_sp', HEADER_SP_GRID5, 0, 1,
     'cu2i2_veratrole_methoxyO_startA.xyz'),
    ('cu2i2_veratrole_methoxyO_startA_grid5_smd_sp', HEADER_SP_SMD,    0, 1,
     'cu2i2_veratrole_methoxyO_startA.xyz'),
    ('cu2i2_rhombic_grid5_gas_sp', HEADER_SP_GRID5, 0, 1, 'cu2i2_rhombic.xyz'),
    ('cu2i2_rhombic_grid5_smd_sp', HEADER_SP_SMD,    0, 1, 'cu2i2_rhombic.xyz'),
    # veratrole_free SPs are built later via build_veratrole_sps.py
]

for name, hdr, chrg, mult, xyz in JOBS:
    inp = os.path.join(INP, f"{name}.inp")
    with open(inp, 'w') as f:
        f.write(hdr.format(chrg=chrg, mult=mult, xyzfile=xyz))
    print(f"  wrote {name}.inp")

print("DONE - stage 1 + stage 2(non-veratrole) inputs ready")
