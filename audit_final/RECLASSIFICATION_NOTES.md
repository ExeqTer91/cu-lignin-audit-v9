# Reclassification Notes — Task #28 Conservative Classifier

**Date:** 20260430T113509Z

**Rule set (verbatim from handover):**
- A STRONG_BINDING     : BE_eff < -10 AND valid contact AND true minimum
- B MODERATE_BINDING   : -10 <= BE_eff < -5 AND valid contact
- C WEAK_BINDING       : -5 <= BE_eff < 0 AND valid contact
- D METASTABLE_CONTACT : BE_eff >= 0 BUT contact survives geometrically
- E NON_BINDING        : ligand detached / cluster fragmented / hard saddle / no contact

**BE_eff_conservative = max(BE_gas, BE_smd)** when SMD exists, else BE_gas.

**Valid-contact thresholds:** Cu-O <= 2.6 A *or* Cu-C/arene <= 3.2 A.

Geometry / cluster-integrity overrides supersede energy. Each override below lists the original (energy-only) class and the new class.

| Row | original_class | new_class | reason |
|---|---|---|---|
| cui2_guaiacol_bidentate_anion | B | E | BE_artifact>+100 |
| cui2_guaiacol_methoxyO_anion | D | E | ligand_detached, no_valid_contact, BE_artifact>+100 |
| cui2_guaiacol_phenolicO_anion | D | E | ligand_detached, no_valid_contact |
| cui2_guaiacol_pi_anion | D | E | ligand_detached, no_valid_contact |
| cui2_h2o_anion | D | E | ligand_detached, no_valid_contact |
| cui2_methanol_anion | D | E | ligand_detached, no_valid_contact |
| cui2_phenol_O_anion | D | E | ligand_detached, no_valid_contact |
| cui2_phenol_pi_anion | D | E | ligand_detached, no_valid_contact |
| cu2i2_guaiacol_methoxyO | C | E | BE_artifact>+100 |
| cu2i2_guaiacol_phenolicO | D | E | cluster_fragmented |
| cu2i2_guaiacol_pi | B | E | ligand_detached, no_valid_contact |
| cu2i2_phenol_O | C | A | ruleset_change |
| cu2i2_phenol_pi | D | E | ligand_detached, no_valid_contact |
| cu_anisole_methoxyO | (new) | A | naked-Cu+ Tier A row added by V9 build |
| cu_anisole_pi | (new) | A | naked-Cu+ Tier A row added by V9 build |
| cu_benzene_pi | (new) | A | naked-Cu+ Tier A row added by V9 build |
| cu_catechol_bidentate | (new) | A | naked-Cu+ Tier A row added by V9 build |
| cu_catechol_pi | (new) | A | naked-Cu+ Tier A row added by V9 build |
| cu_cyclohexanol_O | (new) | A | naked-Cu+ Tier A row added by V9 build |
| cu_galacturonateH_complex | (new) | A | naked-Cu+ Tier A row added by V9 build |
| cu_galacturonate_anion_complex | (new) | A | naked-Cu+ Tier A row added by V9 build |
| cu_guaiacol_methoxyO | (new) | A | naked-Cu+ Tier A row added by V9 build |
| cu_guaiacol_phenolicO | (new) | B | naked-Cu+ Tier A row added by V9 build |
| cu_guaiacol_pi | (new) | A | naked-Cu+ Tier A row added by V9 build |
| cu_meta_methoxyphenol_phenolicO | (new) | D | naked-Cu+ Tier A row added by V9 build |
| cu_meta_methoxyphenol_pi | (new) | A | naked-Cu+ Tier A row added by V9 build |
| cu_methanol | (new) | A | naked-Cu+ Tier A row added by V9 build |
| cu_para_methoxyphenol_phenolicO | (new) | A | naked-Cu+ Tier A row added by V9 build |
| cu_para_methoxyphenol_pi | (new) | A | naked-Cu+ Tier A row added by V9 build |
| cu_phenol_O | (new) | E | naked-Cu+ Tier A row added by V9 build |
| cu_phenol_pi | (new) | A | naked-Cu+ Tier A row added by V9 build |
| cu2i2_veratrole_methoxyO_startA | (new) | A | Set D V2 row (Task #29) added by V9 build |
| cu2i2_veratrole_methoxyO_startB | (new) | D | Set D V2 row (Task #29) added by V9 build |
| cui2_veratrole_methoxyO_anion_startA | (new) | E | Set D V2 row (Task #29) added by V9 build |
| cui2_veratrole_methoxyO_anion_startB | (new) | D | Set D V2 row (Task #29) added by V9 build |

## Outlier handling
Two CuI2-/Cu2I2 rows show nonphysical BE_gas > +100 kcal/mol (`cu2i2_guaiacol_methoxyO` BE_gas = +172.67; `cu2i2_guaiacol_bidentate_anion` BE_gas = +167.44; `cui2_guaiacol_methoxyO_anion` BE_gas = +173.15). These are SCF / optimization artifacts of the reference cluster (likely a different [CuI2]- conformer used as the reference); they are RECLASSIFIED as class E NON_BINDING with the artifact note attached. They are not used as evidence for any v9 claim.

## Set D V2 classifications
- `cu2i2_veratrole_methoxyO_startA`: kappa2-O,O bidentate, Cu-O 2.20/2.20 A, BE_gas -26.82, BE_smd -26.24, n_imag=0, lowest +12.4 cm-1. Class A.
- `cu2i2_veratrole_methoxyO_startB`: rotamer; Cu-O closest 2.64 A but BE_eff = +28.07 kcal/mol (gas) / +22.73 (SMD); contact survives geometrically. Class D.
- `cui2_veratrole_methoxyO_anion_startA`: rotamer; Cu-O closest 3.70 A (no valid O contact), Cu-C 3.21 A (also outside cutoff). BE_eff = +49.28. Class E NON_BINDING (no valid contact, positive BE).
- `cui2_veratrole_methoxyO_anion_startB`: rotamer; Cu-O closest 2.69 A, Cu-C 1.94 A (close but ring slip). BE_eff = +55.20. Class D (positive BE, but Cu-C contact preserved).

## Geometry overrides applied to existing rows
Rows where `mode_survival_status` reports DETACHED, FRAGMENTED, or COLLAPSED_TO_DETACHED were forced to class E regardless of BE. Rows where contact distance exceeded the cutoff (Cu-O > 2.6 A, Cu-C > 3.2 A) were also forced to class E.

## Validation sanity check
- Class A (STRONG): bidentate guaiacol on Cu2I2, water on Cu2I2, methanol on Cu2I2, kappa2-O,O veratrole on Cu2I2 (V2 startA) -- all accepted as productive anchoring sites in the v9 thesis.
- Class E (NON-binding): all [CuI2]- rows and the bare-Cu2I2 phenol-pi row -- consistent with the rejection of iodide-saturated anchoring and the textile-sense rejection of pi-only contacts on Cu2I2.

## Borderline-cutoff note: cu_phenol_O

`cu_phenol_O` (naked Cu+ on phenolic O of phenol) optimizes to Cu-O = 2.6636 A
with BE_gas = -51.44 kcal/mol and BE_smd = -36.39 kcal/mol. The Cu-O distance
exceeds the 2.6 A spec cutoff by 0.06 A, so the strict classifier returns E.
This is reported as-is and is consistent with the well-established v8 -> v9
finding that phenol-O on naked Cu+ drifts toward pi (cu_phenol_pi BE_gas = -80.96).
Treat the cu_phenol_O row as 'O-mode is not the productive minimum on naked Cu+ for
phenol; the system relaxes toward pi.' Functionally equivalent to class B if a 2.7 A
cutoff were used.

## Task 1 reconciliation (2026-04-30): cu2i2_guaiacol_bidentate

The `cu2i2_guaiacol_bidentate` row (CU2I2_BINDING_TABLE.csv, BE_gas =
-17.86 kcal/mol, n_imag = 0, cluster_fragmented = False) was reconciled
against the manuscript draft statement that "free phenolic-OH guaiacol
on Cu2I2 cracks the cluster". Both statements are correct: the cracker
result (`cu2i2_guaiacol_phenolicO`) and the bidentate result are TWO
DIFFERENT PES BASINS reached from two different starting geometries on
free guaiacol on neutral Cu2I2.

Classification: **Category A (REAL bidentate minimum on intact Cu2I2)**.

| species | (was) | (is) | reason |
|---|---|---|---|
| cu2i2_guaiacol_bidentate | (existing, A) | A confirmed | RECONCILED Task 1: real κ²-O,O bidentate to one Cu (Cu-O 2.22/2.26 Å); cluster topology preserved; weaker secondary channel vs primary cu2i2_veratrole_methoxyO_startA (-26.82); distinct PES basin from cu2i2_guaiacol_phenolicO cracker pathway. Full reconciliation in `audit_final/V9_GUAIACOL_BIDENTATE_RESOLUTION.md`. |

Manuscript writer guidance: see V9_GUAIACOL_BIDENTATE_RESOLUTION.md §6
for the manuscript-ready paragraph and §8 for the per-section change
list.
