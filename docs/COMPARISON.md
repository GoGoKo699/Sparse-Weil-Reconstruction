# From Chidambaram–Keller to the quadratic threshold

[← Reconstruction](RECONSTRUCTION.md) · [Reading guide](READING_GUIDE.md) · [Sources →](SOURCES.md)

Galbraith is the primary teaching anchor: it supplies the language of curves,
Jacobians, Frobenius polynomials, and exact computation. Chidambaram–Keller is
the secondary anchor: it brings that language to the same first-$`g`$
reconstruction question studied here.

> **The progression:** the same input problem, a different recovery argument,
> and a quadratic sufficient field-size threshold.

## The common problem

Use this repository's convention

```math
\begin{aligned}
P(T)&=\prod_{i=1}^{2g}(1-\alpha_iT)
     =\sum_{j=0}^{2g}c_jT^j,\\
K_m&=\prod_{i=1}^{2g}(1-\alpha_i^m).
\end{aligned}
```

The promises are integer coefficients, $`c_0=1`$, inverse-root modulus
$`|\alpha_i|=\sqrt q`$, and reciprocity
$`c_{2g-j}=q^{g-j}c_j`$. The first-$`g`$ input consists of $`q`$, $`g`$, and the true
exact integers $`K_1,\ldots,K_g`$. The desired output is $`P`$.

For an abelian variety over $`\mathbb F_q`$, these inputs are extension-field
group cardinalities. For a Jacobian, they count divisor classes rather than
points on the curve. Ordinary curve point counts give power sums directly;
the group cardinalities instead package them into products. This distinction
is the starting point of the [tutorial](TUTORIAL.md).

## The matched first-g guarantees

Chidambaram–Keller establish first-$`g`$ recovery and polynomial bit
time. Their [arXiv v2 paper](https://arxiv.org/pdf/2606.28989v2), Theorem 1.1,
uses

```math
\begin{gathered}
q>Q(g),\\
Q(g)=\bigl(16g^3p(2g)\bigr)^{2g+2},
\end{gathered}
```

where $`p(n)`$ is the partition function. Remark 7.12 discusses the refinement
$`Q(g)=g^{O(g)}`$ and asks about a polynomial threshold.

| Feature | Chidambaram–Keller | Here |
|---|---|---|
| Supplied values | $`K_1,\ldots,K_g`$ | $`K_1,\ldots,K_g`$ |
| Recovered object | Frobenius polynomial | Frobenius polynomial |
| Sufficient field size | $`q>Q(g)`$ above | $`q\ge65{,}536g^2`$ |
| Coordinates | Inverse-root power sums | Weighted coefficients |
| Error control | Möbius inversion; induction | Coefficient fixed point |
| Bit time | $`\widetilde O(g^4\log q)`$ (§6) | Polynomial in $`g`$, $`\log q`$ |

Chidambaram–Keller use Möbius inversion in the small range and induction in
the large range. The local fixed point corrects the weighted polynomial
coefficients simultaneously.

Both algorithms have polynomial bit complexity; the new guarantee concerns
field size. Both displayed thresholds are sufficient; smaller
fields can admit recovery, and $`g`$ values need not be minimal. In particular,
for $`g=1`$, recovery is elementary for every $`q`$.

## Why the coefficient argument gives a quadratic scale

The [local proof](../research/first_g_reconstruction_v1/THEOREM.md) starts
by rescaling $`P`$ to $`F(z)=P(z/\sqrt q)`$. Its coefficients are palindromic,
so the first $`g`$ coefficients determine the rest. Weighted by
$`r=1/(8g)`$, every promised polynomial lies in a small coefficient ball.

Taking logarithms turns each supplied product into a leading term plus
higher-multiple terms. The latter are called aliases: the measurement at
index $`n`$ also contains contributions from $`2n,3n,\ldots`$. A candidate
coefficient vector predicts those aliases. Subtract its prediction from the
observed logarithms, exponentiate through degree $`g`$, and obtain an updated
vector.

This update corrects all $`g`$ coefficients together. Its controlling ratio is

```math
\kappa=\frac{8g}{\sqrt q}\le\frac1{32}.
```

The alias operator then has norm at most $`1/31`$, and the complete update has
Lipschitz constant below $`1/6`$ on an invariant ball. The promised polynomial
is a fixed point there. Iteration therefore recovers it, and two promised
polynomials with the same data must coincide. The condition on $`\kappa`$ is
exactly the displayed quadratic field-size condition.

The distinction is the choice of coordinates and error budget.
Chidambaram–Keller also use contraction estimates within their power-sum
induction; here the decisive estimate controls a whole coefficient vector
in one norm. Sections 2–5 of the local proof establish that estimate.
Sections 6–9 then turn the analytic iteration into a finite rational
algorithm: certified logarithms, truncated series, controlled denominators,
and final integer rounding. The implementation never needs exact arithmetic
in $`\sqrt q`$.

## The complementary all-field result

The second theorem addresses a different choice: allow more selected inputs
and remove the large-field condition. For every integer $`q\ge2`$ and $`g\ge32`$,
put $`h=g-2`$ and supply

```math
D_h=\{1,\ldots,h\}\cup\{2,4,\ldots,2h\}.
```

This uses $`h+\lceil h/2\rceil<2g`$ values, with largest index $`2g-4`$.
These are selected indices, not a consecutive prefix of that length.

Its route follows Kedlaya's logarithm–Möbius–Newton framework, with a selected
support and uniform tail estimate, followed by endpoint completion with
earlier precedent. The [reconstruction guide](RECONSTRUCTION.md) explains
the mechanism; the [all-field reading edition](ALL_FIELD_PROOF.md)
contains the proof. It complements the first-$`g`$ theorem by trading more
supplied values for coverage of every field.

## Further reading

The [full predecessor comparison](../research/manuscript_background_v1/WEIL_RECONSTRUCTION.md)
and [contribution assessment](../research/contribution_assessment_v1/ASSESSMENT.md)
retain the other matched statements and search limits. The
[source guide](SOURCES.md) identifies the teaching editions and locators.
The [application note](../research/finite_field_application_v1/COROLLARIES.md)
states the geometric consequences: isogeny-class determination for abelian
varieties and curve-zeta reconstruction for promised Jacobians. Count
acquisition and authentication remain separate tasks.

---

[← Reconstruction](RECONSTRUCTION.md) · [Reading guide](READING_GUIDE.md) · [Sources →](SOURCES.md)
