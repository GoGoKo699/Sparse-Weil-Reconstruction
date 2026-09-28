# Current scope: reconstruction and reader preparation

Read README.md, STATUS.md, PROVENANCE.md, and
`research/consolidation_v1/AUDIT.md`, and
`research/finite_field_application_v1/COROLLARIES.md`.
The reader entry point is `docs/READING_GUIDE.md`: Galbraith is the primary
teaching anchor and Chidambaram–Keller is the secondary research anchor.
The source-supported background starts at
`research/manuscript_background_v1/README.md`.
Manuscript preparation remains on hold.

## Scientific checkpoint

The first-g theorem supplies a quadratic sufficient field-size threshold,
`q >= 65536*g^2`, with a finite rational decoder and polynomial bit time.
The preserved selected-data theorem works over every field for `g >= 32`.
The fresh internal mathematical and implementation audits found no substantive
gap. All three pinned research reports reproduce.

The focused source comparison found no inspected result subsuming the quadratic
guarantee. It includes the closest predecessor's polynomial-time algorithm and
its suggested superpolynomial threshold refinement. Search and access limits
are recorded; this is not universal priority certification.

The previous bounded extension question is closed by
`research/consolidation_v1/METHOD_BOUNDARY.md`: the present whole-algebra,
single-radius small-norm proof cannot reach a subquadratic field-size regime.
The note proves neither a necessary threshold for reconstruction nor failure
of the actual iteration. No consequential extension was obtained in this pass.

The finite-field application pass is also complete. It verifies both theorem
hypotheses for general abelian varieties, states the Jacobian-to-curve-zeta
corollary, and separates compact Frobenius reconstruction from exponentially
large expanded abelian-variety zeta output. Ordinary curve point counts remain
a distinct input problem with the standard Newton reconstruction. These are
application clarifications, not another novelty claim. No decoder, pinned
report, or threshold changed.

The manuscript background pass is complete: foundations, matched Weil
reconstruction theorems, generic cyclic-resultant results, algorithmic methods,
and claim-level citations are integrated with a reusable bibliography. The
source record distinguishes primary-text inspection from metadata-only
historical references. The remaining historical access gaps do not leave a
used mathematical dependency unsupported. No additional matched competitor
was found in the bounded search. This does not assert exhaustive priority.

## Teaching checkpoint

The repository now has a Galbraith-led reading path with a notation map,
worked algebraic examples, self-checks, and a bridge to the two proofs.
`docs/COMPARISON.md` explains the shared first-g problem, the change from
successive power-sum recovery to simultaneous coefficient correction, and
the resulting quadratic sufficient field-size bound. It credits the
predecessor's polynomial bit complexity and contraction estimates.

Use the author's online Galbraith numbering and the pinned Chidambaram–Keller
v2 PDF. Keep the textbook and research reading roles clear. The comparison
should explain the mathematical progression in neutral terms. New exposition
must agree with the canonical promises, signs, and precision bounds.

## Next work

The scientific package is complete within its stated scope at the level of
written proofs, internal audit, explicit application, scientific background,
and executable evidence. Consolidation should lead with the quadratic-threshold
theorem and retain the all-field result as the complementary regime. The
teaching path and background package now supply the reader preparation,
citations, and attribution for future writing. Manuscript drafting waits for
the user's instruction.

Reopen scientific work when there is a concrete correctness concern, a
competing primary theorem, or a clearly consequential extension. Do not
automatically restart the same audit, optimize the constant, or launch a
small-parameter census. All-field first-g reconstruction, optimal query counts,
and other recovery norms are optional future projects, not unfinished gates
for the present result.

External peer review, universal publication priority, query optimality, and
Jacobian realization of the controls remain unestablished. These limits must
stay separate from the completed internal checks.

## Preserve and reproduce

Keep the 17 files in `provenance/import-manifest.json` unchanged. Retain the
first-g theorem and experiment as a versioned checkpoint. New scientific
changes belong in a successor directory. Never change reference outputs to
make a modified decoder pass. Run `python3 verify.py` before and after changes
affecting proofs, decoder, or verification, and report what actually ran.

Keep the true-count promise, selected versus consecutive indices, q-reciprocity,
integrality, inverse-root modulus, and genus/field thresholds visible. Preserve
the distinctions between reconstruction, acquisition, authentication, and
curve realization. No quantum implementation, external messages, paid
computation, manuscript drafting, release tags, or unrelated changes are part
of this work order.
