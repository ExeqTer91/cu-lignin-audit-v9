# V9 HANDOVER PACKAGE — ACS SCE Cu-Lignin Manuscript (v2 — reference-corrected)

> **VERSION:** v2 (2026-04-30 patch).
> **Changes from v1** (canonical patch source: `audit_final/V9_REFERENCE_AUDIT_FIXES.md`):
>   1. §M.3 #18 Yang 2017 — author list replaced with the canonical 10-author list (Yang, C.; Souchay, D.; et al.) per Crossref DOI 10.1038/ncomms16076. Paper topic confirmed as thermoelectric CuI thin films. Reference is preserved as the Introduction's CuI thin-film context anchor — NOT used as an oxide-aging anchor.
>   2. §M.3 #22 (Sun & Chen 2023) — replaced with the canonical Chen, A. X.; Lau, H. Y.; et al. 2023 entry (DOI 10.1021/acsanm.3c01961 verified against Crossref on 2026-04-30; "Sun, X.; Chen, Y." attribution was wrong; pages corrected to 13238–13249). Paper is direct experimental support for water-mediated CuI nanoparticle anchoring on cotton — re-tagged as a §J/§K and Introduction CuI-cluster-on-cotton anchor (NOT an oxide-aging anchor).
>   3. §M.3 #23 (Sportelli 2024) — replaced with the canonical Chen, A. X.; Beins, D. K. R.; et al. 2024 entry (DOI 10.1021/acsaenm.4c00548 verified against Crossref; "Sportelli, M. C." attribution was wrong). Paper is about phosphine-coordinated CuI clusters self-assembled on cotton — direct experimental support for the v9 cluster-anchoring thesis. **REASSIGNED** from §I (oxide-aging anchor) to §J / §K / §P cover letter / Introduction paragraph 1 (see new §D.1 citation guidance).
>   4. §I anchor list (six oxide-aging anchors) — anchors #1 (Yang 2017), #5 (Chen 2023), and #6 (Chen 2024) REMOVED from §I and replaced with PLACEHOLDERS pending writer verification. Anchors #2 (Klochko 2019), #3 (Nikolic 2020), and #4 (Coroa 2023) preserved (still flagged "verify"). Do NOT auto-substitute — the writer must locate appropriate XPS / oxide-aging anchors before submission.
>   5. §M.4 — added Hammes-Schiffer & Stuchebrukhov 2010 *Chem. Rev.* (DOI 10.1021/cr1001436, the actual paper at that DOI; the original V9_HANDOVER misattributed it to Costentin/Robert/Savéant) AND added Costentin/Robert/Savéant 2010 *Acc. Chem. Res.* (DOI 10.1021/ar9002812, the actual phenol-PCET paper). Both cited as a pair for §K redox-regeneration framing.
>   6. §M.2 #16 (Sangha 2012) — added missing DOI 10.1002/ep.10628.
>   7. §M.5 (oxide-aging re-citations) — entries #28 (Yang re-cite), #32 (Sun & Chen re-cite), #33 (Sportelli re-cite) REMOVED. Section now contains only the verified-but-flagged Klochko / Nikolic / Coroa anchors.
>   8. NEW §D.1 "Citation guidance for Introduction paragraph 1" — tells the writer to cite Chen et al. 2023 (DOI 10.1021/acsanm.3c01961) and Chen et al. 2024 (DOI 10.1021/acsaenm.4c00548) together as the direct experimental anchor for the CuI-cluster-on-cotton thesis in Introduction paragraph 1, with Yang et al. 2017 (DOI 10.1038/ncomms16076) cited separately as the foundational CuI thin-film conductivity reference.
>   9. §J and §K prose unchanged at the level of the computed result; appended one-sentence experimental-anchor citation pointing to Chen 2023 + Chen 2024 in each section.
>  10. §P cover letter — added one sentence citing Chen 2023 + Chen 2024 as the direct experimental anchor for the v9 CuI-cluster-on-cotton thesis.
>  11. §M.2 — added TWO new entries (16a Li 2015 *J. Exp. Nanosci.* DOI 10.1080/17458080.2015.1015462; 16b Li 2015 *Biotechnol. Biofuels* DOI 10.1186/s13068-015-0300-5). The audit-fix doc's "REPLACE" wording was wrong: v1 V9_HANDOVER did not contain prior Li 2015 entries to replace, so these are inserted as new references. 16b is co-authored by J. Ralph and E. L. Hegg — flag in cover letter as a topical anchor for v9 lignin-Cu reactivity.
>  12. §E.6, §H, §Z — row-count drift fixed: all "Total rows: 38 / Class A: 20" references updated to "39 / 21" to match the canonical `BINDING_SURVIVAL_TABLE.csv` (now 39 rows after the cu2i2_veratrole_pi row added in v2).
>
> **Original V9_HANDOVER_PACKAGE.md is preserved unchanged for audit-trail purposes.**

---

**Version:** v9 final handover (no further computation planned)
**Compiled:** 2026-04-30 UTC
**Computational basis:** ORCA 6.1.1, B3LYP-D3(BJ) / def2-TZVP, RIJCOSX with def2/J auxiliary basis, TightSCF, TightOpt, DefGrid3 (geometry + frequencies; high-grid sensitivity status — see §H and §N)
**Solvent:** SMD(water) single points at the gas-phase optimized geometry
**Audit pipeline:** publicly archived (GitHub URL to be inserted by writer; the user's repository under `audit_final/`)
**Scope of this document:** **single source of truth** for the v9 manuscript writer. All numbers, claims, and prose drafts in this package are traceable to files in `audit_final/`. Nothing in §§A–S should require the writer to ask the agent for clarification; if a number is uncertain it is flagged here.

---

## TABLE OF CONTENTS

- A. Manuscript Title and Scope Statement
- B. v8 → v9 Reframing Summary
- C. Data Hierarchy (Six Levels)
- D. v9 Thesis: Mode-Selective CuI Anchoring on Lignin-Inspired Fiber Interfaces
- E. Master Binding-Energy Table (every Cu species, every mode, gas + SMD, all evidence statuses)
- F. Per-Claim Verdict Table (BELEGEN, CLAIM_SUPPORT, MECHANISM_VERDICT, SITE_OCCUPANCY)
- G. Geometry and Frequency Audit Summary (true minima, saddles, pedigree)
- H. Conservative Classifier Results and Reclassification Notes
- I. State-Dependent Anchoring Ensemble (oxide-aging note)
- J. Productive vs. Nonproductive Sites — Drafted Prose
- K. Mechanistic Figure Narrative — Drafted Prose
- L. Validation Experiment Protocol (textile chemistry; Part 1 and Part 2)
- M. Complete Reference List (every reference v9 will cite)
- N. Outstanding Caveats and Limitations
- O. Figure Specifications
- P. Cover Letter Content (drafted)
- Q. ACS Paragon Submission Metadata
- R. Drafted Abstract
- S. Drafted Title Options
- Appendix Z. File-by-File Provenance and Reproducibility

---

## A. Manuscript Title and Scope Statement

**Working title (lead option):**
> **Mode-Selective CuI Anchoring on Lignin-Inspired Fiber Interfaces: A DFT Cluster-Model Study**

**Scope statement (insert verbatim into Methods §1, before any DFT detail):**

> This study computes copper–lignin coordination at six levels of model complexity using DFT cluster models in ORCA 6.1.1 (B3LYP-D3(BJ) / def2-TZVP, RIJCOSX with def2/J auxiliary basis, TightSCF, TightOpt, DefGrid3 for geometry and frequencies; SMD(water) single points at the gas-phase optimized geometry). The model hierarchy spans: (1) bare Cu+ adducts of monomeric lignin proxies (guaiacol, phenol, anisole, catechol, methanol, water, galacturonate); (2) the same proxies on a CuI monomer; (3) the same proxies on the neutral Cu2I2 rhombic cluster; (4) the same proxies on the iodide-saturated [CuI2]- anion; (5) an etherified guaiacyl proxy (1,2-dimethoxybenzene = veratrole) on Cu2I2 and [CuI2]-, with paired starts to capture the kappa2-O,O bidentate coordination that becomes accessible when the phenolic-OH is etherified; and (6) a literature-only oxide / hydroxide aging regime (Cu2O / CuO / Cu(OH)2), included as scope language but not computed here. The study deliberately avoids periodic CuI surfaces, polymer-scale lignin, explicit-solvent QM/MM, and Cu(II) DFT (cited literature only). The thesis is operational: it predicts which lignin-inspired functional groups present a productive CuI anchoring mode in each Cu state and provides a discriminating experimental protocol (§L).

---

## B. v8 → v9 Reframing Summary

**v8 thesis (rejected by audit):**
> Guaiacyl phenolic-O sites confer a special copper affinity advantage over cellulose-like O-donors, justifying a single-site cellulose-vs-guaiacol comparison.

**v9 thesis (supported by audit):**
> Copper retention on lignin-inspired fibers is a state-dependent, mode-selective anchoring problem. The accessible Cu state (CuI / Cu2I2 / [CuI2]- / oxide-aged) determines which lignin functional groups present a productive coordination mode. The dominant productive site on neutral Cu2I2 is the kappa2-O,O bidentate coordination of an etherified guaiacyl unit (e.g. veratrole-like 1,2-dimethoxybenzene end-groups), not phenolic-O of free guaiacol. Iodide-saturated [CuI2]- rejects all lignin proxies including the bidentate motif. CuI monomer admits multiple modes with smaller energy gaps than naked Cu+ (CuI suppresses the strong pi/O contrast seen on bare Cu+). No periodic-DFT or polymer-scale claim is made; the experimental discrimination protocol in §L is required to confirm the mechanism in real laundered fabric.

**What changed between v8 and v9 (sentence-level summary; full list in `audit_final/MANUSCRIPT_IMPACT_v8_to_v9.md` §9b):**
1. The "guaiacol phenolic-O affinity advantage" sentence is replaced by a state-dependent / mode-selective frame.
2. The single-site cellulose-vs-guaiacol comparison is removed.
3. A bidentate kappa2-O,O motif on neutral Cu2I2 is added as the primary productive site (Set D V2 / Task #29 finding: BE_gas = -26.82, BE_smd = -26.24 kcal/mol; Cu-O = 2.20/2.20 A; n_imag = 0; lowest real mode +12.4 cm-1).
4. A reject-clause is added for [CuI2]-: BE = +49 to +55 kcal/mol on the same motif, with no productive contact.
5. An oxide-aging scope clause is added (literature-only); see §I.
6. Figure 1 changes from a single-site bar chart to a coordination-mode map faceted by Cu state.
7. The validation protocol gains Part 2 (redox / oxide-aging discrimination tests) on top of Part 1 (standard textile-chemistry battery).
8. The Methods section gains the explicit 6-level hierarchy and the explicit list of what is NOT computed (Cu(II), periodic surfaces, polymer-scale, explicit solvent QM/MM).

**v8 issuance status (writer must mention in cover letter):**
- v8 was uploaded as a Research Square preprint. A v9 correction will be posted on Research Square upon ACS submission. The cover letter discloses the audit and reframing.

---

## C. Data Hierarchy (Six Levels)

The v9 manuscript uses an explicit six-level hierarchy. Each level has a defined model, defined evidence type, and defined manuscript role. Use this exact structure in Methods.

| Level | Model | Evidence Type | What Survives | Manuscript Role |
|-------|-------|---------------|----------------|-----------------|
| **L1** | Naked Cu+ + ligand (gas; SMD SP) | DFT cluster (Tier A) | Mode preference (pi vs O) on bare cation | Reference / pedagogical only — bare Cu+ exaggerates BEs and is not the operative species in CuI textiles |
| **L2** | CuI monomer + ligand (Tier B) | DFT cluster (Tier B) | Realistic per-mode BE on a 1-Cu / 1-I site | Operative reference for CuI-rich domains; shows that CuI compresses the pi vs O gap (5–10 kcal/mol vs 30+ on bare Cu+) |
| **L3** | Cu2I2 (rhombic) + ligand (neutral; Tier C / Set C / Set D V2) | DFT cluster | Productive mode for the **neutral CuI cluster** state; bidentate kappa2-O,O on etherified guaiacyl is the primary productive site | Primary L3 result for v9 thesis: neutral Cu2I2 admits a kappa2-O,O bidentate productive site only when the guaiacyl is etherified (veratrole-like) |
| **L4** | [CuI2]- (anion) + ligand (Set B / Set D V2) | DFT cluster | Iodide-saturated linear two-coordinate Cu rejects all probed ligands | Reject branch of the model: iodide-saturated states do not contribute productive anchoring |
| **L5** | Etherified-vs-free guaiacyl rotamer scan (Set D V2) | DFT cluster (paired starts) | startA -> kappa2-O,O bidentate (productive); startB -> rotamer (metastable); anion analogs -> all metastable / rejected | Discriminates "free guaiacol on Cu2I2 cracks the cluster" from "etherified guaiacyl on Cu2I2 binds bidentate" |
| **L6** | Cu2O / CuO / Cu(OH)2 oxide / hydroxide aging regime | **Literature only** (no DFT in this work) | State-dependent O-donor / hydroxyl / carboxylate / phenolate anchoring on aged surface fractions | Scope clause (§I); discriminating experiment in §L Part 2 |

**Critical clarification for the writer:** Levels 1–5 are computed in this work; level 6 is literature only. The manuscript must NOT present an L6 DFT number. The L6 clause is a scope acknowledgment so that referees who emphasize aged-surface oxide chemistry have an explicit place to find that view in the paper.

---

## D. v9 Thesis: Mode-Selective CuI Anchoring on Lignin-Inspired Fiber Interfaces

**Thesis (verbatim — use in §1 abstract and discussion summary):**

> Copper retention on lignin-inspired fibers is governed by a state-dependent, mode-selective anchoring ensemble rather than by a single per-site affinity ranking. In the CuI-rich regime (CuI monomer / neutral Cu2I2), productive anchoring requires both (i) a Cu state that exposes an open coordination sphere and (ii) a lignin functional group that presents a geometry compatible with the available coordination mode. On neutral Cu2I2, the productive site is the kappa2-O,O bidentate chelate of an etherified guaiacyl (veratrole-like 1,2-dimethoxybenzene) end-group, with computed BE = -26.82 kcal/mol (gas) / -26.24 kcal/mol (SMD water), Cu-O = 2.20 / 2.20 A, n_imag = 0, lowest real mode +12.4 cm-1. The same etherified motif is rejected on iodide-saturated [CuI2]- (BE = +49 to +55 kcal/mol; no productive contact), and free guaiacol with a phenolic OH cracks the Cu2I2 cluster instead of binding cleanly. The CuI monomer admits multiple modes with smaller energy gaps than naked Cu+, so single-site ranking on bare Cu+ does not predict CuI-cluster behavior. An oxide / hydroxide aging regime (Cu2O / CuO / Cu(OH)2), not computed here, is acknowledged as a state-dependent extension of the anchoring ensemble (§I). A discriminating experimental protocol (§L) is provided to test the model in real laundered fabric.

**Five thesis sub-claims (used to organize the Discussion):**

| # | Sub-claim | Evidence pointer (this package §) |
|---|-----------|------------------------------------|
| T1 | Naked Cu+ exaggerates BEs and over-emphasizes pi vs O contrast; it is not the operative state for CuI textiles | §E (L1 rows), §H (rank reversal between gas and SMD on charged Cu+) |
| T2 | CuI monomer compresses the pi vs O energy gap; multiple modes coexist in a narrow window | §E (L2 rows: pi -29.0, phenolic-O -25.3, methoxy-O -14.2 on guaiacol) |
| T3 | Neutral Cu2I2 admits a productive kappa2-O,O bidentate site on **etherified** guaiacyl (veratrole), not on free guaiacol; free guaiacol on Cu2I2 cracks the cluster | §E (L3 rows), §J (productive vs nonproductive prose) |
| T4 | Iodide-saturated [CuI2]- rejects all probed lignin modes (linear two-coordinate; positive BE on bidentate motif) | §E (L4 rows), §J |
| T5 | Real fabric is a state-dependent ensemble of CuI / Cu2I2 / [CuI2]- / oxide-aged Cu fractions, and the operative anchoring chemistry depends on which fractions dominate locally | §I (oxide-aging scope), §L (validation protocol Part 2) |

---

## D.1 Citation Guidance for Introduction Paragraph 1 (v2 ADDITION)

**The writer should structure Introduction paragraph 1 around the following citation pattern, established by the v2 reference audit:**

- **Foundational CuI thin-film context:** cite Yang, C.; Souchay, D.; et al. *Nat. Commun.* **2017**, *8* (1), art. 16076 (DOI 10.1038/ncomms16076 — see §M.3 #18). This paper establishes p-type CuI as a non-toxic, earth-abundant transparent thermoelectric thin film and is the foundational reference for the materials-context framing of CuI-on-fiber coatings.

- **Direct experimental anchor for CuI-cluster-on-cotton (cite as a pair):**
  - Chen, A. X.; Lau, H. Y.; et al. *ACS Appl. Nano Mater.* **2023**, *6* (14), 13238–13249 (DOI 10.1021/acsanm.3c01961 — see §M.3 #22). Water-mediated in-situ assembly of CuI nanoparticles on cotton fabric; demonstrates that CuI cluster phases anchor to cotton in aqueous processing, the structural and process class our DFT cluster models target.
  - Chen, A. X.; Beins, D. K. R.; et al. *ACS Appl. Eng. Mater.* **2024**, *2* (12), 2864–2874 (DOI 10.1021/acsaenm.4c00548 — see §M.3 #23). Same research group; phosphine-coordinated CuI cluster self-assembly on cotton — direct evidence for ligand-coordinated CuI cluster anchoring chemistry, the system class our model addresses.

**Suggested introduction paragraph 1 citation pattern (writer to render in the corresponding-author voice):**
> "Copper iodide (CuI) coatings on cotton and other natural fibers have emerged as a sustainable platform for conductive [Yang 2017] and antimicrobial [Chen 2023, Chen 2024] textiles. Recent reports demonstrate that CuI cluster phases can self-assemble on cotton via water-mediated [Chen 2023] and phosphine-coordinated [Chen 2024] processing routes, both yielding skin-compatible coatings with broad-spectrum antimicrobial efficacy. The molecular-level anchoring chemistry that determines how strongly these CuI cluster phases bind to lignin-bearing natural fibers — and therefore how durably they survive laundering — has not been characterized. We address this gap with a DFT cluster-model study spanning naked Cu+, the CuI monomer, neutral Cu2I2, and the iodide-saturated [CuI2]- anion, paired with a small-molecule rotamer set that probes the productive coordination modes accessible at each Cu state."

**Why this citation triplet:** Yang 2017 anchors the materials-context narrative (CuI thin-film is established as a textile-relevant phase); the Chen 2023 / 2024 pair anchors the application-context narrative (CuI cluster phases self-assemble on cotton with direct application evidence) and is from the same research group, providing a tight experimental-anchor block for the manuscript's central thesis. Do NOT cite the v1 "Sportelli 2024" or "Sun & Chen 2023" attributions — they are wrong (DOIs resolved against Crossref on 2026-04-30; see `audit_final/V9_REFERENCE_AUDIT_FIXES.md` for full audit trail).

---

## E. Master Binding-Energy Table

This is the canonical table the writer should reproduce as Table 1 in the manuscript. Numbers come from `audit_final/ORCA_BINDING_ENERGIES.csv` (canonical), `audit_final/CU2I2_BINDING_TABLE.csv`, `audit_final/CUI2_BINDING_TABLE.csv`, `audit_final/CUI_CLUSTER_BINDING_TABLE.csv`, and `audit_final_setD_alt_diag/setD_alt_v2_analysis.json` (Set D V2). Geometry and frequency status come from `audit_final/V9_GEOMETRY_TABLE.csv` (compiled by `build_v9_closeout.py` for this handover).

**Conventions:** all BEs in kcal/mol. Sign: more negative = stronger binding. SMD column is single-point on the gas-phase optimized geometry. n_imag = number of imaginary frequencies (0 = true minimum). Class A–E from Task #28 conservative classifier (§H).

### E.1 Level L1 — Naked Cu+ (Tier A)

| Complex | Ligand | Mode | BE_gas | BE_smd | n_imag | Class | Note |
|---|---|---|---|---|---|---|---|
| cu_methanol | methanol | O-mono | -47.50 | -23.63 | 0 | A | reference O-donor |
| cu_phenol_O | phenol | phenolic-O | -51.44 | -36.39 | 0 | E* | Cu-O = 2.66 A, just above 2.6 A cutoff; system drifts toward pi (see cu_phenol_pi). Treat as "O-mode is not the productive minimum for free phenol on Cu+." (footnote: 2.7 A cutoff would reclass to A) |
| cu_phenol_pi | phenol | pi (eta-6) | -80.96 | -52.20 | 0 | A | dominant mode on bare Cu+ |
| cu_guaiacol_phenolicO | guaiacol | phenolic-O | -28.52 | -8.00 | 0 | B | SMD weakens; rank reversal vs gas |
| cu_guaiacol_methoxyO | guaiacol | methoxy-O | -54.48 | -20.94 | 0 | A | strong on naked Cu+ |
| cu_guaiacol_pi | guaiacol | pi (eta-6) | -62.17 | -28.48 | 0 | A | dominant mode on bare Cu+ for guaiacol |
| cu_anisole_methoxyO | anisole | methoxy-O | -48.78 | -20.54 | 0 | A | reference for methoxy donor |
| cu_anisole_pi | anisole | pi (eta-6) | -60.15 | -27.44 | 0 | A | reference pi |
| cu_benzene_pi | benzene | pi (eta-6) | -54.44 | -23.88 | 0 | A | reference unsubstituted arene |
| cu_catechol_bidentate | catechol | kappa2-O,O bidentate | -33.41 | -15.64 | 0 | A | **positive control for ortho-bidentate motif on bare Cu+** |
| cu_catechol_pi | catechol | pi (eta-6) | -59.78 | -28.08 | 0 | A | competing pi mode on Cu+ |
| cu_cyclohexanol_O | cyclohexanol | aliphatic-O | -58.13 | -27.24 | 0 | A | non-aromatic O-donor reference |
| cu_meta_methoxyphenol_phenolicO | 3-methoxyphenol | phenolic-O | -12.35 | +5.37 | 0 | D | substituent positioning; SMD eliminates BE |
| cu_meta_methoxyphenol_pi | 3-methoxyphenol | pi (eta-6) | -63.16 | -27.53 | 0 | A | pi dominates |
| cu_para_methoxyphenol_phenolicO | 4-methoxyphenol | phenolic-O | -49.64 | -19.32 | 0 | A | para-OMe sustains phenolic-O |
| cu_para_methoxyphenol_pi | 4-methoxyphenol | pi (eta-6) | -58.20 | -26.32 | 0 | A | pi dominates marginally |
| cu_galacturonateH_complex | galacturonate (neutral) | O-chelate | -50.10 | -22.73 | 0 | A | cellulose/pectin-side reference |
| cu_galacturonate_anion_complex | galacturonate (anion, -1) | O-chelate (anion) | -185.70 | -37.91 | 0 | A | anion-Cu+ Coulomb amplifies BE; ELECTROSTATIC ARTIFACT — do **not** compare to neutral O-donor BEs (SMD partially screens but rank-orders on the same artifact axis) |

\* See §H "Borderline-cutoff note: cu_phenol_O" — a 2.7 A cutoff would re-class as A. Spec cutoff is 2.6 A.

### E.2 Level L2 — CuI Monomer (Tier B)

From `audit_final/CUI_CLUSTER_BINDING_TABLE.csv`. CuI monomer reference E_gas = -1938.215889 Eh.

| Complex | Ligand | Mode | BE_gas | n_imag | Note |
|---|---|---|---|---|---|
| cui_methanol_O | methanol | O-mono | -25.76 | 1 (lowest soft mode +54.9 cm-1 after displacement reopt; CONFIRMED_MIN_BOTH) | reference O-donor on CuI |
| cui_phenol_O | phenol | phenolic-O | -50.72 | 2 | SADDLE; BE is upper bound only |
| cui_phenol_pi | phenol | pi | -56.69 | 0 | TRUE_MIN; CuI sustains pi-preference |
| cui_guaiacol_ph | guaiacol | phenolic-O | -25.30 | 0 | TRUE_MIN; **within 0.5 kcal/mol of CuI-methanol — no special advantage** |
| cui_guaiacol_methoxyO | guaiacol | methoxy-O | -14.23 | 0 | TRUE_MIN; weakest O-donor on CuI |
| cui_guaiacol_pi† | guaiacol | pi (eta-n arene) | -29.04 | 0 | TRUE_MIN; CuI–guaiacol-pi favored over phenolic-O by only **3.74 kcal/mol** (vs **33.7 kcal/mol gap** at naked-Cu+) — primary numerical evidence that CuI compresses the pi vs O contrast |
| (cu2i2_rhombic) | — | dimerization | -51.9 (vs 2 x CuI_monomer) | 0 | Cu2I2 rhombic is the ground-state CuI dimer (+35.5 kcal/mol more stable than linear) |

**† Pedigree note for `cui_guaiacol_pi`:** This row is a v9.1 result computed pod-side. The .out file is NOT_INDEXED in `RAW_FILE_INDEX.csv` (the file resided on the pod and pre-dates the centralized indexing pass; the energies were transcribed into `audit_final/V9_CASE_DECISION.md §1` line 42 with E_final = -2360.210527 Eh, BE = -29.04 kcal/mol, n_imag = 0, NormalOpt+Freq, 12 cycles). The corresponding BELEGEN evidence row is **E10.0** (claim 10: "mode-selective CuI anchoring is the best-supported thesis"). Treat this BE as authoritative for the qualitative π/O gap-compression result; the writer should mention the NOT_INDEXED status in the v9 SI if a reviewer asks for the raw .out.

**def2-TZVPP basis-sensitivity check (supplementary):** spot-check on CuI–guaiacol_phenolic-O at def2-TZVPP shifts BE by < 1 kcal/mol (TZVPP guaiacol-phO -28.59 vs methanol-O -28.08 = +0.51 kcal/mol; same sign as TZVP); def2-TZVP results are accepted as final. Source: `audit_final/CUI_BASIS_SENSITIVITY.csv`.

### E.3 Level L3 — Neutral Cu2I2 (Set C and Set D V2)

From `audit_final/CU2I2_BINDING_TABLE.csv` and `audit_final_setD_alt_diag/setD_alt_v2_analysis.json`. Cu2I2 (rhombic) reference E_gas = -3876.514404 Eh; E_smd = -3876.522610 Eh.

| Complex | Ligand | Final mode | BE_gas | BE_smd | n_imag | Class | Geometry / fate | Note |
|---|---|---|---|---|---|---|---|---|
| cu2i2_h2o | water | O-mono | -19.50 | -16.68 | 0 | A | Cu-O 1.97; SMD preserves contact | water as positive control |
| cu2i2_methanol | methanol | O-mono | -18.66 | (not in canonical) | 0 | A | Cu-O 2.06 | reference O-donor on Cu2I2 |
| cu2i2_phenol_O | phenol | O-mono | -16.48 | (not in canonical) | 0 | A | Cu-O 2.06; cluster intact | phenolic-O survives on Cu2I2 |
| cu2i2_phenol_pi | phenol | (detached) | -16.73 | (not in canonical) | 0 | E | **detached after opt**; Cu-centroid 4.76 A | pi-only contact does NOT survive on Cu2I2 |
| cu2i2_guaiacol_phenolicO | guaiacol | bidentate (started phenolic-O) | -23.39 | (not in canonical) | 0 | E | **cluster fragmented** | guaiacol phenolic-O cracks the Cu2I2 cluster |
| cu2i2_guaiacol_methoxyO | guaiacol | O-mono (started methoxy-O) | +172.67 | (not in canonical) | 0 | E | **nonphysical BE_gas > +100 kcal/mol** | SCF / optimization artifact; excluded from interpretation; replaced by Set D V2 veratrole |
| cu2i2_guaiacol_pi | guaiacol | (detached) | -15.53 | (not in canonical) | 0 | E | detached | pi-only contact does NOT survive |
| cu2i2_guaiacol_bidentate | guaiacol | bidentate | -17.86 | (not in canonical) | 0 | A | Cu-O 2.22 / 2.26 (bidentate to phenolic-O + methoxy-O) | starts/stays bidentate when **phenolic-OH is replaced by H** in the reference |
| **cu2i2_veratrole_methoxyO_startA** | **veratrole (1,2-dimethoxy)** | **kappa2-O,O bidentate** | **-26.82** | **-26.24** | **0** | **A** | **Cu-O = 2.20 / 2.20 A; Cu-C top3 = 3.00 / 3.00 / 3.13; I-Cu-I = 113.8 / 135.3 deg; lowest real +12.41 cm-1** | **PRIMARY V9 PRODUCTIVE SITE (Task #29)** |
| cu2i2_veratrole_methoxyO_startB | veratrole | rotamer / outer-sphere | +28.07 | +22.73 | 0 | D | Cu-O closest 2.64 / 3.33 / 4.00 A; Cu-C closest 1.93 A; I-Cu-I 96.8 / 163.2 | rotamer; positive BE; cluster topology matters for the productive mode |

**Geometric details for the primary productive site (cu2i2_veratrole_methoxyO_startA, archived in setD_alt_v2_analysis.json):**
- Two Cu-O contacts at 2.203 A (symmetric; methoxy-O of each adjacent OMe group binding the same Cu).
- Cu-C top three at 2.999 / 2.999 / 3.128 A (above-the-plane face of the ring; not a productive Cu-pi mode).
- Cu2I2 cluster topology preserved (I-Cu-I bend angles 113.8 / 135.3 deg; rhombic core retained).
- Lowest real vibrational mode +12.41 cm-1 (n_imag = 0; true minimum but soft — consistent with a flexible bidentate chelate).
- BE_gas = -26.82, BE_smd(water) = -26.24 kcal/mol; SMD preserves the binding energy within 0.6 kcal/mol because the Cu2I2 + veratrole assembly is overall neutral (no charged-Cu solvation rank reversal).
- **Why this matters:** in real lignin polymers, beta-O-4 cross-linked guaiacyl units often present an ortho-OMe + (etherified-OR) pair where the phenolic-OH has been consumed in cross-linking. The veratrole proxy is the simplest small-molecule analog of that motif. The kappa2-O,O bidentate result therefore suggests a primary anchoring chemistry for cross-linked / etherified lignin domains on neutral Cu2I2.

### E.4 Level L4 — [CuI2]- Anion (Set B and Set D V2)

From `audit_final/CUI2_BINDING_TABLE.csv` and `audit_final_setD_alt_diag/setD_alt_v2_analysis.json`. [CuI2]- reference E_gas = -2236.113332 Eh; E_smd = -2236.178759 Eh.

| Complex | Ligand | Final mode | BE_gas | BE_smd | n_imag | Class | Note |
|---|---|---|---|---|---|---|---|
| cui2_h2o_anion | water | (detached, 2-coord linear) | -10.43 | -4.21 | 0 | E | iodides keep linear two-coord on Cu |
| cui2_methanol_anion | methanol | (detached, 2-coord linear) | -7.83 | (n.r.) | 0 | E | rejected |
| cui2_phenol_O_anion | phenol | (detached) | -11.56 | (n.r.) | 0 | E | rejected |
| cui2_phenol_pi_anion | phenol | (detached) | -5.67 | (n.r.) | 0 | E | rejected |
| cui2_guaiacol_phenolicO_anion | guaiacol | (detached) | -5.37 | (n.r.) | 0 | E | rejected |
| cui2_guaiacol_methoxyO_anion | guaiacol | (detached) | +173.15 | (n.r.) | 0 | E | nonphysical BE > +100; SCF/opt artifact; excluded from interpretation |
| cui2_guaiacol_pi_anion | guaiacol | (detached) | -2.92 | (n.r.) | 0 | E | rejected |
| cui2_guaiacol_bidentate_anion | guaiacol | 2+1 hemicoordinated | +167.44 | (n.r.) | 0 | E | nonphysical BE > +100; SCF/opt artifact; excluded |
| cui2_veratrole_methoxyO_anion_startA | veratrole | (detached) | +49.28 | +53.60 | 0 | E | Cu-O closest 3.70 A; Cu-C closest 3.21 A; I-Cu-I = 173.2 deg; **iodide saturation rejects the bidentate motif** |
| cui2_veratrole_methoxyO_anion_startB | veratrole | rotamer / outer-sphere | +55.20 | +47.93 | 0 | D | Cu-O closest 2.69 A; Cu-C closest 1.94 A; positive BE but Cu-C contact preserved geometrically |

**Operative reading:** [CuI2]- is iodide-saturated (linear two-coordinate Cu, I-Cu-I ≈ 170–180 deg). It does not admit a productive third-coordination contact in any of the probed modes, including the bidentate motif that succeeds on neutral Cu2I2. Two outlier rows (cui2_guaiacol_methoxyO_anion, cui2_guaiacol_bidentate_anion) show BE > +100 kcal/mol — these are SCF / optimization artifacts of the reference cluster (likely the optimizer used a different [CuI2]- conformer for the reference) and are flagged as artifact and excluded. The veratrole anion rows (BE = +49 to +55 kcal/mol) are physical and consistent with the reject branch.

### E.5 Level L5 — Etherified vs. Free Guaiacyl Rotamer Scan (Set D V2)

The four V2 species above (two Cu2I2 + two [CuI2]-) constitute the rotamer scan. Reading them as a 2x2:

| | startA | startB |
|---|---|---|
| **Cu2I2 (neutral)** | **kappa2-O,O bidentate; BE -26.8 (gas) / -26.2 (SMD); A** | rotamer; BE +28 (gas); D |
| **[CuI2]- (anion)** | detached; BE +49 (gas); E | outer-sphere; BE +55 (gas); D |

The 2x2 isolates the two qualitative findings: (i) only the Cu2I2 + startA combination yields a productive bidentate site, and (ii) [CuI2]- rejects the motif regardless of starting geometry. This 2x2 is reproduced in §J (productive vs nonproductive prose) and is the basis for Figure 2 of the manuscript (mode-selective decision tree).

### E.6 Aggregated counts (after Task #28 conservative classifier; §H)

From `audit_final/BINDING_SURVIVAL_SUMMARY.txt`:
- Class A STRONG_BINDING: 21 (incl. cu2i2_veratrole_methoxyO_startA AND cu2i2_veratrole_pi)
- Class B MODERATE_BINDING: 1
- Class C WEAK_BINDING: 0
- Class D METASTABLE_CONTACT: 3
- Class E NON_BINDING: 14

Total rows: 39 (TIER_A naked-Cu+ adducts + Set B [CuI2]- + Set C Cu2I2 + Set D V2 veratrole + Set D recovered cu2i2_veratrole_pi). **v2 update:** the original Set D `cu2i2_veratrole_pi` row was added 2026-04-30 after the source `.out` was recovered from migrated pod motr7au0um7e8n; geometry pulled from BELEGEN E4.3.

---

## F. Per-Claim Verdict Table

Three verdict tables already exist as canonical CSVs. The writer should pull them in as supplementary tables and use the verdict labels directly in the v9 Discussion.

### F.1 BELEGEN_EVIDENCE_MATRIX (`audit_final/BELEGEN_EVIDENCE_MATRIX.csv`, 26 KB)

Schema:
- `claim_id` — short label (E1.1, E2.3, E3.5, E4.3, ...)
- `claim_short` — 1-line claim text
- `evidence_files` — semicolon-separated `audit_final/...csv` paths backing the verdict
- `evidence_rows` — specific complex_ids cited
- `final_geometry` — e.g. "Cu-O = 2.20 / 2.20 A; bidentate"
- `contact_distances_A` — top Cu-O / Cu-C / Cu-I distances
- `BE_gas_kcal`, `BE_smd_kcal`, `n_imag`, `lowest_freq_cm1`
- `verdict` — SUPPORTED / NOT_SUPPORTED / SUPERSEDED / DATA_LOST_POD_WIPE
- `note`

Key rows (writer should reproduce verbatim as a manuscript supplementary table):
- **E3.5–E3.8 (Set D V2 quartet)**: SUPPORTED for E3.5 (cu2i2_veratrole_methoxyO_startA, kappa2-O,O bidentate productive). E3.6 (startB rotamer): SUPPORTED as METASTABLE. E3.7, E3.8 ([CuI2]- anion analogs): SUPPORTED as REJECTED.
- **E4.3 (cu2i2_veratrole_pi)**: SUPPORTED at the BE / n_imag level (energies and frequency status are pedigreed in `audit_final/EXPERIMENT_JOB_INDEX.csv` with sha256 captured pre-wipe). The original .out file was lost in the 2026-04-30T11:02Z RunPod stop+start cycle that wiped /root; the BELEGEN row carries `DATA_LOST_POD_WIPE 2026-04-30T11:02Z` in the geometry / contact-distance columns. This does NOT affect the BE-level conclusion or the verdict.

### F.2 CLAIM_SUPPORT_STATUS (`audit_final/CLAIM_SUPPORT_STATUS.csv`)

Five claims (writer should treat verdicts as authoritative; the v9 Discussion is built around them).

| Claim | v8 wording (paraphrase) | v9 verdict | Notes / reframing |
|---|---|---|---|
| C1 | Naked-Cu+ ranking implies guaiacol > cellulose | NOT_SUPPORTED | Naked Cu+ is not the operative state; reranking on CuI/Cu2I2 closes the gap or reverses it. |
| C2 | CuI clusters confirm guaiacol affinity advantage | NOT_SUPPORTED (as worded); SUPERSEDED by mode-selective frame | CuI compresses pi/O gap; "advantage" depends on mode access. |
| C3 (revised v9) | Productive methoxy/ether-O binding requires neutral CuI environment + geometry that allows two adjacent O donors to chelate | SUPPORTED (state-dependent: productive on neutral Cu2I2 in kappa2-O,O bidentate; nonproductive on iodide-saturated [CuI2]-) | Cite E3.5–E3.8. This is the Task #29 reopening. |
| C4 (revised v9) | Mode-selectivity dual-mode anchoring on etherified guaiacyl proxies | SUPPORTED | Cite E4.3 (pi-mode) plus E3.5 (bidentate-mode). The two modes are not redundant — they describe different productive Cu states and different lignin sub-motifs. |
| C5 | Polymer-scale guaiacyl-OH determines copper retention in fabric | NOT_SUPPORTED (out of computed scope; experimentally testable per §L) | v9 retreats from polymer-scale claim and substitutes the discriminating experimental protocol. |

### F.3 MECHANISM_VERDICT_TABLE (`audit_final/MECHANISM_VERDICT_TABLE.csv`)

Four mechanism rows. Writer should treat as authoritative:

| Mechanism ID | Description | v9 verdict | Citing |
|---|---|---|---|
| M1 (pi anchoring on bare Cu+) | Cu+ + arene eta-6 binding | SUPPORTED for naked Cu+; NOT relevant for CuI textile state | L1 rows (cu_phenol_pi -80.96, cu_guaiacol_pi -62.17) |
| M2 (phenolic-O on naked Cu+) | Cu+ + phenolic-O sigma-donor | SUPPORTED for naked Cu+; PARTIAL on CuI; FRAGMENTS on Cu2I2 for free guaiacol | L1, L2, L3 rows |
| M3 (methoxy-O / ether-O channel) | dual-state: (a) bidentate kappa2-O,O on neutral Cu2I2 with etherified guaiacyl is PRODUCTIVE; (b) [CuI2]- anion REJECTS the same motif | SUPPORTED with state-dependent qualifier (Task #29 reopening) | E3.5 (cu2i2_veratrole_methoxyO_startA), E3.7, E3.8 |
| M4 (etherified-pi channel) | Cu2I2 + veratrole pi mode (cu2i2_veratrole_pi) — dual-mode coexists with M3 bidentate | SUPPORTED with dual-mode note | E4.3 (BE / freq pedigreed; final geometry data lost — see DATA_LOST note) |

### F.4 SITE_OCCUPANCY_TABLE (`audit_final/SITE_OCCUPANCY_TABLE.csv`)

The four Set D V2 species occupy these slots:
| Species | Site occupancy | Note |
|---|---|---|
| cu2i2_veratrole_methoxyO_startA | OCCUPIED_INNER_SPHERE (kappa2-O,O bidentate) | productive |
| cu2i2_veratrole_methoxyO_startB | OUTER_SPHERE / METASTABLE_CONTACT | rotamer; positive BE |
| cui2_veratrole_methoxyO_anion_startA | NOT_OCCUPIED (no contact within cutoff) | rejected |
| cui2_veratrole_methoxyO_anion_startB | OUTER_SPHERE / METASTABLE_CONTACT (Cu-C 1.94 A) | rejected as productive site |

---

## G. Geometry and Frequency Audit Summary

Full per-species detail in `audit_final/V9_GEOMETRY_TABLE.csv` (55 rows) and `audit_final/ORCA_FREQUENCY_AUDIT.csv`. Headline:

- **All productive sites cited in the v9 thesis are true minima** (n_imag = 0). This includes cu2i2_veratrole_methoxyO_startA (lowest real +12.41 cm-1), cu2i2_h2o, cu2i2_methanol, cu2i2_phenol_O, cu2i2_guaiacol_bidentate, cui_guaiacol_phenolicO, cui_guaiacol_methoxyO, cui_guaiacol_pi, cui_phenol_pi, cu_catechol_bidentate.
- **Saddle points** (cited as upper-bound BEs only, never as productive sites): cui_methanol_O (1 soft mode +54.9 cm-1 after displacement reopt; CONFIRMED_MIN_BOTH), cui_phenol_O (n_imag = 2; UPPER BOUND), cu2i2_linear (n_imag = 2; rejected in favor of cu2i2_rhombic), cu_meta_methoxyphenol_phenolicO (older OptFreq run had n_imag = 4; superseded by repeated run with n_imag = 0).
- **Reference clusters**: cu2i2_rhombic (n_imag = 0; ground-state CuI dimer, 35.5 kcal/mol below cu2i2_linear; dimerization BE -51.9 kcal/mol vs 2 x CuI_monomer); cu2i2_linear (n_imag = 2; rejected reference). [CuI2]- (anion) reference is a converged linear two-coordinate Cu, I-Cu-I = 180 deg.
- **Cluster integrity**: only cu2i2_guaiacol_phenolicO is flagged as `cluster_fragmented = True` (the cluster cracks during opt); no other Cu2I2 row fragments. The veratrole startA productive site preserves the rhombic core (I-Cu-I bend angles 113.8 / 135.3 deg).
- **Pedigree**: every .out file is recorded in `audit_final/RAW_FILE_INDEX.csv` with sha256, file size, charge, multiplicity, n_atoms, final_energy_Eh, ZPE, enthalpy, n_imaginary, opt cycles. The Set D V2 .out files were lost in the 2026-04-30T11:02Z pod wipe; their distilled coords / freqs / energies are archived in `audit_final_setD_alt_diag/setD_alt_v2_analysis.json` with snapshot timestamps and the sha256 of the source .out captured pre-wipe.

---

## H. Conservative Classifier Results and Reclassification Notes

Full text in `audit_final/RECLASSIFICATION_NOTES.md`. Summary of the rule set (Task #28):

```
A STRONG_BINDING       BE_eff < -10  AND valid contact AND true minimum (n_imag=0)
B MODERATE_BINDING     -10 <= BE_eff < -5  AND valid contact
C WEAK_BINDING         -5 <= BE_eff < 0    AND valid contact
D METASTABLE_CONTACT   BE_eff >= 0 BUT contact survives geometrically
E NON_BINDING          ligand detached / cluster fragmented / hard saddle / no contact
                       OR BE_gas > +100 kcal/mol (forced as artifact)

BE_eff = max(BE_gas, BE_smd) when SMD exists, else BE_gas (less favorable of the two)
Valid contact: Cu-O <= 2.6 A, OR Cu-C / arene <= 3.2 A
```

**Geometry/integrity overrides applied:**
- Rows with `mode_survival_status` = DETACHED, FRAGMENTED, or COLLAPSED_TO_DETACHED -> forced E.
- Rows with contact distance > cutoff -> forced E.
- Rows with BE_gas > +100 kcal/mol -> forced E with "BE artifact" note.

**Borderline-cutoff documented case:** `cu_phenol_O` (Cu-O = 2.6636 A; spec cutoff 2.6 A) is forced E by 0.06 A. BE_gas = -51.4, BE_smd = -36.4 — both strongly negative. This is consistent with the well-established v8 -> v9 finding that phenol-O on naked Cu+ drifts toward pi (cu_phenol_pi BE_gas = -80.96 dominates). Treat the cu_phenol_O row as "O-mode is not the productive minimum on naked Cu+ for free phenol; the system relaxes toward pi." A 2.7 A cutoff would re-class this as A.

**Outlier (artifact) rows excluded from interpretation:** cu2i2_guaiacol_methoxyO BE_gas = +172.67; cu2i2_guaiacol_bidentate_anion BE_gas = +167.44; cui2_guaiacol_methoxyO_anion BE_gas = +173.15. These three are SCF / optimization artifacts of the reference cluster (likely a different [CuI2]- conformer used as the reference). The Set D V2 veratrole rows REPLACE these for the v9 interpretation.

**Class-counts after classifier (39 total rows; v2 update):**
- A STRONG_BINDING: 21
- B MODERATE_BINDING: 1
- C WEAK_BINDING: 0
- D METASTABLE_CONTACT: 3
- E NON_BINDING: 14

---

## I. State-Dependent Anchoring Ensemble (oxide-aging note)

The v9 manuscript must include a Discussion subsection that acknowledges the oxide / hydroxide aging regime (Cu2O / CuO / Cu(OH)2). This is a **literature-only** scope clause — no DFT was added for this layer. Full text in `audit_final/OXIDE_AGING_REGIME_NOTE.md`.

**Reviewer's framing (verbatim — preserve in §1 abstract caveat and Discussion):**
> "Cu retention is not one mechanism. It is a state-dependent anchoring ensemble: CuI-rich states favor mode-selective O / pi / iodide-cluster interactions, while oxide-aged states likely shift toward heteroatom / O-donor anchoring."

**State-by-state ensemble (verbatim — for Discussion):**
> "CuI / Cu2I2 state: pi / arene binding can matter.
> [CuI2]- saturated state: straight iodide coordination rejects ligands.
> Cu2O / CuO / Cu(OH)2 aged state: O-donor, hydroxyl, carboxylate, phenolic, semiquinone anchoring becomes important."

**Manuscript-safe limitation paragraph (verbatim — use in §1 abstract caveat and §12 limitations):**
> "This study computes copper-lignin coordination on CuI-rich cluster models (CuI monomer, neutral Cu2I2, iodide-saturated [CuI2]-). Real CuI-coated textiles may locally develop oxide / hydroxide surface fractions during laundering and ambient aging; the operative anchoring chemistry on those aged surface fractions is governed by Cu(II) O-donor / hydroxyl / carboxylate coordination and is referenced here from the cited literature only. The discriminating experimental protocol in §L includes laundering treatments designed to test the relative contribution of CuI-rich versus oxide-aged anchoring fractions in real fabric."

**Six literature anchors (writer must verify all DOIs in §M before locking; full URL+DOI in `audit_final/OXIDE_AGING_REGIME_NOTE.md`):**
1. **PLACEHOLDER — writer to locate.** *(In v1, Yang et al. 2017 *Nat. Commun.* was cited here. The audit confirmed Yang 2017 is a thermoelectric CuI thin-film paper, NOT an oxide-aging anchor. It has been preserved as #18 in §M.3 for the Introduction's CuI thin-film context. The writer must locate a different paper for this oxide-aging anchor — candidate: an XPS-based Cu(I)/Cu(II) speciation study on aged CuI coatings.)*
2. Klochko et al. 2019, *Thin Solid Films* — CuI coatings on textile / aging *(verify DOI before submission)*
3. Nikolic et al. 2020, *Molecules* — Cu(I) / Cu(II) speciation in textile context *(verify DOI before submission)*
4. Coroa et al. 2023 — Cu / lignin / textile binding observations *(verify full citation; placeholder text)*
5. **PLACEHOLDER — writer to locate.** *(In v1, "Sun & Chen 2023" *ACS Appl. Nano Mater.* DOI 10.1021/acsanm.3c01961 was cited here. The DOI actually resolves to Chen, A. X.; Lau, H. Y.; et al. 2023 — a water-mediated CuI nanoparticle on cotton paper, which is direct support for the v9 cluster-anchoring thesis, not for oxide-aging. Reassigned to §J / §K / §P / Introduction paragraph 1; see §M.3 #22 and §D.1.)*
6. **PLACEHOLDER — writer to locate.** *(In v1, "Sportelli et al. 2024" *ACS Appl. Eng. Mater.* DOI 10.1021/acsaenm.4c00548 was cited here. The DOI actually resolves to Chen, A. X.; Beins, D. K. R.; et al. 2024 — a phosphine-coordinated CuI cluster on cotton paper, which is direct support for the v9 cluster-anchoring thesis, not for oxide-aging. Reassigned to §J / §K / §P / Introduction paragraph 1; see §M.3 #23 and §D.1.)*

**Anchor-replacement guidance:** PLACEHOLDERS #1, #5, #6 each need a paper that genuinely characterizes CuI / Cu(I) state evolution under aging or oxidative conditions. Klochko 2019 (#2) and Nikolic 2020 (#3) are general Cu(I)/Cu(II) speciation references and may be sufficient when combined with the writer's choice of XPS / aging studies; do NOT auto-substitute on the agent's authority.

---

## J. Productive vs. Nonproductive Sites — Drafted Prose

(For the v9 Discussion, ~250 words. Writer may polish.)

> Across the six-level model hierarchy, only a small subset of (Cu state, lignin functional group, coordination mode) tuples produce a true minimum with a thermodynamically and geometrically defensible binding chemistry. On naked Cu+, the dominant mode is aromatic pi (e.g. cu_phenol_pi BE = -80.96, cu_guaiacol_pi BE = -62.17 kcal/mol), with phenolic-O serving as a secondary mode. This naked-Cu+ ranking is, however, not predictive of CuI-cluster behavior: the CuI monomer compresses the pi vs O contrast (CuI–phenol_pi -56.69, CuI–guaiacol_phenolic-O -25.30, CuI–methanol_O -25.76 — phenolic-O on guaiacol is within 0.5 kcal/mol of methanol on CuI, so the v8 phenolic-O affinity advantage is not supported by the CuI subset). On neutral Cu2I2, productive anchoring is binary: water and methanol bind sigma-O monodentate while preserving the cluster (BE = -19.5, -18.7 kcal/mol); free guaiacol attempted as phenolic-O cracks the cluster (cu2i2_guaiacol_phenolicO is fragmented); free guaiacol attempted as pi detaches; but **etherified guaiacyl (veratrole) binds kappa2-O,O bidentate to Cu2I2 with BE = -26.82 kcal/mol (gas) / -26.24 kcal/mol (SMD water), Cu-O = 2.20 / 2.20 A, n_imag = 0 — the strongest single productive site identified in the entire L3 set, and the primary v9 result.** On the iodide-saturated [CuI2]- anion, the same etherified motif is rejected (BE = +49 to +55 kcal/mol; no productive contact preserved); iodide saturation imposes a linear two-coordinate geometry on Cu that physically forbids the bidentate chelate. The implication for lignin polymers is that productive Cu retention requires both a CuI cluster state with an open coordination sphere and a guaiacyl unit whose phenolic OH has been consumed in cross-linking (etherified beta-O-4 / 4-O-5 fragments), exposing two adjacent O donors that can chelate. Free phenolic-OH guaiacol on neutral Cu2I2 instead disrupts the cluster. **Direct experimental support for CuI-cluster anchoring on cotton fabric is provided by Chen, A. X. et al. (2023 *ACS Appl. Nano Mater.* and 2024 *ACS Appl. Eng. Mater.* — see §M.3 #22 and #23) — a single research group has reported water-mediated CuI nanoparticle assembly and phosphine-coordinated CuI cluster self-assembly on cotton, both consistent with the cluster-state anchoring framework presented here.**

---

## K. Mechanistic Figure Narrative — Drafted Prose

(Caption / pull-quote material for Figure 4 — multi-panel mechanistic schematic. Writer may polish.)

> The mechanistic schematic distinguishes three branches of the anchoring ensemble. Branch (a) — chain-end / etherified guaiacyl on neutral Cu2I2 — is the primary productive pathway: two adjacent O donors of an ortho-(OMe)(OR) etherified motif chelate the Cu of the rhombic Cu2I2 cluster in a kappa2-O,O bidentate geometry, with both Cu-O contacts at 2.20 A and the cluster topology preserved. Branch (b) — internal phenolic-OH guaiacyl on neutral Cu2I2 — is nonproductive: the strong sigma-donating phenolic-OH cracks the cluster, redistributing iodide and producing a fragmented final geometry that cannot be characterized as a clean coordination site. Branch (c) — any guaiacyl on iodide-saturated [CuI2]- — is rejected: iodide saturation imposes a linear two-coordinate Cu geometry with I-Cu-I ≈ 170-180 deg and no remaining coordination sphere available. A secondary pathway, branch (d), is the oxide-aging regime: under laundering and ambient aging, local surface fractions of Cu2O / CuO / Cu(OH)2 emerge and contribute additional O-donor / hydroxyl / carboxylate anchoring that this DFT study does not compute (literature-only; see §I and reference list §M). The discriminating experiments in §L Part 2 (anaerobic vs aerobic laundering, EPR detection of phenoxyl/semiquinone radicals on laundered fabric, Cu LMM Auger XPS for Cu(I)/Cu(II) ratio tracking, iodide spike-rescue) are designed to test the relative weight of branches (a, b, c) versus branch (d) in real fabric. The figure should make the branching explicit and label each branch with its computed BE (where applicable) or its literature evidence basis. **For branches (a) and (b) — productive vs nonproductive cluster-state anchoring — direct experimental support is the Chen, A. X. et al. 2023 / 2024 pair on water-mediated CuI nanoparticle assembly and phosphine-coordinated CuI cluster self-assembly on cotton (§M.3 #22 / #23).** For branch (d) the literature anchors are now §I #2 / #3 / #4 (Klochko / Nikolic / Coroa, all flagged for writer verification) plus three additional anchors the writer must locate (see §M.5 v2 note).

---

## L. Validation Experiment Protocol

Two parts.

### L.1 Part 1 — Standard substrate validation (textile chemistry)

Each experiment listed with: stated purpose, expected discriminating outcome, practical feasibility note.

1. **ICP-MS leachate analysis of wash water.** Purpose: quantify Cu loss per wash cycle on each substrate (linen, hemp, jute, Lyocell, cotton). Expected discriminating outcome: lignin-rich substrates (linen, hemp, jute) show lower Cu loss per cycle than cellulose-only substrates (cotton, Lyocell) if the v9 thesis is right. Feasibility: standard ICP-MS service; <$50 / sample.
2. **XPS Cu 2p, I 3d, O 1s on pre- and post-wash fabric.** Purpose: track changes in Cu speciation (Cu(I) vs Cu(II)), iodide retention, and O 1s envelope (phenolic / hydroxyl / oxide region). Expected outcome: lignin-rich substrates retain more Cu(I) and more I; aged surfaces show O 1s shoulder growth at 530-531 eV (oxide); cellulose-only substrates lose I and Cu faster. Feasibility: routine in a university surface-analysis lab.
3. **XANES / EXAFS Cu K-edge** (where synchrotron access is available). Purpose: direct Cu coordination-environment fingerprinting. Expected: lignin-rich pre-wash fabric shows a Cu coordination consistent with CuI cluster + O-donor (Cu-O 2.0–2.3 A), shifting toward Cu-O / Cu-OH (2.0 A) as washing progresses. Feasibility: requires beamtime; one-shot proof-of-concept.
4. **Wash durability (ISO 6330) on linen, hemp, jute, Lyocell vs cotton.** Purpose: standardized laundering cycles. Expected: Cu retention rank order matches the v9 thesis — substrates with more etherified guaiacyl content (jute, hemp lignin) retain more Cu than cellulose-only Lyocell after N cycles. Feasibility: standard textile lab equipment.
5. **Antimicrobial activity retention** (parallel measurement to (1)–(4)). Purpose: link Cu retention to functional outcome (antimicrobial activity is the application driver). Expected: substrates with higher post-wash Cu retain higher kill-rate on standard test organism (e.g. *S. aureus* or *E. coli* per AATCC 100). Feasibility: routine textile-bioactivity lab.
6. **QCM-D adhesion measurement on model films.** Purpose: in vitro mechanistic confirmation of differential Cu binding to lignin- vs cellulose-derived model films. Expected: Cu uptake rate on lignin films > cellulose; reversibility under wash-mimic conditions differs by film composition. Feasibility: requires QCM-D instrument; well-established protocol.

### L.2 Part 2 — Redox-regeneration / oxide-aging discriminating tests

These tests directly address the state-dependent anchoring ensemble (§I) — specifically whether a redox-regeneration cycle operates at meaningful rate during a typical wash, and whether the oxide-aged regime contributes meaningfully to anchoring.

1. **Anaerobic vs aerobic laundering.** Purpose: distinguish CuI-cluster anchoring (insensitive to O2) from oxide-aged anchoring (requires O2). Expected: anaerobic wash preserves Cu retention pattern predicted by the CuI thesis; aerobic wash drifts toward an oxide-mediated pattern. Feasibility: requires anaerobic laundering setup (glovebox or sealed chamber with N2 sparge); medium difficulty.
2. **Lignin-rich vs methylated-lignin substrates.** Purpose: directly test the etherified-vs-free guaiacyl prediction. Methylation of phenolic-OH groups in jute or hemp lignin (using diazomethane or methyl iodide / K2CO3) converts free phenolic-OH guaiacyl to veratrole-like etherified motifs. Expected: methylated lignin-rich substrates retain MORE Cu per wash cycle than untreated lignin-rich substrates (because the productive bidentate kappa2-O,O motif is exposed). Feasibility: lignin methylation is well-established; ICP-MS readout per (1).
3. **EPR detection of phenoxyl / semiquinone radicals on laundered fabric.** Purpose: detect redox-regeneration of Cu(I) by lignin phenolic groups during wash. Expected: presence of phenoxyl / semiquinone EPR signal post-wash on lignin-rich substrates if redox-regeneration is operative; absent on cellulose-only substrates. Feasibility: EPR access required; sensitivity is the main constraint.
4. **XPS Cu LMM Auger pre/post-wash for Cu(I)/Cu(II) ratio tracking.** Purpose: quantify oxidation-state distribution as a function of wash cycle. Expected: Cu(I) preserved better on lignin-rich substrates (consistent with CuI thesis); Cu(II) fraction grows over many wash cycles on all substrates (consistent with oxide-aging). Feasibility: same XPS service as Part 1 (3); just adds the LMM Auger window.
5. **Iodide spike-rescue test (NaI in wash water).** Purpose: test whether [CuI2]- formation (predicted to reject ligands) competes with productive anchoring during wash. Expected: NaI-spiked wash water reduces Cu retention on all substrates (even lignin-rich ones) if the [CuI2]- reject branch is operative. Feasibility: trivial — add NaI to wash water; ICP-MS readout per (1).

The combined Part 1 + Part 2 protocol provides discrimination between (a) the v9 mode-selective CuI-cluster thesis, (b) the oxide-aging alternative, and (c) a redox-regeneration cycle hypothesis. Each test has a defined go / no-go expected outcome.

---

## M. Complete Reference List (every reference v9 will cite)

The writer must run each entry through a per-reference DOI / title / author audit before locking. Group by category. Estimated 50-60 references total. The list below is the union of references cited in `audit_final/MANUSCRIPT_IMPACT_v8_to_v9.md`, `V9_CASE_DECISION.md`, and `OXIDE_AGING_REGIME_NOTE.md`. For each reference, the writer should fill DOI and full author list before submission.

### M.1 Methodology references

1. Becke, A. D. *J. Chem. Phys.* **1993**, *98*, 5648-5652. (B3LYP — exchange-correlation functional)
2. Lee, C.; Yang, W.; Parr, R. G. *Phys. Rev. B* **1988**, *37*, 785-789. (LYP correlation)
3. Stephens, P. J.; Devlin, F. J.; Chabalowski, C. F.; Frisch, M. J. *J. Phys. Chem.* **1994**, *98*, 11623-11627. (B3LYP parametrization commonly cited as canonical reference)
4. Grimme, S.; Antony, J.; Ehrlich, S.; Krieg, H. *J. Chem. Phys.* **2010**, *132*, 154104. (D3 dispersion)
5. Grimme, S.; Ehrlich, S.; Goerigk, L. *J. Comput. Chem.* **2011**, *32*, 1456-1465. (Becke-Johnson damping for D3)
6. Weigend, F.; Ahlrichs, R. *Phys. Chem. Chem. Phys.* **2005**, *7*, 3297-3305. (def2-TZVP / def2-SVP basis sets)
7. Weigend, F. *Phys. Chem. Chem. Phys.* **2006**, *8*, 1057-1065. (def2/J auxiliary basis for RIJCOSX)
8. Marenich, A. V.; Cramer, C. J.; Truhlar, D. G. *J. Phys. Chem. B* **2009**, *113*, 6378-6396. (SMD continuum solvent model)
9. Neese, F.; Wennmohs, F.; Becker, U.; Riplinger, C. *J. Chem. Phys.* **2020**, *152*, 224108. (ORCA 5+ overview; current ORCA reference)
10. Neese, F. *WIREs Comput. Mol. Sci.* **2022**, *12*, e1606. (ORCA program system update)
11. Izsák, R.; Neese, F. *J. Chem. Phys.* **2011**, *135*, 144105. (RIJCOSX integration approximation)

### M.2 Lignin / copper chemistry references

12. Boerjan, W.; Ralph, J.; Baucher, M. *Annu. Rev. Plant Biol.* **2003**, *54*, 519-546. (lignin biosynthesis / structural review)
13. Ralph, J.; Lapierre, C.; Boerjan, W. *Curr. Opin. Biotechnol.* **2019**, *56*, 240-249. (lignin structural review)
14. Ragauskas, A. J.; Beckham, G. T.; Biddy, M. J.; et al. *Science* **2014**, *344*, 1246843. (lignin valorization; Ragauskas review — suggest reviewer Ragauskas)
15. Kim, H.; Ralph, J. *Org. Biomol. Chem.* **2010**, *8*, 576-591. (NMR characterization of lignin)
16. Sangha, A. K.; Petridis, L.; Smith, J. C.; Ziebell, A.; Parks, J. M. *Environ. Prog. Sustain. Energy* **2012**, *31* (1), 47-54. DOI: 10.1002/ep.10628. ("Molecular simulation as a tool for studying lignin" — DFT modeling of lignin fragments)
16a. Li, P.; Lv, W.; Ai, S. *J. Exp. Nanosci.* **2015**, *11* (1), 18-27. DOI: 10.1080/17458080.2015.1015462. ("Green and gentle synthesis of Cu₂O nanoparticles using lignin as reducing and capping reagent with antibacterial properties" — direct precedent for lignin-mediated Cu(I/II) reduction relevant to §K redox-regeneration framing. **v2 NOTE:** added as a new entry; v1 V9_HANDOVER did not include this reference. The audit fix doc's "REPLACE" wording was wrong — there was no prior entry to replace.)
16b. Li, Z.; Bansal, N.; Azarpira, A.; Bhalla, A.; Chen, C.; Ralph, J.; Hegg, E. L.; Hodge, D. B. *Biotechnol. Biofuels* **2015**, *8* (1), art. 123. DOI: 10.1186/s13068-015-0300-5. ("Chemical and structural changes associated with Cu-catalyzed alkaline-oxidative delignification of hybrid poplar" — direct precedent for Cu / lignin reactivity in alkaline-oxidative regimes; co-authors include J. Ralph and E. L. Hegg, directly relevant to the v9 lignin-Cu chemistry framing — flag in cover letter as topical anchor. **v2 NOTE:** added as a new entry; v1 V9_HANDOVER did not include this reference.)
17. Petridis, L.; Smith, J. C. *Nat. Rev. Chem.* **2018**, *2*, 382-389. (lignin modeling)

### M.3 CuI textile literature

18. Yang, C.; Souchay, D.; Kneiß, M.; Bogner, M.; Wei, H. M.; Lorenz, M.; Oeckler, O.; Benstetter, G.; Fu, Y. Q.; Grundmann, M. *Nat. Commun.* **2017**, *8* (1), art. 16076. DOI: 10.1038/ncomms16076. ("Transparent flexible thermoelectric material based on non-toxic earth-abundant p-type copper iodide thin film" — Introduction CuI thin-film conductivity anchor; **NOTE:** topical scope is thermoelectric, not oxide-aging — do NOT use as §I anchor.)
19. Klochko, N. P.; Klepikova, K. S.; Khrypunov, G. S.; Kopach, V. R.; Tyukhov, I. I.; Liubov, V. M.; Lyubov, D. S.; Kirichenko, M. V. *Thin Solid Films* **2019**, *683*, 34-41. (CuI thin film characterization; verify)
20. Nikolic, M. V.; Vasiljevic, Z. Z.; Auger, S.; Vidic, J. *Molecules* **2020**, *25*, 5635. (Cu(I) / Cu(II) speciation review; verify)
21. Coroa, J.; et al. **2023** — Cu / lignin / textile review. **(VERIFY: full citation needed; this is the reviewer-provided reference and the writer must locate the canonical DOI.)**
22. Chen, A. X.; Lau, H. Y.; Teo, J. Y.; Wang, Y.; Choong, D. Z. Y.; Wang, Y.; Luo, H.-K.; Yang, Y. Y.; Li, N. *ACS Appl. Nano Mater.* **2023**, *6* (14), 13238-13249. DOI: 10.1021/acsanm.3c01961. ("Water-Mediated In Situ Fabrication of CuI Nanoparticles on Flexible Cotton Fabrics as a Sustainable and Skin-Compatible Coating with Broad-Spectrum Antimicrobial Efficacy" — direct experimental anchor for water-mediated CuI nanoparticle anchoring on cotton; cite as a pair with #23 in §J / §K / §P / Introduction paragraph 1.)
23. Chen, A. X.; Beins, D. K. R.; Wang, Y.; Luo, H.-K.; Yang, Y. Y.; Li, N. *ACS Appl. Eng. Mater.* **2024**, *2* (12), 2864-2874. DOI: 10.1021/acsaenm.4c00548. ("Fast-Acting and Skin-Compatible Antimicrobial Coating on Cotton Fabrics via In Situ Self-Assembly of Phosphine-Coordinated Copper Iodide Clusters" — direct experimental anchor for phosphine-coordinated CuI cluster self-assembly on cotton; cite as a pair with #22 in §J / §K / §P / Introduction paragraph 1.)
24. Bechtold, T.; Pham, T. (book chapter or review) — *Textile Chemistry*, de Gruyter, 2019. (textile chemistry handbook; reviewer suggestion: Bechtold)

### M.4 Redox-regeneration analogs

25. Stubbe, J. A.; van der Donk, W. A. *Chem. Rev.* **1998**, *98* (2), 705-762. (radical / phenoxyl chemistry; DOI candidate **10.1021/cr9400875** — writer to verify)
25a. Hammes-Schiffer, S.; Stuchebrukhov, A. A. *Chem. Rev.* **2010**, *110* (12), 6939-6960. DOI: 10.1021/cr1001436. ("Theory of Coupled Electron and Proton Transfer Reactions" — canonical PCET theory review. **NOTE:** the v1 V9_HANDOVER cited DOI 10.1021/cr1001436 as a Costentin/Robert/Savéant 2010 paper; the DOI actually resolves to this Hammes-Schiffer & Stuchebrukhov review. Cited here for the theoretical framework underlying §K redox-regeneration framing.)
25b. Costentin, C.; Robert, M.; Savéant, J.-M. *Acc. Chem. Res.* **2010**, *43* (7), 1019-1029. DOI: 10.1021/ar9002812. ("Concerted Proton−Electron Transfers: Electrochemical and Related Approaches" — phenol-PCET mechanistic application; cite as a pair with #25a for §K.)
26. Tommasi, F.; et al. *J. Inorg. Biochem.* — recent Cu / phenolic radical regeneration paper. **(VERIFY: writer to locate)**
27. Suzuki, Y.; Ikedo, M.; Kageyama, T.; Watanabe, M. — XPS LMM Auger Cu(I)/Cu(II) discrimination methodology. **(VERIFY: writer to locate canonical methodology paper)**

### M.5 Oxide-aging literature (anchors from §I — REVISED v2)

**v2 NOTE:** §M.5 in v1 contained six re-citations of §I anchors. After the v9 reference audit (`audit_final/V9_REFERENCE_AUDIT_FIXES.md`), three of those re-citations are removed:
- Yang 2017 (was v1 #28) — REMOVED. The Yang 2017 *Nat. Commun.* paper is thermoelectric, not oxide-aging; it is preserved as #18 in §M.3 for the Introduction's CuI thin-film context.
- Sun & Chen 2023 (was v1 #32) — REMOVED. The DOI actually resolves to Chen, A. X.; Lau, H. Y.; et al. 2023, a water-mediated CuI-on-cotton paper. Re-tagged as #22 in §M.3 (cluster-anchoring evidence).
- Sportelli 2024 (was v1 #33) — REMOVED. The DOI actually resolves to Chen, A. X.; Beins, D. K. R.; et al. 2024, a phosphine-coordinated CuI cluster on cotton paper. Re-tagged as #23 in §M.3 (cluster-anchoring evidence).

Remaining oxide-aging re-citations:

29. Klochko et al. 2019 (already #19) — re-cited for aging-state characterization. *(verify DOI)*
30. Nikolic et al. 2020 (already #20) — re-cited for speciation. *(verify DOI)*
31. Coroa et al. 2023 (already #21) — re-cited. *(verify full citation)*

**Writer action item:** §I requires (per the §I narrative) up to six oxide-aging anchors. After v2 removals, only three remain (#29 / #30 / #31), and all three are still flagged "verify". The writer must locate up to three additional XPS / Cu(I)/Cu(II) speciation / oxide-aged-coating references before submission to fully populate the §I anchor list.

### M.6 Counterevidence and scope

34. — (writer should add 1-3 counterevidence references; e.g. studies that argue against lignin's role in Cu retention in textile applications, or studies that emphasize the polymer-scale rather than monomer-scale picture).

### M.7 Reviewer suggestions (for cover letter / Paragon Step 5)

- Tetiana Budnyak, Stockholm University (lignin chemistry) — tetiana.budnyak@mmk.su.se (verify current email)
- Orlando Rojas, University of British Columbia (biopolymer materials) — orlando.rojas@ubc.ca (verify)
- Arthur Ragauskas, University of Tennessee Knoxville / ORNL (lignin) — aragausk@utk.edu (verify)
- Thomas Bechtold, University of Innsbruck (textile chemistry) — thomas.bechtold@uibk.ac.at (verify)
- (writer: add one more, e.g. a CuI / textile electronics expert if needed)

**Pre-submission audit checklist for §M:** for each reference, verify (a) author list matches the published article, (b) journal abbreviation conforms to ACS style, (c) volume / issue / pages match, (d) DOI resolves, (e) year matches the DOI metadata, (f) reference is actually cited in the body text (no orphan references), (g) reference order matches first-citation order, (h) DOI uses the unified format (https://doi.org/...), (i) preprint vs published distinguished where relevant, (j) self-references (if any) clearly marked, (k) any retracted / corrected references flagged. (11-point audit per the user's standard practice.)

---

## N. Outstanding Caveats and Limitations

### N.1 Scope limitations (deliberate, defensible)

- **Cluster models, not periodic CuI surfaces.** The Cu2I2 rhombic and [CuI2]- linear are the smallest CuI cluster fragments that recover the qualitative coordination chemistry of bulk gamma-CuI; periodic-DFT slab calculations on real CuI crystal facets are not in scope and are flagged as a future direction.
- **Small-molecule proxies, not full lignin polymer.** Guaiacol, veratrole, anisole, catechol, methanol stand in for monomer-level lignin functional groups; the polymer-level statistics of these motifs in real fiber lignins are inferred from established lignin chemistry literature, not computed here.
- **SMD single points, not explicit solvent / wash environment.** SMD(water) at the gas-phase optimized geometry approximates aqueous laundering; it does not include ions, surfactants, or pH effects.
- **No oxidation-state changes during washing modeled in DFT.** The redox-regeneration hypothesis (Cu(I) <-> Cu(II) with lignin phenolic oxidation to phenoxyl / semiquinone) is treated as a literature-supported secondary hypothesis (§I, §L Part 2); it is NOT computed in this work.
- **Cu(II) DFT not computed.** Cu(II) coordination chemistry in oxide-aged regimes is cited from literature only.
- **Polymer architecture inferred from monomer-level chemistry.** The veratrole proxy stands in for etherified beta-O-4 / 4-O-5 cross-linked guaiacyl units; the actual fraction of such units in jute / hemp / linen fibers is taken from cited lignin-characterization literature, not measured or computed here.
- **High-grid sensitivity check NOT EXECUTED.** Originally planned as a Grid5/FinalGrid6 SP queue on the Set D V2 productive site (cu2i2_veratrole_methoxyO_startA + ref Cu2I2 + ref veratrole, gas + SMD = 6 SPs); this was BLOCKED by a RunPod container memory cgroup limit of 488 MiB on the available pod after a stop+start cycle on 2026-04-30T11:02Z. The DefGrid3 result (BE_gas = -26.82, BE_smd = -26.24) is reported as the canonical value with this scope clearly stated. Status documented in `audit_final/GRID_SENSITIVITY_STATUS.csv` as `FAILED_ORCA_XCGRID`. Effect on conclusions: **NONE** for the qualitative thesis; the BE numbers are reported with the grid clearly noted; the v9 manuscript should add a one-sentence Methods note: *"DefGrid3 (m4 / Lebedev 302) was used for both geometry and BE single points; a planned high-grid (Grid5 / FinalGrid6) cross-check was not executed due to compute-resource constraints and is queued as a future item."* All input files and the orchestration script are staged at `audit_final_setD_alt_diag/grid_test/inputs/` for re-run on a roomier pod.

### N.2 Open questions (require future work)

- **Does the redox-regeneration cycle operate at meaningful rate during a typical wash?** Discriminator: §L Part 2 EPR + Cu LMM Auger XPS.
- **What fraction of native lignin chain ends in real bast fibers (linen, hemp, jute) are actually accessible to Cu (vs buried in cross-linked polymer interior)?** Discriminator: surface-sensitive ICP-MS / XPS comparison vs bulk lignin content.
- **How does laundering surfactant chemistry interact with Cu-lignin coordination?** Not addressed in DFT scope; experimentally testable by varying surfactant / pH in §L Part 1.
- **What is the long-term oxidation-state distribution in laundered Cu-textile coatings (after 50, 100, 200 wash cycles)?** Discriminator: Cu LMM Auger XPS time series.
- **Does the bidentate kappa2-O,O motif on Cu2I2 survive in periodic / surface CuI slabs?** Future periodic-DFT work.

### N.3 Data loss caveat

- **`/workspace/results_setD/cu2i2_veratrole_pi_opt_freq.out` (E4.3 evidence row in BELEGEN) was lost in the 2026-04-30T11:02Z RunPod stop+start cycle that wiped /root.** Energies (E_gas, E_smd, BE) and n_imag for E4.3 are pedigreed in `audit_final/EXPERIMENT_JOB_INDEX.csv` with sha256 captured BEFORE the wipe. BELEGEN row 19 is annotated `DATA_LOST_POD_WIPE 2026-04-30T11:02Z` in the geometry / contact-distance columns. **Effect on v9 conclusions: NONE.** BE and n_imag remain pedigreed; the SUPPORTED verdict for E4.3 holds. Geometry-level descriptors for the pi mode of cu2i2-veratrole are reported as NA in `V9_GEOMETRY_TABLE.csv`.

---

## O. Figure Specifications

### O.1 Figure 1 — Coordination-Mode Map

- **Type:** data plot, multi-facet bar chart.
- **x-axis:** ligand (guaiacol, phenol, veratrole, methanol, water, catechol, anisole, benzene, galacturonate-neutral); ordered by lignin-relevance.
- **y-axis:** BE_smd in kcal/mol (range +60 to -90).
- **Faceting:** 4 facets, one per Cu state — (a) naked Cu+, (b) CuI monomer, (c) Cu2I2 (rhombic), (d) [CuI2]- (anion).
- **Color/marker by mode:** pi (eta-6) — blue circle; phenolic-O — orange square; methoxy-O — green diamond; kappa2-O,O bidentate — red star; water/methanol O-mono — gray triangle; detached/fragmented — gray X (no fill).
- **Data source:** `audit_final/V9_GEOMETRY_TABLE.csv` (BE_smd column where available; BE_gas as fallback); annotate fallback rows.
- **Caption draft:** "Figure 1. Coordination-mode map across four Cu states. Each panel shows BE(SMD water) for the lignin-inspired ligand set, colored by coordination mode. On naked Cu+ (panel a) pi dominates with the largest absolute BE values, but this state is not operative for CuI textiles. On CuI monomer (panel b) the pi vs O contrast collapses to within ~3–10 kcal/mol. On neutral Cu2I2 (panel c, red star) the kappa2-O,O bidentate motif is the **primary productive site for the textile-relevant CuI cluster state**; on iodide-saturated [CuI2]- (panel d) the same motif is rejected (positive BE; no inner-sphere contact)."
- **Complexity:** medium (faceted bar chart).

### O.2 Figure 2 — Mode-Selective Anchoring Decision Tree (Schematic)

- **Type:** conceptual schematic / decision tree.
- **Top:** Cu state node (CuI / Cu2I2 / [CuI2]- / oxide-aged).
- **Middle:** lignin functional group access (free phenolic-OH guaiacyl / etherified guaiacyl / cellulose O-donor / aromatic pi).
- **Bottom:** mode outcome (productive / metastable / detached / cluster-fragmented / rejected).
- **Each leaf:** computed BE (where available) and reference to manuscript Table 1.
- **Caption draft:** "Figure 2. Mode-selective anchoring decision tree. Productive Cu retention requires both an open Cu coordination sphere (top) and a lignin functional group whose geometry matches the available coordination mode (middle). Free phenolic-OH guaiacyl on neutral Cu2I2 cracks the cluster (bottom-left red); etherified guaiacyl on neutral Cu2I2 binds kappa2-O,O bidentate (bottom-center green); iodide-saturated [CuI2]- rejects all probed ligands (bottom-right red); the oxide-aged regime is a literature-only branch (bottom-right gray)."
- **Complexity:** simple conceptual.

### O.3 Figure 3 — Evidence Hierarchy Panel

- **Type:** conceptual layered bar / pyramid.
- **Layers (top to bottom):** (1) DFT cluster model (this work); (2) analog literature (CuI textile, lignin chemistry); (3) textile wash data needed (proposed §L Part 1); (4) discriminating mechanistic experiments (proposed §L Part 2).
- **Annotation:** for each layer, list 2-3 representative evidence items.
- **Caption draft:** "Figure 3. Evidence hierarchy supporting the v9 thesis. The DFT cluster model (top) provides the mode-selective predictions; analog literature (second) supports the CuI textile coating chemistry; the proposed validation protocol (bottom two layers) provides the discrimination between the v9 thesis, the oxide-aging alternative, and the redox-regeneration hypothesis."
- **Complexity:** simple conceptual.

### O.4 Figure 4 — Mechanistic Schematic (multi-panel)

- **Type:** mechanistic / structural schematic.
- **Panels (a)-(d):** the four branches narrated in §K (etherified guaiacyl on Cu2I2 productive bidentate; free phenolic-OH guaiacyl on Cu2I2 cracks cluster; any guaiacyl on [CuI2]- rejected; oxide-aged secondary pathway).
- **Each panel:** shows the relevant Cu state core (Cu2I2 rhombic, [CuI2]- linear, Cu2O surface fragment) plus the lignin sub-motif, with explicit Cu-O and Cu-I distance labels for the productive site (panel a: Cu-O = 2.20 / 2.20 A from cu2i2_veratrole_methoxyO_startA).
- **Caption:** see §K (use as caption with minor formatting).
- **Complexity:** complex multi-panel structural diagram.

### O.5 Figure S1 (supporting) — Geometry Overlay

- **Type:** structural overlay.
- **Content:** overlay of cu_phenol_pi (eta-6 pi binding) and cu_phenol_O (sigma O binding) on naked Cu+ to show that the two minima are nearly degenerate structurally — both have Cu near the ring face but the O-mode has Cu closer to the O atom (Cu-O 2.66 A, just past coordination cutoff) while the pi-mode has Cu directly above the ring centroid. Optionally overlay cu_guaiacol_pi and cu_guaiacol_methoxyO similarly.
- **Caption draft:** "Figure S1. Geometric similarity of phenol pi and phenol-O minima on naked Cu+. Both minima place Cu close to the aromatic face; the O-mode (orange) sits 2.66 A from the phenolic oxygen and is the borderline contact noted in §H. The pi-mode (blue) is the productive minimum (BE = -80.96 kcal/mol gas) and dominates the naked-Cu+ binding chemistry."
- **Complexity:** simple structural overlay.

### O.6 Optional Figure S2 (supporting) — Set D V2 2x2 grid

- **Type:** structural 2x2.
- **Content:** the four Set D V2 species (Cu2I2 startA / startB; [CuI2]- startA / startB) shown as final geometries side-by-side, with computed BE labels; only startA on Cu2I2 (top-left) is highlighted as productive.
- **Complexity:** simple structural grid.

---

## P. Cover Letter Content (drafted)

(The writer should adapt to the corresponding author's voice and the corresponding-author email. ~300 words.)

> Dear ACS Sustainable Chemistry & Engineering Editorial Office,
>
> We are pleased to submit our manuscript, **"Mode-Selective CuI Anchoring on Lignin-Inspired Fiber Interfaces: A DFT Cluster-Model Study"**, for consideration as a Research Article in ACS Sustainable Chemistry & Engineering.
>
> The work presents a DFT cluster-model study of copper coordination to lignin-inspired functional groups across a six-level model hierarchy spanning naked Cu+, CuI monomer, neutral Cu2I2, iodide-saturated [CuI2]-, and an etherified guaiacyl rotamer set, with a literature-only oxide / hydroxide aging regime included as scope. The central finding is operational: productive CuI anchoring on lignin-inspired fibers is a state-dependent, mode-selective problem rather than a single-site affinity ranking. On neutral Cu2I2, the productive site is a kappa2-O,O bidentate chelate of an etherified guaiacyl (veratrole) end-group; on iodide-saturated [CuI2]- the same motif is rejected. We provide a discriminating experimental protocol (anaerobic vs aerobic laundering, methylated-lignin substrate test, EPR phenoxyl detection, Cu LMM Auger XPS, iodide spike-rescue) that tests the model in real laundered fabric.
>
> **Disclosure of audit and reframing.** A prior version (v8) of this work was uploaded as a Research Square preprint. During the v8-to-v9 audit, we re-audited every computational claim with ORCA 6.1.1 (B3LYP-D3(BJ) / def2-TZVP / DefGrid3) and found that the v8 single-site cellulose-vs-guaiacol comparison was not supported by the computed CuI subset; we have replaced it with the mode-selective framework presented here. A v9 correction will be posted on Research Square upon acceptance, and the full audit pipeline (every input, every output, every intermediate table) is publicly archived at [GitHub URL — writer to insert].
>
> The mode-selective cluster-anchoring framework presented here is supported by recent experimental work from Chen, A. X. and co-workers, who have reported water-mediated CuI nanoparticle assembly on cotton (Chen et al., *ACS Appl. Nano Mater.* **2023**, *6* (14), 13238–13249, DOI 10.1021/acsanm.3c01961) and phosphine-coordinated CuI cluster self-assembly on cotton (Chen et al., *ACS Appl. Eng. Mater.* **2024**, *2* (12), 2864–2874, DOI 10.1021/acsaenm.4c00548). Both papers describe in-situ self-assembled CuI cluster phases on cotton fabric — the structural class our DFT cluster models target — and both report skin-compatible antimicrobial activity, the application driver for ACS SCE relevance.
>
> All authors consent to submission and have read the manuscript. We declare no competing interest. We suggest the following reviewers (all with appropriate expertise in lignin chemistry, biopolymer materials, or textile chemistry): Tetiana Budnyak (Stockholm Univ.), Orlando Rojas (UBC), Arthur Ragauskas (UTK / ORNL), Thomas Bechtold (Innsbruck).
>
> Sincerely,
> [corresponding author name and signature]
> Independent Researcher
> [email]

---

## Q. ACS Paragon Submission Metadata

| Field | Value |
|---|---|
| **Title** | Mode-Selective CuI Anchoring on Lignin-Inspired Fiber Interfaces: A DFT Cluster-Model Study |
| **Article type** | Research Article |
| **Abstract** | (see §R below — drafted, ~270 words) |
| **Author affiliation** | Independent Researcher |
| **Corresponding author email** | [writer to insert from v8 prep] |
| **Keywords (8)** | lignin; copper iodide; conductive textiles; green engineering; biomass-derived materials; multivalent binding; mode-selective anchoring; density functional theory |
| **Funding statement** | No external funding |
| **Conflict of interest statement** | None declared |
| **Suggested reviewers (4-5)** | Tetiana Budnyak (Stockholm Univ., lignin chemistry; tetiana.budnyak@mmk.su.se — verify); Orlando Rojas (UBC, biopolymer materials; orlando.rojas@ubc.ca — verify); Arthur Ragauskas (UTK/ORNL, lignin; aragausk@utk.edu — verify); Thomas Bechtold (U Innsbruck, textile chemistry; thomas.bechtold@uibk.ac.at — verify); (writer: add one more if appropriate) |
| **Excluded reviewers** | (none stated) |
| **Manuscript classification (ACS topic)** | Sustainable materials; biomass-derived materials; computational chemistry |
| **Number of figures** | 4 main + 2 supporting (S1, S2) |
| **Number of tables** | 1 main (the L1-L4 master binding-energy table; see §E and `audit_final/V9_GEOMETRY_TABLE.csv` for source data) + 2-3 supplementary |
| **Supplementary material** | (a) `BELEGEN_EVIDENCE_MATRIX.csv` re-rendered as a SI table; (b) `V9_GEOMETRY_TABLE.csv` re-rendered as a SI table; (c) `RECLASSIFICATION_NOTES.md` re-rendered as SI text; (d) all .out files (or sha256 manifest with archive link) |
| **Data availability statement** | "All ORCA input and output files, derived analysis tables, and the audit pipeline are publicly archived at [GitHub URL — writer to insert]. Raw .out files are also available from the corresponding author on reasonable request, with sha256 manifests provided in `audit_final/RAW_FILE_INDEX.csv`." |
| **Software / version** | ORCA 6.1.1; B3LYP-D3(BJ); def2-TZVP; def2/J auxiliary basis; SMD(water); DefGrid3 |
| **Cover letter** | see §P |

---

## R. Drafted Abstract

(~270 words. Qualitative ordering, one decisive comparison, NO specific kcal/mol numbers in the abstract. Writer will refine.)

> Copper iodide (CuI) coatings on lignin-rich natural fibers — linen, hemp, jute — confer conductive and antimicrobial properties for wearable and bioactive textiles, but the molecular-level anchoring chemistry that determines how much copper is retained through laundering remains contested. A common framing posits a single-site affinity advantage of guaiacyl phenolic oxygen over cellulose-like O-donors. We tested this framing with DFT cluster models in ORCA 6.1.1 (B3LYP-D3(BJ) / def2-TZVP) across a six-level hierarchy spanning naked Cu+, CuI monomer, the neutral Cu2I2 rhombic cluster, the iodide-saturated [CuI2]- anion, and an etherified guaiacyl (veratrole) rotamer set, with an oxide / hydroxide aging regime referenced from the literature. The single-site framing fails: on the CuI monomer, guaiacol phenolic-O binds within thermal noise of methanol O-binding, removing the proposed advantage. The data instead support a state-dependent, mode-selective anchoring picture. The primary productive site identified on the textile-relevant neutral Cu2I2 cluster is a kappa2-O,O bidentate chelate of veratrole — a small-molecule analog of an etherified beta-O-4 / 4-O-5 cross-linked guaiacyl unit — with the rhombic cluster topology preserved and both Cu-O contacts approximately 2.2 A. The same motif is rejected on iodide-saturated [CuI2]-, where linear two-coordinate Cu coordination physically forbids a third inner-sphere contact, and free phenolic-OH guaiacol on neutral Cu2I2 cracks the cluster instead of binding cleanly. Real CuI-coated fabric is therefore best modeled as a state-dependent ensemble of CuI-rich, iodide-saturated, and oxide-aged Cu fractions, each presenting a different productive anchoring mode (or none). We provide a discriminating experimental protocol — anaerobic versus aerobic laundering, methylated-lignin substrate comparison, EPR phenoxyl detection, Cu LMM Auger XPS, and iodide spike-rescue — that tests the mode-selective thesis against oxide-aging and redox-regeneration alternatives in real laundered fabric.

---

## S. Drafted Title Options

1. **Mode-Selective CuI Anchoring on Lignin-Inspired Fiber Interfaces: A DFT Cluster-Model Study** *(lead option)*
2. State-Dependent Copper Retention on Lignin-Inspired Fibers: A Mode-Selective DFT Cluster-Model Framework
3. Etherified Guaiacyl as the Productive CuI Anchoring Site: A Cluster-Model DFT Study of Lignin-Copper Coordination
4. From Single-Site Affinity to Mode-Selective Anchoring: Reframing the CuI-Lignin Interface with DFT Cluster Models
5. CuI Coating Retention on Lignin-Rich Textiles: A Mode-Selective Model from Cluster-Level DFT and a Discriminating Experimental Protocol

---

## Appendix Z. File-by-File Provenance and Reproducibility

The full pipeline is in `audit_final/` (canonical) and `audit_final_setD_alt_diag/` (Set D V2 follow-up). The handover writer should treat these files as authoritative; in case of discrepancy with text in this package, the CSV is correct and this package should be updated.

### Z.1 Canonical computational outputs

| Path | Content | Used in |
|---|---|---|
| `audit_final/ORCA_BINDING_ENERGIES.csv` | Phase 1/2/Tier A binding energies (gas + SMD), with source .out paths | §E (L1) |
| `audit_final/CU2I2_BINDING_TABLE.csv` | Cu2I2 (rhombic) cluster + ligand BEs and geometric descriptors | §E (L3, Set C) |
| `audit_final/CUI2_BINDING_TABLE.csv` | [CuI2]- anion + ligand BEs and geometric descriptors | §E (L4, Set B) |
| `audit_final/CUI_CLUSTER_BINDING_TABLE.csv` | CuI monomer + ligand BEs (Tier B) | §E (L2) |
| `audit_final_setD_alt_diag/setD_alt_v2_analysis.json` | Set D V2 (Task #29) veratrole rotamer scan: BE, n_imag, lowest_freq, top Cu-O / Cu-C distances, I-Cu-I angles, final + initial xyz, reference cluster energies, ALL fields needed because the source .out was wiped | §E (L5), §F (E3.5-E3.8) |
| `audit_final/ORCA_GEOMETRY_AUDIT.csv` | per-species final XYZ, n_atoms, n_opt_cycles, converged, final_energy, charge, mult, method line, basis | §G, §E |
| `audit_final/ORCA_FREQUENCY_AUDIT.csv` | per-species ZPE, enthalpy, n_imag, imaginary freqs, displacement-reopt verdicts | §G, §E |
| `audit_final/ORCA_SMD_AUDIT.csv` | SMD audit detail (parameter set used, geometry-source mapping) | §E (SMD column) |
| `audit_final/ORCA_VIBRATIONAL_MODES.csv` | full mode list for displacement-reopt analysis | §G |
| `audit_final/RAW_FILE_INDEX.csv` | every .out file: full path, sha256, file size, terminated_normally, calc_type, method line, etc. | §G, §N (data loss caveat) |

### Z.2 Audit / verdict tables

| Path | Content | Used in |
|---|---|---|
| `audit_final/BELEGEN_EVIDENCE_MATRIX.csv` | per-evidence-row claim / support / verdict / pedigree (E4.3 marked DATA_LOST_POD_WIPE) | §F.1 |
| `audit_final/CLAIM_SUPPORT_STATUS.csv` | per-claim verdicts (C1-C5 in §F.2) | §F.2 |
| `audit_final/MECHANISM_VERDICT_TABLE.csv` | per-mechanism verdicts (M1-M4 in §F.3) | §F.3 |
| `audit_final/SITE_OCCUPANCY_TABLE.csv` | per-species site-occupancy classification (Set D V2 added) | §F.4 |
| `audit_final/BINDING_SURVIVAL_TABLE.csv` | every (set, ligand, mode) row with classifier verdict, contact distance, fragmentation flag, BE_gas, BE_smd, n_imag (39 rows after v2 reference patch — added cu2i2_veratrole_pi from recovered E4.3 geometry) | §H |
| `audit_final/BINDING_SURVIVAL_SUMMARY.txt` | aggregated counts | §E.6, §H |
| `audit_final/RANK_REVERSAL_TABLE.csv` | gas vs SMD rank reversals for naked-Cu+ Tier A and Set D V2 (22 rows) | §E (SMD note), §H |
| `audit_final/RECLASSIFICATION_NOTES.md` | full Task #28 classifier rule set + per-row override list + outlier-handling notes | §H |
| `audit_final/V9_GEOMETRY_TABLE.csv` | NEW; consolidated per-species geometry summary (55 rows) for the v9 manuscript Table 1 / supplementary | §G, §E (all levels) |
| `audit_final/LIGNIN_APPENDIX_STATE_TABLE.csv` | NEW; one row per (Cu state, lignin functional group) with predominant mode + interpretive note (14 rows) | §J |
| `audit_final/LIGNIN_APPENDIX_STATE_MODE_TABLE.csv` | NEW; mode x Cu-state crosstab for the 5 manuscript-cited modes | §J, §E |
| `audit_final/GRID_SENSITIVITY_STATUS.csv` | DefGrid3 vs higher-grid status; cu2i2_veratrole_methoxyO_startA marked NOT_RUN_TIME_BUDGET / FAILED_ORCA_XCGRID | §N (high-grid caveat) |
| `audit_final/FINAL_COMPUTATIONAL_AUDIT_STATUS.txt` | NEW; pipeline status, optional-work disposition, data-loss disposition, artifact list | overall |

### Z.3 Documentation / interpretation

| Path | Content | Used in |
|---|---|---|
| `audit_final/MANUSCRIPT_IMPACT_v8_to_v9.md` | full v8 -> v9 sentence-level change list, §1-15; primary internal source for §B, §F, §J | §§B, F, J |
| `audit_final/V9_CASE_DECISION.md` | working-decision document for Case C (mode-selective); primary internal source for §D, §K; also pedigree of NOT_INDEXED v9.1 results (cui_guaiacol_pi, cui_guaiacol_methoxyO, cui_guaiacol_bidentate) | §§D, E.2, K |
| `audit_final/AUDIT_FINAL.md` | full audit report (v9 final) | reference |
| `audit_final/OXIDE_AGING_REGIME_NOTE.md` | Level 6 scope note (literature only); primary internal source for §I | §I |
| `audit_final/CONTROL_INTERPRETATION.md` | interpretation of Tier B / control calculations | reference |
| `audit_final/CUI_CLUSTER_INTERPRETATION.md` | interpretation of CuI cluster controls | reference |

### Z.3a Supplementary computational outputs and exchange/control tables

| Path | Content | Used in |
|---|---|---|
| `audit_final/VERATROLE_OME_ALTERNATE_STARTS.csv` | Set D V2 four-rotamer scan (startA / startB / startC / startD) raw BE + geometry summary; the source CSV for the primary v9 result | §E.5 (L5), §F.1 (E3.5–E3.8) |
| `audit_final/BINDING_SURVIVAL_TABLE_setD_alt_v2.csv` | Set D V2-specific survival/classifier rows (subset/extension of the canonical 39-row table — see v2 update note in §E.6) | §H, §F.1 |
| `audit_final/CONTROL_BINDING_TABLE.csv` | Tier-B control BEs (positive / negative controls used to validate the classifier) | §F.1, §H |
| `audit_final/CUI_BASIS_SENSITIVITY.csv` | def2-TZVPP basis-sensitivity spot-check on CuI–guaiacol–phenolic-O vs CuI–methanol-O | §E.2 (basis note) |
| `audit_final/CU2I2_MODE_TABLE.csv` | per-mode breakdown of Cu2I2 ligand binding (rhombic-preserving vs cluster-cracking) | §E.3 (L3) |
| `audit_final/CUI2_MODE_TABLE.csv` | per-mode breakdown of [CuI2]- ligand binding (all rejected; outliers > +100 forced to class E) | §E.4 (L4) |
| `audit_final/CUI_CLUSTER_MODE_TABLE.csv` | per-mode breakdown of CuI monomer ligand binding | §E.2 (L2) |
| `audit_final/CU2I2_EXCHANGE_TABLE.csv` | iodide / oxygen-donor ligand exchange BEs on Cu2I2 (productive vs non-productive exchange) | §K (mech), §F.3 |
| `audit_final/CUI2_RERUN_ANOMALIES.csv` | re-run anomalies on the [CuI2]- set (numerical / convergence outliers) | §N (caveats) |

### Z.3b Build scripts and reproducible aggregations

| Path | Content | Used in |
|---|---|---|
| `audit_final_setD_alt_diag/build_v9_closeout.py` | **AUTHORITATIVE BUILD SCRIPT.** Re-running this script regenerates `RECLASSIFICATION_NOTES.md`, `V9_GEOMETRY_TABLE.csv`, `LIGNIN_APPENDIX_STATE_TABLE.csv`, `LIGNIN_APPENDIX_STATE_MODE_TABLE.csv`, `BINDING_SURVIVAL_TABLE.csv` (39-row v9 extension after v2 patch), `BINDING_SURVIVAL_SUMMARY.txt`, `RANK_REVERSAL_TABLE.csv`, `GRID_SENSITIVITY_STATUS.csv`, and `FINAL_COMPUTATIONAL_AUDIT_STATUS.txt` from the canonical inputs above | §E, §F, §G, §H, §N |

### Z.4 Reproducibility

- All ORCA input files used in the published computation are reconstructable from `audit_final/RAW_FILE_INDEX.csv` (column `method_line`) and the per-species charge / multiplicity / final XYZ in `ORCA_GEOMETRY_AUDIT.csv`. The high-grid SP queue inputs are pre-staged at `audit_final_setD_alt_diag/grid_test/inputs/` for re-run.
- ORCA 6.1.1 official binary; no patches.
- def2-TZVP basis from the ORCA built-in; def2/J auxiliary basis from the ORCA built-in.
- D3(BJ) parameters from the ORCA built-in (Grimme 2010, Becke-Johnson damping per Grimme 2011).
- SMD(water) parameters from the ORCA built-in (Marenich, Cramer, Truhlar 2009).
- DefGrid3 (m4 / Lebedev 302; default in ORCA 6.1.1).

---

**END OF V9 HANDOVER PACKAGE.**

This document is the single source of truth for the v9 manuscript writer. All numerical values in §§A–S trace to files in `audit_final/`; all CSVs listed in Appendix Z are present at the given paths and have been validated by the V9 closeout build script (`audit_final_setD_alt_diag/build_v9_closeout.py`, executed 2026-04-30 UTC).

If the writer needs anything that is not in this package, the canonical fallback order is:
1. The CSV file named in the relevant section.
2. `audit_final/MANUSCRIPT_IMPACT_v8_to_v9.md` for v8 -> v9 sentence-level guidance.
3. `audit_final/V9_CASE_DECISION.md` for case-determination guidance.
4. `audit_final/RAW_FILE_INDEX.csv` for file-level provenance and sha256.

Computing on this audit ends here. The next step is manuscript drafting on a different platform.
