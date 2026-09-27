# Manuscript background and source guide

28 September 2026 (Asia/Shanghai). Scientific background for the two
reconstruction guarantees, with sources checked against the current project.
This is a research resource; manuscript drafting remains on hold.

## What the background must explain

The problem is to recover an integral reciprocal Weil polynomial from a finite
set of supplied exact cyclic resultants. For an abelian variety these are
cardinalities over field extensions. The polynomial is a compact arithmetic
invariant: it determines the isogeny class over the base field and, for a
Jacobian, the curve zeta function. Acquisition of the cardinalities is a
separate computational task.

The literature already supplies full-sequence uniqueness results, finite
generic determination bounds, all-field consecutive-count reconstruction, and
efficient first-$g$ reconstruction in a large-field regime. The main candidate
contribution here is the **quadratic sufficient field-size threshold** for
first-$g$ reconstruction, with deterministic polynomial bit time. The selected
all-field schedule is a complementary refinement of existing machinery.
The comparison must keep the input class, indices, threshold, and computational
model together; query count alone does not describe the result.

## Background package

| Need | Resource |
|---|---|
| Frobenius, Weil polynomials, abelian varieties, curves, and geometric interpretation | [Foundations](FOUNDATIONS.md) |
| Closest finite-field reconstruction theorems, thresholds, endpoints, and count acquisition | [Weil reconstruction predecessors](WEIL_RECONSTRUCTION.md) |
| General cyclic-resultant determination, genericity, recurrences, and errata | [Cyclic-resultant context](CYCLIC_RESULTANTS.md) |
| Logarithms, Möbius/Newton reconstruction, contraction, and bit complexity | [Algorithmic context](ALGORITHMIC_CONTEXT.md) |
| Which source or local proof supports each prospective manuscript claim | [Claim map](CLAIM_MAP.md) |
| Reusable citation metadata | [BibTeX bibliography](REFERENCES.bib) |
| Versions, inspected locations, searches, and unresolved source access | [Source record](SOURCE_RECORD.md) |
| Executed preservation and reproducibility checks | [Verification receipt](VERIFICATION.json) |

Citation keys such as `Kedlaya2006` refer to the BibTeX file. The source record
distinguishes inspected theorem passages, metadata-only entries, and earlier
inspection records. A bibliography entry is not evidence that its full text
was read. Sources are linked, not copied into the repository.

## Connection to the existing scientific package

| Eventual manuscript component | Canonical material already present |
|---|---|
| Exact input model and main theorem | [First-$g$ theorem, Section 1](../first_g_reconstruction_v1/THEOREM.md#1-theorem-and-exact-promises) |
| Contraction, finite precision, rational algorithm, and bit bounds | [First-$g$ theorem, Sections 2–9](../first_g_reconstruction_v1/THEOREM.md) |
| Complementary all-field theorem | [Note 28](../../exploration/phase_2/ORDINARY_QUERY_THEOREM_AUDIT_28.md) and [proof/complexity audit](../../exploration/phase_2/RECONSTRUCTION_PROOF_REVIEW_29.md) |
| Geometric corollaries and exact output-size boundary | [Finite-field application](../finite_field_application_v1/COROLLARIES.md) |
| Evidence and limitations of internal verification | [Consolidation audit](../consolidation_v1/AUDIT.md) and the three experiment directories linked from the [root README](../../README.md#read-and-reproduce) |
| Restricted limitation of the current norm argument | [Method boundary](../consolidation_v1/METHOD_BOUNDARY.md) |

These remain the canonical proofs and executable evidence. The background
does not duplicate or replace them, improve the constants, or certify geometric
realizability of the fixtures. Earlier versioned assessments remain historical
checkpoints; this package gathers the citation support for future writing.

## Coverage boundary

The package covers the background needed for the stated theorems, their proof
methods, their geometric interpretation, and their direct literature comparison.
It does not require a survey of point-counting algorithms, quantum algorithms,
cryptographic protocols, or the classification of all Jacobians: no performance
or realization theorem in those areas is claimed. The source record retains
access limits and the scope of the competing-result search. Absence from that
search supports a qualified comparison, not universal priority.

No additional discovery is required to use this material for manuscript
preparation. Bibliographic versions should be checked again when writing; a
new competing theorem or a concrete correctness issue would change the
scientific assessment.
