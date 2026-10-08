# Repository maintenance

This standalone project studies classical reconstruction of integral reciprocal
Weil polynomials from supplied exact cyclic resultants. Read README.md and the
relevant proof before editing. Galbraith is the primary teaching anchor;
Chidambaram–Keller is the secondary research anchor.

Present the results, methods, and reproducible examples directly. Keep progress
reports, development history, and lists of unrelated unperformed work out of
reader-facing documents. Use the purpose and contact notice in README.md.

Preserve the mathematical statements, source attribution, LICENSE, executable
code, fixtures, and reference reports. Substantive scientific changes belong in
a versioned successor. Documentation-only edits to manifest-pinned files require
updated documentation checksums with the original identities retained. Never
change reference outputs or weaken checks to obtain a pass.

Keep the exact input promises visible: true supplied counts, selected indices,
q-reciprocity, integrality, inverse-root modulus, and genus/field thresholds.
Distinguish Jacobian cardinalities from curve point counts and reconstruction
from authentication. Controls are supplied polynomials; finite tests support
implementations, while the proofs establish the uniform guarantees.

Use protected inline math and GitHub math fences. Retain code formatting for
executable syntax, identifiers, paths, and hashes. Keep llms.txt and local links
aligned with the canonical proofs and reading path. Verify primary sources
before strengthening novelty claims; preserve material source-access limits.

Run `python3 verify.py` after changes affecting proofs, documentation integrity,
or the decoder. Do not use Python optimization flags. Check the diff and links.
Report the checks actually executed in the pull request.

Repository maintenance does not authorize outside messages, paid computation,
submissions, release tags, or unrelated repository changes.
