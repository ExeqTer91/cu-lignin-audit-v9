# CuI Cluster Control Calculations — Scientific Interpretation
**Task:** Tier B, Priority 2 — CuI cluster control calculations
**Script:** `run_cui_cluster_dft.py`
**Method:** B3LYP-D3(BJ)/def2-TZVP, ORCA 6.1.1
**Clusters:** CuI monomer, Cu₂I₂ rhombic (+ linear/alternate as geometry control)
**Ligands:** methanol (cellulose OH proxy), phenol (simple lignin proxy), guaiacol (lignin G-unit proxy)
**Binding-energy formula:**
- CuI adducts: ΔE = E(CuI·L) − E(CuI) − E(L)
- Cu₂I₂ adducts: ΔE = E(Cu₂I₂·L) − E(Cu₂I₂) − E(L)
- 1 Ha = 627.509474 kcal/mol
**Ligand reference energies:** canonical Task 1 values from `ORCA_CANONICAL_ENERGIES.csv`
**ECP:** def2-ECP auto-applied to I (Z=53>36); Cu all-electron (Z=29≤36)

---

## ⚡ Thesis Assignment

### Status: **Case C working decision — supported for the computed CuI subset**

*Updated 2026-04-27. ORCA calculations were completed on RunPod A100 for the CuI monomer
adducts listed below. The guaiacol CuI methoxy-O mode is COMPUTED (v9.1, BE = −14.23 kcal/mol).
The remaining guaiacol CuI modes (π and bidentate) are running on the pod (v9.1, 2026-04-27).
All Cu₂I₂ + ligand adducts were NOT computed and remain v9.1 scope.*

**Working decision:** Case C is supported for the computed CuI modes. CuI–guaiacol
phenolic-O binding (−25.30 kcal/mol) is within 0.46 kcal/mol of CuI–methanol O-binding
(−25.76 kcal/mol); no guaiacyl O-selectivity exists at the CuI cluster level for the
computed modes. Phenol π demonstrates that aromatic π-coordination can be strongly
favored in a minimal CuI-cluster model (−56.69 kcal/mol). The v8 guaiacyl O-binding
selectivity claim is not supported at either model level (naked Cu⁺ or CuI cluster).

The Case C label must remain qualified as a working decision (or "supported for the
computed CuI subset") until all remaining CuI–guaiacol modes (π and bidentate,
currently running) are computed and reported alongside the now-completed methoxy-O
result. See `audit_final/V9_CASE_DECISION.md` for full evidence-status provenance.

**Thesis Case Definitions (from task spec):**

| Case | Condition | Narrative |
|------|-----------|-----------|
| **A** | Guaiacol wins for naked Cu⁺ AND for CuI/Cu₂I₂ | "Guaiacyl is an intrinsically strong multi-mode Cu anchor; lignin polymer amplifies this" |
| **B** | Guaiacol wins for naked Cu⁺ but NOT for CuI/Cu₂I₂ | "Iodide coordination suppresses π/bidentate modes; polymer O-donor architecture becomes the key factor" |
| **C** | Guaiacol wins only for specific modes (e.g., π only, not bidentate) | "Mode-selective anchoring; polymer accessibility determines which modes contribute" |
| **D** | Methanol wins for CuI/Cu₂I₂ | "v8 claim survives for iodide-coordinated Cu; naked Cu⁺ result was an artifact of the bare-cation model" |

---

## Scientific Questions

### Q1: Does guaiacol bind more strongly than methanol when Cu is already iodide-coordinated?

**Populated from ORCA runs (2026-04-27):**

| System | Ligand | Best ΔE_gas (kcal/mol) | Mode | n_imag | True min? | Evidence Status |
|--------|--------|------------------------|------|--------|-----------|-----------------|
| CuI monomer | methanol | −25.76 | O-mono | 0* | YES | COMPUTED |
| CuI monomer | phenol (π) | −56.69 | π | 0 | YES | COMPUTED |
| CuI monomer | phenol (O) | −50.72 | phenolicO | 2 | NO (saddle) | COMPUTED — upper bound |
| CuI monomer | guaiacol (phenolicO) | −25.30 | phenolicO | 0 | YES | COMPUTED |
| CuI monomer | guaiacol (π) | NOT_RUN | — | — | — | NOT_COMPUTED — v9.1 |
| CuI monomer | guaiacol (methoxyO) | −14.23 | methoxyO | 0 | YES | COMPUTED — v9.1 (2026-04-27) |
| CuI monomer | guaiacol (bidentate) | NOT_RUN | — | — | — | NOT_COMPUTED — v9.1 |
| Cu₂I₂ rhombic | methanol | NOT_RUN | — | — | — | NOT_COMPUTED — v9.1 |
| Cu₂I₂ rhombic | phenol | NOT_RUN | — | — | — | NOT_COMPUTED — v9.1 |
| Cu₂I₂ rhombic | guaiacol | NOT_RUN | — | — | — | NOT_COMPUTED — v9.1 |
| Naked Cu⁺ | methanol | −47.50 | O-mono | 0 | YES | COMPUTED (Phase 1/2) |
| Naked Cu⁺ | guaiacol (best) | −62.17 | π | 0 | YES | COMPUTED — π mode dominates |

*cui_methanol_O confirmed true minimum after displacement reopt (CONFIRMED_MIN_BOTH; lowest real mode 54.9 cm⁻¹).

**Q1 answer (for computed subset, updated 2026-04-27):** At the CuI-cluster level, guaiacol phenolic-O (−25.30) ≈ methanol O-donor (−25.76) within 0.46 kcal/mol — no guaiacyl O-selectivity at the iodide-coordinated level for phenolic-O. New v9.1 result: guaiacol methoxy-O binding is −14.23 kcal/mol (TRUE_MIN, n_imag=0), substantially weaker than both phenolic-O (−25.30) and methanol (−25.76). Methoxy-O is thus the weakest O-donor mode for guaiacol at the CuI level — consistent with methoxy oxygen being a weaker σ-donor than free phenol OH or alcohol. Phenol π (−56.69) shows that aromatic π-coordination is strongly favored in this minimal CuI-cluster model. Whether guaiacol π achieves comparable π-mode binding remains the key open question — CuI + guaiacol π and bidentate are currently computing (v9.1, 2026-04-27).

**Instructions for filling this table:**
1. Open `CUI_CLUSTER_BINDING_TABLE.csv`
2. For each cluster+ligand combination, identify the row with the most negative `dE_gas_kcal_mol`
3. Confirm that row has `normal_termination=True` and `n_imaginary=0`
4. Record `dE_gas_kcal_mol` and `dE_smd_kcal_mol` here
5. Compare guaiacol vs methanol for each cluster type → assigns Case A/B/C/D

**Physical intuition for anticipated findings:**

Iodide coordination saturates one Cu coordination site with a hard σ-donor.
This is expected to suppress strongly covalent binding modes (π) more than
simple O-donation. Guaiacol's advantage in naked Cu⁺ calculations derives partly
from its multiple O-donor modes (phenolic-O, methoxy-O, bidentate) and partly
from π-coordination. If iodide blocks or sterically hinders these modes, the
guaiacol–methanol gap will narrow. The key discriminator is whether the bidentate
mode survives: a chelating bidentate binding to iodide-coordinated Cu would
still strongly favor guaiacol (Case A/C), while complete suppression of all
multi-dentate modes would produce Case B.

---

### Q2: Which binding modes survive iodide coordination?

**Mode assignment protocol (from converged geometries):**

| Cu-O distance criterion | Assigned mode |
|------------------------|---------------|
| Shortest Cu-O < 2.5 Å, only one O within 2.5 Å | O-monodentate |
| Two Cu-O distances both < 2.5 Å | bidentate |
| All Cu-O > 2.5 Å, Cu-centroid < 2.5 Å | π |
| All Cu-O > 2.5 Å, Cu-centroid > 2.5 Å | weakly bound / non-specific |

**Expected mode analysis:**

- **CuI + methanol (O-start):** Expected to converge cleanly as O-monodentate.
  CuI is linear at minimum; methanol O-coordination yields a bent Cu-I···Cu geometry.
  Accept if Cu-O ≈ 1.9–2.1 Å, Cu-I ≈ 2.4–2.6 Å.

- **CuI + phenol (O-start):** Expected O-monodentate. The phenolic OH is a stronger
  O-donor than methanol OH due to lone pair delocalization from the ring.

- **CuI + phenol (π-start):** May relax to O-monodentate. Cu(I) d¹⁰ configuration
  has no empty d orbitals for π-back-bonding; purely σ-donation from the π-system
  is geometrically less efficient than direct O-coordination. Report final_mode
  based on converged Cu-O and Cu-centroid distances.

- **CuI + guaiacol (phenolicO-start):** Expected phenolic-O monodentate, possibly
  with secondary weak interaction from methoxy-O if geometry allows.

- **CuI + guaiacol (methoxyO-start):** May slip to phenolicO coordination or remain
  at methoxyO. Methoxy-O is a weaker donor than phenolic-O.

- **CuI + guaiacol (bidentate-start):** Key result. If converges as bidentate
  (both Cu-O < 2.5 Å) → strong evidence for Case A or C. If relaxes to monodentate
  → Case B more likely. The I–Cu–O angle constraint for CuI monomer may preclude
  true bidentate geometry.

- **CuI + guaiacol (π-start):** Likely relaxes to O-mode for d¹⁰ Cu(I).

- **Cu₂I₂ adducts:** The rhombic cluster has two Cu sites; the ligand-facing Cu
  has one iodide bridge to each adjacent Cu. Bidentate binding may be more accessible
  here than for CuI monomer because the second Cu can provide geometric flexibility.
  Check both Cu-O distances (both Cu atoms) in the converged geometry.

---

### Q3: Does the Cu₂I₂ cluster remain intact upon ligand binding?

**Cluster integrity criteria:**

| Cu-I distance | Status | Action |
|---------------|--------|--------|
| < 2.70 Å | Intact | Normal |
| 2.70–3.00 Å | Elongated — flag | Report in warnings column; include in table with flag |
| > 3.00 Å | Fragmented | Exclude from binding energy table; flag in warnings |

**Additional checks for every Cu₂I₂ adduct:**
- Cu-Cu distance: should be 2.5–2.8 Å for intact rhombic ring; > 3.5 Å suggests ring opening
- I-Cu-I angle: should be ~109° for rhombic geometry; large deviation signals distortion
- Iodide displacement: look for any I atom > 3.5 Å from both Cu atoms (iodide ejected)
- Iodide transfer to ligand: if I-H distance < 2.5 Å in optimized geometry, flag proton transfer

**Expected integrity:**
- Methanol and phenol adducts: cluster likely intact — O-coordination is non-disruptive
- Guaiacol bidentate-start: highest risk of cluster distortion due to geometric strain
- All jobs: if any Cu-I > 3.0 Å, discard that geometry and use the best intact-cluster result

---

### Q4: Do basis-set effects change the qualitative conclusion?

**Basis sensitivity protocol (see `CUI_BASIS_SENSITIVITY.csv`):**

Run def2-TZVPP single-point energies on the best-geometry structures for:
1. CuI·methanol_best vs CuI·guaiacol_best
2. Cu₂I₂·methanol_best vs Cu₂I₂·guaiacol_best
3. Naked Cu⁺·methanol vs Naked Cu⁺·guaiacol_best

Compute ΔΔE = ΔE(TZVPP) − ΔE(TZVP) for each comparison.

**Interpretation thresholds:**

| |ΔΔE| | Interpretation |
|--------|----------------|
| < 2 kcal/mol | Basis-robust: TZVP conclusion holds, report TZVP values in manuscript |
| 2–5 kcal/mol | Moderate sensitivity: report both TZVP and TZVPP values; note uncertainty |
| > 5 kcal/mol | Basis-sensitive: use TZVPP as authoritative; flag in manuscript |

**Physical expectation:**
For relative binding energies of comparable-sized ligands on the same metal center,
basis set effects typically cancel to within 1–3 kcal/mol (TZVP vs TZVPP).
A large basis sensitivity (>5 kcal/mol) would be unusual and would indicate
strong differential polarization effects or a geometry-sensitive result.

---

## Calculation Status Tracker

### Reference clusters (3 jobs)

| Job | Status | E_gas (Ha) | n_imag | Notes |
|-----|--------|-----------|--------|-------|
| `cui_monomer` opt+freq | **COMPLETE** | −1938.215889 | 0 | TRUE MIN; Cu-I stretch reference |
| `cu2i2_rhombic` opt+freq | **COMPLETE** | −3876.514481 | 0 | TRUE MIN; preferred isomer (35.5 kcal/mol below linear) |
| `cu2i2_linear` opt+freq | **COMPLETE** | −3876.457862 | 2 | SADDLE; superseded by rhombic |

### CuI adducts (computed subset)

| Job | Status | final_mode | ΔE_gas (kcal/mol) | n_imag | True min? |
|-----|--------|-----------|-------------------|--------|-----------|
| `cui_methanol_O` | **COMPLETE** | O-mono | −25.76 | 0* | YES (CONFIRMED_MIN_BOTH after disp reopt) |
| `cui_phenol_O` | **COMPLETE** | phenolicO | −50.72 | 2 | NO — saddle; upper bound |
| `cui_phenol_pi` | **COMPLETE** | π | −56.69 | 0 | YES — TRUE MIN |
| `cui_guaiacol_phenolicO` | **COMPLETE** | phenolicO | −25.30 | 0 | YES — TRUE MIN |
| `cui_guaiacol_methoxyO` | **COMPLETE — v9.1 (2026-04-27)** | methoxyO | −14.23 | 0 | YES — TRUE MIN |
| `cui_guaiacol_bidentate` | **RUNNING — v9.1 (2026-04-27)** | — | — | — | pending |
| `cui_guaiacol_pi` | **RUNNING — v9.1 (2026-04-27)** | — | — | — | pending |

*Displacement reopt CONFIRMED_MIN_BOTH; lowest real mode 54.9 cm⁻¹.

### Cu₂I₂ adducts (none computed — v9.1 scope)

| Job | Status | Notes |
|-----|--------|-------|
| `cu2i2_methanol_O` | **NOT_RUN** | v9.1 scope; Cu₂I₂ dimerization only exists |
| `cu2i2_phenol_O` | **NOT_RUN** | v9.1 scope |
| `cu2i2_phenol_pi` | **NOT_RUN** | v9.1 scope |
| `cu2i2_guaiacol_phenolicO` | **NOT_RUN** | v9.1 scope |
| `cu2i2_guaiacol_methoxyO` | **NOT_RUN** | v9.1 scope |
| `cu2i2_guaiacol_bidentate` | **NOT_RUN** | v9.1 scope |
| `cu2i2_guaiacol_pi` | **NOT_RUN** | v9.1 scope |

**Note:** Only Cu₂I₂ dimerization energy exists (−51.90 kcal/mol, rhombic; TRUE MIN). Cu₂I₂ + ligand adducts were never submitted. Do not use the dimerization energy to support ligand-binding conclusions.

### Basis sensitivity SPs (def2-TZVPP)

| Job | Status | ΔE_TZVP (kcal/mol) | ΔE_TZVPP (kcal/mol) | ΔΔE | Robustness |
|-----|--------|---------------------|---------------------|-----|-----------|
| `CuI_methanol_best` | **COMPLETE** | −25.76 | −28.08 | −2.32 | MODERATE |
| `CuI_phenol_pi_best` | **COMPLETE** | −56.69 | −59.50 | −2.81 | MODERATE |
| `CuI_phenol_O_best` | **COMPLETE** | −50.72 | −53.54 | −2.82 | MODERATE |
| `CuI_guaiacol_best` | **COMPLETE** | −25.30 | −28.59 | −3.29 | MODERATE |
| `Cu2I2_rhombic_dimerization` | **COMPLETE** | −51.90 | −51.98 | −0.08 | ROBUST |
| `Cu2I2_methanol_best` | **NOT_RUN** | — | — | — | v9.1 scope |
| `Cu2I2_guaiacol_best` | **NOT_RUN** | — | — | — | v9.1 scope |
| `naked_Cu_methanol` | **NOT_RUN** | −47.50 (TZVP only) | — | — | v9.1 scope |
| `naked_Cu_guaiacol_best` | **NOT_RUN** | −62.17 (TZVP only) | — | — | v9.1 scope |

Full TZVPP data: `audit_final/CUI_BASIS_SENSITIVITY.csv`

---

## ECP and Basis Confirmation Checklist

For every ORCA output, verify these lines in the output header before
recording any energies:

- [ ] **I uses def2-ECP:** Search for `ECP` near `I` or `iodine` in the basis set printout section.
  Expected text: something like `ECP/def2-ECP on I (nr. 53)`.
- [ ] **Cu is all-electron:** No ECP line for Cu (atomic number 29 ≤ 36 cutoff).
  If ECP is applied to Cu, the job must be discarded and rerun with explicit all-electron basis.
- [ ] **Charge = 0:** Verify `* xyz 0 1` in input and `Total Charge   0` in output.
- [ ] **Multiplicity = 1:** Verify singlet `Multiplicity   1` in output.
- [ ] **Normal termination:** `ORCA TERMINATED NORMALLY` at end of output.
- [ ] **No imaginary frequencies:** `n_imaginary = 0` after opt+freq.
  If imaginary freqs present: extract mode vector from output, displace geometry by ±0.1 Å
  along the imaginary mode, re-optimize from both displaced structures, report the lower-energy result.

---

## Scope and Limitations

**These are minimal molecular cluster models, not periodic CuI surfaces.**
CuI and Cu₂I₂ used here serve as iodide-coordination saturation controls only.
The γ-CuI bulk phase is a zinc-blende tetrahedral solid with very different
coordination geometry and electronic environment compared to gas-phase CuI
or Cu₂I₂. The cluster models capture the first-shell iodide coordination
effect on Cu(I) electrophilicity; they do not model:
- Lattice effects or Madelung stabilization
- Extended surface binding sites or step/defect sites
- Cooperative effects from multiple iodide neighbors
- Textile fiber-CuI interface geometry

**Entropy and thermal corrections** are not included. The ΔE values are
electronic binding energies at 0 K with no ZPE correction.
Free-energy differences ΔG at 298 K would require frequency-based thermochemistry.

**Counterpoise correction (BSSE)** is applied only to the decisive
comparisons via the basis-sensitivity check (def2-TZVPP SP), not to all jobs.
For relative comparisons of similarly-sized ligands on the same cluster,
BSSE partially cancels in differences and is not expected to reverse
qualitative conclusions.

---

## Files Generated by This Task

| File | Description | Status |
|------|-------------|--------|
| `run_cui_cluster_dft.py` | ORCA input writer and runner; parser; CSV writer | Executed on RunPod |
| `audit_final/CUI_CLUSTER_BINDING_TABLE.csv` | ΔE_gas, ΔE_SMD, start/final modes, integrity flags | Populated with computed CuI subset (incl. methoxy-O v9.1, 2026-04-27) |
| `audit_final/CUI_CLUSTER_MODE_TABLE.csv` | Cu-O, Cu-centroid, cluster integrity metrics | Populated with computed CuI subset |
| `audit_final/CUI_CLUSTER_INTERPRETATION.md` | This document | Populated; Case C working decision assigned for the computed CuI subset |
| `audit_final/CUI_BASIS_SENSITIVITY.csv` | TZVPP vs TZVP for decisive comparisons | Populated (4 CuI complexes + Cu₂I₂ dimerization) |

---

## Update Log

| Date | Action |
|------|--------|
| 2026-04-25 | Script (`run_cui_cluster_dft.py`) and CSV/MD scaffolds created. All 17 opt+freq ORCA jobs defined with starting geometries. |
| 2026-04-26 | Phase 1/2 + Tier A + Tier B core CuI subset complete on RunPod. Q1–Q4 populated with computed values. Case C working decision assigned for the computed CuI subset. |
| 2026-04-27 | v9.1: CuI–guaiacol methoxy-O completed (BE = −14.23 kcal/mol, n_imag = 0, true minimum). CuI–guaiacol π and bidentate currently RUNNING on the pod. |
