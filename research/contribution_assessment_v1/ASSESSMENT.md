# Sampling schedules and prior reconstruction results

The two reconstruction guarantees differ in their supplied indices and
field-size regimes. This comparison relates them to earlier cyclic-resultant
methods and quantifies the size of the selected input transcript.
Source versions and inspected passages are listed in [SOURCES.md](SOURCES.md).

## 1. The comparison problem

Use the [README's exact polynomial promises](../../README.md#the-polynomial-and-supplied-data).
For the monic polynomial

```math
\chi(X)=X^{2g}P(1/X)=\prod_{i=1}^{2g}(X-\alpha_i),
```

the ordinary cyclic resultant is

```math
\mathrm{Res}(\chi,X^m-1)
=\prod_i(\alpha_i^m-1)=K_m.
```

The sign agrees because the degree is even. Thus the input is the same scalar
invariant used in the cited reconstruction literature. For a Jacobian it is
an abelian-variety point count, not a curve point count.

Compare the number of supplied integers, their indices, the allowed polynomial
class, and the decoder's bit complexity separately. Neither a curve equation
nor a factorization is supplied. Acquisition and authentication of counts are
outside this comparison.

## 2. The primary statements

Reference identifiers below link to the version and inspection record in
[SOURCES.md](SOURCES.md). Here $`d`$ denotes general polynomial degree; our case
has $`d=2g`$. “Does not imply” concerns the specified statement or construction,
not every possible adaptation of the paper.

| Source and location | Proven input/output guarantee | Relation to this project |
|---|---|---|
| [K06], Sections 8–9, PDF pp. 11–14 | Consecutive counts through $`\max(18,2g)`$; polynomial-time reconstruction via normalized Möbius inversion and Newton rounding | Principal algorithmic predecessor. Its analytic supplied-count argument works for small $`q`$ too; acquisition has separate restrictions. The selected support in Note 28 needs a new sufficiency argument. |
| [CK26], Theorem 1.1 and Section 6, PDF pp. 2, 9–10 | First $`g`$ counts for $`q>Q(g)`$; constructive recovery with an explicit polynomial bit-complexity statement | Uses fewer counts in its large-field regime. It does not give the all-field selected-data guarantee. |
| [S09], Section 4.1, Lemma 4, PDF p. 11 | $`P(1),P(-1)`$ determine the polynomial for $`g\le3`$ and sufficiently large $`q`$; exact endpoint algebra in genus two | Endpoint recovery is prior machinery. This is not a uniform varying-genus sparse schedule. |
| [HL07], Theorems 1.1, 1.4 and Section 4 | Generic initial-segment bounds $`2^{d+1}`$, or $`2\cdot3^{d/2}`$ for monic reciprocal polynomials; also short polynomial recurrences | Generic sufficient bounds and recurrences are different from a uniform Weil decoder. A recurrence depending on the unknown polynomial is not an input-free recovery algorithm. |
| [B08], Théorème 1.3, p. 172 | First $`d+1`$ resultants distinguish monic polynomials whose root tuples lie in a specified existential Zariski-open set, excluding the stated roots of unity | A linear generic bound was already known. Its open set is not explicitly determined. It neither covers every Weil input nor supplies the required uniform algorithm. |
| [H05] and its erratum, Theorem 1.1 and corollaries | Characterization of equal full nonzero resultant sequences; corresponding uniqueness consequences | Full-sequence uniqueness does not give the finite selected-data decoder. The erratum's missing parity case is irrelevant when the compared polynomials have nonzero constant terms. |
| [RSV25], Lemma 2.10 | Restates the consecutive $`\max(18,2g)`$ supplied-count polynomial-time theorem | A useful modern formulation of the comparator, not evidence of our priority. |
| [St12], Section 2, Corollary 2; [St13], Theorems 1.1–1.3 | Bounds on constant absolute cyclic-resultant runs, cyclotomic norms, and exceptional units | These are not equal-transcript bounds for two arbitrary polynomials and do not supply a reconstruction competitor. |

Bézivin supplies a linear generic bound, and Chidambaram–Keller supply efficient
first-$`g`$ recovery for sufficiently large fields.

## 3. The selected-support refinement

The new part is the support-and-error lemma. With $`h=g-2`$, the cutoff

```math
k_n=\max\bigl(2,\lfloor h/n\rfloor\bigr)
```

keeps every required logarithm inside
$`D_h=\{1,\ldots,h\}\cup\{2,4,\ldots,2h\}`$, while its normalized analytic
error remains below $`1/3`$ for every $`q\ge2`$, $`g\ge32`$.
This permits exact coefficient rounding. The existing endpoint equations then
recover the last two independent coefficients.

This is not obtained by calling the consecutive-data theorem with missing
inputs. Its proof does, however, closely adapt the prior method. Möbius
cancellation, the use of Newton residue information, logarithmic reconstruction,
and endpoint evaluation should not be described as discoveries of this project.
Without endpoint completion, a similar schedule through $`g`$ already suggests
the same leading $`3g/2`$ query scale; endpoints provide an additive improvement.

It also gives a separation statement: two distinct polynomials in that promised
class differ at some index in $`D_h`$. This is a corollary of the decoder, not a
separate novelty claim or a lower bound on necessary observations.

## 4. The large-field comparison

[CK26, Theorem 1.1] permits

```math
Q(g)=\bigl(16g^3p(2g)\bigr)^{2g+2},
```

where $`p`$ is the partition function, and assumes $`q>Q(g)`$. Section 6 states
$`\widetilde O(g^4\log q)`$ bit complexity. Remark 7.12 discusses improvements
to this sufficient threshold and leaves a polynomial-in-$`g`$ threshold open.
The current version is v2, 14 July 2026; an older author-hosted PDF omits the
explicit complexity paragraph. The current version controls this comparison.

The proven schedules occupy different regimes:

| Supplied-data theorem | Field/genus regime | Number of counts | Largest index |
|---|---|---:|---:|
| Consecutive reconstruction [K06], [RSV25] | Every $`q\ge2`$; use $`g\ge32`$ for this comparison | $`2g`$ | $`2g`$ |
| Note 28 | Every $`q\ge2`$, $`g\ge32`$ | $`g-2+\lceil(g-2)/2\rceil`$ | $`2g-4`$ |
| First-$`g`$ reconstruction [CK26] | $`q>Q(g)`$ | $`g`$ | $`g`$ |

These schedules are not nested. For $`g\ge32`$, $`D_{g-2}`$ contains every index
through $`g`$ except the largest odd index at most $`g`$, namely
$`2\lceil g/2\rceil-1`$. It compensates with selected even indices above $`g`$.
Thus neither decoder can simply be run on the other's full supplied transcript
without checking its missing inputs. This observation does not alter the fact
that the first-$`g`$ schedule has the smaller query count where its hypotheses hold.

Applying a large-field theorem after base extension is not a free resolution
of the small-field problem. It gives the polynomial with inverse roots
$`\alpha_i^a`$, and obtains counts at indices $`a,2a,\ldots,ga`$. Recovering the
original roots requires justified descent and additional data. For example,
the two-prime descent in [K06, Section 8] uses distinct primes $`a,b>2g`$ with
additional arithmetic conditions. Two first-$`g`$ schedules then use $`2g`$
distinct indices: $`ia=jb`$ with $`1\le i,j\le g`$ is impossible. This particular
composition does not imply our sparse schedule; no impossibility result for
other descent methods follows.

## 5. Quantitative meaning and limits

Write $`r=\lceil h/2\rceil`$. The exact degree-weight sum is

```math
\sum_{m\in D_h}m=h(h+1)+r^2.
```

This follows by splitting $`D_h`$ into all even indices through $`2h`$ and the odd
indices through $`h`$. The two sums are $`h(h+1)`$ and $`r^2`$.

| Genus | Schedule | Count | Largest index | Sum of indices |
|---:|---|---:|---:|---:|
| 32 | Consecutive through $`2g`$ | 64 | 64 | 2080 |
| 32 | Note 28 | 45 | 60 | 1155 |
| 32 | First $`g`$, where applicable | 32 | 32 | 528 |
| 64 | Consecutive through $`2g`$ | 128 | 128 | 8256 |
| 64 | Note 28 | 93 | 124 | 4867 |
| 64 | First $`g`$, where applicable | 64 | 64 | 2080 |

Relative to the consecutive all-field schedule, the count ratio tends to $`3/4`$
and the index-sum ratio to $`5/8`$. The largest-index ratio tends to one. Since
$`K_m`$ has $`O(gm\log q+g)`$ bits, both full transcripts retain an
$`O(g^3\log q)`$ bit envelope. These are supplied-data comparisons, not measured
runtime or count-acquisition speedups. They do not change a complexity exponent.

The general reciprocal-polynomial theorems also cannot be transferred by a
silent rescaling. Dividing each $`\alpha_i`$ by $`\sqrt q`$ gives roots paired by
inversion, but its ordinary cyclic resultants differ from $`K_m`$: rescaling
changes the radius at which the resultant factors are evaluated. Moreover,
genericity does not cover repeated roots or every point of the Weil class.

No dimension-counting argument establishes that $`g`$ integer observations are
necessary. Integer answers have varying bit lengths. Selected indices and an
initial consecutive segment are different optimization problems.

## 6. The quadratic-threshold theorem

The [first-$`g`$ proof](../first_g_reconstruction_v1/THEOREM.md) establishes the
sufficient condition $`q\ge65{,}536g^2`$ for the promised polynomial class. It uses
a weighted coefficient norm, a uniformly invariant domain, and an explicit
finite-precision contraction algorithm. Intermediate iterates need not be Weil
polynomials; the domain estimates cover them.

This changes the growth of the sufficient field-size threshold while retaining
$`g`$ supplied counts and polynomial bit time. It addresses the polynomial-threshold
question in [CK26, Remark 7.12]. A sufficient contraction bound failing is not
nonuniqueness. The [norm-method boundary](../consolidation_v1/METHOD_BOUNDARY.md)
identifies which estimates impose the quadratic scale.
