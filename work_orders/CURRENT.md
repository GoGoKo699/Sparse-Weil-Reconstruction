# Current scope: release readiness and reader preparation

Read README.md, STATUS.md, PROVENANCE.md, and
`research/consolidation_v1/AUDIT.md`, and
`research/finite_field_application_v1/COROLLARIES.md`.
The reader entry point is `docs/READING_GUIDE.md`: Galbraith is the primary
teaching anchor and Chidambaram–Keller is the secondary research anchor.
The source-supported background starts at
`research/manuscript_background_v1/README.md`.
Manuscript preparation remains on hold.

## Current checkpoint

[STATUS](../STATUS.md) is the current scientific index; the
[release check](../docs/RELEASE_CHECK.md) records the latest audit.
The two reconstruction guarantees have written proofs, internal mathematical
and implementation audits, finite-field corollaries, source-supported
background, and exact executable evidence. Retain their regimes and limitations
when describing either result.

The [method boundary](../research/consolidation_v1/METHOD_BOUNDARY.md) closes
the previous bounded extension question for the present whole-algebra,
single-radius norm argument. It is neither a reconstruction lower bound nor
a failure result for the actual iteration.

## Reader and discovery guidance

Use the author's online Galbraith numbering and the pinned Chidambaram–Keller
v2 PDF. Keep the textbook and research reading roles clear. The comparison
should explain the mathematical progression in neutral terms. New exposition
must agree with the canonical promises, signs, and precision bounds.
Use GitHub math fences for display equations and protected inline formulas in
teaching and research notes. Keep comparison tables
compact and introduce the two reconstruction regimes in prose with their exact
conditions. Formatting repairs must preserve mathematical content; retain the
17 manifest-pinned baseline files byte for byte and keep dated verification
receipts unchanged.

Keep [llms.txt](../llms.txt) aligned with canonical proofs and current file
paths. It supplies retrieval context, not an indexing guarantee or additional
theorem. [CITATION.cff](../CITATION.cff) describes the repository; do not invent
a publication, DOI, version, or release date.

## Next work

Lead with the quadratic-threshold first-g theorem and retain the all-field
result as the complementary regime. Manuscript drafting waits for the user's
instruction.

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
