# Focused source recheck

Inspected 27 September 2026. This successor record supplements the broader
[source comparison](../contribution_assessment_v1/SOURCES.md). It separates
fresh primary-text inspection from a bounded search for competing results.

## Current first-g predecessor

[Chidambaram–Keller, arXiv:2606.28989](https://arxiv.org/abs/2606.28989)
still lists v2, 14 July 2026, as current. The
[canonical PDF](https://arxiv.org/pdf/2606.28989) has 17 pages.
Theorem 1.1 gives first-g recovery above
`Q(g)=(16g^3 p(2g))^(2g+2)`; Section 6 already states polynomial bit time.
Remark 7.12 discusses `g^{O(g)}` and leaves a polynomial threshold open.
The geometric statement's extension to our polynomial class is an inference
from its arithmetic hypotheses, not a separately stated theorem.

The root reviewer independently reopened the metadata, theorem, complexity
paragraph, and threshold discussion after the delegated source review.

## Nearby results reopened

| Primary text | Inspected statement | Comparison |
|---|---|---|
| [Hillar–Levine, current PDF](https://arxiv.org/pdf/math/0411414), v4 | Theorems 1.1 and 1.4; Section 4 | Generic finite-resultant bounds and short recurrences do not give uniform first-g Weil recovery. The short recurrence can depend on the unknown polynomial. |
| [Bézivin 2008, publisher PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/83965) | Théorème 1.3 and its qualification | The first d+1 bound holds on an existential Zariski-open set. This is a linear generic predecessor, not a guarantee for every Weil input. |

The other primary comparisons in the previous source record were not all
reread during this pass. They remain identified as earlier inspections.

## Actual search log

The focused search used these queries through the routine search engine:

1. `"2606.28989" polynomial threshold`
2. `"Weil polynomial" "reconstruction" "quadratic"`
3. `"cyclic resultants" "Weil" reconstruction polynomial`
4. `"Point counts of abelian varieties" reconstruction`
5. `"cyclic resultants" "polynomial" reconstruction Weil threshold`
6. `"Sur les résultants cycliques" Bézivin 2007 pdf`
7. `"cyclic resultants" "quadratic" reconstruction`
8. `"zeta function" "point counts" "threshold" Keller`
9. `"Weil polynomials" "first" "contraction"`
10. `"Chidambaram" "Keller" "quadratic" zeta`
11. `"first g" "Weil" polynomial reconstruction`
12. `"cyclic resultants" "Banach"`

A second engine, with a 120-day recency filter, checked:

13. `"point counts" "polynomial" "threshold" "Chidambaram"`
14. `"Weil" "reconstruction" "contraction" polynomial`
15. `"first g" "point counts" polynomial`

The searches returned the established predecessors and unrelated results;
no additional matched theorem emerged. The second-engine batch was mostly
unrelated and supplies no useful negative evidence. Search silence is not a
theorem about priority.

## Remaining access and coverage limits

Bézivin's 2007 *Sur les résultants cycliques*,
[DOI 10.3792/pjaa.83.157](https://doi.org/10.3792/pjaa.83.157), remains
uninspected in full. The attempted J-STAGE routes failed, and Project Euclid
presented an access barrier. This is a disclosed source gap, not a result
assumed to be irrelevant.

No exhaustive thesis or citation-graph search was performed. No unpublished
argument is excluded. No external author code or Lean proof was executed,
and no author was contacted. The supported finding is that none of the
inspected statements subsumes the quadratic-threshold guarantee. A universal
priority certificate is neither claimed nor treated as a finishable research task.
