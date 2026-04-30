#!/usr/bin/env python3
"""
Propagate Task #29 V2 alternate-start findings into the three summary tables:
  - audit_final/CLAIM_SUPPORT_STATUS.csv  (claim 3, claim 4)
  - audit_final/MECHANISM_VERDICT_TABLE.csv (M3, M4)
  - audit_final/SITE_OCCUPANCY_TABLE.csv  (add 4 V2 species rows)

Run from repo root:  python3 audit_final_setD_alt_diag/propagate_v2_to_summary_tables.py
"""
import csv, pathlib, shutil, datetime

ROOT = pathlib.Path(__file__).resolve().parents[1] / "audit_final"
STAMP = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

def backup(p):
    bk = p.with_suffix(p.suffix + f".bak_{STAMP}")
    shutil.copy2(p, bk)
    return bk

def read_csv(p):
    with open(p, newline="") as f:
        r = csv.reader(f)
        rows = list(r)
    return rows[0], rows[1:]

def write_csv(p, header, rows):
    with open(p, "w", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        w.writerow(header)
        for row in rows:
            w.writerow(row)

# ---------------- CLAIM_SUPPORT_STATUS.csv ---------------------------------
csp = ROOT / "CLAIM_SUPPORT_STATUS.csv"
backup(csp)
hdr, rows = read_csv(csp)
# columns: claim_id, claim_text, n_evidence_rows, n_supported, n_partially_supported,
#          n_contradicted, n_not_tested, n_invalidated_geometry, n_invalidated_energetics,
#          n_needs_experimental, final_status, key_data_points, scope_limitations, recommended_validation
new_rows = []
for r in rows:
    if r[0] == "3":
        # was: 4 rows / 1 supp / 1 partial / 0 contra / 0 not_tested / 0 invalid_geom / 2 invalid_energ / 0 needs_exp; PARTIALLY_SUPPORTED
        # Task #29 added E3.5 SUPPORTED, E3.6 PARTIALLY_SUPPORTED, E3.7 CONFIRMS_E3.4 (=PARTIAL),
        # E3.8 CONFIRMS_E3.4 (=PARTIAL). Total now: 8 rows; supp=2 (E3.1 cu_anisole + E3.5 cu2i2_v_OO);
        # partial=4 (E3.2 cui_guaiacol + E3.6 + E3.7 + E3.8); invalid_energ=2 (E3.3 cu2i2_g_OMe + E3.4 cui2_g_OMe).
        r[2] = "8"     # n_evidence_rows
        r[3] = "2"     # n_supported
        r[4] = "4"     # n_partially_supported
        r[5] = "0"     # n_contradicted
        r[6] = "0"     # n_not_tested
        r[7] = "0"     # n_invalidated_geometry
        r[8] = "2"     # n_invalidated_energetics  (unchanged: E3.3 + E3.4 SCF artifacts)
        r[9] = "0"     # n_needs_experimental
        r[10] = "PARTIALLY_SUPPORTED (state-dependent: productive on neutral Cu2I2 in bidentate kappa^2-O,O geometry; nonproductive on iodide-saturated [CuI2]-)"
        r[11] = (
            "Productive at naked-Cu+ (cu_anisole_methoxyO BE_gas -48.78, BE_smd -20.54, TRUE_MIN). "
            "Weak but real at CuI (cui_guaiacol_methoxyO -14.23, TRUE_MIN; weakest O-donor). "
            "Non-physical at Cu2I2 and [CuI2]- in original Set D (BE +172.67 / +173.15; FAILED_SCF_STATE / SCF artifact). "
            "TASK #29 V2 RESULT: cu2i2_veratrole_methoxyO_startA reveals a TRUE bidentate kappa^2-O,O methoxy chelate "
            "at BE_gas -26.82, BE_smd -26.24 kcal/mol (both Cu-O = 2.203 A, n_imag=0). This is more binding than the "
            "veratrole eta^n-arene pi-mode on Cu2I2 (E4.3, BE_smd -23.11). [CuI2]- alternate starts (E3.7, E3.8) "
            "remain endothermic (+48 to +55 kcal/mol), confirming the iodide-saturated anion rejects methoxy-O regardless "
            "of starting orientation."
        )
        r[12] = (
            "Methoxy-O productivity is STATE-DEPENDENT: TRUE on neutral Cu2I2 when geometry permits adjacent O,O chelation; "
            "FALSE on the iodide-saturated [CuI2]- regardless of seed. Single mono-OMe contacts on Cu2I2 (E3.6) remain metastable. "
            "Bidentate basin around startA needs rotamer/perturbation scan to confirm it is the global minimum; one Phase-2 high-grid "
            "single-point on startA is recommended to rule out a DefGrid3 artifact (deferred at 2026-04-30T~10:00Z; pending follow-up #3)."
        )
        r[13] = (
            "Already done: 4 alternate-start opt+freq + 4 SMD-SP at B3LYP-D3BJ/def2-TZVP DefGrid3 (Task #29 V2). "
            "Recommended: (a) 3-4 rotamer/perturbation opt+freq seeds around the cu2i2 bidentate-OMe basin; "
            "(b) one Grid5/FinalGrid6 single-point on cu2i2_veratrole_methoxyO_startA to confirm the -26 kcal/mol BE survives a tighter grid."
        )
    elif r[0] == "4":
        # was: 3 rows / 0 supp / 0 partial / 2 contra / 1 not_tested; CONTRADICTED (with veratrole leg pending)
        # E4.3 (cu2i2_veratrole_pi) is now SUPPORTED; veratrole-pi binds at -22.98/-23.11 even though guaiacol/phenol-pi collapse.
        # Plus the new bidentate finding (E3.5) opens a SECOND productive channel on the same neutral-Cu2I2 substrate.
        r[2] = "3"     # n_evidence_rows  (unchanged; E3.5 lives under claim 3)
        r[3] = "1"     # n_supported  (E4.3 promoted)
        r[4] = "0"     # n_partially_supported
        r[5] = "2"     # n_contradicted (guaiacol-pi, phenol-pi still detached)
        r[6] = "0"     # n_not_tested  (veratrole-pi now done)
        r[7] = "0"     # n_invalidated_geometry
        r[8] = "0"     # n_invalidated_energetics
        r[9] = "0"     # n_needs_experimental
        r[10] = "PARTIALLY_SUPPORTED (substrate-dependent; veratrole binds via pi, guaiacol/phenol detach)"
        r[11] = (
            "cu2i2_guaiacol_pi: COLLAPSED_TO_DETACHED, BE_gas = -15.53, Cu-O >= 3.75 A. "
            "cu2i2_phenol_pi: COLLAPSED_TO_DETACHED, BE_gas = -16.73, Cu-O 4.76 A. "
            "cu2i2_veratrole_pi: TRUE MINIMUM (E4.3), BE_gas = -22.98, BE_smd = -23.11; the two methoxy substituents stabilise the eta^n-arene mode "
            "where guaiacol/phenol cannot. TASK #29 V2 ALSO reveals a SECOND productive channel on the SAME complex: a bidentate "
            "kappa^2-O,O methoxy chelate at BE_smd = -26.24 (E3.5; logged under claim 3 but mechanistically dual-mode with the pi channel). "
            "Veratrole/etherified guaiacyl on neutral Cu2I2 therefore supports DUAL-MODE anchoring: pi (-23.1) and bidentate O,O (-26.2)."
        )
        r[12] = (
            "Substrate scope is small: pi-mode tested only for guaiacol, phenol, and veratrole. Free-phenolic substrates (guaiacol, phenol) "
            "do not retain pi contact; etherified veratrole does. No other etherified or beta-O-4 fragments tested. Manuscript wording must "
            "say 'etherified guaiacyl-like motifs (veratrole proxy) bind via pi on neutral Cu2I2', not 'all aromatic substrates bind via pi on Cu2I2'."
        )
        r[13] = (
            "Already done: cu2i2_veratrole_pi opt+freq + SMD-SP and the V2 alternate-start audit (Task #29). "
            "Recommended: re-extract cu2i2_veratrole_pi geometry locally on rbqua6cf61ki73 to remove the BELEGEN row-15 'geometry not re-verified' caveat (follow-up #2)."
        )
    new_rows.append(r)
write_csv(csp, hdr, new_rows)

# ---------------- MECHANISM_VERDICT_TABLE.csv ------------------------------
mvt = ROOT / "MECHANISM_VERDICT_TABLE.csv"
backup(mvt)
hdr, rows = read_csv(mvt)
# columns: mechanism_id, mechanism_name, primary_claim_ids, verdict, n_supporting_or_partial,
#          n_adverse_or_invalidated, n_not_tested_or_needs_exp, key_BE_evidence_kcal_mol,
#          scope_caveat, source_documents, counting_rule_note
counting_rule = (
    "n_supporting_or_partial = #{SUPPORTED, PARTIALLY_SUPPORTED}; "
    "n_adverse_or_invalidated = #{CONTRADICTED, INVALIDATED_BY_GEOMETRY, INVALIDATED_BY_ENERGETICS}; "
    "n_not_tested_or_needs_exp = #{NOT_TESTED, NEEDS_EXPERIMENTAL_VALIDATION}. Per-mechanism counts derived directly from "
    "BELEGEN_EVIDENCE_MATRIX.csv support_status column for the rows where claim_id = primary_claim_id."
)
new_rows = []
for r in rows:
    if r[0] == "M3":
        # M3 = Methoxy-O sigma-anchoring; under claim 3 (now state-dependent)
        r[3] = "PARTIALLY_SUPPORTED (state-dependent: bidentate kappa^2-O,O productive on neutral Cu2I2; mono-OMe on iodide-saturated [CuI2]- nonproductive)"
        r[4] = "6"   # supp+partial: cu_anisole + cui_guaiacol_methoxyO + cu2i2_v_OO_startA + cu2i2_v_OO_startB(partial) + cui2_v_OMe_startA(partial CONFIRMS) + cui2_v_OMe_startB(partial CONFIRMS)
        r[5] = "2"   # invalid_energ: cu2i2_guaiacol_methoxyO + cui2_guaiacol_methoxyO_anion (FAILED_SCF_STATE)
        r[6] = "0"
        r[7] = (
            "Productive at naked-Cu+ (cu_anisole_methoxyO -48.78 / -20.54 SMD); weak at CuI (cui_guaiacol_methoxyO -14.23, weakest O-donor); "
            "non-physical SCF in original Set D for cu2i2 + cui2 anion guaiacol cases (+172.67 / +173.15). "
            "Task #29 V2 RESCUES claim 3 on Cu2I2 with the bidentate veratrole minimum: "
            "cu2i2_veratrole_methoxyO_startA BE_gas = -26.82, BE_smd = -26.24 (Cu-O 2.203 A x 2, n_imag=0). "
            "[CuI2]- veratrole alternates remain endothermic +48 to +55 (E3.7, E3.8)."
        )
        r[8] = (
            "Productivity requires neutral CuI cluster + adjacent O,O donor geometry (here: 1,2-dimethoxy on veratrole). "
            "Single mono-OMe contacts remain metastable on Cu2I2. Bidentate basin needs rotamer scan + Grid5/FinalGrid6 single-point to confirm robustness."
        )
        r[9] = (
            "CONTROL_BINDING_TABLE.csv; CUI_CLUSTER_BINDING_TABLE.csv; CU2I2_BINDING_TABLE.csv; CUI2_BINDING_TABLE.csv; "
            "CUI2_RERUN_ANOMALIES.csv; VERATROLE_OME_ALTERNATE_STARTS.csv; BINDING_SURVIVAL_TABLE_setD_alt_v2.csv; "
            ".local/tasks/task-29-veratrole-ome-alternates.md"
        )
        r[10] = counting_rule
    elif r[0] == "M4":
        # M4 = Aromatic pi-coordination on neutral Cu2I2; under claim 4 (now substrate-dependent: veratrole binds, guaiacol/phenol detach)
        r[3] = "PARTIALLY_SUPPORTED (substrate-dependent: veratrole pi minimum -23.1 kcal/mol survives; guaiacol/phenol pi-starts collapse to detached)"
        r[4] = "1"   # supp+partial: cu2i2_veratrole_pi
        r[5] = "2"   # contradicted: cu2i2_guaiacol_pi + cu2i2_phenol_pi (both detached)
        r[6] = "0"
        r[7] = (
            "cu2i2_guaiacol_pi -15.53 (DETACHED, Cu-O >= 3.75 A); cu2i2_phenol_pi -16.73 (DETACHED, Cu-O 4.76 A); "
            "cu2i2_veratrole_pi BE_gas = -22.98, BE_smd = -23.11, n_imag=0 (TRUE eta^n-arene minimum, E4.3 SUPPORTED 2026-04-30 via Task #29 V2). "
            "Veratrole's two adjacent -OMe substituents stabilise the pi mode where free phenolic guaiacol/phenol cannot. "
            "DUAL-MODE NOTE: on the SAME Cu2I2 + veratrole complex, an alternate kappa^2-O,O bidentate seed (cu2i2_veratrole_methoxyO_startA, "
            "BELEGEN E3.5) gives BE_smd = -26.24, slightly more binding than the pi channel by ~3 kcal/mol. Both channels are viable on Cu2I2 + veratrole."
        )
        r[8] = (
            "pi-mode is substrate-dependent on Cu2I2: etherified veratrole binds, free phenolic guaiacol/phenol do not. "
            "Manuscript wording must say 'etherified guaiacyl/veratrole motifs bind via pi on neutral Cu2I2', not 'aromatic substrates bind via pi'. "
            "Other etherified substrates (e.g. beta-O-4 fragments) untested."
        )
        r[9] = (
            "CU2I2_BINDING_TABLE.csv; CU2I2_MODE_TABLE.csv; VERATROLE_OME_ALTERNATE_STARTS.csv; "
            "BELEGEN_EVIDENCE_MATRIX.csv (E4.3 + E3.5); .local/tasks/task-29-veratrole-ome-alternates.md"
        )
        r[10] = counting_rule
    new_rows.append(r)
write_csv(mvt, hdr, new_rows)

# ---------------- SITE_OCCUPANCY_TABLE.csv ---------------------------------
sot = ROOT / "SITE_OCCUPANCY_TABLE.csv"
backup(sot)
hdr, rows = read_csv(sot)
# columns: complex_id, cluster, ligand, start_mode, final_mode, BE_gas_kcal, BE_smd_kcal,
#          min_Cu_X_distance_A, contact_type, n_imag, occupancy_class, decision_basis,
#          raw_file_path, raw_file_sha256, notes

POD_BASE = "/root/orca_calc_setD_alt/logs"
new_v2_rows = [
    [
        "cu2i2_veratrole_methoxyO_startA", "Cu2I2", "veratrole",
        "bidentate-kappa^2-O,O seed (both Cu-O ~2.40 A, OMe/OMe)",
        "bidentate kappa^2-O,O methoxy chelate",
        "-26.82", "-26.24",
        "2.203",
        "Cu-bidentate (kappa^2-O,O); two equivalent Cu-OMe contacts at 2.203 A",
        "0",
        "OCCUPIED_INNER_SPHERE",
        "Both Cu-OMe at 2.203 A (well inside coordination sphere); BE_gas -26.82 / BE_smd -26.24; n_imag=0; lowest mode 12.4 cm-1; cluster intact (Cu2I2 rhombic preserved). NEW MINIMUM not present in original Set D mono-OMe seed (which gave +33.8 METASTABLE).",
        f"{POD_BASE}/cu2i2_veratrole_methoxyO_startA_restart_v2_opt_freq.out",
        "a14cc98b6efe57681336694d4e0834a499812adb8cb46914f56a924801f13256",
        "Task #29 V2 startA discovery; BELEGEN E3.5; reopens claim 3 for veratrole on neutral Cu2I2 in bidentate geometry. Slightly more binding than the pi channel on the same complex (cu2i2_veratrole_pi BE_smd -23.11) by ~3 kcal/mol.",
    ],
    [
        "cu2i2_veratrole_methoxyO_startB", "Cu2I2", "veratrole",
        "tilted single-OMe seed (one Cu-OMe ~2.4 A, ring tilted 60 deg)",
        "single-OMe + eta^1-aryl mixed mode",
        "+28.07", "+22.73",
        "1.930",
        "Cu-O 2.642 A (mono-OMe) + Cu-C 1.930 A (strong eta^1-aryl)",
        "0",
        "OCCUPIED_INNER_SPHERE (mode-mixed, energetically metastable)",
        "Cu-O 2.642 A and Cu-C 1.930 A both inside inner sphere; n_imag=0. BE +28.07 gas / +22.73 SMD = endothermic vs separated reactants -> METASTABLE_CONTACT. Distinct local minimum, not the global one.",
        f"{POD_BASE}/cu2i2_veratrole_methoxyO_startB_restart_v2_opt_freq.out",
        "d9301256a5c78665b7311695bdc85119ba1d4fd10773c0b1c07f542a0d4ae8bd",
        "Task #29 V2 startB; BELEGEN E3.6. Mode-mixes single-OMe with eta^1-aryl; not productive vs free reactants.",
    ],
    [
        "cui2_veratrole_methoxyO_anion_startA", "[CuI2]-", "veratrole",
        "long-distance methoxy seed (Cu-O ~2.83 A initial, linear [CuI2]-)",
        "outer-sphere eta^2-arene drift (ligand pushed away by linear [CuI2]-)",
        "+49.28", "+53.60",
        "3.214",
        "Cu-O 3.697 A (no Cu-O contact); weak Cu-C 3.214 A; I-Cu-I 173.2 deg (near-linear)",
        "0",
        "DISSOCIATED",
        "Cu-O 3.697 / 5.364 A both well outside inner sphere; weakest Cu-C 3.214 A is an arene drift, not coordination; I-Cu-I retained near linear. BE +49.28 gas / +53.60 SMD endothermic. Linear d10 [CuI2]- unable to bend to accommodate the methoxy-O.",
        f"{POD_BASE}/cui2_veratrole_methoxyO_anion_startA_restart_v2_opt_freq.out",
        "e14cedb434d71a00a4147aae57dd56b7db1be57348ba3c5c79b47357db464ef9",
        "Task #29 V2 anion startA; BELEGEN E3.7. CONFIRMS_E3.4_AT_VERATROLE: methoxy-O does not bind the iodide-saturated anion regardless of seed.",
    ],
    [
        "cui2_veratrole_methoxyO_anion_startB", "[CuI2]-", "veratrole",
        "rotated 180-deg methoxy seed (ring rotated around Cu-O axis)",
        "single-OMe + eta^1-aryl mixed mode (cluster bent to 124 deg I-Cu-I)",
        "+55.20", "+47.93",
        "1.938",
        "Cu-O 2.692 A (held); strong Cu-C 1.938 A (eta^1-aryl); I-Cu-I 124.4 deg (cluster bent)",
        "0",
        "OCCUPIED_INNER_SPHERE (mode-mixed, energetically metastable; cluster geometry distorted)",
        "Cu-O 2.692 A and Cu-C 1.938 A both inside inner sphere; cluster bent from linear (179 deg) to 124 deg to retain a single Cu-O. n_imag=0. BE +55.20 gas / +47.93 SMD endothermic. Reproduces the original cui2_guaiacol_methoxyO_anion result (+167 was SCF-artifact-inflated; this V2 startB at +55 is the physical answer, within 0.4 mEh of the SP-restart re-runs).",
        f"{POD_BASE}/cui2_veratrole_methoxyO_anion_startB_restart_v2_opt_freq.out",
        "b2a5bb4424890e42806ada39f5345d4332b99a482faa488143e68397c2602836",
        "Task #29 V2 anion startB; BELEGEN E3.8. CONFIRMS_E3.4_AT_VERATROLE.",
    ],
]
rows.extend(new_v2_rows)
write_csv(sot, hdr, rows)

# ----- summary
print("Updated:")
for p in (csp, mvt, sot):
    print(f"  {p}  ({sum(1 for _ in open(p))} lines)")
print(f"Backups stamped {STAMP}")
