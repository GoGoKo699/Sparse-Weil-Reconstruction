# Predecessor comparison and verification sources

The proof combines the reconstruction ingredients below with the selected query
set and uniform tail bound. Consolidated source coverage and exact versions are
recorded in the [primary-source record](../../research/contribution_assessment_v1/SOURCES.md).

## 1. Kiran S. Kedlaya

Quantum computation of zeta functions of curves, Computational Complexity 15
(2006), 1-19. arXiv:math/0411623v3, 30 November 2005.
https://arxiv.org/pdf/math/0411623
https://arxiv.org/abs/math/0411623

Sections 8-9 supply the cutoff-dependent Mobius formula,
Newton residue information, consecutive max(18,2g) schedule, and explicit query-
count question. Section 8 also records the separate condition used to acquire
orders via Proposition 11. The metadata identifies v3 as the refereed version.

The present construction uses the same normalized power-sum approximation, not
a new cancellation principle. The sparse input support, varying cutoff within
that support, all-field g>=32 tail bound and range-reduced decoder are proved in
Note 28.

## 2. Andrew V. Sutherland

A Generic Approach to Searching for Jacobians, Mathematics of Computation 78
(2009), 485-507; arXiv:0708.3168.
https://arxiv.org/pdf/0708.3168

Section 4.1, Lemma 4 concerns genus at most three
and sufficiently large q, with unconditional exact endpoint algebra in genus two.
It is a direct predecessor for endpoint/twist reasoning. The comparison uses
the lemma's text and formulas.

## 3. Christopher J. Hillar and Lionel Levine

Polynomial recurrences and cyclic resultants, arXiv:math/0411414v4,
7 November 2006; Proceedings of the AMS.
https://arxiv.org/pdf/math/0411414
https://arxiv.org/abs/math/0411414

The introduction, Theorem 1.1 and Conjecture 1.2 distinguish sufficient initial
segments from the short-sequence conjecture. The generic monic result has 2^(d+1) initial resultants; the generic monic
palindromic even-degree case has 2*3^(d/2). Their short-initial-segment conjecture
is not a proved optimal query theorem for q-reciprocal integer Weil polynomials.
A polynomial recurrence of short length is not automatically an effective
worst-case reconstruction with that many observations.

## 4. Christopher J. Hillar

Cyclic Resultants, Journal of Symbolic Computation 39 (2005), 653-669;
arXiv:math/0401220v3, 28 April 2005.
https://arxiv.org/pdf/math/0401220
https://www.sciencedirect.com/science/article/pii/S0747717105000374

The introduction and Theorem 1.1 characterize identical full nonzero
cyclic-resultant sequences. This differs from finite selected-data reconstruction.

## 5. Diptajit Roy, Nitin Saxena and Madhavan Venkatesh

Complexity of counting points on curves and the factor P_1(T) of the zeta function
of surfaces, arXiv:2511.02262v1, 4 November 2025.
https://arxiv.org/html/2511.02262v1
https://arxiv.org/abs/2511.02262

Lemma 2.10 assumes the consecutive max(18,2g) counts; Lemma 2.11 treats base-field
descent. These give later applications of the consecutive count bound.

## Exact verification

The source implements exact rational range reduction and
Mobius/Newton/endpoint reconstruction. All source and expected report bytes are
pinned in MANIFEST.json. Seven test polynomials are constructed from specified
quadratic factors and factors 1+q^a*T^(2a); they have the required Weil/reciprocity
properties but are not claimed to be Jacobians. Only q,g and requested K-values
are passed to the decoder. A separate companion-matrix determinant routine checks
36 small factor-generated orders.
