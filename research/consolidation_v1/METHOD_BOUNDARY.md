# Why the norm argument has a quadratic scale

The [first-g proof](../first_g_reconstruction_v1/THEOREM.md) uses a single weighted
norm for the coefficient ball and the alias operator. The proposition below
shows why these two estimates require a quadratic field-size scale.

## Proposition: a limitation of the single-radius argument

Fix integers $`g\ge1`$, $`q\ge2`$, put $`p=q^{-1/2}`$, and let $`0\lt s\lt1`$.
For a radius $`r>0`$, use the weighted algebra

```math
\mathcal A_r=\left\{H(z)=\sum_{m\ge0}h_mz^m:
  \|H\|_r=\sum_{m\ge0}|h_m|r^m\lt \infty\right\}.
```

Suppose both conditions hold:

1. Every polynomial satisfying the theorem's algebraic promises (degree $`2g`$,
   $`c_0=1`$, integral coefficients, $`q`$-reciprocity, and inverse-root modulus
   $`\sqrt q`$), without imposing its field-size threshold, has normalization
   $`F(z)=P(z/\sqrt q)`$ satisfying $`\|F-1\|_r\le s`$.
2. The alias formula on polynomials extends to a bounded linear operator
   from $`\mathcal A_r`$ to its degree-$`1,\ldots,g`$ coefficient space, with the same weights:

```math
(AH)(z)=\sum_{n=1}^{g}\left(
  \sum_{k\ge2}h_{nk}p^{n(k-1)}\right)z^n.
```

Then

```math
q\ge\frac{g^2}{s^2}.
```

### Proof

Let $`t=\lceil\sqrt q\rceil`$. Since $`\sqrt q\le t\lt2\sqrt q`$, the inverse roots of
$`1-tT+qT^2`$ form a complex conjugate pair of modulus $`\sqrt q`$. Therefore

```math
P(T)=(1-tT+qT^2)^g
```

is integral, $`q`$-reciprocal, and in the polynomial class of condition 1.
Its normalized polynomial is

```math
F(z)=(1-az+z^2)^g,\qquad a=t/\sqrt q\ge1.
```

Its linear coefficient alone gives

```math
gr\le gar\le\|F-1\|_r\le s,
\qquad\text{hence }r\le s/g.
```

For $`m\ge2`$, take the polynomial $`H_m(z)=z^m/r^m`$, which has norm one.
The output coefficient at $`n=1`$ implies

```math
\|AH_m\|_r\ge(p/r)^{m-1}.
```

If $`p>r`$, these norms are unbounded as $`m`$ grows. Thus a bounded extension
requires $`p\le r`$. Combining this with $`r\le s/g`$ gives the claimed inequality.

At the endpoint $`p=r`$, the alias norm is exactly $`g`$: any coefficient contributes
at most once to each of the $`g`$ outputs, and the monomial of degree
$`2\mathrm{lcm}(1,\ldots,g)`$ attains all $`g`$ contributions. Boundedness alone is therefore
much weaker than the small operator norm used in the contraction proof.

## Consequence and precise limits

Uniformly keeping all true polynomials in a small ball around 1 forces a
radius of order at most $`1/g`$. A bounded whole-algebra alias estimate forces
the sampling radius $`1/\sqrt q`$ to be no larger. Thus changing numerical
constants while retaining these two requirements cannot yield a subquadratic
field-size condition as $`g`$ varies.

This necessity statement applies to the two norm requirements above. It does
not establish an optimal field-size threshold for reconstruction: the test
monomials used to prove unboundedness need not be logarithms of candidate
polynomials.
