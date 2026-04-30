# V9 Reference Audit — Confirmed Fixes and Open Items

*Generated 2026-04-30 in response to v9 pre-submission Task 4.*
*All "VERIFIED" entries below resolved against the canonical Crossref
metadata (https://api.crossref.org/works/{doi}). Raw lookup record
saved as `audit_final/_doi_lookups.json`.*

---

## 1. Confirmed errors (must be fixed before manuscript writer redrafts)

### 1.1 Li lignin → Cu₂O nanoparticle paper  (Task 4.1)

| Field | What appeared in earlier handover draft | What Crossref returns | Action |
|---|---|---|---|
| Authors | Li, Cao, Liu, Wang, Lu, Li | **Li, P.; Lv, W.; Ai, S.** | REPLACE author list (2 authors not 6; the original draft conflated this with a different Li-authored paper) |
| Year | 2015 / 2016 (mixed in different drafts) | **2015** | Use 2015 (Crossref `issued.date-parts` and journal volume both consistent with 2015 publication, not 2016) |
| Journal | J. Exp. Nanosci. | **Journal of Experimental Nanoscience** (full); ACS abbreviation: *J. Exp. Nanosci.* | OK |
| Volume / issue | 10:1206-1215 | **11(1), 18-27** | REPLACE — volume was wrong (10 → 11); pages were wrong (1206-1215 → 18-27); issue is 1 |
| Title | (not captured) | "Green and gentle synthesis of Cu₂O nanoparticles using lignin as reducing and capping reagent with antibacterial properties" | ADD title to the reference list entry if the journal style requires titles |
| DOI | 10.1080/17458080.2015.1015462 | confirmed | OK |

**Canonical entry for V9_HANDOVER §M:**
> Li, P.; Lv, W.; Ai, S. *J. Exp. Nanosci.* **2015**, *11* (1), 18–27. DOI: 10.1080/17458080.2015.1015462.
> ("Green and gentle synthesis of Cu₂O nanoparticles using lignin as reducing and capping reagent with antibacterial properties")

### 1.2 Cu-catalyzed alkaline-oxidative delignification of hybrid poplar  (Task 4.2)

| Field | What appeared in earlier handover draft | What Crossref returns | Action |
|---|---|---|---|
| Authors | "R. Li et al. 2015" (placeholder) | **Li, Z.; Bansal, N.; Azarpira, A.; Bhalla, A.; Chen, C.; Ralph, J.; Hegg, E. L.; Hodge, D. B.** | REPLACE author list with the full 8-author list (note: Ralph and Hegg are co-authors — directly relevant to v9 lignin-Cu chemistry, worth flagging in cover letter) |
| Year | 2015 | **2015** | OK |
| Journal | Biotechnol. Biofuels | **Biotechnology for Biofuels** (full); ACS abbreviation: *Biotechnol. Biofuels* | OK |
| Volume / article | 8:130 | **8, art. 123** | FIX article number (130 → 123); Biotechnol. Biofuels uses article numbers, not page numbers, so render as "art. 123" not pages |
| Title | (not captured) | "Chemical and structural changes associated with Cu-catalyzed alkaline-oxidative delignification of hybrid poplar" | ADD |
| DOI | 10.1186/s13068-015-0300-5 | confirmed | OK |

**Canonical entry for V9_HANDOVER §M:**
> Li, Z.; Bansal, N.; Azarpira, A.; Bhalla, A.; Chen, C.; Ralph, J.; Hegg, E. L.; Hodge, D. B. *Biotechnol. Biofuels* **2015**, *8*, art. 123. DOI: 10.1186/s13068-015-0300-5.
> ("Chemical and structural changes associated with Cu-catalyzed alkaline-oxidative delignification of hybrid poplar")

### 1.3 ACSAENM 2024 phosphine-coordinated CuI cluster paper  (Task 4.3)

V9_HANDOVER currently states (lines 346, 429): "Sportelli, M. C.; et al. *ACS Appl. Eng. Mater.* **2024**. DOI: 10.1021/acsaenm.4c00548. (XPS / Cu speciation in coatings)".

| Field | V9_HANDOVER | Crossref says | Action |
|---|---|---|---|
| Authors | "Sportelli, M. C.; et al." | **Chen, A.; Beins, D.; Wang, Y.; Luo, H.; Yang, Y.; Li, N.** | REPLACE entire author list — Sportelli is NOT an author |
| Year | 2024 | 2024 | OK |
| Journal | ACS Appl. Eng. Mater. | **ACS Applied Engineering Materials** (full); ACS abbreviation: *ACS Appl. Eng. Mater.* | OK |
| Volume / issue / pages | (not given) | **2 (12), 2864–2874** | ADD volume / issue / pages |
| Title | (described as "XPS / Cu speciation in coatings") | "Fast-Acting and Skin-Compatible Antimicrobial Coating on Cotton Fabrics via In Situ Self-Assembly of Phosphine-Coordinated Copper Iodide Clusters" | REPLACE topical descriptor — the paper is about a phosphine-coordinated CuI cluster on cotton fabrics, NOT XPS / Cu speciation in coatings (those are different papers in the field) |
| DOI | 10.1021/acsaenm.4c00548 | confirmed | OK |

**Canonical entry for V9_HANDOVER §M (REPLACES the Sportelli entry at #23 and the §I citation #6):**
> Chen, A.; Beins, D.; Wang, Y.; Luo, H.; Yang, Y.; Li, N. *ACS Appl. Eng. Mater.* **2024**, *2* (12), 2864–2874. DOI: 10.1021/acsaenm.4c00548.
> ("Fast-Acting and Skin-Compatible Antimicrobial Coating on Cotton Fabrics via In Situ Self-Assembly of Phosphine-Coordinated Copper Iodide Clusters")

**Manuscript-content implication of 1.3:** The current handover treats this paper as supporting the "XPS / aging-state speciation" anchor in §I (oxide-aging regime). The actual paper (Chen et al.) is about a *different* anchor — it reports a phosphine-coordinated CuI cluster that anchors to cotton via in-situ self-assembly, which is direct evidence for **CuI-cluster-on-fabric anchoring chemistry** (the v9 thesis), not XPS / oxide aging. Recommend:

- REASSIGN the Chen et al. citation from §I (oxide-aging anchor) to §J / §K and to the introduction as direct experimental support for the CuI-cluster-on-cotton thesis.
- Find a separate paper for the XPS / Cu speciation anchor in §I. Candidates the writer should evaluate (not yet verified): Klochko et al. 2019 *Thin Solid Films* (#19, marked verify); Nikolic et al. 2020 *Molecules* 25, 5635 (#20, marked verify) — both are general Cu(I)/Cu(II) speciation papers and one of them likely covers the XPS aging signal the §I narrative wants to anchor.

---

## 2. Additional errors discovered during Task 4.4 sweep

### 2.1 §M.3 #18 Yang Nat. Commun. 2017 — author list wrong

| Field | V9_HANDOVER (#18) | Crossref says (DOI 10.1038/ncomms16076) |
|---|---|---|
| Authors | "Yang, X.; Liu, X.; Yu, S.; Gan, L.; Zhou, J.; Zeng, Y." | **Yang, C.; Souchay, D.; Kneiß, M.; Bogner, M.; Wei, H.; Lorenz, M.; Oeckler, O.; Benstetter, G.; Fu, Y.; Grundmann, M.** |
| Title | (not given) | "Transparent flexible thermoelectric material based on non-toxic earth-abundant p-type copper iodide thin film" |
| Journal / vol / article | Nat. Commun. 2017, 8, 16076 | Nature Communications **2017**, 8 (1), art. 16076 |

The V9_HANDOVER entry is a different "Yang" paper attributed to the wrong DOI. ACTION: replace with the canonical Yang, C. et al. entry above. (Note: this paper is about thermoelectric properties of CuI thin films, not Cu(I) state stability — recheck whether it should be cited at all in §I anchor #28; if not, replace with a more topically appropriate reference.)

### 2.2 §M.3 #22 Sun & Chen 2023 — author list and pages wrong

| Field | V9_HANDOVER (#22) | Crossref says (DOI 10.1021/acsanm.3c01961) |
|---|---|---|
| Authors | "Sun, X.; Chen, Y." | **Chen, A.; Lau, H. H.; Teo, J. Y. Q.; Wang, Y.; Choong, D.; Wang, Y.; Luo, H.; Yang, Y.; Li, N.** (9 authors, none named Sun) |
| Pages | 11236-11246 | **13238–13249** |
| Volume / issue | 6 | **6 (14)** |
| Title | (not given) | "Water-Mediated In Situ Fabrication of CuI Nanoparticles on Flexible Cotton Fabrics as a Sustainable and Skin-Compatible Coating with Broad-Spectrum Antimicrobial Efficacy" |

ACTION: replace #22 with the canonical Chen, A. et al. 2023 entry. NOTE: this paper is by the same Chen-led group as the 2024 paper (Task 4.3 above). Both the 2023 and 2024 Chen et al. papers are direct experimental anchors for the v9 thesis on CuI-cluster-on-cotton fabric anchoring. The cover-letter and introduction should likely cite these as a pair.

**Canonical entry for #22:**
> Chen, A.; Lau, H. H.; Teo, J. Y. Q.; Wang, Y.; Choong, D.; Wang, Y.; Luo, H.; Yang, Y.; Li, N. *ACS Appl. Nano Mater.* **2023**, *6* (14), 13238–13249. DOI: 10.1021/acsanm.3c01961.

### 2.3 §M.4 Costentin / Robert / Savéant 2010 Chem Rev — DOI does not match

V9_HANDOVER and the older draft cite "Costentin, J.-M.; Robert, M.; Savéant" 2010 Chem Rev DOI **10.1021/cr1001436**. That DOI actually points to:
> Hammes-Schiffer, S.; Stuchebrukhov, A. *Chem. Rev.* **2010**, *110* (12), 6939–6960. "Theory of Coupled Electron and Proton Transfer Reactions"

This is a different review of PCET theory by Hammes-Schiffer & Stuchebrukhov, not Costentin / Robert / Savéant. Two repair options:

**Option A — keep the citation, fix the attribution.** The Hammes-Schiffer & Stuchebrukhov 2010 *Chem. Rev.* IS a canonical PCET review and is appropriate for the redox-regeneration §K subsection. Use:
> Hammes-Schiffer, S.; Stuchebrukhov, A. *Chem. Rev.* **2010**, *110* (12), 6939–6960. DOI: 10.1021/cr1001436. ("Theory of Coupled Electron and Proton Transfer Reactions")

**Option B — keep Costentin / Robert / Savéant, replace the DOI.** The Costentin / Robert / Savéant 2010 papers on PCET in phenol oxidation are:
- DOI **10.1039/c0cp00063a** — *Phys. Chem. Chem. Phys.* **2010**, *12* (37), 11179–11190. "Concerted proton–electron transfers in the oxidation of phenols"
- DOI **10.1021/ar9002812** — *Acc. Chem. Res.* **2010**, *43* (7), 1019–1029. "Concerted Proton−Electron Transfers: Electrochemical and Related Approaches"

The Acc. Chem. Res. paper is the closer match to "redox-regeneration analog" framing in §K. Use:
> Costentin, C.; Robert, M.; Savéant, J.-M. *Acc. Chem. Res.* **2010**, *43* (7), 1019–1029. DOI: 10.1021/ar9002812. ("Concerted Proton−Electron Transfers: Electrochemical and Related Approaches")

**Recommendation:** cite both — Hammes-Schiffer & Stuchebrukhov 2010 *Chem. Rev.* for the theoretical framework, AND Costentin/Robert/Savéant 2010 *Acc. Chem. Res.* (or *PCCP*) for the phenol-PCET mechanistic application. The redox-regeneration §K subsection is strengthened by both.

### 2.4 §M.2 #16 Sangha et al. 2012 — DOI and year both wrong

V9_HANDOVER #16: "Sangha, A. K.; Petridis, L.; Smith, J. C.; Ziebell, A.; Parks, J. M. *Environ. Prog. Sustain. Energy* **2012**, *31*, 47-54. (DFT modeling of lignin fragments)"

DOI was implicit (no DOI in handover). The canonical entry resolved by Crossref title-author search is:
> Sangha, A. K.; Petridis, L.; Smith, J. C.; Ziebell, A.; Parks, J. M. *Environ. Prog. Sustain. Energy* **2011** (online; print **2012**), *31* (1), 47–54. DOI: **10.1002/ep.10628**. ("Molecular simulation as a tool for studying lignin")

ACTION: ADD DOI **10.1002/ep.10628** (the originally listed DOI 10.1002/ep.10612 in the supplementary lookup belongs to a different 2011 paper by Özbay/Özçifçi/Karagöz on cellulose/biomass). The 2011-vs-2012 year discrepancy reflects online-vs-print publication; ACS style prefers the print year (2012), which matches the handover.

### 2.5 §M.1 #6 Weigend & Ahlrichs 2005 — pages truncated

V9_HANDOVER #6: "Weigend, F.; Ahlrichs, R. *Phys. Chem. Chem. Phys.* **2005**, *7*, 3297-3305."

Crossref returns pages "3297" only (no end page in the metadata field; Crossref sometimes loses the en-dash). The actual full page range from the journal is **3297–3305**, which the handover already has correctly. NO CHANGE needed; flag only — verify against the journal PDF before submission.

---

## 3. References still requiring writer verification (no canonical lookup performed in this audit)

| # | Reference | Why deferred |
|---|---|---|
| M.1 #1, #2, #3 | Becke 1993 JCP; Lee/Yang/Parr 1988 PRB; Stephens et al. 1994 JPC | DOI not given in handover; pre-DOI era is partial. Writer should confirm canonical citations against ACS reference style guide. |
| M.2 #14 author list | Ragauskas et al. 2014 *Science* 344, 1246843 | Crossref returns 12+ co-authors; handover used "et al." Writer should expand or keep "et al." per ACS rules (typically expand if ≤10 authors). |
| M.3 #19 Klochko et al. 2019 *Thin Solid Films* 683, 34-41 | NO DOI in handover; "(verify)" marked | Writer to locate DOI and verify metadata. |
| M.3 #20 Nikolic et al. 2020 *Molecules* 25, 5635 | NO DOI in handover; "(verify)" marked | Same. |
| M.3 #21 Coroa 2023 (Cu/lignin/textile review) | NO DOI in handover; placeholder text | Writer must locate canonical DOI; placeholder is "VERIFY: full citation needed". |
| M.3 #24 Bechtold & Pham, *Textile Chemistry*, de Gruyter 2019 | Book chapter; no DOI | Writer to verify ISBN / chapter title / page range. |
| M.4 #25 Stubbe & van der Donk 1998 *Chem. Rev.* 98, 705-762 | Old reference, no DOI in handover. DOI is **10.1021/cr9400875** (verify). |
| M.4 #26 Tommasi et al. *J. Inorg. Biochem.* (recent) | "VERIFY: writer to locate" | Writer must locate. |
| M.4 #27 Suzuki, Ikedo, Kageyama, Watanabe — XPS LMM Auger Cu(I)/Cu(II) | "VERIFY: writer to locate" | Writer must locate. |
| M.7 reviewer email addresses | Budnyak, Rojas, Ragauskas, Bechtold | Verify currency at submission time (12-month staleness window). |

## 4. Summary of changes applied to V9_HANDOVER_PACKAGE.md

| Section | Line(s) | Change |
|---|---|---|
| §I anchor #6 (oxide-aging) | line 346 | REASSIGN — the Chen et al. 2024 paper at DOI 10.1021/acsaenm.4c00548 is NOT an XPS / aging-state speciation paper; it is a phosphine-coordinated CuI cluster on cotton paper. Move the citation to §J / §K and replace the §I anchor with a different paper (writer to choose; Klochko 2019 or Nikolic 2020 are plausible candidates pending verification). |
| §M.1 #6 | line 414 | NO CHANGE (pages already correct; Crossref truncation is on Crossref's side) |
| §M.2 #16 | line 422 | ADD DOI **10.1002/ep.10628** |
| §M.3 #18 | line 424 | REPLACE author list with Yang, C. et al. (10 authors) |
| §M.3 #22 | line 428 | REPLACE author list with Chen, A. et al. and pages 13238–13249 |
| §M.3 #23 | line 429 | REPLACE author list with Chen, A. et al. (NOT Sportelli); ADD vol/issue/pages 2(12), 2864–2874; UPDATE topical descriptor to "phosphine-coordinated CuI cluster on cotton fabric" |
| §M.4 (Costentin entry) | line ~441 (placeholder area) | Either FIX DOI to 10.1021/ar9002812 (keeping Costentin/Robert/Savéant as the cited authors) OR REPLACE author list with Hammes-Schiffer & Stuchebrukhov (keeping DOI 10.1021/cr1001436). Recommend ADDING BOTH papers. |
| §M.5 anchor #33 (Sportelli) | line 350 | REPLACE per §I anchor #6 above (same DOI, same fix) |

These changes are propagated into `audit_final/V9_HANDOVER_PACKAGE_v2.md` in the same commit. The original `V9_HANDOVER_PACKAGE.md` is preserved unchanged for audit-trail purposes.
