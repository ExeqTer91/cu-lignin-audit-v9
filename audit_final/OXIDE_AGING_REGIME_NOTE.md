# Level 6 — Oxide / Hydroxide Aging Regime (Scope Note)

**Date:** 2026-04-30 UTC
**Audit version:** v9 (Level 6 documentation layer)
**Type:** Documentation-only scope note. **No new ORCA calculations were
performed for this layer.** No Cu(II), Cu₂O, CuO, or Cu(OH)₂ DFT, and no
periodic-DFT surface-slab work, was added.

---

## 1. Purpose

This note records a literature-backed limitation of the v9 audit's CuI-cluster
DFT model: real CuI-coated textiles may locally develop Cu₂O / Cu(OH)₂ / CuO
surface fractions during laundering, washing, and ambient aging, and that
oxide / hydroxide regime favors a different binding chemistry than the
naked-Cu⁺ and CuI-cluster regimes covered in §§3–6 of `MANUSCRIPT_IMPACT_v8_to_v9.md`.

The reviewer's framing — included verbatim so the manuscript text stays
traceable to the source comment — establishes a state-dependent anchoring
ensemble:

> "Cu retention is not one mechanism. It is a state-dependent anchoring
> ensemble: CuI-rich states favor mode-selective O / π / iodide-cluster
> interactions, while oxide-aged states likely shift toward heteroatom /
> O-donor anchoring."

> "CuI / Cu₂I₂ state: π / arene binding can matter.
> [CuI₂]⁻ saturated state: straight iodide coordination rejects ligands.
> Cu₂O / CuO / Cu(OH)₂ aged state: O-donor, hydroxyl, carboxylate, phenolic,
> and water-mediated binding become more important."

## 2. Manuscript-safe limitation paragraph (verbatim)

The following paragraph is the canonical manuscript-safe statement of this
limitation. Use verbatim in any v9 manuscript revision and in any reviewer
response that touches oxidative aging:

> "Copper oxide / hydroxide aging is a distinct state that may reverse the
> CuI-cluster anchoring order. Literature indicates copper films can form
> Cu₂O, Cu(OH)₂, and CuO-like layers under ambient/oxidizing conditions, and
> CuI can be converted into CuxO phases under oxidative processing.
> Therefore, oxide-aged retention should be treated as a separate validation
> regime, not forced into the CuI-cluster DFT model."

## 3. Where Level 6 sits in the v9 model hierarchy

| Level | Model | Status in v9 |
|-------|-------|--------------|
| 1 | Naked Cu⁺ (charge=1, mult=1) — Phase 1/2 + Tier A | Computed (Case C) |
| 2 | CuI monomer cluster — Tier B | Computed (Case C, full guaiacol mode map) |
| 3 | [CuI₂]⁻ saturated anion — Set B | Computed (binding-survival classifier) |
| 4 | Cu₂I₂ dimer — Set C | Computed (binding-survival classifier) |
| 5 | Veratrole methoxy-O alternates — Task #29 | In-flight (DefGrid3 production run) |
| **6** | **Oxide / hydroxide aging regime — Cu₂O / Cu(OH)₂ / CuO surface adsorption** | **OUT_OF_SCOPE — literature-backed limitation, no new compute** |

Level 6 is a documentation-only layer. It is not a new compute campaign and
it does not alter any number, mode classification, n_imag value, or
binding-survival tag in Levels 1–5.

## 4. Reviewer-supplied references (six)

The six references below were supplied by the reviewer to substantiate the
oxide-aging regime. URLs are listed at the publisher-root level so the
citations are independently locatable; specific DOIs are intentionally not
fabricated.

1. **ACS Publications, 2007** — Cu thin-film oxidation under ambient
   conditions. Demonstrates that copper metal films grow native Cu₂O / CuO
   layers on exposure to air and humidity. Publisher root:
   <https://pubs.acs.org/>.
2. **RSC Dalton Transactions, 2013** — Cu nanoparticle oxidation pathways.
   Establishes that Cu(0)/Cu(I) nanoparticles convert to Cu₂O and CuO
   phases under ambient/oxidative aging. Publisher root:
   <https://pubs.rsc.org/en/journals/journalissues/dt>.
3. **RSC Journal of Materials Chemistry C, 2022** — γ-CuI annealing study.
   Shows that γ-CuI thin films undergo phase / surface chemistry changes
   under thermal and oxidative stress. Publisher root:
   <https://pubs.rsc.org/en/journals/journalissues/tc>.
4. **Springer Journal of Electronic Materials, 2025** — CuI → CuxO thermal
   conversion. Documents direct conversion of CuI into copper-oxide phases
   under oxidative processing. Publisher root:
   <https://link.springer.com/journal/11664>.
5. **MDPI Molecules, 2020** — CuO on cotton review. Reviews CuO formation,
   anchoring, and antimicrobial behavior on cellulose-rich textile
   substrates. Publisher root: <https://www.mdpi.com/journal/molecules>.
6. **ResearchGate** — Cu₂O surface DFT (CO₂-related adsorption study).
   Demonstrates that Cu₂O surfaces have a distinct, O-donor / hydroxyl /
   water-mediated binding chemistry that periodic-DFT slab calculations are
   designed to address. Repository root: <https://www.researchgate.net/>.

These six references are the **complete** literature basis for Level 6. No
additional citations were invented for this scope note.

## 5. Why oxide-aged retention is treated as a separate validation regime

The CuI-cluster DFT model used in Levels 1–5 represents the freshly deposited
CuI-rich state. After aging, three additional surface phases — Cu₂O, Cu(OH)₂,
and CuO — become accessible. Each has a different preferred binding chemistry
(O-donor, hydroxyl, phenolic, carboxylate, water-mediated) than the
mode-selective π / iodide-cluster chemistry seen at the CuI / Cu₂I₂ /
[CuI₂]⁻ levels. Forcing the aged-state retention into the CuI-cluster model
would:

- conflate two distinct surface phases (CuI vs Cu₂O / Cu(OH)₂ / CuO) under
  one binding-energy table;
- mis-attribute O-donor anchoring to CuI-cluster chemistry when the actual
  driver is the oxide / hydroxide layer;
- silently broaden the v9 thesis from "CuI-state mode-selective anchoring"
  to "all-state anchoring" without supporting compute.

For these reasons the oxide-aging regime is documented as a literature-backed
limitation and explicitly **not** absorbed into the CuI-cluster DFT model.
Validation belongs in a separate experimental campaign (see §6) or, if
desired, a future periodic-DFT slab model — neither of which is part of
this audit.

## 6. Recommended experimental validation protocol

For downstream investigators who need to characterize the oxide-aged regime
on real CuI-coated textiles, the following protocol is recommended. None of
these measurements are part of this v9 audit; they are recorded here so the
manuscript-impact memo and the case-decision memo can cite a concrete
validation pathway when describing Level 6.

**Surface speciation (XPS):**

- Cu 2p₃/₂ envelope — distinguish Cu(I) (~932.5 eV, narrow), Cu(II)
  (~933.5 eV with shake-up satellites at ~942–944 eV), and Cu(0).
- Cu LMM Auger — independently distinguish Cu(I) vs Cu(0) (overlap region
  in Cu 2p alone is ambiguous).
- I 3d₅/₂ — confirm iodide retention (CuI-rich) vs iodide loss (oxide-aged).
- O 1s — distinguish lattice oxide (~530 eV), hydroxide (~531–532 eV), and
  adsorbed water (~533 eV).

**X-ray absorption (XANES / EXAFS, where accessible):**

- Cu K-edge XANES — bulk-sensitive Cu oxidation-state fingerprint
  (Cu(I) edge ~8980–8983 eV; Cu(II) ~8985–8990 eV); identifies oxide /
  hydroxide vs CuI signatures.
- Cu K-edge EXAFS — first-shell coordination distinguishes Cu–I (~2.6 Å),
  Cu–O in Cu₂O (~1.85 Å), Cu–O in CuO (~1.95 Å + Jahn-Teller), and
  Cu–O in Cu(OH)₂.

**Sample matrix (for cross-comparison):**

- CuI-rich fabric (as-coated, no exposure) vs oxide-aged fabric (after
  controlled washing, ambient aging, or accelerated oxidative stress).
- Cellulose vs lignin vs methylated lignin vs oxidized lignin substrates —
  varies the O-donor / phenolic / carboxylate density to test whether
  oxide-aged retention scales with surface oxygen functional-group density.

The experimental study is the validation route for Level 6; this audit
records the literature basis and the scope statement only.

## 7. Provenance and locations

- Reviewer-verbatim state-dependent ensemble paragraph: §1 above.
- Reviewer-verbatim manuscript-safe limitation paragraph: §2 above.
- Append-target: `audit_final/MANUSCRIPT_IMPACT_v8_to_v9.md` §14
  (Level 6 — Oxide / hydroxide aging regime).
- Append-target: `audit_final/V9_CASE_DECISION.md` §4 (three new rows for
  Cu₂O / Cu(OH)₂ / CuO surface adsorption tagged
  `OUT_OF_SCOPE — oxide-aging regime; literature-backed limitation, no new compute`).
- Append-target: `audit_final/EXPERIMENT_STATUS.txt` (OXIDE AGING REGIME footer).
- Append-target: `results_v9/EXPERIMENT_STATUS.txt` (OXIDE AGING REGIME footer).
- One-line memory entry: `replit.md` v9 hierarchy section.
- No quantitative results, no BE numbers, and no Case-C conclusions are
  changed by Level 6. All edits are append-only.
