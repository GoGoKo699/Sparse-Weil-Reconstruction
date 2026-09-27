# Primary-source record

Inspected 27 September 2026. Scope: finite supplied-count reconstruction,
not acquisition of the counts. The sources below were opened as primary texts;
search snippets alone were not used to decide theorem scope. This extends the
preserved historical source lists without altering them.

## Matched reconstruction statements

- **[K06]** Kiran S. Kedlaya, *Quantum computation of zeta functions of curves*,
  Computational Complexity 15 (2006), 1–19.
  [arXiv:math/0411623v3](https://arxiv.org/pdf/math/0411623v3).
  Sections 8–9, PDF pp. 11–14: logarithmic/Möbius reconstruction, Newton residue
  information, analytic error, acquisition restrictions, two-prime descent, and
  the fewer-than-$2g$ question. The distinction between acquiring and decoding
  small-field counts is explicit in the original argument.

- **[CK26]** Shiva Chidambaram and Timo Keller, *Point counts of abelian varieties
  over finite fields determining their zeta function*.
  [arXiv:2606.28989v2](https://arxiv.org/pdf/2606.28989v2), 14 July 2026,
  17 pages; manuscript date 15 July. Read Theorem 1.1, Sections 3–6, and the
  relevant Section 7 discussion, especially Remark 7.12. Theorem 1.1 is stated
  for abelian varieties. Extending the reconstruction argument to the analogous
  abstract integral paired-root Weil class is an inference from its algebraic
  hypotheses, not a separately stated theorem. No domain advantage should be
  inferred merely from that difference in presentation.

  The [author research page](https://people.math.wisc.edu/~chidambaram3/research.html)
  and [author repository](https://github.com/TimoKellerMath/PointCountsAbelianVarieties)
  corroborate the identity. An [author-hosted PDF](https://people.math.wisc.edu/~chidambaram3/papers/PointCountsOnAbVars_ZetaFunction.pdf)
  is an older, 15-page text dated 29 June. Its different pagination and absent
  complexity paragraph must not be used to characterize v2. No author code was
  imported, executed, or formally checked.

- **[S09]** Andrew V. Sutherland, *A Generic Approach to Searching for Jacobians*,
  Mathematics of Computation 78 (2009), 485–507.
  [Primary PDF](https://arxiv.org/pdf/0708.3168).
  Section 4.1, Lemma 4, PDF p. 11 and surrounding endpoint discussion.

- **[RSV25]** Diptajit Roy, Nitin Saxena and Madhavan Venkatesh, *Complexity of
  counting points on curves, and the factor P_1(T) of the zeta function of surfaces*.
  [arXiv:2511.02262v1](https://arxiv.org/html/2511.02262v1), 4 November 2025.
  Lemmas 2.10–2.11 and their use in certification. The preprint's consecutive
  reconstruction lemma is attributed there to Kedlaya.

## Generic and infinite-sequence results

- **[HL07]** Christopher J. Hillar and Lionel Levine, *Polynomial recurrences
  and cyclic resultants*, Proceedings of the AMS 135 (2007), 1607–1618.
  [arXiv:math/0411414v4](https://arxiv.org/pdf/math/0411414v4).
  Theorems 1.1 and 1.4, Conjectures 1.2–1.3, and Section 4. The final discussion
  in Section 4 explicitly distinguishes a short polynomial-dependent recurrence
  from a universal recurrence.

- **[B08]** Jean-Paul Bézivin, *Résultants cycliques et polynômes cyclotomiques*,
  Acta Arithmetica 131.2 (2008), 171–181; DOI 10.4064/aa131-2-4.
  [Publisher PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/83965).
  Introduction, Théorème 1.3 and its following qualification, p. 172;
  Proposition 2.1. The theorem's Zariski-open domain is not explicitly
  determined by its proof. Do not replace that domain with all Weil polynomials
  or with every polynomial satisfying Hillar's named genericity conditions.

- **[H05]** Christopher J. Hillar, *Cyclic Resultants*, Journal of Symbolic
  Computation 39 (2005), 653–669.
  [arXiv:math/0401220](https://arxiv.org/pdf/math/0401220).
  Theorem 1.1 and Corollaries 1.4, 1.7 and 1.12, read together with the
  [author's erratum](https://qualiaphile.com/files/hillarcyclicerrata.pdf),
  DOI 10.1016/j.jsc.2005.05.001. The erratum corrects a missing parity case
  involving zero-root multiplicities and states that other results are
  unaffected. Here both constant terms are nonzero, so those multiplicities
  vanish. Fried's older theorem is encountered through these accounts, not
  claimed as a newly inspected original paper.

## Resolved adjacent leads

- **[St12]** C. L. Stewart, *Exceptional units and cyclic resultants*,
  Acta Arithmetica 155.4 (2012), 407–418; DOI 10.4064/aa155-4-5.
  [Author-hosted complete PDF](https://uwaterloo.ca/pure-mathematics/sites/default/files/uploads/documents/aa155-4-05.pdf).
  Theorems 1–2 and Section 2, especially Corollary 2, pp. 409–410. That
  corollary controls equal absolute values within one polynomial's sequence.
  It does not control equality between two arbitrary resultant sequences.

- **[St13]** C. L. Stewart, *Exceptional units and cyclic resultants, II*.
  Contemporary Mathematics 587 (2013), 191–200; DOI 10.1090/conm/587/11698.
  [Author-hosted complete PDF](https://uwaterloo.ca/pure-mathematics/sites/default/files/uploads/documents/exceptional_units-5_0.pdf).
  Theorems 1.1–1.3 and the introductory scope were checked. No reconstruction
  algorithm or matching sparse-data theorem is stated in those results.

## Search record and limits

The work order's Chidambaram–Keller lead is resolved, not left as an unsupported
bibliographic assertion. Focused author/title searches found the exact arXiv
identifier and author materials after a broader engine query returned unrelated
results. Several arXiv abstract/HTML opens initially failed; the primary PDF
subsequently opened successfully. The current PDF version, not a search result's
version/date snippet, determines the comparison.

Other queries combined “Weil polynomial”, “Jacobian”, “cardinalities”,
“reconstruction”, “cyclic resultants”, “Kedlaya”, and “fewer”, followed by exact
author/title searches for Stewart and Bézivin. Stewart's bibliography led to
Bézivin; the Hillar citation trail exposed the erratum. Author-hosted and
publisher PDFs resolved both of those primary-text gaps. References discovered
in secondary search results were used only as leads.

This is not an exhaustive thesis, software, or citation-graph search. A recent
conference-slide search hit was not used as independent theorem evidence.
The bibliographic lead Bézivin, *Sur les résultants cycliques* (2007), DOI
10.3792/pjaa.83.157, was identified, but primary full-text access failed at
J-STAGE and Project Euclid; that paper is not marked fully inspected.
No unpublished argument is excluded. No author was contacted. “Not subsumed
by the inspected statements” is the supported conclusion; “first ever” is not.

A final focused search for first-$g$ recovery with polynomial/quadratic field
thresholds and contraction methods found no additional primary theorem with
that guarantee. The arXiv metadata still listed CK26 v2 as current when checked.
This bounded check also does not establish priority for the companion theorem.

The citations are for reconstruction scope and comparison. They do not certify
every proof or implementation in the cited papers. No source text or third-party
code is copied into this repository.
