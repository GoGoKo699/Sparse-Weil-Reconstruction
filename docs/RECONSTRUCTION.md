# From group cardinalities to polynomial coefficients

[← Foundations](TUTORIAL.md) · [Reading guide](READING_GUIDE.md) · [Comparison →](COMPARISON.md)

Galbraith gives us the objects: a Weil polynomial, its power sums, and the
cardinalities they describe. The next question is algorithmic: **how can a few
supplied group cardinalities recover every coefficient?** This page develops
the bridge to the repository's two reconstruction guarantees. The main route
uses the first $`g`$ cardinalities; the final section explains the complementary
all-field route.

Throughout, $`P(T)=\sum_{j=0}^{2g}c_jT^j=\prod_i(1-\alpha_iT)`$ has integral
coefficients, $`c_0=1`$, inverse roots of modulus $`\sqrt q`$, and reciprocity
$`c_{2g-j}=q^{g-j}c_j`$. The supplied integers $`K_m=\prod_i(1-\alpha_i^m)`$
are the true exact values. The algebraic statements allow integers $`q\ge2`$;
the geometric interpretation requires a finite field.

## 1. The information inside one cardinality

Write $`S_m=\sum_i\alpha_i^m`$. Ordinary curve point counts give this power
sum directly:

```math
N_m=q^m+1-S_m.
```

Once $`S_1,\ldots,S_g`$ are known, Newton identities give $`c_1,\ldots,c_g`$,
and reciprocity supplies the rest. Group cardinalities $`K_m`$, including
Jacobian cardinalities, contain the power sums in a different form.

Reciprocity pairs the inverse roots as $`\alpha`$ and $`q/\alpha`$, so

```math
\frac{K_n}{q^{gn}}
=\prod_i\left(1-\frac{\alpha_i^n}{q^n}\right).
```

Take the real logarithm and expand $`-\log(1-x)=\sum_{k\ge1}x^k/k`$:

```math
\begin{aligned}
L_n:=\log\frac{q^{gn}}{K_n}
&=\sum_{k\ge1}\frac{S_{nk}}{kq^{nk}}\\
&=\frac{S_n}{q^n}+\frac{S_{2n}}{2q^{2n}}+\cdots.
\end{aligned}
```

The series converges absolutely because $`|\alpha_i/q|=q^{-1/2}<1`$.
The paired factors make the product positive; the real logarithm is unambiguous.
For comparison with the full proofs, their quantity named $`L_n`$ is
$`\log(K_n/q^{gn})`$, the negative of the convention on this page.

> **One supplied logarithm mixes a desired power sum with power sums at all
> its multiples.**

Simply discarding those extra terms need not give sufficient
accuracy for integer recovery. The two methods below control that mixture in
different ways.

## 2. Predict the unwanted terms, then correct the coefficients

The first-$`g`$ theorem applies when

```math
g\ge1,\qquad q\ge65{,}536g^2.
```

Its organizing idea is to use a candidate polynomial to predict the unwanted
terms. Correct the observed logarithms using that prediction, then convert
the corrected logarithms back to a better polynomial.

| Operation | Purpose |
|---|---|
| Complete by reciprocity | Represent the polynomial with $`g`$ coefficients |
| Take the formal logarithm | Predict the power sums |
| Subtract higher-multiple terms | Isolate low logarithmic coefficients |
| Exponentiate through degree $`g`$ | Produce the next candidate |

To prove that this loop improves the answer, normalize

```math
p=q^{-1/2},\qquad F(z)=P(z/\sqrt q)=\sum_{j=0}^{2g}a_jz^j.
```

Then $`a_j=c_jq^{-j/2}`$, and reciprocity becomes the simple symmetry
$`a_{2g-j}=a_j`$. Given $`a=(a_1,\ldots,a_g)`$, let $`F_a`$ be its completed
polynomial, with constant and leading coefficient $`1`$; include the middle
coefficient $`a_g`$ only once.

Write $`\log F(z)=\sum_{m\ge1}\ell_mz^m`$. Its coefficients are

```math
\ell_m=-\frac{S_m}{m q^{m/2}}.
```

The observed data therefore give

```math
y_n:=-\frac{L_n}{np^n}
=\ell_n+\sum_{k\ge2}\ell_{nk}p^{n(k-1)}.
```

Call the second sum the **alias term**: coefficients at higher multiples
contribute to the observation at index $`n`$. For a series $`H=\sum_m h_mz^m`$,
package these terms into

```math
(\mathcal A H)(z)=\sum_{n=1}^{g}
 \left(\sum_{k\ge2}h_{nk}p^{n(k-1)}\right)z^n.
```

Put $`Y(z)=\sum_{n=1}^g y_nz^n`$, and let $`\pi_g`$ keep only degrees
$`1,\ldots,g`$, dropping the constant term. The correction loop is

```math
\boxed{\mathcal T(a)=\pi_g\exp\bigl(Y-\mathcal A\log F_a\bigr)}.
```

At the true coefficients $`a_*`$, subtraction removes exactly the aliases.
Exponentiation then returns $`a_*`$: the answer is a fixed point of the loop.
The first $`g`$ exponential coefficients depend only on the first $`g`$
coefficients of its exponent, which explains why this truncation is valid.

## 3. Why the correction converges

Measure a series using

```math
\|H\|_r=\sum_m|h_m|r^m,\qquad r=\frac1{8g}.
```

The weights make a high-degree coefficient count less, while retaining it in
the analysis. They also respect multiplication:
$`\|HG\|_r\le\|H\|_r\|G\|_r`$. Consequently the usual logarithm and
exponential series give bounds on whole polynomials at once.
For a vector $`a`$, use the same weighted sum over $`j=1,\ldots,g`$.

The Weil bounds imply $`\|F-1\|_r<1/3`$. Work with candidate vectors in the
slightly larger ball $`\|a\|_r\le1/2`$. Their completed polynomials also stay
close enough to $`1`$ for the logarithm estimates; their roots need not satisfy
the Weil condition.

The key ratio is

```math
\kappa=\frac p r=\frac{8g}{\sqrt q}\le\frac1{32}.
```

An alias from degree $`nk`$ to degree $`n`$ receives a factor
$`\kappa^{n(k-1)}`$ in the weighted norm. Summing these contributions gives
$`\|\mathcal A H\|_r\le\|H\|_r/31`$. After including the logarithm,
completion, and exponential bounds, the
[fixed-point proof](../research/first_g_reconstruction_v1/THEOREM.md#5-fixed-point-and-its-uniform-constants)
establishes

```math
\begin{gathered}
\|\mathcal T(a)-\mathcal T(b)\|_r
\le\frac{65}{434}\|a-b\|_r,\\
\frac{65}{434}<\frac16.
\end{gathered}
```

It also proves that the loop stays inside the ball. Starting at zero, each
exact step reduces the error by at least a factor of six. Two promised
polynomials giving the same data would be fixed points of this same
contraction, so they must coincide.

This explains the quadratic scale: controlling all true coefficients uses
$`r`$ of order $`1/g`$, and making the aliases small requires $`1/\sqrt q`$ to
be smaller still. The constant $`65{,}536`$ is sufficient. The
[method-boundary note](../research/consolidation_v1/METHOD_BOUNDARY.md)
describes this norm argument's limitation; it does not establish an optimal
threshold for reconstruction.

## 4. From convergence to a finite exact answer

The normalization is a proof device. The implemented loop stores raw rational
coefficients $`c_j`$ and uses integer powers of $`q`$; it computes neither roots
nor $`\sqrt q`$.

For example, if $`\log P_c(T)=\sum_m b_mT^m`$, the finite corrected exponent
in raw coordinates has coefficients

```math
Z_n=-\frac{q^n}{n}\widehat L_n
 -\sum_{\substack{k\ge2\\nk\le M}}
 b_{nk}q^{-n(k-1)}.
```

Here $`\widehat L_n`$ is a certified rational approximation and $`M`$ is a
proved cutoff. Formal logarithm and exponential coefficients are computed
by rational recurrences. At each iteration, round the stored coefficients
to a fixed dyadic denominator, a power of two. This controls denominator
growth across iterations as well as numerical error.

The [finite precision schedule](../research/first_g_reconstruction_v1/THEOREM.md#6-a-finite-certified-precision-schedule)
budgets logarithm, truncation, and rounding errors. It reaches raw coefficient
error below $`1/32`$, so final rounding recovers the unique integer coefficients.
The iteration count, precision, and intermediate fraction sizes are polynomial
in $`g`$ and $`\log q`$. These size bounds turn convergence into a deterministic
polynomial **bit-time** reconstruction algorithm.

## 5. The companion route: cancel using selected extra counts

The all-field theorem trades extra supplied values for applicability to every
$`q\ge2`$ when $`g\ge32`$. A miniature cancellation illustrates its mechanism:

```math
L_n-\frac12L_{2n}
=\sum_{\substack{k\ge1\\k\text{ odd}}}
 \frac{S_{nk}}{kq^{nk}}.
```

Every even multiple disappears. This identity alone is not the theorem:
smaller indices require additional cancellations and a uniform tail estimate.

Set $`h=g-2`$ and supply precisely

```math
D_h=\{1,\ldots,h\}\cup\{2,4,\ldots,2h\}.
```

For $`1\le n\le h`$, choose $`k_n=\max(2,\lfloor h/n\rfloor)`$. All the
indices $`ni`$ with $`1\le i\le k_n`$ belong to $`D_h`$. Möbius weights give

```math
\begin{gathered}
A_n=\frac{q^n}{n}\sum_{i=1}^{k_n}\frac{\mu(i)}i L_{ni},\\
\left|A_n-\frac{S_n}{n}\right|<\frac13.
\end{gathered}
```

The divisor identity for $`\mu`$ cancels the terms through $`k_n`$; the
[uniform estimate](ALL_FIELD_PROOF.md#3-uniform-analytic-error-proof)
bounds everything left. Newton identities then recover coefficients one at a
time. Earlier coefficients and power sums are already exact, so only the new
term needs an error allowance. A numerical error at most $`1/24`$ leaves total
coefficient error below $`3/8`$, enough for unique integer rounding.

After recovering through $`c_{g-2}`$, use $`P(1)=K_1`$ and
$`P(-1)=K_2/K_1`$. These two endpoint equations determine $`c_{g-1},c_g`$;
reciprocity finishes the polynomial. Kedlaya supplies the logarithm–Möbius–Newton
framework, and Sutherland supplies direct endpoint precedents. The selected
support and uniform tail bound are the repository's contribution here.

There are $`h+\lceil h/2\rceil`$ supplied values, with largest index $`2g-4`$.
For $`g=32`$, that is 45 values reaching index 60, not the first 45 values.
The two regimes complement one another, with sufficient thresholds.

Continue with the [comparison to Chidambaram–Keller](COMPARISON.md), the
[complete first-$`g`$ proof](../research/first_g_reconstruction_v1/THEOREM.md),
or the [complete all-field proof](ALL_FIELD_PROOF.md).
The [first-$`g`$](EXPERIMENTS.md#first-g-reconstruction) and
[all-field](EXPERIMENTS.md#all-field-reconstruction) experiments
reproduce exact supplied-polynomial controls. See the
[experiment guide](EXPERIMENTS.md#what-the-controls-establish) for their role
in checking the implementations and the distinction between reconstruction
and authentication.

---

[← Foundations](TUTORIAL.md) · [Reading guide](READING_GUIDE.md) · [Comparison →](COMPARISON.md)
