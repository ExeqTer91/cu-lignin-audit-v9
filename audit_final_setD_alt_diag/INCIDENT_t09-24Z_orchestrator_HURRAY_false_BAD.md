# INCIDENT — Orchestrator v2 false-negative HURRAY check

**Time of misfire:** 2026-04-30T09:24:30Z (post detection on next polling pass)  
**Pod:** rbqua6cf61ki73 @ 154.54.102.26:10598  
**Affected runs:** all 4 V2 opt+freq jobs of Task #29  
**Severity:** Medium — no scientific data was lost or corrupted; the bug only delayed the SMD-SP launch by ~20 min and required manual intervention.

## Symptom

After the 4 V2 opt+freq jobs converged (last one finishing at `09:23:48Z`),
the orchestrator polling loop classified all four as `DONE_BAD` despite the
ORCA `.out` files containing a normal `ORCA TERMINATED NORMALLY`, a final
energy, a vibrational block, and `n_imag = 0`.

The downstream auto-launch of the 4 SMD single-points was therefore **suppressed**.
The user authorized a manual sequential SMD-SP launch at `09:43:19Z`, which
completed all 4 jobs cleanly by `09:49:21Z`.

## Root cause

The orchestrator's "is the geometry converged?" gate was implemented as

```bash
grep -q "HURRAY THE OPTIMIZATION HAS CONVERGED" "$out"
```

i.e. a single-line literal match.  ORCA 6.1.1, however, emits the HURRAY
banner across **two lines**:

```
                        *****************************************************
                        *               *****************                   *
                        *               *  HURRAY      *                   *
                        *               *  THE OPTIMIZATION HAS CONVERGED  *
                        *               *****************                   *
                        *****************************************************
```

so the literal phrase `HURRAY THE OPTIMIZATION HAS CONVERGED` never appears
on a single line, and `grep -q` always returns 1.  The orchestrator therefore
forced every converged run into the `DONE_BAD` bucket.

A simple `grep -q "HURRAY"` (or a 2-line `grep -A1 "HURRAY"` /
`pcregrep -M`) would have classified them correctly.

## Verified-correct convergence evidence (all 4 species)

```
$ for f in /root/orca_calc_setD_alt/logs/*restart_v2_opt_freq.out; do
    echo "=== $(basename $f) ==="
    grep -c "HURRAY" "$f"          # banner line count (>=1 means yes)
    grep -c "ORCA TERMINATED NORMALLY" "$f"
    grep "FINAL SINGLE POINT ENERGY" "$f" | tail -1
    awk '/VIBRATIONAL FREQUENCIES/,/NORMAL MODES/' "$f" \
      | awk '$2+0 < -10 {n++} END {print "n_imag =", n+0}'
  done
```

| job_id                                        | HURRAY hits | TERM_NORM | E_final (Eh)      | n_imag |
|----------------------------------------------:|:-----------:|:---------:|------------------:|-------:|
| cu2i2_veratrole_methoxyO_startA               |     2       |    1      | -4337.78499105    |   0    |
| cu2i2_veratrole_methoxyO_startB               |     2       |    1      | -4337.69751323    |   0    |
| cui2_veratrole_methoxyO_anion_startA          |     2       |    1      | -2697.26264594    |   0    |
| cui2_veratrole_methoxyO_anion_startB          |     2       |    1      | -2697.25321321    |   0    |

All 4 satisfy the strict 5-gate `TERM_NORMAL ∧ HURRAY ∧ FINAL_E ∧ VIB_BLOCK ∧ n_imag=0`.

## Fix (for any future use of this orchestrator)

Replace the convergence gate with one of:

```bash
# A. simple substring (matches the boxed banner)
grep -q "HURRAY" "$out"

# B. two-line aware (more specific)
grep -B0 -A1 "HURRAY" "$out" | grep -q "OPTIMIZATION HAS CONVERGED"

# C. perl-regex multiline
pcregrep -M "HURRAY[^\\n]*\\n[^\\n]*OPTIMIZATION HAS CONVERGED" "$out"
```

Recommended: **option B**, because it both confirms the banner header and
the trailing "OPTIMIZATION HAS CONVERGED" sentinel in one pipeline.

## Remediation timeline

| t (UTC)            | event |
|---|---|
| 09:23:48Z | last v2 opt+freq finished |
| ~09:24:30Z | orchestrator marked all 4 as `DONE_BAD` (false-negative) |
| ~09:35Z   | manual inspection identified the 2-line HURRAY banner mismatch |
| 09:43:19Z | manual SMD-SP runner started (`/tmp/setD_alt_smd_v2_runner.sh`) |
| 09:49:21Z | all 4 SMD-SPs finished `4/4 OK` |

**Net delay introduced: ~19 minutes.  No re-computation required.**
