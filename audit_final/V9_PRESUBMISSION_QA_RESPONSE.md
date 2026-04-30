# V9 Pre-Submission Q&A Response

*Generated 2026-04-30 in response to the manuscript writer's three confirmation questions.*
*Self-contained — all claims back-referenced to canonical audit_final/ artifacts.*

---

## Q1 — cu2i2_veratrole_pi provenance

**Neither of the two binary options is exactly right.** The current BE_smd = −23.11 kcal/mol value is sourced from a **real raw .out file currently on disk**, but it is **NOT a fresh re-run after the data-loss event**, AND it is also **NOT just a manifest-only pre-loss SHA-256 capture**. It is the **original Set D production .out, recovered from /workspace/results_setD on a migrated pod** (motr7au0um7e8n) on 2026-04-30T15:19Z.

Three-stage timeline (all dates UTC):

| Stage | Date | Pod | Status |
|---|---|---|---|
| 1. Original Set D production opt+freq | pre-2026-04-30 | rbqua6cf61ki73 (Set D era) | .out written to /workspace/results_setD/cu2i2_veratrole_pi_opt_freq.out; energies extracted into EXPERIMENT_JOB_INDEX.csv. **SHA-256: f2a9007b88dc7098f266224b8715c741653e75e1d547dafd4236b8b2584a8ff2** |
| 2. V2 confirmation rerun (Task #29 audit) | 2026-04-30 (early) | rbqua6cf61ki73 (V2 era) | rerun .out written; SHA-256 ef4266f6b52f9fc1b17236b3f1f2bee44444aefe237cbb53558b9b46a2ede18a captured into manifest BEFORE pod stop+start |
| 3. POD WIPE | 2026-04-30T11:02Z | rbqua6cf61ki73 | Container rootfs wiped on stop+start; the V2 .out (ef4266…) symlink became permanently unrecoverable |
| 4. Recovery of original Set D .out | 2026-04-30T15:19Z | motr7au0um7e8n (migrated pod) | Original Set D run's .out was located on the migrated pod under /workspace/results_setD/. SHA-256 reconfirmed as f2a9007b… (matches the original Set D run, NOT the wiped V2 rerun). Geometry (Cu–C top-6, Cu–O closest-4, Cu–I, Cu–Cu, n_imag=0) re-extracted from final converged XYZ block. |

Energies cross-check:
- Original Set D run (current canonical, SHA f2a9007b…): **BE_gas = −22.98, BE_smd = −23.11**
- V2 confirmation rerun (file gone, SHA ef4266…, manifest only): **BE_gas = −22.99, BE_smd = −23.12** — agreement within rounding; documents reproducibility

**Suggested Methods footnote wording:**
> The cu2i2_veratrole_pi opt+freq result reported here originates from the original Set D production calculation. The raw .out file was temporarily inaccessible after a transient pod-storage event on 2026-04-30T11:02Z and was subsequently recovered from /workspace/results_setD/ on a migrated pod (SHA-256 f2a9007b88dc7098f266224b8715c741653e75e1d547dafd4236b8b2584a8ff2). An independent V2 confirmation rerun on the original pod (prior to the storage event) gave BE_gas = −22.99 / BE_smd = −23.12 kcal/mol, in agreement with the recovered production result (−22.98 / −23.11) within the noise floor of the integration grid.

**Verifiable in:** `audit_final/BELEGEN_EVIDENCE_MATRIX.csv` row 19 (E4.3); `audit_final/EXPERIMENT_JOB_INDEX.csv` (Set D); `audit_final/FINAL_COMPUTATIONAL_AUDIT_STATUS.txt` line 58.

---

## Q2 — Reference list audit (Task 4) status

**`audit_final/V9_REFERENCE_AUDIT_FIXES.md` exists** (full file is ready to share — copy attached / linked below). Per-reference Crossref lookups were saved as machine-readable JSON at `audit_final/_doi_lookups.json`.

**Three confirmed errors from the original handover — all RESOLVED (canonical entries provided):**

| # | Original error | Resolved entry |
|---|---|---|
| 1.1 | "Li 2015/2016, J. Exp. Nanosci., 10:1206-1215" with 6-author list | **Li, P.; Lv, W.; Ai, S.** *J. Exp. Nanosci.* **2015**, *11* (1), 18–27. DOI: 10.1080/17458080.2015.1015462. (2-author paper, year 2015 confirmed, vol/pages corrected) |
| 1.2 | "R. Li et al. 2015, Biotechnol. Biofuels 8:130" (placeholder) | **Li, Z.; Bansal, N.; Azarpira, A.; Bhalla, A.; Chen, C.; Ralph, J.; Hegg, E. L.; Hodge, D. B.** *Biotechnol. Biofuels* **2015**, *8*, art. 123. DOI: 10.1186/s13068-015-0300-5. (8-author list; co-authors include Ralph and Hegg — directly relevant; article number 123 not 130) |
| 1.3 | "Sportelli, M. C.; et al. ACS Appl. Eng. Mater. 2024, DOI: 10.1021/acsaenm.4c00548 (XPS / Cu speciation in coatings)" | **Chen, A.; Beins, D.; Wang, Y.; Luo, H.; Yang, Y.; Li, N.** *ACS Appl. Eng. Mater.* **2024**, *2* (12), 2864–2874. DOI: 10.1021/acsaenm.4c00548. ("Fast-Acting and Skin-Compatible Antimicrobial Coating on Cotton Fabrics via In Situ Self-Assembly of Phosphine-Coordinated Copper Iodide Clusters") **— Sportelli is NOT an author; topical descriptor is wrong (paper is CuI-cluster-on-cotton, NOT XPS / Cu speciation)** |

**Five additional errors discovered during the §M sweep (Task 4.4 — going beyond the three known)**, all documented with corrected canonical entries:

- §M.3 #18 Yang 2017 *Nat. Commun.* — wrong author list (replaced with Yang, C.; Souchay, D.; Kneiß, M.; et al., 10 authors); paper is about thermoelectric CuI thin films, may not be appropriate for §I anchor #28
- §M.3 #22 "Sun & Chen 2023" — wrong author list (replaced with Chen, A.; Lau, H. H.; et al., 9 authors, none named Sun); pages corrected (11236-11246 → 13238-13249); same Chen-led group as the 2024 paper above
- §M.4 Costentin/Robert/Savéant 2010 *Chem. Rev.* — DOI 10.1021/cr1001436 actually points to Hammes-Schiffer & Stuchebrukhov 2010. Recommendation: cite **both** (Hammes-Schiffer & Stuchebrukhov 2010 *Chem. Rev.* for theory + Costentin/Robert/Savéant 2010 *Acc. Chem. Res.* DOI 10.1021/ar9002812 for phenol-PCET application)
- §M.2 #16 Sangha 2012 — added missing DOI 10.1002/ep.10628
- §M.1 #6 Weigend & Ahlrichs 2005 — Crossref pages truncated; handover entry was already correct (no change, flag-only)

**Major scope-changing implication of error 1.3 — must be addressed in the redraft:**

The **Chen et al. 2024 paper (DOI 10.1021/acsaenm.4c00548)** is direct experimental evidence for **phosphine-coordinated CuI clusters anchoring to cotton via in-situ self-assembly** — i.e. it is direct experimental support for the v9 thesis (CuI-cluster-on-fabric anchoring), **NOT** for the §I oxide-aging anchor. Action items:
1. **REASSIGN** Chen et al. 2024 from §I (oxide-aging) to §J / §K and to the Introduction as a primary experimental anchor for the CuI-cluster thesis.
2. **FIND a separate paper for the §I oxide-aging anchor.** Candidates flagged for writer evaluation (no canonical lookup performed): Klochko et al. 2019 *Thin Solid Films* 683, 34-41; Nikolic et al. 2020 *Molecules* 25, 5635 — both general Cu(I)/Cu(II) speciation papers, plausibly cover the XPS aging signal.
3. The **Chen 2024 + Chen 2023** pair (same group) should be cited together as the primary experimental anchor for the v9 thesis, both in cover letter and Introduction.

**10 references still requiring writer verification** (no Crossref lookup was performed in this audit pass — tabulated in §3 of V9_REFERENCE_AUDIT_FIXES.md):

| # | Reference | Reason deferred |
|---|---|---|
| M.1 #1, #2, #3 | Becke 1993; Lee/Yang/Parr 1988; Stephens 1994 | Pre-DOI / partial DOI; writer to confirm against ACS style |
| M.2 #14 | Ragauskas et al. 2014 *Science* 344, 1246843 | 12+ co-authors; writer to expand or keep "et al." per ACS rules |
| M.3 #19 | Klochko et al. 2019 *Thin Solid Films* 683, 34-41 | No DOI; writer to locate |
| M.3 #20 | Nikolic et al. 2020 *Molecules* 25, 5635 | No DOI; writer to locate |
| M.3 #21 | Coroa 2023 (Cu/lignin/textile review) | Placeholder; writer to locate canonical DOI |
| M.3 #24 | Bechtold & Pham, *Textile Chemistry*, de Gruyter 2019 | Book chapter; verify ISBN/chapter title/pages |
| M.4 #25 | Stubbe & van der Donk 1998 *Chem. Rev.* 98, 705-762 | Tentative DOI 10.1021/cr9400875; writer to verify |
| M.4 #26 | Tommasi et al. *J. Inorg. Biochem.* (recent) | Writer must locate |
| M.4 #27 | Suzuki et al. — XPS LMM Auger Cu(I)/Cu(II) | Writer must locate |
| M.7 reviewer emails | Budnyak, Rojas, Ragauskas, Bechtold | Verify currency at submission (12-month staleness window) |

**⚠ IMPORTANT CAVEAT — file flagged in audit but NOT propagated yet:**

Section 4 of `V9_REFERENCE_AUDIT_FIXES.md` states: *"These changes are propagated into `audit_final/V9_HANDOVER_PACKAGE_v2.md` in the same commit. The original `V9_HANDOVER_PACKAGE.md` is preserved unchanged for audit-trail purposes."*

**This v2 file does not exist on disk.** Only the original `V9_HANDOVER_PACKAGE.md` is present, and it still contains the uncorrected Sportelli/Yang/Sun citations. The Section-4 patch table in V9_REFERENCE_AUDIT_FIXES.md is therefore a **prescriptive list of edits to apply**, not a record of edits already applied. The manuscript writer must apply those §M-section patches to V9_HANDOVER_PACKAGE.md (or to the redrafted manuscript reference list directly) using V9_REFERENCE_AUDIT_FIXES.md §4 as the authoritative source.

---

## Q3 — Final canonical row count + class distribution

**`audit_final/BINDING_SURVIVAL_TABLE.csv` data rows: 38** (unchanged from prior handover).

The Category-C resolution of cu2i2_guaiacol_bidentate did NOT add a new row. Both PES basins for free guaiacol on Cu₂I₂ are present as **separate pre-existing rows** in the 38-row table:

| complex_id | binding_class | BE_gas | BE_smd | cluster_fragmented | basin |
|---|---|---|---|---|---|
| cu2i2_guaiacol_phenolicO | E (NON_BINDING) | −23.39 | −21.67 | **True** | cluster-cracking phenolic-O pathway |
| cu2i2_guaiacol_bidentate | A (STRONG_BINDING) | −17.86 | −17.81 | False | intact-cluster bidentate κ²-O,O pathway |

Note: `cu2i2_guaiacol_phenolicO` is class **E (NON_BINDING)** despite a deeply favorable BE_gas of −23.39 kcal/mol — the classifier penalizes cluster fragmentation (cluster_fragmented=True), which is exactly the v9 framing the collaborator described.

**Class distribution (csv-aware count via Python):**

| Class | Label | Count |
|---|---|---|
| A | STRONG_BINDING | 20 |
| B | MODERATE_BINDING | 1 |
| C | (CLUSTER_FRAGMENTED — none classified C; the cracker pathway is logged as E with cluster_fragmented=True flag) | 0 |
| D | METASTABLE_CONTACT | 3 |
| E | NON_BINDING / DISSOCIATED / SCF artifact | 14 |
| **Total** | | **38** |

**By cluster (cluster × class):**

| Cluster | A | B | D | E | Total |
|---|---|---|---|---|---|
| Cu⁺ (naked) | 15 | 1 | 1 | 1 | 18 |
| Cu₂I₂ (neutral) | 5 | 0 | 1 | 4 | 10 |
| [CuI₂]⁻ (anion) | 0 | 0 | 1 | 9 | 10 |

(**Note on Class A on Cu₂I₂ = 5:** these are cu2i2_h2o, cu2i2_methanol, cu2i2_phenol_O, cu2i2_guaiacol_bidentate, and cu2i2_veratrole_methoxyO_startA — i.e. the κ²-O,O methoxy chelate is the strongest survivor, with phenol-O as the next strongest free-OH species. Methanol/water dominate by exchange.)

**⚠ FOLLOW-UP TASK SURFACED — `cu2i2_veratrole_pi` (E4.3, BE_smd = −23.11) is MISSING from BINDING_SURVIVAL_TABLE.csv:**

The central E4.3 finding (veratrole-π survives on Cu₂I₂ where guaiacol-π and phenol-π both detach) is fully documented in:
- `BELEGEN_EVIDENCE_MATRIX.csv` (E4.3, row 19, SUPPORTED, A_STRONG)
- `MECHANISM_VERDICT_TABLE.csv` (M4, PARTIALLY_SUPPORTED with veratrole-π as the supporting case)
- `CLAIM_SUPPORT_STATUS.csv` (claim 4, PARTIALLY_SUPPORTED, dual-mode anchor on Cu₂I₂)
- `SITE_OCCUPANCY_TABLE.csv` (cu2i2_veratrole_methoxyO_startA row, BELEGEN E3.5)

But **`BINDING_SURVIVAL_TABLE.csv` has only the four veratrole-methoxyO startA/startB rows (cu2i2_*_startA/B and cui2_*_startA/B); the cu2i2_veratrole_pi row is absent.** Adding it as a class-A row (STRONG_BINDING, BE_smd −23.11, η^n-arene mode, cluster intact) would make the canonical row count **39**, not 38, and would close the dual-channel framing on Cu₂I₂ (κ²-O,O at −26.24 + π at −23.11) inside this single table.

**Recommendation for the writer:** either (a) add cu2i2_veratrole_pi to BINDING_SURVIVAL_TABLE.csv before redraft (39 rows), or (b) keep BINDING_SURVIVAL_TABLE at 38 rows and explicitly point readers to BELEGEN_EVIDENCE_MATRIX.csv for the π-channel evidence in the manuscript Methods/SI. Option (a) is cleaner and more reviewer-defensible.

---

## Files to share with the writer (alongside this Q&A)

- `audit_final/V9_REFERENCE_AUDIT_FIXES.md` — full reference audit (Sections 1–4)
- `audit_final/_doi_lookups.json` — raw Crossref lookups (machine-readable backup)
- `audit_final/BELEGEN_EVIDENCE_MATRIX.csv` row 19 — cu2i2_veratrole_pi recovered geometry + provenance
- `audit_final/V9_HANDOVER_PACKAGE.md` — the original handover (Section M lines 414–441 are the citation block that still has the uncorrected entries)
- `audit_final/BINDING_SURVIVAL_TABLE.csv` — 38-row canonical table (with the cu2i2_veratrole_pi gap noted above)
