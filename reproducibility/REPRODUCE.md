# Reproducing ORCA Calculations

All ORCA input files used in this study are reconstructable from the
canonical CSV files. This document describes the reconstruction
procedure.

## Required software

- ORCA 6.1.1 official binary (free for academic use; available from
  <https://orcaforum.kofo.mpg.de/>)
- Sufficient compute to run B3LYP-D3(BJ)/def2-TZVP optimizations and
  frequency analyses on systems up to 30 atoms. Production
  calculations in this study were run on NVIDIA A100 GPUs (RunPod)
  with wall times of 30 minutes to 6 hours per opt+freq job.

## Reconstructing an input file

For any `complex_id` in `audit_final/BINDING_SURVIVAL_TABLE.csv`:

1. Look up the species in `audit_final/RAW_FILE_INDEX.csv` and copy
   the `method_line` column. This is the ORCA simple-input keyword
   line.
2. Look up the species in `audit_final/ORCA_GEOMETRY_AUDIT.csv` and
   copy the `charge`, `mult`, and final XYZ coordinates.
3. Build the ORCA input as:

   ```
   <method_line>
   * xyz <charge> <mult>
   <XYZ block>
   *
   ```

4. Run with: `orca input.inp > output.out`

Example template inputs are provided in
[`orca_input_templates/`](orca_input_templates/) for the Set D V2
veratrole rotamer scan and the Cu2I2 rhombic reference monomer at
both DefGrid3 and Grid5 grid settings.

## Reconstructing a Set D V2 calculation

The Set D V2 (veratrole rotamer scan) starting geometries are in
`audit_final_setD_alt_diag/setD_alt_v2_analysis.json` under the
`initial_xyz` field for each species. Use the method_line and
charge/mult specifications described in the same JSON.

## Reproducing a high-grid sensitivity check

The grid-sensitivity test infrastructure is in
`audit_final_setD_alt_diag/grid_test/inputs/`. Three reference
monomer single points (gas + SMD) at Grid5/FinalGrid6 converged to
sub-0.05 mEh of DefGrid3 values; complex high-grid SP is queued for
re-execution on a roomier compute node.

## Verifying file integrity

All raw `.out` files have SHA-256 hashes recorded in
`audit_final/RAW_FILE_INDEX.csv`. To verify a downloaded copy:

```
sha256sum <filename>.out
```

and compare with the recorded value.

## Notes on missing files

The `cu2i2_veratrole_pi_opt_freq.out` file was temporarily inaccessible
during the audit pipeline and was subsequently recovered. The current
canonical SHA-256 is recorded in `BINDING_SURVIVAL_TABLE.csv` `notes`
column. If the file is missing from the repository at clone time,
the input can still be reconstructed and re-executed using the
procedure above.
