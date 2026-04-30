# control_calculations/

This directory holds all raw ORCA `.out` files and parsed summaries for the
Tier A mode-isolation control calculations.

## Expected contents (populated after ORCA jobs complete)

| File pattern | Description |
|---|---|
| `benzene_opt_freq.out` | Free benzene Opt+Freq |
| `cu_benzene_pi_opt_freq.out` | Cu–benzene π-adduct Opt+Freq |
| `anisole_opt_freq.out` | Free anisole Opt+Freq |
| `cu_anisole_methoxyO_opt_freq.out` | Cu–anisole methoxy-O adduct |
| `cu_anisole_pi_opt_freq.out` | Cu–anisole π-adduct |
| `meta_methoxyphenol_opt_freq.out` | Free 3-methoxyphenol |
| `cu_meta_methoxyphenol_phenolicO_opt_freq.out` | Cu–3-MeOPhOH phenolicO adduct |
| `cu_meta_methoxyphenol_pi_opt_freq.out` | Cu–3-MeOPhOH π-adduct |
| `para_methoxyphenol_opt_freq.out` | Free 4-methoxyphenol |
| `cu_para_methoxyphenol_phenolicO_opt_freq.out` | Cu–4-MeOPhOH phenolicO adduct |
| `cu_para_methoxyphenol_pi_opt_freq.out` | Cu–4-MeOPhOH π-adduct |
| `catechol_opt_freq.out` | Free catechol |
| `cu_catechol_bidentate_opt_freq.out` | Cu–catechol bidentate adduct |
| `cu_catechol_pi_opt_freq.out` | Cu–catechol π-adduct |
| `cyclohexanol_opt_freq.out` | Free cyclohexanol |
| `cu_cyclohexanol_O_opt_freq.out` | Cu–cyclohexanol O-adduct |
| `*_smd_sp.out` | Corresponding SMD-water single-point files |
| `run_summary.json` | Metadata: date, nprocs, maxcore, Cu+ ref energy used |

## Optional jobs (run if compute budget allows)

| File pattern | Description |
|---|---|
| `o_cresol_opt_freq.out` | Free o-cresol |
| `cu_o_cresol_phenolicO_opt_freq.out` | Cu–o-cresol phenolicO adduct |
| `cu_o_cresol_pi_opt_freq.out` | Cu–o-cresol π-adduct |
| `veratrole_opt_freq.out` | Free veratrole |
| `cu_veratrole_bidentate_opt_freq.out` | Cu–veratrole bidentate adduct |
| `cu_veratrole_pi_opt_freq.out` | Cu–veratrole π-adduct |

## Submission instructions

Run from the compute cluster:

```bash
# Required jobs only
python run_tier_a_controls.py

# Required + optional jobs
python run_tier_a_controls.py --optional
```

Set environment variables before running:

```bash
export ORCA_PATH=/opt/orca/orca
export ORCA_NPROCS=20         # 16-24 recommended
export ORCA_MAXCORE=5000      # MB per process; 4000-6000
export TIER_A_WORKSPACE=/workspace/tier_a_controls
```

After jobs complete, `audit_final/CONTROL_BINDING_TABLE.csv` and
`audit_final/CONTROL_MODE_TABLE.csv` are auto-populated.
Then update `audit_final/CONTROL_INTERPRETATION.md` with numerical answers
to Q1–Q5.

## Mode-tracking policy

Every row in CONTROL_MODE_TABLE.csv records both `start_mode` (the intended
starting geometry) and `final_mode` (the converged coordination mode as
determined from the optimised Cartesian coordinates). A job that starts
as phenolicO-start but converges to π is reported as
`start_mode=phenolicO, final_mode=pi, mode_changed_from_start=True`.
This is a scientific result, not a failed job.
