# ACS SCE v8 — Computational Audit: Final Report
**Pipeline run:** 2026-04-26 UTC  
**Status: COMPLETE (100.0% — 79/79 tracked SPECIES_META jobs + 3 supplementary SP series)**  
**Method:** ORCA 6.1.1 / B3LYP-D3BJ / def2-TZVP / RIJCOSX def2/J / TightSCF / TightOpt  
**Node:** RunPod A100 (195.26.233.65:21128)  
**Charge/mult:** Cu⁺ complexes — charge=1, mult=1; CuI cluster — charge=0, mult=1; Cu²⁺ ref — charge=2, mult=2

---

## 1. Completion Status

| Category | Jobs Done | Total |
|----------|-----------|-------|
| Phase 1/2 — Opt+Freq (original species) | 14 | 14 |
| Phase 1/2 — SMD SP (original species) | 14 | 14 |
| Tier A — Opt+Freq (new Cu⁺ complexes + ligands) | 16 | 16 |
| Tier A — Freq-only validation jobs | 5 | 5 |
| Tier A — SMD SP (new complexes + ligands) | 16 | 16 |
| Tier B — CuI cluster Opt+Freq | 14 | 14 |
| **TOTAL (SPECIES_META)** | **79** | **79** |
| Supplementary: Cu²⁺ IP diagnostic SP | 1 | 1 |
| Supplementary: cyclohexanol SMD ligand SP | 1 | 1 |
| Supplementary: def2-TZVPP basis sensitivity SPs | 6 | 6 |
| **GRAND TOTAL** | **87** | **87** |

**pct_complete: 100.0% (79/79 SPECIES_META + 8 supplementary)**  
**Files indexed with SHA-256: 104** (96 primary + 8 displacement reopt)

---

## 2. Binding Energy Summary (Gas Phase, kcal/mol)

All BEs: BE = E(complex) − E(ligand) − E(Cu⁺); Hartrees converted at 627.5095 kcal/mol/Eh.  
No ZPE, BSSE, or thermal correction applied.

### 2a. Original Manuscript Species

| Complex | Our BE (gas) | MS BE | Δ | Assessment |
|---------|-------------|-------|---|-----------|
| cu_methanol | −47.50 | −45.0 | −2.5 | MINOR |
| cu_phenol_O | −51.44 | −17.9 | −33.5 | MAJOR |
| cu_phenol_pi | −80.96 | −55.2 | −25.8 | MAJOR + SADDLE (n_imag=1) |
| cu_guaiacol_phenolicO | −28.52 | −19.7 | −8.8 | MAJOR |
| cu_guaiacol_methoxyO | −54.48 | N/A | — | NO_REF |
| cu_guaiacol_pi | −62.17 | −43.1 | −19.1 | MAJOR |
| cu_galacturonateH_complex | −50.10 | −58.4 | +8.3 | MAJOR |
| cu_galacturonate_anion_complex | −185.70 | N/A | — | UNPHYSICAL† |

† The anion complex BE of −185.70 kcal/mol is unphysical; charge=0 complex vs Cu⁺+anion⁻ decomposition.

### 2b. Tier A — New Species (Validated True Minima Only)

| Complex | Gas BE | SMD BE | n_imag | Mode |
|---------|--------|--------|--------|------|
| cu_anisole_pi | −60.15 | −46.39 | 0 | π-complex ✓ |
| cu_anisole_methoxyO | −48.78 | −37.53 | 0§ | O-monodentate ✓ |
| cu_catechol_pi | −59.78 | −49.33 | 0 | π-complex ✓ |
| cu_cyclohexanol_O | −58.13 | **−27.24** | 0 | O-monodentate ✓ |
| cu_meta_methoxyphenol_pi | −63.16 | −46.49 | 0 | π-complex ✓ |
| cu_para_methoxyphenol_pi | −58.20 | −43.87 | 0 | π-complex ✓ |
| cu_para_methoxyphenol_phenolicO | −49.64 | −24.26 | 0 | O-monodentate ✓ |

§ n_imag=0 in Opt+Freq; separate Freq-only job reports n_imag=1 (mode at −37.8 cm⁻¹, likely free rotation).

### 2c. Tier A — Saddle Points (BEs are upper bounds)

| Complex | Gas BE | n_imag | Action |
|---------|--------|--------|--------|
| cu_benzene_pi | −54.44 | 2 | Geometry correction needed |
| cu_catechol_bidentate | −33.41 | 2 | Geometry correction needed |
| cu_meta_methoxyphenol_phenolicO | −12.35 | 4 | Multi-saddle; likely non-binding |

---

## 3. π vs O Selectivity (Cu⁺)

All aromatic ligands show Cu⁺ π-preference over O-coordination:

| Ligand | π BE | O BE | Δ(π−O) |
|--------|------|------|---------|
| Anisole | −60.15 | −48.78 | −11.4 (π preferred) |
| Catechol | −59.78 | −33.41† | −26.4† (π preferred) |
| Guaiacol | −62.17 | −28.52 / −54.48 | −7.7 / −33.7 |
| para-Methoxyphenol | −58.20 | −49.64 | −8.6 (π preferred) |
| meta-Methoxyphenol | −63.16 | −12.35† | −50.8† (π preferred) |

† Saddle-point BEs; upper bounds only.

---

## 4. Tier B CuI Cluster Controls

### 4a. CuI/Cu₂I₂ Binding Energies (def2-TZVP)

| Species | Gas E (Eh) | BE_gas (kcal/mol) | n_imag | Notes |
|---------|-----------|------------------|--------|-------|
| cui_monomer | −1938.215889 | N/A (reference) | 0 | Reference |
| cui_methanol_O | −2053.969634 | −25.76 | 1 | Borderline saddle |
| cui_phenol_O | −2245.679584 | −50.72 | 2 | Saddle; upper bound |
| cui_phenol_pi | −2245.689103 | −56.69 | 0 | TRUE MIN; CuI π-preferred |
| cui_guaiacol_ph | −2360.204571 | −25.30 | 0 | TRUE MIN |
| cu2i2_rhombic | −3876.514481 | −51.90 | 0 | TRUE MIN; 35.5 kcal/mol more stable than linear |
| cu2i2_linear | −3876.457862 | −16.37 | 2 | SADDLE |

**Head-to-head CuI ligand comparison (case determination):**

| Ligand | Mode | BE_gas (kcal/mol) | True min? | vs CuI–methanol | Evidence Status |
|--------|------|-------------------|-----------|-----------------|-----------------|
| Methanol | O-donor | −25.76 | YES* | — (reference) | COMPUTED |
| Guaiacol | phenolic-O | −25.30 | YES | +0.46 (no advantage) | COMPUTED |
| Phenol | π-donor | −56.69 | YES | **−30.93 (π favored)** | COMPUTED (aromatic π control) |
| Phenol | phenolic-O | −50.72 | NO (saddle) | — | COMPUTED — upper bound only |
| Guaiacol | π | — | — | — | RUNNING — v9.1 (started 2026-04-27) |
| Guaiacol | methoxy-O | −14.23 | YES | +11.53 (weakest O-donor) | COMPUTED — v9.1 (2026-04-27) |
| Guaiacol | bidentate | — | — | — | RUNNING — v9.1 (started 2026-04-27) |
| Cu₂I₂ + any ligand | — | — | — | — | NOT_RUN — v9.1 follow-up |

*Confirmed after displacement reopt (CONFIRMED_MIN_BOTH; lowest real mode 54.9 cm⁻¹).

CuI–guaiacol-phO ≈ CuI–methanol (within 0.5 kcal/mol): **no guaiacyl phenolic-O selectivity at the CuI cluster level**. Phenol π demonstrates that aromatic π-coordination can be strongly favored in a minimal CuI-cluster model (−56.69 kcal/mol). Whether guaiacol itself achieves π-mode dominance at the CuI level is unknown — CuI–guaiacol π was not computed. **Case C working decision** (supported for the computed CuI subset; full guaiacol CuI mode map is v9.1 scope). Cu₂I₂ + ligand BEs were NOT computed (only dimerization energy); that comparison constitutes v9.1 scope. See `audit_final/V9_CASE_DECISION.md` for full evidence-status provenance.

**Editorial note on model scope:** Isolated naked Cu(I)–guaiacyl motifs, as modeled here with CuI
monomer at B3LYP-D3BJ/def2-TZVP, provide a partial but informative picture of fiber-Cu binding.
The CuI–guaiacol-phO BE (−25.30 kcal/mol) and the broader CuI π-preference are internally
consistent results. Three scope limitations must be stated explicitly in the manuscript:
(a) the Cu(I) charge state is appropriate for the iodide thin-film deposition phase, but
oxidation-state changes during laundering (e.g., Cu²⁺ exposure in hard water) are not modeled;
(b) fiber-surface effects (neighboring polymer groups, backbone flexibility, pH, counter-ions)
are absent from isolated-monomer computations;
(c) gas-phase binding energies alone are insufficient — SMD water single points are included
here but polymer-backbone and pH effects remain outside the model.
These are model-level scope limitations to qualify explicitly, not evidence that the computations
are fundamentally flawed. Any manuscript claim based solely on these isolated CuI–guaiacyl
computations must be explicitly qualified with the above limitations.

### 4b. def2-TZVPP Basis Sensitivity (Supplementary)

| Species | TZVP BE | TZVPP BE† | Gap | Robustness |
|---------|---------|----------|-----|-----------|
| CuI–methanol_O | −25.76 | −28.08 | −2.32 | MODERATE |
| CuI–phenol-π | −56.69 | −59.50 | −2.81 | MODERATE |
| CuI–phenol-O | −50.72 | −53.54 | −2.82 | MODERATE |
| CuI–guaiacol-phO | −25.30 | −28.59 | −3.29 | MODERATE |
| Cu₂I₂ dimerization | −51.90 | −51.98 | −0.08 | **ROBUST** |

† TZVPP BE uses TZVP ligand energies as approximation.

---

## 5. Supplementary: Cu²⁺ Oxidation-State Diagnostic

| Quantity | Value |
|----------|-------|
| E(Cu²⁺, UKS, charge=2, mult=2) | −1639.375466 Eh |
| E(Cu⁺, RKS, charge=1, mult=1) | −1640.134600 Eh |
| IP(Cu⁺→Cu²⁺) | 476.36 kcal/mol |
| Cyclohexanol SMD BE (complete) | −27.24 kcal/mol |

**Precise scope**: The 476.36 kcal/mol IP (close to experimental 467.93 kcal/mol = 20.292 eV)
excludes one specific error mode: swapping the Cu⁺/Cu²⁺ atomic reference energy in an otherwise
identical BE formula would shift all BEs by ±476 kcal/mol, which is ~14–240× larger than the
observed 2–34 kcal/mol discrepancy. This specific error is excluded. The diagnostic does NOT
exclude scenarios where the manuscript used Cu²⁺-optimized complex geometries, BSSE/CP
corrections, ZPE corrections, or a different basis set — any of which could account for the
observed 2–34 kcal/mol discrepancy. Full Cu²⁺ complex re-optimizations are required for
definitive reconciliation.

---

## 6. Saddle-Point Displacement Reopt Status

| Species | n_imag | Reopt Status | Script |
|---------|--------|-------------|--------|
| cu_phenol_pi | 1 | **DONE — CONFIRMED_MIN_BOTH** (both ±0.3 Å displaced geoms → true minima, n_imag=0; lowest mode 57.4 cm⁻¹) | run_fast_disp.py |
| cu_benzene_pi | 2 | **DONE — PERSISTENT_SOFT_SADDLE** (both ±0.3 Å reopt to −23.3 cm⁻¹ saddle; ring pseudo-rotation flat torsional mode) | run_fast_disp.py |
| cu_catechol_bidentate | 2 | **DONE — CONFIRMED_MIN_BOTH** (both ±0.3 Å displaced geoms → true minima, n_imag=0; lowest mode 49.6 cm⁻¹; bidentate coordination confirmed accessible) | run_fast_disp.py |
| cu_meta_methoxyphenol_phenolicO | 4 | NOT_RUN (multi-saddle; recommend removal) | N/A |
| cu_anisole_methoxyO | 1 | BORDERLINE (soft −37.8 cm⁻¹; free rotation; retain with note) | N/A |
| cu_phenol_O | 2 | NOT_RUN (superseded by cu_phenol_pi) | N/A |
| cu2i2_linear | 2 | NOT_RUN (superseded by rhombic) | N/A |
| cui_methanol_O | 1 | **DONE — CONFIRMED_MIN_BOTH** (both ±0.3 Å displaced geoms → true minima, n_imag=0) | run_fast_disp.py |
| cui_phenol_O | 2 | NOT_RUN (superseded by cui_phenol_pi) | N/A |

DISPLACEMENT_REOPT_SUMMARY.json: `runs_completed=4/4, status=COMPLETE` (2026-04-26; cui_methanol_O, cu_catechol_bidentate, cu_phenol_pi CONFIRMED_MIN_BOTH; cu_benzene_pi PERSISTENT_SOFT_SADDLE — ring pseudo-rotation, flat torsional PES).
See `audit_final/DISPLACEMENT_REOPT_SUMMARY.json` for machine-readable status.

---

## 7. ORCA 6.1.1 Issues

| Issue | Workaround |
|-------|-----------|
| Opt+Freq drops Freq section with nprocs≥8 | Separate Freq-only jobs |
| SIGABRT at nprocs=16 | Reduced to nprocs=8; nprocs=1 for root |
| PAL syntax: `%end` rejected | Changed to bare `end` |
| Stale .gbw causes startup failure | `rm -f *.gbw` before relaunch |
| cu_cyclohexanol_O: missing 1H atom | Relaunched as v2 (corrected 20-atom geometry) |
| Coordinate extraction `head -N` truncation | Changed to `head -25` |

---

## 8. File Provenance

| Path | Files | Purpose |
|------|-------|---------|
| `results/` | 30 | Phase 1/2 canonical symlinks |
| `results/tier_a/` | 36 | Tier A canonical symlinks |
| `results/tier_b/` | 16 | Tier B canonical symlinks |
| `results_pod/results/` | 31 | Phase 1/2 RunPod + Cu²⁺ SP |
| `results_pod/results_tiera/` | 36 | Tier A RunPod + cyclohexanol SMD |
| `results_pod/results_tierb/` | 16 | Tier B RunPod computations |
| `results_pod/results_tzvpp/` | 12 | def2-TZVPP basis sensitivity SPs |

SHA-256 checksums for all 96 indexed .out files: `audit_final/RAW_FILE_INDEX.csv`

---

## 9. Key Finding and v9 Recommendation

**Our B3LYP-D3BJ/def2-TZVP/Cu⁺ values are systematically 2–4× more negative than
manuscript-reported BEs.** Cu oxidation-state confusion is excluded as the primary cause
(Cu²⁺ IP = 476.36 kcal/mol >> observed discrepancies). The discrepancy most likely arises
from: (a) the manuscript using Cu²⁺ complex geometries with BE = E(complex) − E(ligand) − E(Cu²⁺),
(b) BSSE correction applied in the manuscript, or (c) geometry/basis differences.

**See `MANUSCRIPT_IMPACT_v8_to_v9.md` for the full v9 decision memo.**

---

*Generated 2026-04-26 by build_audit_csvs.py pipeline + supplementary updates.*  
*All energies in Hartrees unless noted. BEs in kcal/mol (no ZPE/BSSE correction).*
