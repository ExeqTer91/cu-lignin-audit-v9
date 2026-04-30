"""
Update BELEGEN_EVIDENCE_MATRIX row 19 (E4.3 cu2i2_veratrole_pi) with explicit
DATA_LOST_POD_WIPE annotation.

Original raw .out (`/workspace/results_setD/cu2i2_veratrole_pi_opt_freq.out`,
which was a /root symlink) became unrecoverable when the pod was stopped+started
2026-04-30T11:02Z. Energies and binding class status are preserved through the
prior extraction in EXPERIMENT_JOB_INDEX.csv with sha256 ef4266f6...ede18a.
Verdict (SUPPORTED) is unchanged because the energies + n_imag are pedigreed.
"""
import csv, shutil, os, time
P = 'audit_final/BELEGEN_EVIDENCE_MATRIX.csv'
ts = time.strftime('%Y%m%dT%H%M%SZ', time.gmtime())
bak = f'audit_final/BELEGEN_EVIDENCE_MATRIX.csv.bak_dataloss_{ts}'
shutil.copy2(P, bak)
print(f"backup: {bak}")

rows = list(csv.reader(open(P)))
hdr = rows[0]
i_geom = hdr.index('final_geometry')
i_dist = hdr.index('contact_distances_A')
i_notes = hdr.index('notes')

# Row 19 in 1-indexed = index 18 in 0-indexed
target_idx = None
for i, r in enumerate(rows):
    if i == 0: continue
    if r[hdr.index('evidence_id')] == 'E4.3' and 'cu2i2_veratrole_pi' in r[hdr.index('computation_id')]:
        target_idx = i
        break
assert target_idx is not None, "could not find E4.3 row"
r = rows[target_idx]
print(f"updating row {target_idx} (1-indexed line {target_idx+1})")
print(f"  evidence_id={r[hdr.index('evidence_id')]}, computation={r[hdr.index('computation_id')]}")

r[i_geom] = ("DATA_LOST_POD_WIPE 2026-04-30T11:02Z: η^n-arene mode (qualitative); raw .out file unrecoverable from pod after stop+start "
             "wiped /root volume. Geometry-level re-extraction would require re-running cu2i2_veratrole_pi opt+freq from scratch (~30-60 min wall A100).")
r[i_dist] = ("DATA_LOST_POD_WIPE: contact distances were never extracted into local audit JSON before .out was lost. "
             "Energies, n_imag, and binding class are pedigreed via EXPERIMENT_JOB_INDEX.csv + sha256 ef4266f6...ede18a.")
r[i_notes] = (r[i_notes].rstrip().rstrip('"') if r[i_notes].endswith('"') else r[i_notes].rstrip()) + \
    " | POD_WIPE_DATA_LOSS 2026-04-30T11:02Z: original raw .out file at /workspace/results_setD/cu2i2_veratrole_pi_opt_freq.out (a /root symlink) became unrecoverable when the pod was stopped+started; container rootfs was wiped while /workspace/orca_6_1_1 (17GB) and /workspace/audit_final/ (25MB) survived. Energies (BE_gas -22.98, BE_smd -23.11), n_imag=0, and SUPPORTED verdict remain valid because they were extracted into EXPERIMENT_JOB_INDEX.csv prior to the wipe with sha256-recorded provenance. Geometry-level re-extraction (Cu-centroid distance, Cu-C top-3, lowest-frequency value, etc.) is not currently recoverable; would require re-running the opt+freq from a seed."
rows[target_idx] = r

with open(P, 'w', newline='') as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    w.writerows(rows)
print(f"wrote {P}")
print()
print("updated final_geometry:", r[i_geom][:100], "...")
print("updated contact_distances_A:", r[i_dist][:100], "...")
print("notes length:", len(r[i_notes]), "chars")
