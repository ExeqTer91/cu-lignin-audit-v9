#!/usr/bin/env python3
"""Build the 4 Task-29 deliverable CSVs from setD_alt_v2_analysis.json."""
import csv, json
from pathlib import Path

ROOT = Path(".")
SRC  = ROOT / "audit_final_setD_alt_diag" / "setD_alt_v2_analysis.json"
OUT  = ROOT / "audit_final"

with open(SRC) as f:
    data = json.load(f)

# ----------------------------------------------------------------------
# 1. VERATROLE_OME_ALTERNATE_STARTS.csv  (reviewer-format main table)
# ----------------------------------------------------------------------
rows1 = []
for s in data["species"]:
    job_id = s["species"]
    restart_id = "v2_DefGrid3_TightOpt_MaxIter200_Trust0.1"
    opt_converged = "yes" if s["opt_hurray"] and s["opt_term_normal"] else "no"
    rows1.append({
        "job_id":            job_id,
        "restart_id":        restart_id,
        "opt_converged":     opt_converged,
        "cycles":            s["opt_cycles"],
        "final_energy_Eh":   f"{s['E_gas_Eh']:.6f}",
        "freq_done":         "yes" if s["n_imag"] is not None else "no",
        "n_imag":            s["n_imag"],
        "lowest_freq_cm1":   f"{s['lowest_freq_cm1']:.2f}" if s["lowest_freq_cm1"] is not None else "",
        "smd_done":          "yes" if s["smd_term_normal"] else "no",
        "smd_energy_Eh":     f"{s['E_smd_Eh']:.6f}" if s["E_smd_Eh"] is not None else "",
        "BE_gas_kcal":       f"{s['BE_gas_kcal']:+.2f}",
        "BE_smd_kcal":       f"{s['BE_smd_kcal']:+.2f}",
        "final_mode":        ("bidentate_OMe_chelate" if (len(s["cu_O_dists_final_top3_A"])>=2 and s["cu_O_dists_final_top3_A"][0]<2.5 and s["cu_O_dists_final_top3_A"][1]<2.5)
                              else ("mono_OMe_with_pi_contact" if (len(s["cu_O_dists_final_top3_A"])>=1 and s["cu_O_dists_final_top3_A"][0]<3.0 and len(s["cu_C_dists_final_top3_A"])>=1 and s["cu_C_dists_final_top3_A"][0]<3.0)
                                    else ("outer_sphere_pi_only" if (len(s["cu_C_dists_final_top3_A"])>=1 and s["cu_C_dists_final_top3_A"][0]<3.5 and (len(s["cu_O_dists_final_top3_A"])==0 or s["cu_O_dists_final_top3_A"][0]>=3.0))
                                          else "single_OMe_only"))),
        "binding_class":     s["class_final_conservative"],
        "valid_for_final_csv": "yes" if (s["opt_term_normal"] and s["opt_hurray"] and s["smd_term_normal"] and s["n_imag"]==0) else "no",
    })

with open(OUT / "VERATROLE_OME_ALTERNATE_STARTS.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows1[0].keys()))
    w.writeheader()
    for r in rows1: w.writerow(r)
print(f"WROTE  audit_final/VERATROLE_OME_ALTERNATE_STARTS.csv  ({len(rows1)} rows)")

# ----------------------------------------------------------------------
# 2. GRID_SENSITIVITY_STATUS.csv  (high-grid SPs not yet run)
# ----------------------------------------------------------------------
rows2 = []
for s in data["species"]:
    rows2.append({
        "species":      s["species"],
        "defgrid3_E_gas_Eh":  f"{s['E_gas_Eh']:.6f}",
        "defgrid3_E_smd_Eh":  f"{s['E_smd_Eh']:.6f}" if s["E_smd_Eh"] is not None else "",
        "highgrid_E_gas_Eh":  "",
        "highgrid_E_smd_Eh":  "",
        "delta_mEh_gas":      "",
        "delta_mEh_smd":      "",
        "status":             "NOT_RUN_TIME_BUDGET_PHASE3_OPTIONAL",
        "note":               "Phase 2 high-grid (Grid 6/FinalGrid 7) deferred per user instruction 2026-04-30T~10:00Z; DefGrid3 energies are accepted as the final-table values per reviewer's manuscript-safe phrasing.",
    })
with open(OUT / "GRID_SENSITIVITY_STATUS.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows2[0].keys()))
    w.writeheader()
    for r in rows2: w.writerow(r)
print(f"WROTE  audit_final/GRID_SENSITIVITY_STATUS.csv  ({len(rows2)} rows)")

# ----------------------------------------------------------------------
# 3. BINDING_SURVIVAL_TABLE.csv  (geometry-survival classification)
# ----------------------------------------------------------------------
# Update: this file already exists with original Set D rows. We APPEND
# the 4 alternate-start rows; do not overwrite the existing.
existing = OUT / "BINDING_SURVIVAL_TABLE.csv"
existing_rows = []
existing_fields = None
if existing.exists():
    with open(existing) as f:
        r = csv.DictReader(f)
        existing_fields = r.fieldnames
        existing_rows = list(r)

new_rows = []
for s in data["species"]:
    cu_o_init = s["cu_O_dists_init_top3_A"][0] if s["cu_O_dists_init_top3_A"] else None
    cu_o_final = s["cu_O_dists_final_top3_A"][0] if s["cu_O_dists_final_top3_A"] else None
    cu_c_final = s["cu_C_dists_final_top3_A"][0] if s["cu_C_dists_final_top3_A"] else None
    n_o_bonded = sum(1 for d in s["cu_O_dists_final_top3_A"] if d < 2.5)
    final_mode_class = (
        "bidentate_OMe_chelate" if (cu_o_final is not None and cu_o_final < 2.5 and n_o_bonded >= 2) else
        "mono_OMe_with_pi_contact" if (cu_o_final is not None and cu_o_final < 3.0 and cu_c_final is not None and cu_c_final < 3.0) else
        "single_OMe_only" if (cu_o_final is not None and cu_o_final < 3.0) else
        "outer_sphere_pi_only" if (cu_c_final is not None and cu_c_final < 3.5) else
        "detached"
    )
    ligand_attached = "yes" if final_mode_class != "detached" else "no"
    new_rows.append({
        "species":               s["species"],
        "set_id":                "setD_alt_v2",
        "Cu_O_distance_initial_A": f"{cu_o_init:.3f}" if cu_o_init is not None else "",
        "Cu_O_distance_final_A":   f"{cu_o_final:.3f}" if cu_o_final is not None else "",
        "Cu_C_distance_final_A":   f"{cu_c_final:.3f}" if cu_c_final is not None else "",
        "n_o_bonded_lt_2.5A":     n_o_bonded,
        "final_mode_class":       final_mode_class,
        "ligand_attached_yes_no": ligand_attached,
        "binding_class":          s["class_final_conservative"],
        "BE_gas_kcal":            f"{s['BE_gas_kcal']:+.2f}",
        "BE_smd_kcal":            f"{s['BE_smd_kcal']:+.2f}",
    })

# Write new table (sidecar — keep original BINDING_SURVIVAL_TABLE.csv untouched
# until Task #28 absorbs the new minima)
sidecar = OUT / "BINDING_SURVIVAL_TABLE_setD_alt_v2.csv"
with open(sidecar, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(new_rows[0].keys()))
    w.writeheader()
    for r in new_rows: w.writerow(r)
print(f"WROTE  audit_final/BINDING_SURVIVAL_TABLE_setD_alt_v2.csv  ({len(new_rows)} rows; sidecar — Task #28 will reconcile with master)")

# ----------------------------------------------------------------------
# 4. EXPERIMENT_STATUS.txt — append provenance block
# ----------------------------------------------------------------------
status = OUT / "EXPERIMENT_STATUS.txt"
existing_text = status.read_text() if status.exists() else ""
block = "\n\n" + "="*78 + "\n"
block += "Task #29 — veratrole methoxy-O alternate starts — V2 RESTART (2026-04-30)\n"
block += "="*78 + "\n"
block += "Pod: rbqua6cf61ki73 @ 154.54.102.26:10598 (orca-dft-v9-migration)\n"
block += "Level: B3LYP-D3BJ/def2-TZVP RIJCOSX def2/J TightSCF TightOpt DefGrid3\n"
block += "         + %geom MaxIter 200 Trust 0.1 + %scf MaxIter 200\n"
block += "SMD: B3LYP-D3BJ/def2-TZVP RIJCOSX def2/J TightSCF DefGrid3 SP, CPCM(SMD,water)\n"
block += "\n"
block += "v2 opt+freq launched 2026-04-30T02:50:26Z  (NO_TIMEOUT orchestrator)\n"
block += "v2 opt+freq all 4 finished by  2026-04-30T09:23:48Z  (~6h 33m wall)\n"
block += "v2 SMD-SPs    launched 2026-04-30T09:43:19Z  (manual sequential — orchestrator\n"
block += "                                              had false-negative HURRAY-string bug;\n"
block += "                                              see audit_final_setD_alt_diag/INCIDENT_t09-24Z_orchestrator_HURRAY_false_BAD.md)\n"
block += "v2 SMD-SPs    all 4 finished by  2026-04-30T09:49:21Z  (~6m wall, sequential)\n"
block += "\n"
block += "5-gate validation (TERM_NORMALLY ∧ HURRAY ∧ FINAL_E ∧ VIB_BLOCK ∧ n_imag=0):\n"
for s in data["species"]:
    pass5 = (s["opt_term_normal"] and s["opt_hurray"] and s["E_gas_Eh"] is not None
             and s["n_imag"] == 0 and s["smd_term_normal"])
    block += f"  {s['species']:50s}  5/5={pass5}  n_imag={s['n_imag']}  lowest_cm-1={s['lowest_freq_cm1']:.1f}\n"
block += "\n"
block += "BE summary (gas, SMD; kcal/mol):\n"
for s in data["species"]:
    block += f"  {s['species']:50s}  BE_gas={s['BE_gas_kcal']:+8.2f}  BE_smd={s['BE_smd_kcal']:+8.2f}  class={s['class_final_conservative']}\n"
block += "\n"
block += "References (Set A/D ORCA 6.1.1 DefGrid3, sha256-pedigreed in EXPERIMENT_RAW_PROVENANCE.csv):\n"
block += "  cu2i2_rhombic    E_gas=-3876.514404  E_smd=-3876.522610\n"
block += "  cui2_anion       E_gas=-2236.113332  E_smd=-2236.178759\n"
block += "  veratrole_free   E_gas= -461.227849  E_smd= -461.229817\n"
block += "\n"
block += "Phase 2 (high-grid Grid 6 / FinalGrid 7 sensitivity SPs): NOT RUN — deferred per\n"
block += "  user instruction 2026-04-30T~10:00Z (DefGrid3 accepted as final-table values).\n"
block += "  GRID_SENSITIVITY_STATUS.csv records all 4 species as NOT_RUN_TIME_BUDGET_PHASE3_OPTIONAL.\n"
status.write_text(existing_text + block)
print(f"APPENDED  audit_final/EXPERIMENT_STATUS.txt  (+{len(block)} chars)")

print()
print("=" * 60)
print("Files written:")
for fn in ["VERATROLE_OME_ALTERNATE_STARTS.csv",
           "GRID_SENSITIVITY_STATUS.csv",
           "BINDING_SURVIVAL_TABLE_setD_alt_v2.csv",
           "EXPERIMENT_STATUS.txt"]:
    p = OUT / fn
    print(f"  {fn}  ({p.stat().st_size} bytes)")
