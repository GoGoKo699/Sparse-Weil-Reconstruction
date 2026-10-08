# Scientific background and source guide

The background covers the finite-field interpretation, reconstruction
predecessors, and analytic methods behind the two guarantees. Source versions,
inspection dates, and access limits are recorded in the
[source record](SOURCE_RECORD.md).

## Background package

| Topic | Resource |
|---|---|
| Frobenius, Weil polynomials, abelian varieties, curves, and geometric interpretation | [Foundations](FOUNDATIONS.md) |
| Finite-field reconstruction theorems, thresholds, endpoints, and count acquisition | [Weil reconstruction predecessors](WEIL_RECONSTRUCTION.md) |
| Cyclic-resultant determination, genericity, recurrences, and errata | [Cyclic-resultant context](CYCLIC_RESULTANTS.md) |
| Logarithms, Möbius/Newton reconstruction, contraction, and bit complexity | [Algorithmic context](ALGORITHMIC_CONTEXT.md) |
| Claim-level evidence and conditions | [Claim map](CLAIM_MAP.md) |
| Citation metadata | [BibTeX bibliography](REFERENCES.bib) |

Citation keys such as `Kedlaya2006` resolve in the bibliography. The source
record distinguishes inspected theorem passages from metadata-only entries.
The comparisons use the recorded statements and versions.

## Canonical proofs and verification

| Result | Proof or evidence |
|---|---|
| Exact input model and quadratic sufficient threshold | [First-$`g`$ theorem](../first_g_reconstruction_v1/THEOREM.md#1-theorem-and-exact-promises) |
| Contraction, finite precision, rational algorithm, and bit bounds | [First-$`g`$ proof, Sections 2–9](../first_g_reconstruction_v1/THEOREM.md) |
| Complementary all-field theorem | [Proof and bit complexity](../../docs/ALL_FIELD_PROOF.md) |
| Geometric corollaries and output-size boundary | [Finite-field application](../finite_field_application_v1/COROLLARIES.md) |
| Mathematical and implementation checks | [Proof and arithmetic checks](../consolidation_v1/AUDIT.md) · [Reproduce the experiments](../../README.md#read-and-reproduce) |
| Limitation of the single-radius norm argument | [Method boundary](../consolidation_v1/METHOD_BOUNDARY.md) |
