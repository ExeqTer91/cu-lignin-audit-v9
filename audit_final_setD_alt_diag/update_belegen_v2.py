#!/usr/bin/env python3
"""
Update audit_final/BELEGEN_EVIDENCE_MATRIX.csv to reflect Task #29 V2 results:
  1. Replace row 15 (E4.3 cu2i2_veratrole_pi NOT_TESTED) with energies + verdict.
  2. Add 4 new rows under claim 3 (E3.5..E3.8) for the methoxy-O alternates.
"""
import csv
from pathlib import Path

P = Path("audit_final/BELEGEN_EVIDENCE_MATRIX.csv")
rows = list(csv.reader(open(P)))
header = rows[0]
data   = rows[1:]

# ----------------------------------------------------------------------
# (1) Update existing E4.3 row (cu2i2_veratrole_pi)
# ----------------------------------------------------------------------
# References:
#   cu2i2_rhombic    E_gas=-3876.514404  E_smd=-3876.522610
#   veratrole_free   E_gas= -461.227849  E_smd= -461.229817
#   cu2i2_veratrole_pi  E_gas=-4337.778875  E_smd=-4337.789265
#   BE_gas = (-4337.778875 + 3876.514404 + 461.227849) * 627.5095 = -22.98 kcal/mol
#   BE_smd = (-4337.789265 + 3876.522610 + 461.229817) * 627.5095 = -23.11 kcal/mol
SHA_PI_OUT  = "ef4266f6b52f9fc1b17236b3f1f2bee44444aefe237cbb53558b9b46a2ede18a"
SHA_PI_SMD  = "7fa791602d15e066f4dc0164ea78767c60dd61dcef568e4baaa649e43a591ba3"
new_E43 = [
    "4",                                                    # claim_id
    "etherified guaiacyl/veratrole π on Cu2I2",             # claim_short
    "E4.3",                                                  # evidence_id
    "OptFreq Cu2I2 + veratrole (π start)",                   # required_evidence
    "cu2i2_veratrole_pi",                                    # computation_id
    "audit_final/EXPERIMENT_JOB_INDEX.csv (Set D); audit_final/VERATROLE_OME_ALTERNATE_STARTS.csv", # source_table
    "-22.98",                                                # BE_gas_kcal
    "-23.11",                                                # BE_smd_kcal
    "η^n-arene mode; geometry not re-verified locally on rbqua6cf61ki73 (.out left in earlier pod /workspace/results_setD/, sha256-pedigreed)", # final_geometry
    "(geometry not re-extracted; energies and n_imag pedigreed via EXPERIMENT_JOB_INDEX.csv)", # contact_distances_A
    "n_imag=0 (per EXPERIMENT_JOB_INDEX)",                   # frequency_status
    "A_STRONG (BE_gas −22.98, BE_smd −23.11)",               # binding_class
    "SUPPORTED",                                             # support_status
    "/workspace/results_setD/cu2i2_veratrole_pi_opt_freq.out", # raw_file_path
    SHA_PI_OUT,                                              # raw_file_sha256
    "Veratrole-π on Cu2I2 IS a true minimum at BE_gas=-22.98, BE_smd=-23.11 (cf. guaiacol-π/phenol-π which DETACH at BE -15.5/-16.7). Veratrole's two -OMe groups stabilize the η^n-arene mode where guaiacol/phenol cannot. Updated 2026-04-30 from prior NOT_TESTED via Task #29.", # notes
]

# Find the E4.3 row by index (row 15 in CSV → index 14 in data)
e43_idx = None
for i, r in enumerate(data):
    if r[0] == "4" and r[2] == "E4.3":
        e43_idx = i; break
assert e43_idx is not None, "Could not find E4.3 row"
data[e43_idx] = new_E43
print(f"UPDATED row {e43_idx+2} (E4.3 cu2i2_veratrole_pi): NOT_TESTED → SUPPORTED  BE_gas=-22.98  BE_smd=-23.11")

# ----------------------------------------------------------------------
# (2) Insert 4 new rows under claim 3 (E3.5..E3.8) for the methoxy-O alternates.
# ----------------------------------------------------------------------
# Already-known references:
#   cu2i2_rhombic    E_gas=-3876.514404  E_smd=-3876.522610
#   cui2_anion       E_gas=-2236.113332  E_smd=-2236.178759
#   veratrole_free   E_gas= -461.227849  E_smd= -461.229817

V2_SHAS_OUT = {
    "cu2i2_veratrole_methoxyO_startA":          "a14cc98b6efe57681336694d4e0834a499812adb8cb46914f56a924801f13256",
    "cu2i2_veratrole_methoxyO_startB":          "d9301256a5c78665b7311695bdc85119ba1d4fd10773c0b1c07f542a0d4ae8bd",
    "cui2_veratrole_methoxyO_anion_startA":     "e14cedb434d71a00a4147aae57dd56b7db1be57348ba3c5c79b47357db464ef9",
    "cui2_veratrole_methoxyO_anion_startB":     "b2a5bb4424890e42806ada39f5345d4332b99a482faa488143e68397c2602836",
}

V2_RESULTS = [
    # (eid, comp_id, BE_gas, BE_smd, geom, contacts, freq, bclass, support, notes)
    ("E3.5", "cu2i2_veratrole_methoxyO_startA",
     "-26.82", "-26.24",
     "bidentate κ²-O,O methoxy chelate",
     "Cu-O(methoxy) 2.203, 2.203 Å (both); Cu-C(arene) 3.00 Å closest",
     "n_imag=0; lowest=12.4 cm⁻¹",
     "A_STRONG (BE_gas -26.82, BE_smd -26.24)",
     "SUPPORTED",
     "Cu2I2 + veratrole bidentate-OMe seed (Task #29 V2 startA): NEW true minimum more binding than the π-mode (E4.3 -22.98). Two -OMe groups in 1,2-positions allow chelation; bidentate Cu-O at 2.20 Å each. Re-opens claim 3 for VERATROLE on neutral Cu2I2: methoxy-O IS productive in bidentate geometry."),
    ("E3.6", "cu2i2_veratrole_methoxyO_startB",
     "+28.07", "+22.73",
     "single-OMe + π-arene mixed mode",
     "Cu-O 2.642, 3.328 Å; Cu-C 1.93 Å (strong η¹-aryl)",
     "n_imag=0; lowest=22.0 cm⁻¹",
     "C_METASTABLE_CONTACT (BE_gas +28.07, BE_smd +22.73)",
     "PARTIALLY_SUPPORTED",
     "Cu2I2 + veratrole tilted single-OMe seed (Task #29 V2 startB): metastable, mode-mixes with η¹-aryl. Endothermic vs separated reactants (+28/+23). Distinct local minimum, not the global one."),
    ("E3.7", "cui2_veratrole_methoxyO_anion_startA",
     "+49.28", "+53.60",
     "outer-sphere η²-arene drift (ligand pushed away by linear [CuI2]⁻)",
     "Cu-O 3.697, 5.364 Å (no Cu-O contact); Cu-C 3.214 Å (weak); I-Cu-I 173.2°",
     "n_imag=0; lowest=22.6 cm⁻¹",
     "C_METASTABLE_CONTACT / NEAR_NON_BINDING (BE_gas +49.28, BE_smd +53.60)",
     "CONFIRMS_E3.4_AT_VERATROLE",
     "[CuI2]⁻ + veratrole long-distance methoxy seed (Task #29 V2 startA): linear [CuI2]⁻ unable to bend; ligand drifts to outer sphere with weak η²-arene only. Endothermic ~+49 to +54 kcal/mol. Confirms E3.4 verdict at the veratrole substrate."),
    ("E3.8", "cui2_veratrole_methoxyO_anion_startB",
     "+55.20", "+47.93",
     "single-OMe + η¹-aryl mixed mode (cluster bent to 124° I-Cu-I)",
     "Cu-O 2.692 Å (held); Cu-C 1.94 Å (strong η¹-aryl); I-Cu-I 124.4° (cluster bent)",
     "n_imag=0; lowest=29.0 cm⁻¹",
     "C_METASTABLE_CONTACT (BE_gas +55.20, BE_smd +47.93)",
     "CONFIRMS_E3.4_AT_VERATROLE",
     "[CuI2]⁻ + veratrole rotated 180° methoxy seed (Task #29 V2 startB): reproduces original cu/i2_veratrole_methoxyO_anion result (E_gas within 0.4 mEh). Endothermic ~+55/+48 kcal/mol. Confirms methoxy-O does not bind the iodide-saturated anion regardless of starting orientation."),
]

# Build new rows in the BELEGEN format
def make_row(eid, comp, be_g, be_s, geom, contacts, freq, bclass, support, notes):
    raw_path = f"/root/orca_calc_setD_alt/logs/{comp}_restart_v2_opt_freq.out (pod rbqua6cf61ki73)"
    return [
        "3",                                          # claim_id
        "methoxy-O is productive anchoring",          # claim_short
        eid,                                          # evidence_id
        f"OptFreq+SMD-SP {comp} (Task #29 V2 alternate-start)",
        comp,                                         # computation_id
        "audit_final/VERATROLE_OME_ALTERNATE_STARTS.csv; audit_final/BINDING_SURVIVAL_TABLE_setD_alt_v2.csv; audit_final_setD_alt_diag/setD_alt_v2_analysis.json",
        be_g,
        be_s,
        geom,
        contacts,
        freq,
        bclass,
        support,
        raw_path,
        V2_SHAS_OUT[comp],
        notes,
    ]

new_e3_rows = [make_row(*v) for v in V2_RESULTS]

# Insert these 4 rows after the existing E3.4 row (so they appear within claim 3 block)
e34_idx = None
for i, r in enumerate(data):
    if r[0] == "3" and r[2] == "E3.4":
        e34_idx = i; break
assert e34_idx is not None
data = data[:e34_idx+1] + new_e3_rows + data[e34_idx+1:]
print(f"INSERTED 4 new rows after E3.4 row (E3.5..E3.8 for V2 methoxy-O alternates).")

# ----------------------------------------------------------------------
# Write back
# ----------------------------------------------------------------------
with open(P, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(header)
    for r in data: w.writerow(r)
print(f"WROTE  {P}  ({len(data)} data rows)")
