# Tier A Mode-Isolation Control Calculations — Interpretation Framework

**Status:** Pre-computation framework. All five scientific questions are posed here with
the analytical logic and interpretation criteria. Numerical answers are filled in once
ORCA jobs complete. Refer to `CONTROL_BINDING_TABLE.csv` and `CONTROL_MODE_TABLE.csv`
for raw data.

**Canonical Cu⁺ reference energy:** −1640.134600256611 Eh (gas, B3LYP-D3BJ/def2-TZVP,
`/workspace/results/cu_ion_sp.out`, SHA-256: b8e25fdc…)

**Phase 1 context (from ORCA_BINDING_ENERGIES.csv):**
- cu_guaiacol_pi (π-start) overwhelmingly preferred over phenolic-O and methoxy-O starts,
  reversing the manuscript's claim of O-coordination as dominant mode.
- All guaiacol adducts still PENDING for final energies; mode assignments in progress.

---

## Scientific Questions and Interpretation Criteria

### Q1 — Is guaiacol's strong Cu⁺ binding driven by the *ortho* O,O-chelation geometry?

**Hypothesis:** The ortho arrangement of phenolic-OH and methoxy-O in guaiacol creates
a unique bidentate chelation pocket. Removing the ortho geometry (meta or para
substitution) should weaken or eliminate the bidentate mode.

**Controls:**
| System | Feature removed |
|--------|----------------|
| `meta_methoxyphenol` | Ortho geometry — OMe now at C3 |
| `para_methoxyphenol` | Ortho geometry — OMe now at C4 |
| `catechol` | Methoxy group — replaced by phenolic OH, preserving ortho O,O |

**Decision logic:**
- If `cu_meta_methoxyphenol` and `cu_para_methoxyphenol` adducts do **not** achieve
  bidentate final modes, and their best BE (kcal/mol) is substantially weaker than
  the Phase 1 guaiacol bidentate/π result → ortho geometry **is** the driver.
- If meta/para adducts still prefer π and match guaiacol in BE → ortho geometry is
  **not** the key discriminator; π-binding dominates regardless of OMe position.
- If `cu_catechol_bidentate` achieves strong bidentate (expected: most negative BE in
  this set) → confirms ortho O,O geometry per se is a strong bidentate driver when
  the two donors are both hydroxyl.

**Planned answer (fill after jobs):** PENDING

---

### Q2 — Is π-binding alone (benzene) sufficient to exceed the aliphatic OH baseline?

**Hypothesis:** π-coordination of bare Cu⁺ to an aromatic ring is intrinsically
favorable enough to exceed simple aliphatic O-coordination (cyclohexanol or methanol
Phase 1 reference). If so, the aromatic π-system is the primary structural feature
enabling strong lignin–Cu binding.

**Controls:**
| System | Role |
|--------|------|
| `cu_benzene_pi` | Pure aromatic π — no O-donor |
| `cu_cyclohexanol_O` | Aliphatic OH baseline (better cellulose proxy than methanol) |
| Phase 1 `cu_methanol` | Methanol O-baseline (pending) |

**Decision logic:**
- Compare BE(cu_benzene_pi, gas) vs BE(cu_cyclohexanol_O, gas) and same for SMD.
- If BE(benzene-π) is more negative than BE(cyclohexanol-O) → aromatic π alone
  exceeds the cellulose OH reference. This has significant implications for
  polymer-accessibility (see Q5).
- If BE(benzene-π) ≈ BE(cyclohexanol-O) or less negative → π-binding alone is not
  sufficient; additional O-donor interaction is needed to explain guaiacol's preference.
- Also compare with Phase 1 methanol result when available as secondary reference.

**Planned answer (fill after jobs):** PENDING

---

### Q3 — Do the meta/para isomers remove the bidentate advantage seen in guaiacol?

**Hypothesis:** Moving the methoxy group from ortho to meta or para breaks the
geometric constraint required for simultaneous O,O-chelation. The adducts should
instead converge to either pure π-binding or single-O binding.

**Controls:**
| System | Start mode | Expected convergence |
|--------|-----------|---------------------|
| `cu_meta_methoxyphenol_phenolicO` | phenolicO | Single-O or π-slip |
| `cu_meta_methoxyphenol_pi` | pi | π or single-O |
| `cu_para_methoxyphenol_phenolicO` | phenolicO | Single-O or π-slip |
| `cu_para_methoxyphenol_pi` | pi | π or single-O |

**Decision logic:**
- Record `final_mode` from CONTROL_MODE_TABLE.csv for all four adducts.
- If any meta/para adduct achieves `final_mode = bidentate` → geometry constraint
  is relaxed at meta/para, OR the DFT optimizer finds an unexpected path (report
  with Cu–O distances and O–Cu–O angle).
- If all meta/para adducts converge to `pi` or `phenolicO` (single) → ortho geometry
  is confirmed as prerequisite for bidentate mode.
- Compare best BE of meta/para vs guaiacol best BE (Phase 1):
  - If Δ(BE) > 5 kcal/mol in favour of guaiacol → ortho chelation provides a
    measurable stabilisation beyond what π or single-O can provide.
  - If Δ(BE) < 3 kcal/mol → guaiacol's preference is dominated by π, not chelation.

**Planned answer (fill after jobs):** PENDING

---

### Q4 — Does catechol confirm a strong O,O bidentate positive control?

**Hypothesis:** Catechol (1,2-dihydroxybenzene) has two phenolic OHs in the ortho
arrangement — the strongest possible hydroxyl-based bidentate donor. It should exhibit
the most negative BE among the O-donor controls, and the bidentate start should be
a stable minimum.

**Controls:**
| System | Start mode | Expected |
|--------|-----------|---------|
| `cu_catechol_bidentate` | bidentate | Strong bidentate minimum |
| `cu_catechol_pi` | pi | May slip to bidentate or remain π |

**Decision logic:**
- Check `final_mode` for cu_catechol_bidentate: if it remains `bidentate` with
  Cu–O1 and Cu–O2 both < 2.2 Å and O–Cu–O angle ~65–80° → confirms bidentate
  minimum is real and stable.
- If cu_catechol_pi converges to bidentate as well → bidentate is the global minimum
  regardless of start geometry; strong positive control confirmed.
- Compare BE(catechol bidentate) vs BE(meta/para phenolicO):
  - Expect catechol bidentate to be more negative by 5–15 kcal/mol.
  - If the gap is smaller → O,O bidentate advantage is modest.

**Tier B context:** If Tier B (Task #3) shows CuI/Cu₂I₂ does not exhibit bidentate
with guaiacol, catechol's bidentate result here tells us the geometric feature *can*
support bidentate with naked Cu⁺ but is blocked in the organometallic context.

**Planned answer (fill after jobs):** PENDING

---

### Q5 — Which binding modes are plausibly polymer-accessible?

**Hypothesis:** Bidentate and some π modes may require Cu⁺ to approach the aromatic
ring from a sterically unhindered direction. In a cross-linked lignin or lignocellulosic
polymer, ring faces and chelation pockets may be blocked by adjacent chains.

**Polymer-accessibility analysis (to be completed after jobs):**

| Mode | Steric demand | Expected accessibility in polymer |
|------|--------------|----------------------------------|
| Single O-binding (phenolicO, methoxyO) | Low — Cu approaches lone pair on pendant O | High — O groups on periphery |
| π-binding | Medium — Cu must approach ring face | Low-to-medium — rings often π-stacked or embedded |
| Bidentate O,O | High — Cu must simultaneously contact two O atoms in correct geometry | Low — pocket may be blocked by adjacent polymer |
| Cyclohexanol O (aliphatic) | Low — same as phenolicO | High — modelling cellulose OH |

**Key test:** Compare:
- BE(cu_cyclohexanol_O) — accessible in polymer ✓
- BE(cu_benzene_pi) — sterically hindered in polymer ✗
- BE(cu_catechol_bidentate) — very hindered in polymer ✗
- BE(cu_anisole_pi) vs BE(cu_anisole_methoxyO) — which is preferred, and which is accessible?

If the most stable modes (largest |BE|) are also the least polymer-accessible
(π and bidentate), then the manuscript's effective binding affinity in the polymer
may be much weaker than the naked-Cu⁺ gas-phase numbers suggest.

**Planned answer (fill after jobs):** PENDING

---

## Tier B Integration

Results from Tier B (CuI complex controls, Task #3) are essential context:

- If Tier B shows that the actual CuI source (CuI salt or Cu₂I₂) does **not** bind
  guaiacol in the bidentate or π modes (due to iodide competition or steric blocking),
  then the Tier A bare-Cu⁺ results represent an upper bound on binding affinity that
  is never reached in practice.

- If Tier B shows that CuI binds guaiacol similarly to bare Cu⁺, the Tier A mode
  hierarchy (π > bidentate > single-O >> aliphatic-O) is directly applicable to the
  experimental system.

- The manuscript claims O-coordination dominates. If Tier A shows π ≫ O for bare Cu⁺,
  and Tier B shows the same trend holds for CuI, the manuscript's central claim is
  falsified across both models.

**Tier B status:** PENDING (Task #3 runs in parallel or immediately after Task #2)

---

## Data Provenance

| File | Contents |
|------|----------|
| `CONTROL_BINDING_TABLE.csv` | ΔE_gas and ΔE_SMD for all adducts; start_mode and final_mode |
| `CONTROL_MODE_TABLE.csv` | Coordination mode assignments with Cu–O distances and Cu–centroid distances |
| `control_calculations/` | All raw .out files and parsed summaries |
| `control_calculations/run_summary.json` | Metadata for the calculation run |

**ORCA settings used:**
- Opt+Freq: `! B3LYP D3BJ def2-TZVP RIJCOSX def2/J TightSCF TightOpt Opt Freq`
- SMD SP: `! B3LYP D3BJ def2-TZVP RIJCOSX def2/J TightSCF Grid5 FinalGrid6 SP`
  with `%cpcm smd true SMDsolvent "water" end` (cpcm_block syntax)
- nprocs: 16–24, MAXCORE: 4000–6000 MB, MAX_CONCURRENT_RUNPOD_JOBS: 2
- Cu⁺ reference energy shared with Phase 1 canonical set (no re-calculation)
