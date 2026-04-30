# INCIDENT — false finalizer trigger at 21:20:08Z (29 Apr 2026)

## What happened
- The original `/tmp/setD_alt_finalizer.sh` was launched at 15:20:08Z with a hardcoded
  6-hour deadline: `deadline=$(( $(date +%s) + 6*3600 ))`.
- At 21:20:08Z (deadline) the wait loop exited even though all 4 ORCA optimizations
  were still actively running.
- The collator (`run_setD_alt.py --collate-only`) parsed PARTIAL outputs and wrote
  an INVALID `VERATROLE_OME_ALTERNATE_STARTS.csv` (1833 bytes, 4 rows).
- A `/tmp/setD_alt_FINALIZER_DONE` marker was touched.

## Verification that ORCA was still running at 21:25Z
- `pgrep -af orca` → 4 main ORCA procs (PIDs 6036-6039) + active mpirun children.
- `pgrep -af run_setD_alt` → 4 wrappers (PIDs 6031-6034), etime 6h39m.
- `.out` last-write ages: 12-78 s (active output).
- Cycle counts at 21:25:53Z snapshot: cu2i2_startA 50/72, cu2i2_startB 39/72,
  cui2_startA 52/69, cui2_startB 43/69. None converged, none at MaxIter.
- Tails of all 4 .out files show mid-cycle activity (mid-SCF, mid-gradient, mid-FSPE).

## Remediation
1. Removed `/tmp/setD_alt_FINALIZER_DONE`.
2. Quarantined invalid deliverables:
   - `VERATROLE_OME_ALTERNATE_STARTS.csv` → `INVALID_PARTIAL_VERATROLE_OME_ALTERNATE_STARTS_t21-20Z.csv`
   - `VERATROLE_OME_ALTERNATE_STARTS_NOTES.md` → `INVALID_PARTIAL_VERATROLE_OME_ALTERNATE_STARTS_NOTES_t21-20Z.md`
3. Archived false finalizer log: `setD_alt_finalizer.log` → `setD_alt_finalizer_FALSE_TRIGGER_t21-20Z.log`.
4. Deployed `/tmp/setD_alt_finalizer_v2.sh` (PID 117593) with NO timeout. It will:
   - Wait until all 4 wrappers truly exit.
   - Verify each .out has `ORCA TERMINATED NORMALLY` before invoking the collator.
   - Touch `/tmp/setD_alt_FINALIZER_V2_DONE` only on success.
5. Watcher `/tmp/setD_alt_watcher.sh` (PID 7832) is unaffected and continues to update
   `/tmp/setD_alt_progress.txt` every 60s.

## NO BE TABLE has been (or will be) reported from the partial outputs.
Per user directive: BE table requires opt + ORCA-normal-term + freq + imag-count + SMD complete.
