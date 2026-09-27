# Claims, evidence, and attribution

28 September 2026. This is a source map for future writing, not manuscript text.
Citation keys resolve in [REFERENCES.bib](REFERENCES.bib); exact external
locators and inspection status are in [SOURCE_RECORD.md](SOURCE_RECORD.md).

## Claim-to-source map

| Prospective claim | Evidence to cite or use | Qualification that belongs with the claim |
|---|---|---|
| Extension cardinalities of an abelian variety are cyclic resultants of its Frobenius polynomial | `MilneAV1986`, Section 19; [Foundations](FOUNDATIONS.md) | $q$ is a prime power for the geometric interpretation; use the stated Frobenius convention. |
| The recovered polynomial determines the base-field isogeny class | `Tate1966`, Theorem 1(c) | This neither identifies an isomorphism class nor constructs an isogeny. |
| Jacobian cardinalities recover the curve zeta function under the theorem's regimes | `MilneJV1986`, Section 11, and [local corollary](../finite_field_application_v1/COROLLARIES.md#2-curves-and-jacobians) | Inputs count Jacobian elements. Ordinary curve point counts are different data. |
| Full-sequence uniqueness, generic finite determination, and uniform efficient recovery are distinct questions | `Hillar2005` with `HillarErratum2005`, `HillarLevine2007`, `Bezivin2008`; [comparison](CYCLIC_RESULTANTS.md) | Keep the generic domains, resultant convention, and finite versus infinite data explicit. |
| Normalized logarithmic/Möbius reconstruction with Newton residue information is prior machinery | `Kedlaya2006`, Section 8; [method context](ALGORITHMIC_CONTEXT.md) | The cited quantum acquisition procedure and the classical supplied-data decoder are separate. |
| Endpoint evaluation has a direct low-genus precedent | `Sutherland2009`, Section 4.1 | Its stated small-genus conclusion is not a varying-genus sparse-schedule theorem. |
| First-$g$ reconstruction and polynomial bit complexity already exist in a large-field regime | `ChidambaramKeller2026`, Theorem 1.1 and Section 6 | Use the inspected v2; retain its strict sufficient inequality and its polynomial-time statement. |
| The local first-$g$ theorem has sufficient threshold $q\ge65{,}536g^2$ | [Theorem, Sections 1–9](../first_g_reconstruction_v1/THEOREM.md); compare `ChidambaramKeller2026`, Remark 7.12 | Candidate improvement is threshold growth. It is neither a first-$g$ priority claim nor an optimal threshold theorem. |
| A fixed sparse schedule suffices for all $q\ge2$, $g\ge32$ | [Note 28](../../exploration/phase_2/ORDINARY_QUERY_THEOREM_AUDIT_28.md) and [Note 29](../../exploration/phase_2/RECONSTRUCTION_PROOF_REVIEW_29.md); compare `Kedlaya2006` and `RoySaxenaVenkatesh2025` | State $D_{g-2}$ exactly. Its size is not an initial-segment length and does not establish minimum query count. |
| The finite rational first-$g$ algorithm runs in polynomial bit time | [Theorem, Sections 6–9](../first_g_reconstruction_v1/THEOREM.md) and [audit, Section 3](../consolidation_v1/AUDIT.md#3-finite-arithmetic-and-implementation) | Finite termination, error, and denominator bounds are local proof obligations; a real-arithmetic contraction alone is insufficient. |
| The present norm proof has an intrinsic quadratic scale | [Restricted method-boundary proposition](../consolidation_v1/METHOD_BOUNDARY.md) | Only the specified single-radius, whole-algebra small-ball architecture is covered. It is not a data lower bound or failure theorem for the iteration. |
| $P_A$ is compact, whereas an expanded full abelian-variety zeta function has exponential output size | [Application note, Section 3](../finite_field_application_v1/COROLLARIES.md#3-compact-output-versus-an-expanded-abelian-variety-zeta-function); standard identity in `MilneAV1986`, Corollary 19.4 | Polynomial-time output is the degree-$2g$ polynomial. The curve zeta function remains compact. |
| Exact controls reproduce the promised-input decoder | Experiment READMEs, manifests, and reports linked from the [root README](../../README.md#read-and-reproduce) | Finite controls do not replace a proof, authenticate supplied counts, or establish that fixtures are Jacobians. |

## Quantities that should remain separate

The comparison should report the polynomial class, field/genus regime, selected
indices, number of integers supplied, maximum extension index, transcript bit
length, and decoder bit complexity. Count acquisition costs require an
additional model and are not inferred from a smaller number of inputs.

There are three different output claims: a coefficient list for $P_A$, the
compact curve zeta function when $A$ is a promised Jacobian, and mathematical
determination of the full $Z_A$. The last one does not promise expansion of its
numerator and denominator in polynomial time.

## Attribution and novelty discipline

Standard Frobenius facts, Newton identities, Möbius inversion, endpoint
evaluations, Banach-algebra estimates, and the contraction principle should be
identified as tools. The local work lies in the chosen support and tail bounds,
or in the weighted coefficient reconstruction with its invariant domain and
certified finite implementation. The primary predecessor discussion is in
[WEIL_RECONSTRUCTION.md](WEIL_RECONSTRUCTION.md).

The supported comparison is that the inspected statements do not subsume the
two stated local guarantees. It does not justify “first ever”, minimum-query
optimality, an optimal quadratic threshold, an unconditional acquisition
speedup, or a resolved general reciprocal-polynomial conjecture. A change to
these assertions requires new evidence, not a stronger adjective.

The written proofs and reproducibility checks have internal review. External
peer review and priority remain separate from those completed checks.
