# Changelog

All notable changes to the **Cu-Lignin DFT Audit Pipeline (v9)** dataset are
documented in this file.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/);
versioning follows the manuscript-revision cycle, not strict semver.

---

## [v9.4] — 2026-05-03

### Added
- `audit_final/cu2i2_veratrole_pi_opt_freq_v2.{out,xyz,hess,gbw,property.txt,inp,opt,trj.xyz}`
  — full Opt + analytical Freq re-run of the **η²-π Cu₂I₂·veratrole** species
  on a fresh A100-host CPU pod (RunPod, 8 MPI ranks, 5000 MB/core), warm-started
  from the recovered v1 `.gbw`.
  - Method: `B3LYP D3BJ def2-TZVP def2/J RIJCOSX TightSCF DefGrid3 Opt Freq`
  - Charge / multiplicity: `0 / 1`
  - Convergence: standard `Opt` criteria, **HURRAY at cycle 23** (3 of 4
    geometric criteria explicitly converged; `MaxIter 200`).
  - Final energy: `E = −4337.780088 Eh`
  - **n_imag = 1** at **−15.82 cm⁻¹** (see below for mode analysis).
  - Total walltime: **1 h 05 min 26 s**.
  - SHA-256 (`.out`): `3c76460b77de8f20cb4ad35619bab2b4e99b31778199cf061fd1bc0665063939`

### Changed
- `audit_final/BINDING_SURVIVAL_TABLE.csv`, row 40 (`cu2i2_veratrole_pi`):
  - `strongest_contact_distance`: `2.2400 → 2.2278` Å.
  - `n_imag`: `0 → 1`; `min_freq_cm1`: `(empty) → −15.82` cm⁻¹.
  - `notes` updated with v9.4 re-optimisation summary, fragment-decomposed
    mode-6 character (Cu+I core = 2.4 %; methoxy torsion = 50.3 %;
    arene C-H wag = 30.1 %), and the new `.out` SHA-256.
  - `timestamp_utc`: `20260430T151900Z → 20260503T124654Z`.

### Confirmed (geometry vs manuscript)
| Quantity                       | v9.4 (cycle-23 v2) | manuscript value | Δ        |
|--------------------------------|--------------------|------------------|----------|
| Cu–O closest (Å)               | 3.941              | 3.91             | +0.031   |
| Cu–C η²-π pair (Å)             | 2.228 / 2.388      | 2.24 / 2.37      | ≤ 0.018  |
| Cu–C, third (Å)                | 2.768              | —                | (η² gap) |
| Cu–Cu (Å)                      | 2.4766             | 2.478            | −0.001   |
| Cu–I, sorted (Å)               | 2.495 / 2.497 / 2.697 / 2.734 | 2.499 / 2.501 / 2.700 / 2.710 | ≤ 0.024 |

The Cu₂I₂ core is preserved; the η²-π anchor signature is clean (gap of
0.38 Å between the two short Cu–C contacts and the third).

### Frequency-analysis disposition
The single imaginary mode at −15.82 cm⁻¹ is mass-weighted-Cartesian-decomposed
across fragments as:

| Fragment                       | % of mode-6 motion |
|--------------------------------|--------------------|
| Cu + I (Cu₂I₂ core)            | **2.4 %**          |
| arene ring carbons (C4-C9)     | 17.3 %             |
| arene C–H wagging (H20-H23)    | 30.1 %             |
| methoxy-1 (O-CH₃)              | 31.2 %             |
| methoxy-2 (O-CH₃)              | 19.1 %             |

The Cu–arene contact carries only ~10 % of the motion (η²-π C8/C9 carbons);
the dominant character is coupled methoxy torsion + aryl C–H wag on a flat PES.
This matches the canonical signature of a numerical-grid small-imaginary
artefact on a methoxy-rich aromatic ligand and is **not** a Cu-arene contact
instability. The geometry is therefore treated as an **effective minimum**
for engineering-relevant comparison, with the imaginary mode disclosed in
SI rather than removed via a symmetry-breaking re-start.

### Provenance
- Original recovered `.out` (SHA-256 `f2a9007b88dc7098f266224b8715c741653e75e1d547dafd4236b8b2584a8ff2`)
  remains the historical evidence for E4.3 (BE / n_imag pedigree).
  The v2 re-optimisation supersedes its **geometry-level** descriptors only;
  BE values are unchanged.

### Documentation patches
- `CITATION.cff`: target-journal language replaced with neutral
  "submitted to a peer-reviewed journal; under review" pending acceptance.
- `audit_final/FINAL_COMPUTATIONAL_AUDIT_STATUS.txt`: the legacy "DATA LOSS"
  section is now explicitly annotated as SUPERSEDED inline (the file-level
  banner already noted recovery; the section body now agrees).
- `reproducibility/REPRODUCE.md`: hardware description tightened to make
  explicit that calculations ran on the **CPU host** of A100 nodes and that
  the A100 GPU itself is not used.

---

## [v9.0] — 2026-04-30

Initial public deposit accompanying manuscript submission. See
`audit_final/V9_HANDOVER_PACKAGE.md` for the full handover record.
