# Weil reconstruction: the matched predecessors

Checked 28 September 2026. This is a source-backed comparison for eventual
writing, not a manuscript or a claim of universal priority. Bibliographic keys
below are stable identifiers for this background package. The polynomial
promises and the two repository theorems remain those in the
[README](../../README.md#the-polynomial-and-supplied-data).

## Compare the same input problem

The decoder receives $q$, $g$, and **true exact** values
$K_m=\prod_{i=1}^{2g}(1-\alpha_i^m)$. For an abelian variety these are group
cardinalities over extensions. For a curve's Jacobian they are not ordinary curve
point counts. It is useful to keep four questions separate: which indices
are supplied, whether they determine the polynomial, the bit cost of recovery,
and the cost or certification of obtaining the counts.

For the monic polynomial $\chi(X)=X^{2g}P(1/X)$, the usual cyclic resultant
is exactly $\operatorname{Res}(\chi,X^m-1)=K_m$: the sign disappears in even
degree. The geometric statements below concern prime-power $q$. The
repository's algebraic theorems allow any integer $q\ge2$ satisfying their
polynomial promises. Geometric versus polynomial phrasing alone is not an
established novelty distinction.

## Primary statements and their role

| Key and inspected location | Matched statement | Consequence for positioning |
|---|---|---|
| **Kedlaya2006**, [§8, arXiv PDF pp. 11–13; §9, pp. 13–14](https://arxiv.org/pdf/math/0411623) | Classical reconstruction from $K_1,\ldots,K_{\max(18,2g)}$ in polynomial time, using normalized logarithms, truncated Möbius inversion and Newton residue information. The supplied-count argument handles $q\ge2$. | The main algorithmic predecessor for the all-field theorem. Its separate quantum acquisition hypothesis is $16g<\sqrt q$; §8 expressly says this restriction enters through acquisition. |
| **Sutherland2009**, [§4.1, Lemma 4, arXiv PDF p. 11](https://arxiv.org/pdf/0708.3168) | For smooth projective geometrically irreducible curves of genus $g\le3$, $P(1),P(-1)$ determine $P$ for sufficiently large $q$. The proof gives the sufficient genus-three condition $q\ge40^2$. Genus two is exact endpoint algebra without a large-field restriction. | Endpoint recovery predates this project. Low-genus recovery and its group-operation costs do not imply a uniform varying-genus sparse schedule. |
| **ChidambaramKeller2026**, [Theorem 1.1, p. 2; §6, pp. 9–10; Remark 7.12, pp. 15–16](https://arxiv.org/pdf/2606.28989) | For a $g$-dimensional abelian variety, the first $g$ counts suffice when $q>Q(g)$, with $Q(g)=(16g^3p(2g))^{2g+2}$ and $p$ the partition function. Section 6 states $\widetilde O(g^4\log q)$ bit complexity. | First-$g$ recovery and polynomial bit time are already prior work. The comparison is the sufficient field-size threshold. |
| **RoySaxenaVenkatesh2025**, [Lemma 2.10](https://arxiv.org/html/2511.02262v1#S2.SS2) | Restates Kedlaya's supplied-count recovery from indices $1,\ldots,\max(18,2g)$ in $\operatorname{poly}(g\log q)$ time. | Useful explicit modern formulation; not a separate sparse-threshold competitor. Lemmas 2.8–2.9 concern an additional randomized certification protocol, absent from our promised-input decoder. |

The two repository regimes should be stated alongside these comparisons:

| Repository result | Sufficient regime | Supplied indices | Maximum index |
|---|---|---|---:|
| [First-$g$ theorem](../first_g_reconstruction_v1/THEOREM.md) | $g\ge1$, $q\ge65{,}536g^2$ | $1,\ldots,g$ | $g$ |
| [All-field theorem](../../exploration/phase_2/ORDINARY_QUERY_THEOREM_AUDIT_28.md) | $g\ge32$, $q\ge2$ | $D_{g-2}=\{1,\ldots,g-2\}\cup\{2,4,\ldots,2g-4\}$ | $2g-4$ |

Both repository decoders have deterministic polynomial bit complexity. No
matched running-time exponent improvement over Chidambaram–Keller is claimed.
The inequalities above deliberately retain their different strictness.

## Qualifications that matter in writing

**Version and threshold.** The [arXiv record](https://arxiv.org/abs/2606.28989)
confirms v2 (14 July 2026; PDF dated 15 July) as current. Remark 7.12 discusses
a $g^{O(g)}$ refinement and leaves a polynomial threshold open. These are
sufficient bounds. Transferring the geometric theorem to the abstract
paired-root class is an inference, not a separately stated theorem.

**Small dimension.** First-$g$ recovery is classical for $g=1$. Their
Proposition 7.4 reports that two counts suffice for dimension three and
prime-power $q\ge16$. The small-field part uses enumeration (Remark 7.5),
which was not rerun here. Thus $g$ counts are not always minimal.

**Endpoints.** The relation $K_2=P(1)P(-1)$ follows directly from the product
definition, so supplying $K_1,K_2$ supplies both endpoints. No twist oracle is
needed for this identity. In genus two our convention gives, by addition and
subtraction,

$$
c_1=\frac{P(1)-P(-1)}{2(q+1)},\qquad
c_2=\frac{P(1)+P(-1)}2-(1+q^2).
$$

These elementary identities are included to fix conventions, not as new
results. The all-field contribution is the selected-support and uniform-error
argument before endpoint completion.

**Base extension.** Kedlaya §8 also uses two suitable prime extension degrees
to descend from large fields. The resulting inputs have different indices.
Applying a large-field theorem after extension does not automatically supply
the transcript required by either repository decoder. Roy–Saxena–Venkatesh
Lemma 2.11 records the corresponding descent separately from reconstruction.

**Output.** Here polynomial-time recovery means writing the degree-$2g$
Frobenius polynomial. This compact datum determines the full abelian-variety
zeta function, whose expanded output can be exponentially large; see the
[application and output note](../finite_field_application_v1/COROLLARIES.md).
No certification protocol or count-acquisition algorithm is obtained merely
by reducing the number of supplied integers.

## What was checked

All four primary texts above were reopened for the cited statements, and
their arXiv metadata were checked. The Kedlaya journal metadata were checked
at [Springer](https://doi.org/10.1007/s00037-006-0204-7); the Sutherland journal
metadata and DOI were checked against his
[author publication list](https://math.mit.edu/~drew/index.html).
The arXiv Sutherland PDF is v2 (30 January 2008), preceding its 2009 journal
publication. Roy–Saxena–Venkatesh remains arXiv v1 (4 November 2025).

A fresh focused search used both search engines, including recent-result
queries, for first-$g$ recovery, polynomial/quadratic thresholds and cyclic
resultants. It found no additional matched primary theorem. Some broad
queries returned mostly unrelated material; this is weak negative evidence.
The Chidambaram–Keller author repository was inspected only as a source/version
lead; its code and formalization were not run. This pass is not a fresh full
proof audit of the predecessors.

Older inspections remain documented in
[the previous source record](../contribution_assessment_v1/SOURCES.md).
They should not be relabelled as fresh inspections by this note. The justified
position is a quadratic sufficient threshold and a complementary all-field
selected-data guarantee relative to the inspected statements. A complete
literature census, exclusion of unpublished work, and minimum-query theorem
are not established.
