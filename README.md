# Sparse Weil Reconstruction

Exact reconstruction of integral Weil polynomials from selected cyclic-resultant values.

Two deterministic polynomial-time guarantees are developed here: sparse
reconstruction over every field for $g\ge32$, and reconstruction from the
first $g$ values under the sufficient condition $q\ge65{,}536g^2$.
This repository preserves the original all-field theorem, proof audit,
implementation, and exact verification reports from the parent
[Quantum Assisted Algorithm Discovery](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery)
project. Its research scope is classical reconstruction theory.

**Status:** written proofs, internal mathematical checks, and exact executable
controls. Publication priority and query optimality remain open.
Manuscript preparation is on hold.

## The polynomial and supplied data

Let $g\ge1$ and $q\ge2$ be integers. Consider

$$
P(T)=\prod_{i=1}^{2g}(1-\alpha_iT)=\sum_{j=0}^{2g}c_jT^j\in\mathbb Z[T],
\qquad c_0=1,
$$

where the inverse roots satisfy $|\alpha_i|=\sqrt q$ and
$c_{2g-j}=q^{g-j}c_j$ for $0\le j\le g$.
Define $K_m=\prod_i(1-\alpha_i^m)$. The inputs to each decoder are
$q$, $g$, and the indicated **true exact integers** $K_m$.

| Guarantee | Sufficient regime | Supplied indices | Number of values |
|---|---|---|---:|
| All-field sparse reconstruction | $g\ge32$, every $q\ge2$ | $D_{g-2}$ below | $g-2+\lceil(g-2)/2\rceil$ |
| First-$g$ reconstruction | $g\ge1$, $q\ge65{,}536g^2$ | $1,\ldots,g$ | $g$ |

Both recover $P$ in deterministic time polynomial in $g$ and $\log q$.
The constants are sufficient, not optimal. Neither decoder acquires or
authenticates its supplied counts.

### All-field sparse reconstruction

Put $h=g-2$. The selected indices are

$$
D_h=\{1,\ldots,h\}\cup\{2,4,\ldots,2h\}
$$

There are $h+\lceil h/2\rceil<2g$ values, and the largest index is $2g-4$.

| Genus | Supplied values | Largest index |
|---:|---:|---:|
| 32 | 45 | 60 |
| 64 | 93 | 124 |

For genus 32 the indices are $1,\ldots,30$ and $32,34,\ldots,60$.
They are not the first 45 indices. The threshold 32 is sufficient, not optimal.

### First-$g$ reconstruction with a quadratic field-size threshold

The [companion theorem](research/first_g_reconstruction_v1/THEOREM.md) uses a
contraction on weighted polynomial coefficients to remove the higher-index
terms from the supplied logarithms. Its rational implementation uses certified
logarithms, finite series, and dyadic rounding; it does not compute roots or
require exact arithmetic in $\sqrt q$.

Chidambaram–Keller already prove first-$g$ reconstruction for sufficiently large
$q$. The candidate improvement here is an explicit **quadratic sufficient
threshold**, with polynomial bit time retained. See the
[matched source assessment](research/contribution_assessment_v1/ASSESSMENT.md).
This complements the all-field guarantee rather than replacing it.

For a curve over $\mathbb F_q$, where $q$ is a prime power, $P$ is its zeta
numerator and $K_m=|J_C(\mathbb F_{q^m})|$ counts **Jacobian elements**.
Ordinary curve point counts are a different input problem.

## Read and reproduce

| Purpose | Entry point |
|---|---|
| First-$g$ theorem, contraction, and finite-precision proof | [Companion theorem](research/first_g_reconstruction_v1/THEOREM.md) |
| Rational first-$g$ decoder and exact controls | [First-$g$ experiment](experiments/first_g_reconstruction_v1/README.md) |
| Current predecessor and significance assessment | [Assessment](research/contribution_assessment_v1/ASSESSMENT.md) · [Primary sources](research/contribution_assessment_v1/SOURCES.md) |
| Full theorem, cancellation, uniform tail proof, and rounding | [Note 28](exploration/phase_2/ORDINARY_QUERY_THEOREM_AUDIT_28.md) |
| Proof audit and explicit bit complexity | [Note 29](exploration/phase_2/RECONSTRUCTION_PROOF_REVIEW_29.md) |
| Decoder and seven supplied-polynomial controls | [Reconstruction experiment](experiments/all_field_reconstruction_v1/README.md) |
| Irreducible degree-64 control and accepted-corruption boundary | [Audit experiment](experiments/reconstruction_audit_v1/README.md) |
| Preserved baseline source comparison | [Historical sources](experiments/reconstruction_audit_v1/SOURCES.md) |
| Exact import origin and historical context | [Provenance](PROVENANCE.md) |
| Current evidence and next research task | [Status](STATUS.md) · [Work order](work_orders/CURRENT.md) |

Python 3.10 or later; standard library only:

```sh
python3 verify.py
```

This checks the 17 preserved files against their import hashes, runs both
inherited verifiers, and checks the first-$g$ successor experiment. Each
regenerates its exact report in temporary storage.
Do not use `-O` or `-OO`. For import integrity alone, use
`python3 verify.py --integrity-only`.

## Scope and attribution

The decoder receives $q$, $g$, and the selected count map. It does not receive a
curve equation, a twist oracle, or a factorization. It does not acquire or
authenticate the counts. Successful decoding can accept a corrupted transcript;
the audit retains an explicit example. Supplied test polynomials have not been
shown to be curve Jacobians.

Kedlaya's Möbius/Newton reconstruction framework, Sutherland's endpoint
precedents, and Chidambaram–Keller's first-$g$ reconstruction are essential
context. The candidate contributions are the selected-data all-field guarantee
and the quadratic-threshold first-$g$ decoder.
The source comparison is bounded; it does not establish publication priority.
No quantum speedup or minimum-query theorem is claimed here.

The two numbered notes and two inherited experiment directories are preserved historical
records. Statements inside them about a proposed repository or past verification
runs refer to their original checkpoints. This README, [STATUS.md](STATUS.md),
and the [work order](work_orders/CURRENT.md) describe the current project.

MIT license, Copyright (c) 2026 Ruge Lin.
