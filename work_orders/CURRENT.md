# Next task: assess the remaining field/query trade-off

Read README.md, STATUS.md, PROVENANCE.md, the contribution assessment, and
`research/first_g_reconstruction_v1/THEOREM.md`. Manuscript preparation remains
on hold. No publication target is recorded in this repository.

## Completed scientific checkpoint

The predecessor comparison is concrete. Chidambaram–Keller is
arXiv:2606.28989v2, with first-g reconstruction and polynomial bit time under a
large explicit field-size threshold. Its existence, current version, and
complexity statement are resolved. Bézivin's generic first-(d+1) result and
Hillar's erratum are included. Source-search limitations remain explicit.

The companion theorem now proves first-g supplied-count reconstruction for
q >= 65536*g^2, g >= 1, with a contraction and an explicit rational finite
algorithm. The internal audit checked normalization, repeated divisors, the
invariant domain, finite-series errors, final integer rounding, and polynomial
intermediate sizes. Five exact controls and independent determinant routes pass.
The original all-field sparse theorem for g >= 32 is retained unchanged.

## Focused question

What can be established about the gap between the all-field sparse schedule
and first-g recovery below the quadratic sufficient threshold?

First distinguish three claims: failure of this sufficient norm estimate,
failure of this particular iteration, and nonuniqueness of the supplied data.
They are not equivalent. Do not imply that q >= 65536*g^2 is necessary.

The next bounded deliverable is an analytic obstruction-or-extension note.
Inspect whether a change of norm/domain gives a qualitative extension of the
field-size regime, or whether an explicit family demonstrates a limitation of
the recovery map or the data themselves. A limitation of the map must not be
reported as a limitation of all decoders. Explain whether the additional result
would materially strengthen the current two-theorem package before implementing
another experiment. Merely reducing the constant 65536 is not the objective.

If no consequential extension or obstruction follows from this focused pass,
record that outcome and assess the current mathematical scope for consolidation.
Do not turn this into an open-ended search or a broad small-parameter census.
Publication priority remains a qualified literature assessment, not a guarantee
that every paper, thesis, implementation, or unpublished argument was found.

## Preserve and reproduce

Keep all 17 files in `provenance/import-manifest.json` unchanged. Keep the
first-g proof and experiment as a versioned checkpoint as well. New scientific
changes belong in a successor directory. Never overwrite expected output to
make a modified decoder pass. Run `python3 verify.py` before and after changes
affecting proofs, decoder, or verification, and report what actually ran.

Keep the precise input promises, selected versus consecutive indices, and
count acquisition/authentication boundaries visible. Controls are Weil
polynomials, not asserted Jacobians. No quantum implementation, external
messages, paid computation, manuscript drafting, or unrelated repository
changes are part of this work order.
