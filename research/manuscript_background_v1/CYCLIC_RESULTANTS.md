# Cyclic-resultant background and comparison boundaries

Checked 28 September 2026. This is background for a future manuscript, not a
manuscript draft or a new reconstruction theorem. The current project promises
and quantitative guarantees remain those in the [README](../../README.md).

## 1. Match the invariant before comparing theorems

For a polynomial $f(X)=a\prod_{i=1}^{d}(X-\lambda_i)$, use the convention

$$
r_m(f)=\operatorname{Res}(f,X^m-1)
=a^m\prod_{i=1}^{d}(\lambda_i^m-1).
$$

This is the convention in [Hillar2005] and [HillarLevine2007]. Reversing the
arguments of a resultant can introduce $(-1)^{dm}$; changing every factor
to $1-\lambda_i^m$ introduces $(-1)^d$. For the project's monic polynomial

$$
\chi(X)=X^{2g}P(1/X)=\prod_{i=1}^{2g}(X-\alpha_i),
$$

the even degree makes $r_m(\chi)=K_m$ exactly. Comparisons below concern the
indexed sequence $(r_m)_{m\ge1}$, rather than an unordered collection of values.
Every $K_m$ is nonzero because $|\alpha_i|=\sqrt q>1$.

Three different questions must be separated:

| Question | What a positive answer establishes | What still needs proof |
|---|---|---|
| Full-sequence uniqueness | Equality at every positive index forces equal polynomials in the stated class | A finite sufficient index set |
| Finite determination | A specified finite transcript distinguishes the permitted polynomials | A uniform algorithm and a bit-complexity bound |
| Efficient reconstruction | An explicit algorithm recovers coefficients from the permitted transcript within a stated cost | Acquisition or authentication of that transcript, unless separately addressed |

An existential open-set theorem is also different from a theorem valid for every
integral reciprocal Weil polynomial. The repository's algorithms include
repeated-root inputs and require no genericity test.

## 2. What the primary results establish

**Hillar's classification.** [Hillar2005, Theorem 1.1], read with
[HillarErratum2005], describes equal full nonzero sequences through factor
reversal and possible powers of $X$. The correction restores a parity case for
zero-root multiplicities; the erratum states that the other results are
unaffected. Corollaries 1.4 and 1.12 treat reciprocal-polynomial uniqueness.
Section 5 also describes Gröbner-basis reconstruction, without the uniform
polynomial bit bound sought here.

A direct consequence: for monic polynomials with all roots strictly outside the
unit disk, no nonconstant factor can be reversed, as its roots would move inside
the disk. Nonzero constant terms exclude powers of $X$. Full-sequence uniqueness
for the project's class therefore follows without genericity. This is prior
background, not the present finite-data contribution.

Primary texts: [corrected arXiv version](https://arxiv.org/pdf/math/0401220)
and [one-page author erratum](https://qualiaphile.com/files/hillarcyclicerrata.pdf).

**Finite generic bounds and recurrences.** [HillarLevine2007, Theorem 1.1]
gives initial-segment bounds $2^{d+1}$ for generic monic degree-$d$ polynomials
and $2\cdot3^{d/2}$ in the generic monic reciprocal even-degree case.
Theorem 1.4 supplies polynomial relations on consecutive blocks of length
$d+1$, or $d/2+1$ in the reciprocal case. A polynomial relation is not itself
a single-valued update rule. Moreover, Section 4 explicitly notes that the
short relation's coefficients depend on the unknown polynomial, whereas its
longer determinant relation is universal. These statements do not provide
the project's uniform polynomial-bit-time decoder from its short transcript.

Primary text: [author-hosted paper](https://pi.math.cornell.edu/~levine/hillarlevineAMSrevised.pdf),
Theorems 1.1 and 1.4, Section 4.

**A linear generic bound was already known.** [Bezivin2008, Théorème 1.3]
proves that the first $d+1$ resultants distinguish two monic degree-$d$
polynomials when both root tuples belong to a suitable Zariski-open subset
$U\subset\mathbb C^d$ and neither has a root of unity of order at most $d+1$.
The paragraph immediately after the theorem says that the proof does not
explicitly determine $U$, or establish coverage of every polynomial satisfying
the paper's named genericity condition. This is a finite generic determination
result, not an all-Weil decoding theorem. Proposition 2.1 converts initial
cyclic resultants into cyclotomic-resultant data by divisor factorization;
that conversion does not remove the restriction to $U$.

Primary text: [publisher PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/83965),
printed p. 172. The predecessor landscape must include this result; describing
generic finite determination as having only exponential known bounds would be
incorrect.

## 3. Why reciprocal rescaling is not a transfer of the input data

The following calculations apply the repository's promises; they are not new
claims about the cited authors' results. With

$$
\widehat\chi(X)=q^{-g}\chi(\sqrt q\,X),
\qquad \beta_i=\alpha_i/\sqrt q,
$$

the polynomial $\widehat\chi$ is monic and ordinarily reciprocal. However,

$$
r_m(\widehat\chi)
=\prod_i(\beta_i^m-1)
=q^{-gm}\prod_i(\alpha_i^m-q^{m/2}),
$$

whereas the supplied $K_m$ is $\prod_i(\alpha_i^m-1)$. Normalization changes
the evaluation point inside every factor. It does not turn $K_m$ into the
ordinary cyclic resultants of $\widehat\chi$ by a known scalar multiplication.
Normalized roots can also be roots of unity: for
$\chi(X)=(X^2+q)^g$, the normalized polynomial is $(X^2+1)^g$, so its fourth
cyclic resultant vanishes even though the original $K_4$ does not.

The generic monic conditions require separate care before normalization too.
In the distinct-subset-product setting discussed by Hillar–Levine and Bézivin,
different subsets of roots must have different products. For $g\ge2$, the
Weil pairing supplies two disjoint root pairs with product $q$, violating that
condition. The generic reciprocal class is a different parameter space; its
results cannot be imported by ignoring the preceding change in supplied data.

Consequently, the manuscript should compare the uniform finite-field results
directly with Kedlaya and Chidambaram–Keller, while using the general literature
to explain the history and distinctions above. The present first-$g$ guarantee
does not establish the general reciprocal-polynomial conjecture.

## 4. Historical and adjacent sources: appropriate citation roles

| Source | Verified role | Citation limit |
|---|---|---|
| [Fried1988], *Cyclic resultants of reciprocal polynomials*, LNM 1345, pp. 124–128 | Historical reciprocal uniqueness result; bibliographic record verified on the [publisher page](https://doi.org/10.1007/BFb0081399) | Original full text was not obtained. For the theorem statement used here, cite the inspected restatement [Hillar2005, Corollary 1.4], explicitly credited there to Fried. The publisher's later electronic date is not the original publication year. |
| [Bezivin2007], *Sur les Résultants cycliques*, 83(8), pp. 157–160 | Bibliographic lead for an alternative treatment of the full-sequence classification | Primary full text remains inaccessible in this check. Do not cite an uninspected theorem number or treat it as an inspected finite reconstruction result. |
| [Stewart2012], Section 2, Corollary 2 | Bounds the length of a constant-absolute-value initial run within one monic integer polynomial's cyclic-resultant sequence | This is not a bound on agreement between two arbitrary sequences. It cannot be substituted for a finite reconstruction theorem. |
| [Stewart2013], Theorems 1.1–1.3 | Estimates cyclotomic norms and exceptional-unit runs | These inspected statements concern growth and units, not the finite supplied-count decoding problem. |

The Stewart primary texts are available from the author:
[2012 PDF](https://uwaterloo.ca/pure-mathematics/sites/default/files/uploads/documents/aa155-4-05.pdf)
and [2013 PDF](https://uwaterloo.ca/pure-mathematics/sites/default/files/uploads/documents/exceptional_units-5_0.pdf).
They are useful for closing misleading citation leads, rather than mandatory
ingredients of the reconstruction proof.

## 5. Search and access limits

This pass reopened the relevant Hillar, Hillar–Levine, Bézivin 2008, and Stewart
primary statements. It followed their bibliography to the Fried publisher
record and retried the Bézivin 2007 DOI, J-STAGE article/PDF paths, and Project
Euclid article/PDF paths. The latter returned errors or an unavailable-page
wrapper, including on direct public PDF retrieval. No access restriction was
bypassed, and no original Bézivin 2007 proof is represented as read. The decisive
full-sequence classification is independently available in Hillar's corrected
text and erratum, so this access gap does not leave that mathematical background
unsupported.

Exact-title and bounded newer searches combined cyclic resultants with
reconstruction, Weil, generic determination, and the cited authors. A newer
primary lead, Yoshizaki's [arXiv:2503.06194v1](https://arxiv.org/html/2503.06194v1),
was screened at its abstract, introduction, and main-statement level: its
Theorems 3.2 and 4.4 concern $p$-adic convergence and covering-space invariants,
not a competing finite Weil reconstruction statement. No additional matching
theorem emerged from this bounded cyclic-resultant search. That conclusion is
not an exhaustive citation-graph, thesis, software, or unpublished-priority
claim. None of the source proofs was formally verified, and no author code was
run in this pass.
