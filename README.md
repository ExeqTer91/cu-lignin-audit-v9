# Cu-Lignin DFT Audit Pipeline (v9)

This repository contains the complete computational audit pipeline for
the manuscript:

**Mode-Selective CuI Anchoring on Lignin-Inspired Fiber Interfaces:
A DFT Cluster-Model Study**

Andrei Ursachi, Independent Researcher, Diepholz, Germany
ORCID: [0009-0002-6114-5011](https://orcid.org/0009-0002-6114-5011)
Contact: contact@andreiursachi.eu

Manuscript DOI: *[to be inserted upon acceptance]*
Preprint (v8): <https://doi.org/10.21203/rs.3.rs-8935698/v1>
&nbsp;&nbsp;*(v9 correction will be posted upon acceptance)*

## What this repository contains

Every input file, output file, and derived analysis table referenced
in the manuscript is here, organized into two directories:

- `audit_final/` — canonical pipeline outputs:
  - 39-row binding-energy survival table with classifier verdicts
  - per-species geometry and frequency audits
  - SHA-256 indexed raw-file manifest
  - per-claim verdict tables (BELEGEN, CLAIM_SUPPORT, MECHANISM_VERDICT,
    SITE_OCCUPANCY)
  - reclassification notes documenting the conservative classifier rules
  - oxide-aging regime literature note (scope statement)
  - case-determination decision document
  - manuscript impact analysis (v8 → v9 sentence-level changes)

- `audit_final_setD_alt_diag/` — Set D V2 follow-up:
  - veratrole rotamer scan (four starting geometries, two cluster types)
  - build script that regenerates all v9 closeout tables from canonical
    inputs
  - grid-sensitivity test inputs

- `manuscript/` — handover documents used by the manuscript writer:
  - `V9_HANDOVER_PACKAGE.md` (v1, original handover)
  - `V9_HANDOVER_PACKAGE_v2.md` (v2, with reference patches applied)
  - `V9_REFERENCE_AUDIT_FIXES.md` (per-reference Crossref audit log)

- `reproducibility/` — instructions and templates for re-running any
  ORCA calculation in the dataset.

## Computational basis

ORCA 6.1.1 official binary; B3LYP-D3(BJ); def2-TZVP all-electron Cu;
def2/J auxiliary basis for RIJCOSX; SMD(water) single points at
gas-phase optimized geometry; TightSCF, TightOpt; DefGrid3 (Lebedev 302
/ m4) for geometry and frequencies. All copper atoms are treated
all-electron; the Karlsruhe def2 basis family is all-electron for
Z ≤ 36. Selected reference monomers were cross-checked at Grid5/
FinalGrid6 with binding energies converged to within 0.05 mEh of
DefGrid3 baseline values. def2-TZVPP single-point checks preserved the key
CuI methanol / guaiacol-phenolic-O comparison: the relative gap
between these two binding modes remained approximately 0.5 kcal/mol,
while absolute binding energies shifted by a few kcal/mol relative to
the def2-TZVP baseline. The qualitative ordering and the manuscript's
mode-selection conclusions are unchanged at the larger basis.

## How to verify a result

1. Locate the result in `audit_final/BINDING_SURVIVAL_TABLE.csv` by
   `complex_id`.
2. The `notes` column lists the relevant data source and any
   provenance flags.
3. Cross-reference the SHA-256 in `audit_final/RAW_FILE_INDEX.csv`
   to confirm the source ORCA output file integrity.
4. For the Set D V2 veratrole rotamer scan, all distilled
   geometry/energy/frequency data is in
   `audit_final_setD_alt_diag/setD_alt_v2_analysis.json`.

## Reproducing a calculation

See [`reproducibility/REPRODUCE.md`](reproducibility/REPRODUCE.md) for
ORCA input file reconstruction from `RAW_FILE_INDEX.csv` method-line
entries plus the per-species charge / multiplicity / starting XYZ in
`ORCA_GEOMETRY_AUDIT.csv`.

## Provenance note

The `cu2i2_veratrole_pi` result was originally computed in the Set D
production run. The raw output file was temporarily inaccessible
after a transient compute-platform storage event on 2026-04-30T11:02Z
and was subsequently recovered from a migrated compute node on
2026-04-30T15:19Z.
SHA-256: `f2a9007b88dc7098f266224b8715c741653e75e1d547dafd4236b8b2584a8ff2`.
An independent confirmation rerun on the original platform (prior to
the storage event) gave binding energies of −22.99 kcal/mol (gas) and
−23.12 kcal/mol (SMD water), in agreement with the recovered
production result (−22.98 / −23.11) within rounding.

## Citation

If you use this dataset, please cite the manuscript and this
repository. See [`CITATION.cff`](CITATION.cff).

## License

This repository is released under the
[Creative Commons Attribution 4.0 International License (CC-BY-4.0)](LICENSE).
You may share and adapt the material for any purpose, including commercially,
provided you give appropriate credit (cite the manuscript and this dataset),
provide a link to the license, and indicate if changes were made.

## Contact

For questions about the dataset, contact the author at
contact@andreiursachi.eu.
