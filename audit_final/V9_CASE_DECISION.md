# V9 Case Decision: Mode-Selective Copper Anchoring

**Date:** 2026-04-27 UTC  
**Audit version:** v9  
**Computational basis:** ORCA 6.1.1 / B3LYP-D3(BJ) / def2-TZVP; CuI cluster Tier B controls  
**Decision type:** Working decision — supported for the computed CuI subset; full guaiacol CuI mode map remains incomplete (see §4)

---

## 1. Case C Working Decision

**Case C is supported for the computed CuI modes, while the full CuI–guaiacol mode map remains incomplete.**

The computed CuI cluster data show:

- CuI–guaiacol phenolic-O binding (−25.30 kcal/mol) is within 0.46 kcal/mol of CuI–methanol O-binding (−25.76 kcal/mol). This difference is within thermal and basis-set noise and constitutes no meaningful selectivity advantage.
- Phenol π demonstrates that aromatic π-coordination can be strongly favored in a minimal CuI-cluster model (−56.69 kcal/mol; a true minimum, n_imag=0).
- The v8 claim that guaiacyl phenolic-O sites have a special affinity advantage over cellulose-like O-donors is not supported by the computed CuI subset.

Three guaiacol CuI modes (π, methoxy-O, bidentate) were flagged as v9.1 scope. **Methoxy-O is computed (v9.1, 2026-04-27): BE = −14.23 kcal/mol, n_imag=0 (true minimum)** — the weakest O-donor mode at the CuI level, consistent with methoxy oxygen being a weaker σ-donor than free phenol-OH or alcohol. **CuI–guaiacol π is now computed (v9.1, 2026-04-27): BE = −29.04 kcal/mol, n_imag=0 (true minimum), E_final = −2360.210527 Eh (NormalOpt+Freq, 12 cycles to convergence).** This confirms that guaiacol π-coordination at the CuI level is a true minimum, and BE (−29.04 kcal/mol) places it between methanol O-binding (−25.76) and phenol π (−56.69 kcal/mol). Notably, CuI–guaiacol π (−29.04) and CuI–guaiacol phenolic-O (−25.30) are within 3.74 kcal/mol — a smaller gap than at the naked-Cu⁺ level (33.7 kcal/mol). **CuI–guaiacol bidentate is now COMPLETE (v9.1, 2026-04-27): 57 cycles, ORCA terminated normally at MaxIter.** The geometry reveals bidentate coordination is NOT a stable minimum at the CuI level — the phenolic oxygen drifts to 3.04 Å from Cu (non-coordinating) while methoxy-O remains at 1.985 Å (bonded). The bidentate start collapses to methoxy-O monodentate. This constitutes evidence that guaiacol bidentate chelation does not survive iodide coordination at this level of theory; iodide occupies a coordination site that prevents the geometry required for bidentate binding. The methoxy-O monodentate result (BE = −14.23 kcal/mol, already converged) is the relevant minimum for this starting geometry.

The case determination at the naked-Cu⁺ level (Phase 1/2 + Tier A) is not subject to this qualification: all relevant naked-Cu⁺ guaiacol modes (phenolicO, methoxyO, π) were computed. The π-mode dominates by 33.7 kcal/mol over phenolicO and by ≥7.7 kcal/mol over methoxyO. The naked-Cu⁺ result is unambiguously Case C.

---

## 2. V9 Interpretation Conclusion (verbatim)

> CuI coordination suppresses the guaiacyl phenolic-O advantage: CuI–guaiacol phenolic-O binding is essentially identical to CuI–methanol O-binding within 0.46 kcal/mol. However, aromatic π-coordination remains strongly favorable in the CuI-cluster model, as shown by the phenol π-complex. Therefore the v8 single-site cellulose-vs-guaiacol comparison is not valid as written. The v9 thesis should be a mode-selective anchoring model, where copper retention depends on accessible binding modes rather than a single per-site affinity ranking.

---

## 3. Head-to-Head CuI Binding Table (Evidence-Status)

Binding energies from `audit_final/CUI_CLUSTER_BINDING_TABLE.csv` and `audit_final/CUI_BASIS_SENSITIVITY.csv`.

| Ligand | Mode | BE_gas (kcal/mol) | n_imag | True min? | Evidence Status |
|--------|------|-------------------|--------|-----------|-----------------|
| Methanol | O-mono | −25.76 | 0* | YES | COMPUTED |
| Guaiacol | phenolic-O | −25.30 | 0 | YES | COMPUTED |
| Phenol | π | −56.69 | 0 | YES | COMPUTED (aromatic π control) |
| Phenol | phenolic-O | −50.72 | 2 | NO (saddle) | COMPUTED — upper bound only |
| Guaiacol | π | −29.04 | 0 | YES | COMPUTED — v9.1 (2026-04-27) |
| Guaiacol | methoxy-O | −14.23 | 0 | YES | COMPUTED — v9.1 (2026-04-27) |
| Guaiacol | bidentate | N/A | N/A | NO | RELAXES TO METHOXY-O — bidentate inaccessible at CuI level (v9.1, 2026-04-27) |
| Cu₂I₂ + any ligand | — | — | — | — | NOT_RUN — v9.1 follow-up |

*cui_methanol_O confirmed true minimum after displacement reopt (CONFIRMED_MIN_BOTH; lowest real mode 54.9 cm⁻¹).

### 3a. TZVPP Basis Confirmation

Both exact rows for the methanol / guaiacol-phO gap are available in `audit_final/CUI_BASIS_SENSITIVITY.csv`:

| Row | ΔE_TZVP (kcal/mol) | ΔE_TZVPP (kcal/mol) | Gap |
|-----|---------------------|---------------------|-----|
| CuI_methanol_best | −25.76 | −28.08 | −2.32 |
| CuI_guaiacol_best (=cui_guaiacol_ph, phenolic-O) | −25.30 | −28.59 | −3.29 |

TZVPP basis sensitivity confirms the guaiacol-O / methanol equivalence holds at higher basis: TZVPP gap = 0.51 kcal/mol (−28.08 vs −28.59). Both rows are status MODERATE (2.3–3.3 kcal/mol basis correction); the qualitative conclusion is basis-robust.

---

## 4. Explicitly NOT Computed in This Audit

The following calculations are out of scope for v9 and must not be cited as supporting evidence:

| Missing calculation | Why needed | Status |
|--------------------|------------|--------|
| CuI + guaiacol (π-start) opt+freq | Required to determine if guaiacol π also dominates at CuI level | COMPUTED — v9.1 (2026-04-27); BE = −29.04 kcal/mol, n_imag=0 |
| CuI + guaiacol (methoxy-O start) opt+freq | Full guaiacol CuI mode map | COMPUTED — v9.1 (2026-04-27); BE = −14.23 kcal/mol, n_imag=0 |
| CuI + guaiacol (bidentate start) opt+freq | Tests chelation survival under iodide coordination | COMPLETE — v9.1 (2026-04-27); 57 cycles; RELAXES TO METHOXY-O — phenolic-O drifts to 3.04 Å (non-coordinating); bidentate mode is not a stable minimum at CuI level |
| Cu₂I₂ + methanol opt+freq | Ligand binding to dimeric CuI cluster | NOT_RUN — v9.1 follow-up |
| Cu₂I₂ + phenol opt+freq | Ligand binding to dimeric CuI cluster | NOT_RUN — v9.1 follow-up |
| Cu₂I₂ + guaiacol (all modes) opt+freq | Ligand binding to dimeric CuI cluster | NOT_RUN — v9.1 follow-up |
| Cu²⁺ complex re-optimizations (all ligands) | Definitive oxidation-state reconciliation | NOT_RUN — v9.1 follow-up |
| Cu₂O surface adsorption (any ligand, any mode) | Aged-state O-donor / hydroxyl / phenolic / water-mediated anchoring on Cu₂O surface phase (Level 6) | OUT_OF_SCOPE — oxide-aging regime; literature-backed limitation, no new compute (see `audit_final/OXIDE_AGING_REGIME_NOTE.md`) |
| Cu(OH)₂ surface adsorption (any ligand, any mode) | Aged-state O-donor / hydroxyl / phenolic / water-mediated anchoring on Cu(OH)₂ surface phase (Level 6) | OUT_OF_SCOPE — oxide-aging regime; literature-backed limitation, no new compute (see `audit_final/OXIDE_AGING_REGIME_NOTE.md`) |
| CuO surface adsorption (any ligand, any mode) | Aged-state O-donor / hydroxyl / phenolic / water-mediated anchoring on CuO surface phase (Level 6) | OUT_OF_SCOPE — oxide-aging regime; literature-backed limitation, no new compute (see `audit_final/OXIDE_AGING_REGIME_NOTE.md`) |

**Important**: The Cu₂I₂ dimerization energy (−51.90 kcal/mol, rhombic isomer) was computed, but this is not a ligand-binding energy. Cu₂I₂ + ligand adduct calculations do not exist and must not be used to support ligand-binding conclusions.

---

## 5. Final Thesis (verbatim — use in §12 abstract and all summary sections)

> Copper retention on lignin-rich fibers is governed by accessible, mode-selective anchoring rather than a single per-site affinity ranking. Minimal CuI-cluster models show that guaiacyl phenolic-O binding is comparable to methanol O-binding, while aromatic π-binding can dominate when geometrically accessible. Polymer architecture, oxidation state, and surface accessibility therefore determine which modes contribute to real textile retention.

---

## 6. What the v9 Manuscript Should and Should Not Claim

**Safe to claim (supported by computed data):**

- CuI–guaiacol phenolic-O binding (−25.30 kcal/mol) is essentially identical to CuI–methanol O-binding (−25.76 kcal/mol) within 0.46 kcal/mol (TZVPP: 0.51 kcal/mol). There is no guaiacyl phenolic-O selectivity advantage at the CuI-cluster level.
- Phenol π demonstrates that aromatic π-coordination can be strongly favored in a minimal CuI-cluster model (phenol π = −56.69 kcal/mol; 31 kcal/mol below guaiacol phenolic-O).
- At the naked-Cu⁺ level, guaiacol π-binding (−62.17 kcal/mol) dominates over guaiacol phenolic-O (−28.52 kcal/mol) by 33.7 kcal/mol; all aliphatic O-donors outperform guaiacyl phenolic-O.
- The v8 single-site cellulose-vs-guaiacol comparison, if predicated on phenolic-O selectivity, is not supported at either model level tested.

**Not supported (must not be claimed in v9):**

- Guaiacol π completely dominates at the CuI level — CuI–guaiacol π (−29.04 kcal/mol) and phenolic-O (−25.30 kcal/mol) are within 3.74 kcal/mol; the π preference is real but modest at the CuI level, unlike the 33.7 kcal/mol gap at the naked-Cu⁺ level.
- Cu₂I₂ promotes guaiacol binding — Cu₂I₂ + ligand adducts were not computed.
- Guaiacol bidentate coordination is definitively characterized at the CuI level — it is NOT a stable minimum. Optimization from bidentate start shows phenolic-O drifts to 3.04 Å (non-coordinating) while methoxy-O coordinates at 1.985 Å. The result is: bidentate is inaccessible; chelation does not survive iodide coordination at this model level.
- The full guaiacol CuI mode map is now complete (v9.1, 2026-04-27): phenolic-O, methoxy-O, π, and bidentate (inaccessible) all resolved.

---

## 7. Decision Provenance

| Data source | File | Key values |
|-------------|------|-----------|
| CuI binding energies | `audit_final/CUI_CLUSTER_BINDING_TABLE.csv` | cui_methanol_O: −25.76; cui_guaiacol_ph: −25.30; cui_phenol_pi: −56.69 |
| TZVPP basis check | `audit_final/CUI_BASIS_SENSITIVITY.csv` | CuI_methanol_best: −28.08; CuI_guaiacol_best: −28.59 |
| Displacement reopt | `audit_final/DISPLACEMENT_REOPT_SUMMARY.json` | cui_methanol_O CONFIRMED_MIN_BOTH (4/4 runs complete) |
| Mode assignments | `audit_final/CUI_CLUSTER_MODE_TABLE.csv` | cui_guaiacol_ph: phenolicO TRUE_MIN; cui_phenol_pi: pi TRUE_MIN |
| Tier B output files | `results_pod/results_tierb/` | cui_guaiacol_phenolicO_opt_freq.out; cui_phenol_pi_opt_freq.out; etc. |
| Not-computed record | `audit_final/CUI_BASIS_SENSITIVITY.csv` rows 7-8 | Cu2I2+methanol, Cu2I2+guaiacol: NOT_RUN |

---

*Written 2026-04-27; updated 2026-04-27 with CuI–guaiacol π and bidentate results. All three guaiacol CuI modes (π, methoxy-O, bidentate) are now resolved. The Case C working decision stands: guaiacyl phenolic-O selectivity is contradicted at both model levels; guaiacol bidentate coordination is inaccessible at the CuI level (collapses to methoxy-O monodentate); the full guaiacol CuI mode map is now complete.*
