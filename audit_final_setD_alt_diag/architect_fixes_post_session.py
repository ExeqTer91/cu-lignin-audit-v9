#!/usr/bin/env python3
"""Architect-requested pre-commit reconciliations on the propagated tables.

Two fixes:
  1) GRID_SENSITIVITY_STATUS.csv -- update the cu2i2_veratrole_methoxyO_startA
     row note to reflect this session's actual blocker (RunPod pod-resume SSH
     key-injection failure) rather than the prior "deferred per user
     instruction" wording. The other three V2-species rows are unchanged
     because they were never re-attempted in this session.

  2) BELEGEN_EVIDENCE_MATRIX.csv -- normalize the support_status of E3.7 and
     E3.8 from the bespoke "CONFIRMS_E3.4_AT_VERATROLE" string to the
     canonical "PARTIALLY_SUPPORTED" so that the claim-counting rule in
     CLAIM_SUPPORT_STATUS / MECHANISM_VERDICT_TABLE is mechanically
     reproducible. The original semantic is preserved by appending
     "CONFIRMS_E3.4_AT_VERATROLE" to the row's notes column.

Plus: tighten the counting_rule_note in CLAIM_SUPPORT_STATUS (claim 3) and
MECHANISM_VERDICT_TABLE (M3) to make the canonical-status mapping explicit.
"""
import csv
import shutil
import sys
from pathlib import Path

ROOT = Path("audit_final")
GRID = ROOT / "GRID_SENSITIVITY_STATUS.csv"
BELEGEN = ROOT / "BELEGEN_EVIDENCE_MATRIX.csv"
CLAIM = ROOT / "CLAIM_SUPPORT_STATUS.csv"
VERDICT = ROOT / "MECHANISM_VERDICT_TABLE.csv"


def fix_grid_sensitivity():
    rows = list(csv.reader(GRID.open()))
    header = rows[0]
    note_col = header.index("note")
    species_col = header.index("species")
    new_note = (
        "Phase 2 high-grid (Grid5/FinalGrid6 per Task #29 reviewer) was "
        "ATTEMPTED 2026-04-30T~11:00Z this session but BLOCKED by RunPod "
        "pod-resume SSH key-injection failure (two podResume cycles, both "
        "rejected the account public key on the new TCP endpoints; pod "
        "stopped to avoid GPU charges; see pod_info.json -> "
        "status_2026-04-30_resume_attempt for diagnostics). DefGrid3 "
        "energies remain accepted as the final-table values; high-grid "
        "validation queued for the next session after manual SSH key "
        "re-injection through the RunPod web console."
    )
    fixed = 0
    for r in rows[1:]:
        if r[species_col] == "cu2i2_veratrole_methoxyO_startA":
            r[note_col] = new_note
            fixed += 1
    if fixed != 1:
        sys.exit(f"GRID fix: expected 1 row update, got {fixed}")
    with GRID.open("w", newline="") as f:
        csv.writer(f).writerows(rows)
    print(f"[OK] GRID_SENSITIVITY_STATUS.csv: updated {fixed} row(s)")


def fix_belegen_e37_e38():
    rows = list(csv.reader(BELEGEN.open()))
    header = rows[0]
    eid_col = header.index("evidence_id")
    sup_col = header.index("support_status")
    notes_col = header.index("notes")
    fixed = 0
    for r in rows[1:]:
        if r[eid_col] in ("E3.7", "E3.8") and r[sup_col].startswith("CONFIRMS_E3.4"):
            old = r[sup_col]
            r[sup_col] = "PARTIALLY_SUPPORTED"
            existing = r[notes_col].rstrip(". ")
            r[notes_col] = (
                (existing + ". " if existing else "")
                + f"Original BELEGEN status (preserved): {old}. "
                + "Re-classified to PARTIALLY_SUPPORTED for the revised "
                + "state-dependent claim 3 verdict, since this evidence "
                + "supports the 'nonproductive on iodide-saturated [CuI2]-' "
                + "half of the dual-state finding (Task #29 V2; architect "
                + "review 2026-04-30 normalization)."
            )
            fixed += 1
    if fixed != 2:
        sys.exit(f"BELEGEN fix: expected 2 row updates, got {fixed}")
    with BELEGEN.open("w", newline="") as f:
        csv.writer(f).writerows(rows)
    print(f"[OK] BELEGEN_EVIDENCE_MATRIX.csv: re-classified {fixed} row(s)")


def fix_counting_rule_notes():
    """Make the canonical-status mapping explicit on claim 3 / M3 rows."""
    # CLAIM_SUPPORT_STATUS has no counting_rule column; it lives on
    # MECHANISM_VERDICT_TABLE. We tighten the verdict's counting_rule_note.
    rows = list(csv.reader(VERDICT.open()))
    header = rows[0]
    mid_col = header.index("mechanism_id")
    rule_col = header.index("counting_rule_note")
    appendix = (
        " Canonical statuses for mechanical counting: SUPPORTED, "
        "PARTIALLY_SUPPORTED, CONTRADICTED, NOT_TESTED, "
        "INVALIDATED_BY_GEOMETRY, INVALIDATED_BY_ENERGETICS, "
        "NEEDS_EXPERIMENTAL. Bespoke labels (e.g. 'CONFIRMS_E*.x_AT_*') "
        "are normalized to the closest canonical status before counting; "
        "the original label is preserved in the BELEGEN notes column."
    )
    fixed = 0
    for r in rows[1:]:
        if r[mid_col] in ("M3", "M4"):
            note = r[rule_col]
            if "Canonical statuses for mechanical counting" not in note:
                r[rule_col] = note.rstrip() + appendix
                fixed += 1
    if fixed != 2:
        sys.exit(f"VERDICT counting-rule fix: expected 2 row updates, got {fixed}")
    with VERDICT.open("w", newline="") as f:
        csv.writer(f).writerows(rows)
    print(f"[OK] MECHANISM_VERDICT_TABLE.csv: extended counting_rule_note on {fixed} row(s)")


def verify_claim3_counts():
    """Sanity: re-count claim 3 evidence from the now-normalized BELEGEN."""
    rows = list(csv.DictReader(BELEGEN.open()))
    c3 = [r for r in rows if r["claim_id"] == "3"]
    from collections import Counter
    cnt = Counter(r["support_status"] for r in c3)
    print(f"[VERIFY] claim 3 BELEGEN status counts: {dict(cnt)} (n={len(c3)})")
    expect = {"SUPPORTED": 2, "PARTIALLY_SUPPORTED": 4, "INVALIDATED_BY_ENERGETICS": 2}
    for k, v in expect.items():
        if cnt.get(k, 0) != v:
            sys.exit(f"[FAIL] claim 3 count mismatch: {k} expected {v}, got {cnt.get(k, 0)}")
    # Cross-check CLAIM_SUPPORT_STATUS row
    claim_rows = list(csv.DictReader(CLAIM.open()))
    c3row = next(r for r in claim_rows if r["claim_id"] == "3")
    assert c3row["n_supported"] == "2"
    assert c3row["n_partially_supported"] == "4"
    assert c3row["n_invalidated_energetics"] == "2"
    assert c3row["n_evidence_rows"] == "8"
    print("[VERIFY] CLAIM_SUPPORT_STATUS.csv claim 3 counts now mechanically reproducible from BELEGEN.")


if __name__ == "__main__":
    fix_grid_sensitivity()
    fix_belegen_e37_e38()
    fix_counting_rule_notes()
    verify_claim3_counts()
    print("\nDONE.")
