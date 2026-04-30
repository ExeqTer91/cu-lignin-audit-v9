# Set D ALT — Restart V2 launched 2026-04-30T02:39:56Z

## Status
All 4 opt+freq jobs MaxIter-hit on first pass (cu2i2 72/72; cui2 69/69).
v1 outputs quarantined (METADIR /workspace/audit_final/QUARANTINE_t02-25Z/).
v1 SMD-SP outputs quarantined as INVALID_PARTIAL (computed on UNCONVERGED geoms).
v2 restart launched 2026-04-30T02:37:16Z on RunPod (orca-dft-v9-migration,
154.54.102.26:10598).

## Restart spec (per user + reviewer)
```
! B3LYP D3BJ def2-TZVP RIJCOSX def2/J TightSCF TightOpt DefGrid3 Opt Freq
%pal nprocs 24 end
%maxcore 5000
%geom
  MaxIter 200
  Trust 0.1          ← reviewer addition (helps step convergence)
end
%scf MaxIter 200 end
%method
  Grid 6             ← ORCA-6 equivalent of legacy "Grid5"
  FinalGrid 7        ← ORCA-6 equivalent of legacy "FinalGrid6"
end
```
Note: ORCA 6.1.1 removed the legacy `Grid5/FinalGrid6` simple-input keywords
(they cause "UNRECOGNIZED OR DUPLICATED KEYWORD" exit-4). The %method-block
syntax is the only valid ORCA-6 path and produces the equivalent angular grids
(Lebedev 590 / 770).

## Files (pod)
- prep+runner script:   /workspace/restart_setD_alt_v2.py
- orchestrator:         /tmp/setD_alt_orchestrator_v2.sh (nohup'd, setsid, NO TIMEOUT)
- live log:             /tmp/setD_alt_orchestrator_v2.log
- DONE markers:         /tmp/setD_alt_RUNNER_V2_DONE_OK | _BAD
- inputs:               /root/orca_calc_setD_alt/calc/*_restart_v2_opt_freq.inp
- outputs:              /root/orca_calc_setD_alt/logs/*_restart_v2_opt_freq.out
- v1 archive:           /root/orca_calc_setD_alt/calc/ARCHIVE_v1_t02-25Z/
- failed-attempt:       /root/orca_calc_setD_alt/calc/FAILED_RESTART_V2_GRID5_t02-34Z/

## Strict validation gate (next-session check)
Per reviewer: a job is VALID_OPT_FREQ only if ALL FIVE are true:
1. `ORCA TERMINATED NORMALLY` present
2. `HURRAY THE OPTIMIZATION HAS CONVERGED` present (or equivalent ncyc<MaxIter+opconv=1)
3. final `FINAL SINGLE POINT ENERGY` parseable
4. `VIBRATIONAL FREQUENCIES` block present (and `NORMAL MODES` / ZPE)
5. imaginary-frequency count parseable

If ANY are false → mark NOT_VALIDATED, do NOT compute BE, do NOT launch SMD,
do NOT add row to final BE CSV (only to incomplete_jobs table).

The orchestrator already enforces 1+2+4 before auto-launching SMD; on resume,
re-verify all five and parse n_imag explicitly.

## Time budget
DefGrid3→Grid6/FinalGrid7 ≈ 1.5–2× slower per gradient call (vs v1's 7-8 min).
Cycle estimate: 12–15 min/cycle. Convergence cycles needed (from v1 final state):
- cu2i2_startA  ≈ 5–20  cycles  (gradient already 5e-5; bouncing in step)
- cu2i2_startB  ≈ 50–100 cycles (still moving substantially)
- cui2_startA   ≈ 50–150 cycles (0.125 Å steps; possibly mode-switching)
- cui2_startB   ≈ 20–40 cycles
Wall-clock estimate (parallel): 12–24 h depending on cui2_startA behavior.

## Resume protocol (NEXT SESSION)
1. SSH key restore: `printf 'L%s' "$RUNPOD_SSH_KEY_B64" | tr -d '\n\r ' | base64 -d > ~/.ssh/runpod_key && chmod 600 ~/.ssh/runpod_key`
   (note the `L` prefix — env var has 1 char stripped from the leading b64)
2. Check `/tmp/setD_alt_RUNNER_V2_DONE_{OK,BAD}` markers
3. If DONE_OK: re-run strict 5-gate verification per .out
4. Build the reviewer's exact-format final table:
   ```
   job_id | restart_id | opt_converged | cycles | final_energy | freq_done |
   n_imag | lowest_freq | smd_done | smd_energy | final_mode | binding_class |
   valid_for_final_csv
   ```
   Classification per Task #29 user rules:
   - METASTABLE_CONTACT: contact survives geometrically but BE > 0
   - NON_BINDING:        ligand detaches at convergence
   - SWITCHABLE_BINDING: mode changed during opt but bound through different contact
5. NO narrative, NO manuscript text — just the table.

## Live status snapshot at 2026-04-30T02:39:56Z
- 108 ORCA processes alive
- 4 .out files all growing (52–57 KB at +90s, past the 13 KB parse-stub size)
- Load avg 9.2; memory 106 GB used of 2003 GB
