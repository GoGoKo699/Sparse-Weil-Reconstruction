# Sparse Weil Reconstruction

Recover a finite-field arithmetic invariant from a small set of exact counts.

An abelian variety has a Frobenius polynomial that determines its cardinalities
over every finite extension. This project studies the reverse direction:
**recovering that polynomial from selected cardinalities**. Its main result
uses the first $g$ counts when $q\ge65{,}536g^2$. A complementary sparse-count
result works for every $q\ge2$ when $g\ge32$. Both algorithms have deterministic
polynomial bit complexity.

**Start with the [Galbraith reading guide](docs/READING_GUIDE.md).**
It leads from textbook objects through worked examples to the reconstruction
proofs. Chidambaram–Keller is the secondary anchor for understanding the step
from the closest predecessor to the quadratic field-size guarantee.

| Start here | Continue with |
|---|---|
| [The polynomial and its counts](docs/TUTORIAL.md) | Definitions, notation, and worked examples |
| [From counts to coefficients](docs/RECONSTRUCTION.md) | Logarithms, correction, convergence, and exact rounding |
| [The step from Chidambaram–Keller](docs/COMPARISON.md) | Shared problem, different proof, and the resulting field-size bound |

**Status:** written proofs, exact executable controls, and a completed
[internal consolidation audit](research/consolidation_v1/AUDIT.md).
Manuscript preparation is on hold.

## The polynomial and supplied data

Let $g\ge1$ and $q\ge2$ be integers. Consider

$$
P(T)=\prod_{i=1}^{2g}(1-\alpha_iT)=\sum_{j=0}^{2g}c_jT^j\in\mathbb Z[T],
\qquad c_0=1,
$$

where $|\alpha_i|=\sqrt q$ and
$c_{2g-j}=q^{g-j}c_j$ for $0\le j\le g$.
The decoder receives $q$, $g$, and the indicated **true exact integers**

$$
K_m=\prod_{i=1}^{2g}(1-\alpha_i^m).
$$

These are cyclic-resultant values. For an abelian variety $A/\mathbb F_q$,
with $q$ a prime power, they are $K_m=\#A(\mathbb F_{q^m})$.
The algebraic reconstruction theorems themselves allow every integer $q$
in their stated regimes.

| Guarantee | Sufficient regime | Supplied indices | Number of values |
|---|---|---|---:|
| First-$g$ reconstruction | $g\ge1$, $q\ge65{,}536g^2$ | $1,\ldots,g$ | $g$ |
| All-field sparse reconstruction | $g\ge32$, every $q\ge2$ | $D_{g-2}$ below | $g-2+\lceil(g-2)/2\rceil$ |

Both recover $P$ in deterministic time polynomial in $g$ and $\log q$.
The thresholds are sufficient bounds.

### First-$g$ reconstruction

Chidambaram–Keller establish efficient first-$g$ recovery for sufficiently
large fields. Here, a contraction on weighted polynomial coefficients gives
an explicit **quadratic sufficient field-size threshold**. The rational
implementation uses certified logarithms, finite series, and dyadic rounding.

The [method explanation](docs/RECONSTRUCTION.md) develops this idea, and the
[comparison](docs/COMPARISON.md) shows how it connects to the predecessor's
power-sum argument. The full [theorem and algorithm](research/first_g_reconstruction_v1/THEOREM.md)
contain the bounds and proof of polynomial bit complexity.

### Sparse reconstruction over every field

Put $h=g-2$. Supply the indices

$$
D_h=\{1,\ldots,h\}\cup\{2,4,\ldots,2h\}.
$$

There are $h+\lceil h/2\rceil<2g$ values, and the largest index is $2g-4$.
For genus 32 this means 45 counts, at indices $1,\ldots,30$ and
$32,34,\ldots,60$. The schedule refines Kedlaya's logarithmic
Möbius/Newton reconstruction framework, with the endpoint precedents recorded
in the [background comparison](research/manuscript_background_v1/WEIL_RECONSTRUCTION.md).
See the [proof](exploration/phase_2/ORDINARY_QUERY_THEOREM_AUDIT_28.md) and
[bit-complexity audit](exploration/phase_2/RECONSTRUCTION_PROOF_REVIEW_29.md).

## What the recovered polynomial tells us

For an abelian variety, $P_A$ determines its $\mathbb F_q$-isogeny class.
For a promised Jacobian $A=J_C$, it gives the curve zeta function

$$
Z_C(T)=\frac{P_A(T)}{(1-T)(1-qT)}.
$$

The inputs here count **Jacobian elements**. Ordinary curve point counts are
a different input: their first $g$ values already recover $P_A$ over every
finite field by Newton identities. The [worked tutorial](docs/TUTORIAL.md)
explains this distinction.

For a general abelian variety, $P_A$ also specifies its full zeta function
compactly; expanding that function has exponential output size. The
[finite-field corollaries](research/finite_field_application_v1/COROLLARIES.md)
state the exact applications and output bounds.

## Read and reproduce

Python 3.10 or later; standard library only:

```sh
python3 verify.py
```

This checks the 17 preserved import files and regenerates all three pinned
research reports in temporary storage. Do not use `-O` or `-OO`.
For import integrity alone, use `python3 verify.py --integrity-only`.

| Scientific material | Entry point |
|---|---|
| Primary and secondary teaching anchors | [Reading guide](docs/READING_GUIDE.md) · [Source map](docs/SOURCES.md) |
| First-$g$ proof and exact implementation | [Theorem](research/first_g_reconstruction_v1/THEOREM.md) · [Experiment](experiments/first_g_reconstruction_v1/README.md) |
| All-field proof and exact implementation | [Note 28](exploration/phase_2/ORDINARY_QUERY_THEOREM_AUDIT_28.md) · [Note 29](exploration/phase_2/RECONSTRUCTION_PROOF_REVIEW_29.md) · [Experiment](experiments/all_field_reconstruction_v1/README.md) |
| Irreducible control and count-corruption example | [Audit experiment](experiments/reconstruction_audit_v1/README.md) |
| Claim-to-source map and bibliography | [Scientific background](research/manuscript_background_v1/README.md) |
| Current mathematical checks and method boundary | [Consolidation audit](research/consolidation_v1/AUDIT.md) · [Norm-method boundary](research/consolidation_v1/METHOD_BOUNDARY.md) |
| Detailed literature assessment | [Assessment](research/contribution_assessment_v1/ASSESSMENT.md) · [Source check](research/consolidation_v1/SOURCES.md) |
| Project state and retained evidence | [Status](STATUS.md) · [Provenance](PROVENANCE.md) · [Work order](work_orders/CURRENT.md) |

## Scope and provenance

The theorems assume the supplied counts are correct. Count acquisition and
authentication are separate tasks; successful decoding alone does not verify
an input transcript. The exact controls test supplied polynomials, without
claiming they are Jacobians of curves. The written proofs establish the
uniform guarantees; the finite controls check their implementations.

The candidate contributions are the quadratic-threshold first-$g$ guarantee
and the selected-data all-field refinement. The
[literature assessment](research/contribution_assessment_v1/ASSESSMENT.md)
records the inspected predecessors and search limits. Optimal thresholds and
minimum query counts remain open in the general setting studied here.

This classical reconstruction project originated in
[Quantum Assisted Algorithm Discovery](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery).
The imported theorem, audit, implementation, and reports are preserved byte
for byte. Versioned notes describe their own checkpoints; this overview,
[STATUS.md](STATUS.md), and the [work order](work_orders/CURRENT.md) describe
the current project.

MIT license, Copyright (c) 2026 Ruge Lin.
