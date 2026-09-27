# Research status

Updated 27 September 2026. Manuscript preparation remains on hold.

The project now has two complementary supplied-count reconstruction guarantees.
Both concern reciprocal integral q-Weil polynomials, true exact cyclic
resultants, and deterministic polynomial bit time.

| Result | Sufficient regime | Supplied indices |
|---|---|---|
| Preserved all-field theorem | $g\ge32$, every $q\ge2$ | $D_{g-2}$, with $g-2+\lceil(g-2)/2\rceil$ values |
| First-$g$ companion | $g\ge1$, $q\ge65{,}536g^2$ | $1,\ldots,g$ |

The [companion proof](research/first_g_reconstruction_v1/THEOREM.md) establishes
a contraction on a weighted coefficient ball and an explicit finite rational
implementation. Quantization after each iteration controls denominator growth.
The constants are sufficient, not optimal.

## Contribution assessment

The [primary-source comparison](research/contribution_assessment_v1/ASSESSMENT.md)
resolves the Chidambaram–Keller lead, includes their current v2 complexity
statement, and adds Bézivin's generic linear bound and Hillar's erratum.

First-$g$ reconstruction is already prior work for sufficiently large fields.
The companion's candidate contribution is the quadratic sufficient field-size
threshold, retaining polynomial bit time. The all-field theorem is a selected
support refinement of Kedlaya's framework. No minimum-query theorem or blanket
advantage over every predecessor is claimed.

The written proofs have internal mathematical checks and executable evidence.
External peer review, publication priority, optimality, and Jacobian realizability
of the controls remain unestablished. This is classical reconstruction research;
no quantum-advantage claim is inherited from the parent project.

## Verification and preserved evidence

All 17 imported files remain byte-identical to the pinned parent baseline
`9ef56e5af6c7af452750b8cd035da6745f1d00c0`.
The preserved theorem, audit, fixtures, decoder, reports, and license were not
refactored. Their exact reports reproduce.

The successor experiment adds five supplied-polynomial controls at genera
1, 2, 3, 4 and 8. All 41 coefficients reconstruct exactly; independent companion
determinants agree on all 18 supplied counts. Exact final coefficient-error
bounds, allowed logarithm perturbations, invalid inputs, and an accepted
count-corruption example are retained. The new verifier reproduces its pinned
report from fresh temporary storage.

Run `python3 verify.py` for all three reports and import integrity.
The [current receipt](research/contribution_assessment_v1/VERIFICATION.json)
records this continuation's executed checks. Historical handoff receipts remain
in `provenance/`. No native point counter, author implementation, Lean proof,
quantum circuit, or hardware was run.

Successful decoding is not count authentication or certification of a claimed
curve. See the [work order](work_orders/CURRENT.md) for the remaining scientific
question and bounded next step.
