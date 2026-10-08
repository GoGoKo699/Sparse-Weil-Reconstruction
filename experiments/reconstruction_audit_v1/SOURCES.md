# Proof audit sources and numerical provenance

This internal audit uses a fresh derivation and a count calculation implemented
separately from the fixture generator. Consolidated source coverage, including
Stewart's results, appears in the [primary-source record](../../research/contribution_assessment_v1/SOURCES.md)
and [background source record](../../research/manuscript_background_v1/SOURCE_RECORD.md).

## Directly compared primary statements

1. K. S. Kedlaya, *Quantum computation of zeta functions of curves*,
   Computational Complexity 15 (2006), 1-19;
   https://arxiv.org/pdf/math/0411623 , v3.
   Sections 8-9 supply the normalized Mobius formula,
   Newton residue information, cutoff convention, and the fewer-than-2g
   question. The conditional cardinality-acquisition interface in Sections 6-8
   remains separate from reconstruction.
   The audited result changes the selected-data support and proves its
   sufficiency; it does not claim the underlying framework or quantum theorem.

2. A. V. Sutherland, *A Generic Approach to Searching for Jacobians*,
   Mathematics of Computation 78 (2009), 485-507;
   https://arxiv.org/pdf/0708.3168 .
   Section 4.1, Lemma 4 supplies the endpoint formulas in genus at most three.

3. C. J. Hillar and L. Levine, *Polynomial recurrences and cyclic resultants*,
   arXiv:math/0411414v4 (2006; Proceedings of the AMS);
   https://arxiv.org/pdf/math/0411414 , v4.
   The introduction, Theorems 1.1 and 1.4, Conjecture 1.2, and Section 4 provide
   generic initial-segment bounds and polynomial recurrences. The sufficient
   bounds are exponential in degree. The short polynomial recurrence may depend
   on unknown coefficients and is not by itself a uniform efficient decoder.
   The first-sequence conjecture and the q-reciprocal integral promise in
   Note 28 are different problems.

4. C. J. Hillar, *Cyclic Resultants*, Journal of Symbolic Computation 39
   (2005), 653-669; https://arxiv.org/pdf/math/0401220 .
   The introduction and Theorem 1.1 concern uniqueness from the full nonzero
   resultant sequence, rather than a finite sparse-data algorithm.

5. D. Roy, N. Saxena, M. Venkatesh, *Complexity of counting points on curves,
   and the factor P_1(T) of the zeta function of surfaces*,
   https://arxiv.org/html/2511.02262v1 (2025 preprint).
   Lemma 2.10 uses counts at every index through max(18,2g); Lemma 2.11 treats descent
   from larger fields. These provide later applications of the consecutive
   count bound.

## Numerical provenance

The tridiagonal fixture was selected with Python's deterministic seed 280029,
from diagonal entries in {-1,0,1}; candidate index 9 is recorded. Selection
required rigorous spectral bounds and a modular irreducibility check, not a
favorable runtime. SymPy 1.14.0 first generated the selected polynomial and
45 integer resultants. Their fingerprint is retained in CONTROL.json.
The default audit independently verifies all required algebra and calculates
the same integers by a standard-library circulant/Bareiss route. This is a
supplied-polynomial control; Jacobian realization is not assumed.

The decoder dependency is pinned by both SHA256 and Git-blob identity in the
manifest. The verifier reproduces the exact expected report from that dependency
and the recorded control.
