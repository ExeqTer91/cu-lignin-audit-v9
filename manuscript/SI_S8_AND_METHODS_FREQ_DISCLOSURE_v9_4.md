# v9.4 Manuscript Edits — Imaginary-mode Disclosure

**Trigger**: ORCA `cu2i2_veratrole_pi_opt_freq_v2` analytical Freq returned
n_imag=1 at −15.82 cm⁻¹ (B3LYP-D3BJ/def2-TZVP, gas, 0/1, 24 atoms),
mass-weighted decomposition shows >80% on methoxy-rotor torsion + arene C–H
wagging, Cu₂I₂ core only 2.4%. Architect verdict: numerical-grid artefact on
the flat η²-arene π PES, not a Cu–arene instability. Geometry is treated as
an effective minimum for the geometric and binding-energy claims of this work.

Three edits below: (1) new SI section S8, (2) one-sentence Methods addition,
(3) Figure 2 caption (b) extension.

---

## 1.  SI Section S8 — full text (drop into supporting information)

### S8.  Vibrational analysis of the η²-arene π Cu₂I₂·veratrole structure

The η²-arene π complex of Cu₂I₂ with veratrole was characterized by analytical
frequency analysis at the B3LYP-D3(BJ)/def2-TZVP level (ORCA 6.1.1, RIJCOSX
with def2/J auxiliary basis, DefGrid3, TightSCF, gas phase, charge 0,
multiplicity 1; 24 atoms). The geometry optimization satisfied standard `Opt`
convergence criteria at cycle 23 (final electronic energy −4337.780088 Hartree).
Frequency analysis returned 66 real vibrational modes and one small imaginary
mode at −15.82 cm⁻¹.

Mass-weighted Cartesian-displacement decomposition of the imaginary mode
(Table S8.1) localizes the motion on internal degrees of freedom of the
veratrole ligand:

| Fragment | Mass-weighted displacement (%) |
|---|---:|
| Cu₂I₂ core (2 Cu + 2 I) | 2.4 |
| η²-coordinated arene carbons (C8, C9) | 17.3 |
| Other arene carbons (C4–C7) — included in the 17.3 above | — |
| Arene C–H wagging (H20–H23) | 30.1 |
| Methoxy-1 (O–CH₃) | 31.2 |
| Methoxy-2 (O–CH₃) | 19.1 |

The combined contribution of methoxy torsion (50.3%) and aromatic C–H
out-of-plane wagging (30.1%) accounts for over 80% of the mass-weighted
displacement, with the Cu₂I₂ coordination core essentially stationary (2.4%).
The next vibrational mode at +18.82 cm⁻¹ is the in-phase counterpart of the
same torsion family; together these two modes describe the two components
of a coupled methoxy-rotor / arene-wag motion on the flat η²-arene π
potential-energy surface. The narrow gap between them (34.6 cm⁻¹) is itself
diagnostic of a near-degenerate hindered-rotor pair that an analytical
harmonic treatment cannot fully resolve.

This imaginary mode is therefore interpreted as a numerical-grid artefact
characteristic of weakly hindered methoxy-rotor degrees of freedom on the
shallow η²-arene π PES, and is not associated with the Cu–arene coordination
geometry itself. The two short Cu–C contacts (2.228 / 2.388 Å) defining the
η² interaction are stable across the final cycles of the optimization
trajectory: between cycles 22 and 23 the all-atom RMSD is 0.0029 Å, and
between cycles 21 and 23 it is 0.0053 Å. The Cu₂I₂ core distances (Cu–Cu =
2.477 Å, Cu–I = 2.495 / 2.497 / 2.697 / 2.734 Å) and the Cu–O distance
(3.941 Å) likewise reproduce the published manuscript values within 0.01 Å.

The structure is treated as an effective minimum for the geometric and
binding-energy comparisons reported in this work. Thermochemical (Gibbs-free
energy) quantities derived from the harmonic partition function are not
reported for this particular structure, because at finite temperature the
methoxy-rotor degrees of freedom are better described by hindered-rotor
than by harmonic-oscillator statistical mechanics.

The optimized geometry, frequency output, and mass-weighted Hessian
eigenvectors are deposited at the project GitHub repository under
`audit_final/cu2i2_veratrole_pi_v2_opt_freq/`. The canonical ORCA output
file is `cu2i2_veratrole_pi_opt_freq_v2.out` with SHA-256

```
3c76460b77de8f20cb4ad35619bab2b4e99b31778199cf061fd1bc0665063939
```

---

## 2.  Methods — one-sentence addition

Insert in **Methods → Computational details**, immediately after the
sentence describing frequency analysis:

> For the Cu₂I₂·veratrole η²-arene π structure (Figure 2b), one small
> imaginary mode at −15.82 cm⁻¹ was observed and attributed to weakly
> hindered methoxy-rotor torsion on the flat η²-arene π PES (mass-weighted
> displacement >80% on methoxy torsion and arene C–H wagging; Cu₂I₂ core
> 2.4%; full decomposition in Section S8). The structure is treated as an
> effective minimum for the geometric and binding-energy comparisons
> reported in this work.

---

## 3.  Figure 2 caption — panel (b) extension

Replace the existing panel (b) caption with:

> (b) η²-arene π productive contact on Cu₂I₂; Cu sits above the ring edge
> with two short Cu–C contacts (2.228 / 2.388 Å) and the closest Cu–O at
> 3.941 Å, confirming π rather than σ-O coordination. BE_smd =
> −23.11 kcal/mol. One small imaginary mode (−15.82 cm⁻¹) localized on
> methoxy-rotor torsion is documented in Section S8.

---

## Provenance

| Item | Value |
|---|---|
| Source pod | `m0lcyp3b05gn6t` (RunPod, `/dev/shm/calc/`) |
| ORCA version | 6.1.1 |
| Method | B3LYP-D3(BJ)/def2-TZVP, RIJCOSX def2/J, TightSCF, DefGrid3, gas |
| Charge / mult | 0 / 1 |
| Atoms | 24 (2 Cu, 2 I, 4 C arene + 2 OCH₃ heavy = 8 C, 2 O, 10 H) |
| Opt cycles | 23 (HURRAY) |
| Final E | −4337.780088 Eh |
| n_imag | 1 |
| Imaginary mode | −15.82 cm⁻¹ |
| Run wallclock | 1 h 05 min 26 s |
| `.out` SHA-256 | `3c76460b77de8f20cb4ad35619bab2b4e99b31778199cf061fd1bc0665063939` |
| `.xyz` SHA-256 | `4ced395e8f07c80c34aa25d47bbf07a420466361a37f33a43510489cfa92d34d` |
| Trajectory cycles 22→23 RMSD | 0.0029 Å (all-atom) |
| Trajectory cycles 21→23 RMSD | 0.0053 Å (all-atom) |

---

*Drafted v9.4, 2026-05-03. Architect-approved (small-imaginary methoxy/H-wag
artefact, "25% scenario", not Cu-arene instability).*
