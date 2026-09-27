# Research status

Updated 27 September 2026.

Sparse Weil Reconstruction is established as a standalone classical research
repository. The inherited baseline is parent commit
`9ef56e5af6c7af452750b8cd035da6745f1d00c0`; all 17 preserved files match its
Git blob identities and the recorded SHA256 values. The existing MIT license
is retained. No inherited proof, decoder, fixture, or report was refactored.

## Established within the current evidence

- A written all-field supplied-count theorem for $g\ge32$, with
  $h+\lceil h/2\rceil$ selected values and maximum index $2g-4$.
- A deterministic exact decoder with an explicit polynomial bit-complexity audit.
- Seven supplied-polynomial controls recovering 489 coefficients and 227 traces.
- A separate irreducible degree-64 control, exact resultant calculations,
  numerical-enclosure controls, and an accepted-corruption example.

These constitute internal mathematical and implementation evidence. External
peer review, publication priority, minimum-query optimality, and realizability
of the test polynomials as curve Jacobians are not established.

## Handoff verification

Both inherited verifiers passed in the standalone layout under Python 3.12.14.
They checked their source/dependency hashes and reproduced both exact reference
reports in temporary directories. The root import-integrity check also passed.
The [verification receipt](provenance/handoff-verification.json) records the
commands and outputs from this handoff.

Earlier quantum, group-order, and unrelated historical suites were not transferred
or rerun. Their previous execution statements remain historical records in the
preserved notes. This handoff does not constitute a new independent proof audit.

## Next decision

Complete a theorem-level predecessor and significance comparison in this
standalone scope. Preserve the selected-query/all-field distinction and resolve
unverified source leads before strengthening novelty language. The
[work order](work_orders/CURRENT.md) defines that task. Manuscript preparation
remains on hold.
