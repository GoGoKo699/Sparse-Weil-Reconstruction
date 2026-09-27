# Sparse Weil Reconstruction

Exact reconstruction of integral Weil polynomials from selected cyclic-resultant values.

The starting result is a deterministic polynomial-time decoder using fewer than
$2g$ supplied values, uniformly over all finite fields when $g\ge32$.
This repository preserves the theorem, proof audit, implementation, and exact
verification reports from the parent
[Quantum Assisted Algorithm Discovery](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery)
project. Its research scope is classical reconstruction theory.

**Status:** the theorem has a written proof and has passed an internal proof and
implementation audit. Publication priority and query optimality remain open.
Manuscript preparation is on hold.

## The theorem

Let $g\ge32$ and $q\ge2$ be integers. Consider

$$
P(T)=\prod_{i=1}^{2g}(1-\alpha_iT)=\sum_{j=0}^{2g}c_jT^j\in\mathbb Z[T],
\qquad c_0=1,
$$

where the inverse roots satisfy $|\alpha_i|=\sqrt q$ and
$c_{2g-j}=q^{g-j}c_j$ for $0\le j\le g$.
Define $K_m=\prod_i(1-\alpha_i^m)$ and $h=g-2$.
The **true exact integers** $K_m$ at the selected indices

$$
D_h=\{1,\ldots,h\}\cup\{2,4,\ldots,2h\}
$$

determine $P$ and permit deterministic reconstruction in time polynomial in
$g$ and $\log q$. The number of supplied values is
$h+\lceil h/2\rceil<2g$, and the largest index is $2g-4$.

| Genus | Supplied values | Largest index |
|---:|---:|---:|
| 32 | 45 | 60 |
| 64 | 93 | 124 |

For genus 32 the indices are $1,\ldots,30$ and $32,34,\ldots,60$.
They are not the first 45 indices. The threshold 32 is sufficient, not optimal.

For a curve over $\mathbb F_q$, where $q$ is a prime power, $P$ is its zeta
numerator and $K_m=|J_C(\mathbb F_{q^m})|$ counts **Jacobian elements**.
Ordinary curve point counts are a different input problem.

## Read and reproduce

| Purpose | Entry point |
|---|---|
| Full theorem, cancellation, uniform tail proof, and rounding | [Note 28](exploration/phase_2/ORDINARY_QUERY_THEOREM_AUDIT_28.md) |
| Proof audit and explicit bit complexity | [Note 29](exploration/phase_2/RECONSTRUCTION_PROOF_REVIEW_29.md) |
| Decoder and seven supplied-polynomial controls | [Reconstruction experiment](experiments/all_field_reconstruction_v1/README.md) |
| Irreducible degree-64 control and accepted-corruption boundary | [Audit experiment](experiments/reconstruction_audit_v1/README.md) |
| Closest inspected primary results and search limitations | [Source comparison](experiments/reconstruction_audit_v1/SOURCES.md) |
| Exact import origin and historical context | [Provenance](PROVENANCE.md) |
| Current evidence and next research task | [Status](STATUS.md) · [Work order](work_orders/CURRENT.md) |

Python 3.10 or later; standard library only:

```sh
python3 verify.py
```

This checks the 17 preserved files against their import hashes and runs both
inherited verifiers. Each regenerates its exact report in temporary storage.
Do not use `-O` or `-OO`. For import integrity alone, use
`python3 verify.py --integrity-only`.

## Scope and attribution

The decoder receives $q$, $g$, and the selected count map. It does not receive a
curve equation, a twist oracle, or a factorization. It does not acquire or
authenticate the counts. Successful decoding can accept a corrupted transcript;
the audit retains an explicit example. Supplied test polynomials have not been
shown to be curve Jacobians.

Kedlaya's Möbius/Newton reconstruction framework and Sutherland's endpoint
precedents are essential ingredients. The candidate contribution is the
selected-data, all-field guarantee with an explicit polynomial-bit-time decoder.
The source comparison is bounded; it does not establish publication priority.
No quantum speedup or minimum-query theorem is claimed here.

The two numbered notes and experiment directories are preserved historical
records. Statements inside them about a proposed repository or past verification
runs refer to their original checkpoints. This README, [STATUS.md](STATUS.md),
and the [work order](work_orders/CURRENT.md) describe the current project.

MIT license, Copyright (c) 2026 Ruge Lin.
