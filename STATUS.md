# Research status

Updated 28 September 2026. Manuscript preparation remains on hold.

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

## Consolidation checkpoint

The [fresh internal audit](research/consolidation_v1/AUDIT.md) found no
substantive gap in the analytic proof, finite-error schedule, rational
implementation, or polynomial denominator bounds. It records an explicit
common denominator and clarifies that the experiment's `max_intermediate_bits`
field samples selected coefficients, rather than all arithmetic temporaries.
No decoder or pinned expected output was changed.

The [bounded extension note](research/consolidation_v1/METHOD_BOUNDARY.md)
proves a limitation of the current single-radius norm argument: covering every
true polynomial by a fixed small ball and bounding the alias operator on the
whole algebra requires a quadratic field-size scale. This is not a lower bound
for reconstruction and does not show failure of the actual iteration.

The core scientific work within the stated two-theorem scope is complete at
the level of written proofs, internal audits, and exact reproducibility.
No known substantive gap remains from these checks. Further threshold or query
improvements are optional; manuscript preparation remains on hold.

## Finite-field application checkpoint

The [application note](research/finite_field_application_v1/COROLLARIES.md)
checks the hypotheses for every abelian variety over a finite field and states
both recovery corollaries with the original thresholds. No simplicity,
ordinarity, genericity, or polarization input is required. The recovered
Frobenius polynomial determines the isogeny class over the given finite field.
For a promised Jacobian it yields the curve zeta function in polynomial bit time.

The note separates Jacobian cardinalities from ordinary curve point counts and
compact Frobenius output from an expanded abelian-variety zeta function. It
derives the latter's exponential output size, including a leading coefficient
with exponentially many bits. These are standard consequences and output
clarifications, not a third novelty claim. No decoder or reference output
changed, and no additional scientific gap was found in this application check.

## Manuscript background checkpoint

The [background package](research/manuscript_background_v1/README.md) now
collects the finite-field foundations, direct reconstruction predecessors,
general cyclic-resultant theory, and analytic/bit-complexity context needed for
future writing. A claim-to-source map connects the standard facts and comparison
statements to the existing local proofs. The reusable bibliography has 17
entries; relevant primary passages were inspected for 15, while two historical
entries retain explicit full-text access limits and supported alternative
citations. Versions, theorem locations, and the bounded search are recorded.

The comparison retains Chidambaram–Keller's existing polynomial-time first-$g$
result, Bézivin's linear generic determination bound, Hillar's erratum, and the
distinction between generic and uniform Weil reconstruction. No newly inspected
statement subsumes the two local guarantees. This is background preparation,
not manuscript drafting, a new theorem, or universal priority certification.

## Reader preparation

The [reading guide](docs/READING_GUIDE.md) now uses Galbraith's *Mathematics
of Public Key Cryptography* as its primary teaching anchor, with
Chidambaram–Keller as the secondary research anchor. The new notes give a
notation map, original worked examples, the logarithmic reconstruction bridge,
and a matched comparison explaining the quadratic field-size guarantee.
The [source map](docs/SOURCES.md) pins the teaching editions and adds a
Galbraith BibTeX supplement to the existing scientific bibliography.

The teaching layer links to the canonical proofs and exact experiments.
All scientific thresholds, decoders, reference reports, and versioned
background files are retained. Manuscript preparation remains on hold.

## Contribution assessment

The [primary-source comparison](research/contribution_assessment_v1/ASSESSMENT.md)
resolves the Chidambaram–Keller lead, includes their current v2 complexity
statement, and adds Bézivin's generic linear bound and Hillar's erratum.

First-$g$ reconstruction is already prior work for sufficiently large fields.
The companion's candidate contribution is the quadratic sufficient field-size
threshold, retaining polynomial bit time. The all-field theorem is a selected
support refinement of Kedlaya's framework. No minimum-query theorem or blanket
advantage over every predecessor is claimed.

A [fresh focused source check](research/consolidation_v1/SOURCES.md) reconfirmed
the current predecessor and found no additional theorem subsuming the quadratic
guarantee. Its actual queries and access limits are recorded.

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
The [background receipt](research/manuscript_background_v1/VERIFICATION.json)
records the scientific-background pass, and the [teaching check](docs/VERIFICATION.md)
records the new exposition checks. Earlier research and handoff receipts
remain at their versioned paths. No native point counter, author
implementation, Lean proof, quantum circuit, or hardware was run.

Successful decoding is not count authentication or certification of a claimed
curve. See the [work order](work_orders/CURRENT.md) for the consolidation scope
and the conditions for reopening scientific work.
