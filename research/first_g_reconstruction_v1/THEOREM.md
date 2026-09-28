# First-g reconstruction with a quadratic field-size threshold

27 September 2026. Classical supplied-count reconstruction.

**Theorem and status:** the proof below and its finite rational algorithm have
passed an internal derivation and independent internal adversarial check.
The [successor experiment](../../experiments/first_g_reconstruction_v1/README.md)
provides targeted exact controls. This is not external peer review or a
proof-assistant verification; publication priority remains qualified.

The preserved all-field theorem remains unchanged. Kedlaya supplies the
logarithmic reconstruction framework, and Chidambaram–Keller already prove
first-g recovery in a large-field regime. The candidate improvement here is the
explicit quadratic sufficient threshold with polynomial bit time retained.
See the [primary-source comparison](../contribution_assessment_v1/ASSESSMENT.md)
for exact predecessor statements, versions, and search limitations.

## 1. Theorem and exact promises

Let $`g\ge1`$ and $`q\ge65{,}536g^2`$ be integers. Suppose

```math
P(T)=\prod_{i=1}^{2g}(1-\alpha_iT)
    =\sum_{j=0}^{2g}c_jT^j\in\mathbb Z[T],\qquad c_0=1,
```

where all inverse roots have modulus $`\sqrt q`$ and

```math
c_{2g-j}=q^{g-j}c_j\qquad(0\le j\le g).
```

Define the **true exact supplied integers**

```math
K_n=\prod_{i=1}^{2g}(1-\alpha_i^n),\qquad 1\le n\le g.
```

**Conclusion.** These first $`g`$ values uniquely determine $`P`$ in this
promised class, and the algorithm specified below recovers it deterministically
in time polynomial in $`g`$ and $`\log q`$.

No curve equation, factorization, acquisition algorithm, authenticity check,
genericity assumption, or root separation is supplied. Primality of $`q`$ is not
used. In an application to a curve these are Jacobian cardinalities, not curve
point counts. The threshold is only a conservative sufficient bound. In
particular, the conclusion is not an all-field first-g theorem.

The case $`g=0`$ is separately trivial, with $`P=1`$. All bounds below explicitly
include $`g=1`$; they are very wasteful there, where one already has
$`c_1 = K_1 - q - 1`$.

## 2. Normalize only for the proof

Put

```math
p=q^{-1/2},\qquad r=\frac1{8g},\qquad
\kappa=\frac p r=\frac{8g}{\sqrt q}\le\frac1{32}.
```

The normalized polynomial

```math
F(z)=P(z/\sqrt q)=\sum_{j=0}^{2g}a_jz^j,
\qquad a_j=c_jq^{-j/2},
```

is palindromic: $`a_{2g-j}=a_j`$, with constant and leading coefficient $`1`$.
Its inverse roots have modulus one. Thus

```math
|a_j|\le {2g\choose j},\qquad
\|F-1\|_r:=\sum_{j=1}^{2g}|a_j|r^j
\le(1+r)^{2g}-1\lt \frac13.
```

Indeed $`(1+r)^{2g}\le\exp(1/4)\lt4/3`$; the latter strict bound follows by
comparing the exponential series with the geometric series at $`1/4`$.

The actual algorithm in Section 8 uses rational coordinates $`c_j`$ and never
computes $`\sqrt q`$. This normalization defines the norm and proves convergence.

## 3. Banach algebra and palindromic completion

Let

```math
\mathcal A_r=\left\{H(z)=\sum_{m\ge0}h_mz^m:
                    \|H\|_r=\sum_{m\ge0}|h_m|r^m\lt \infty\right\}.
```

This is a commutative Banach algebra, and its norm is submultiplicative.
Let $`\pi_g`$ retain only terms of degrees $`1,\ldots,g`$, dropping the constant term.
It has operator norm at most one. For a vector $`a=(a_1,\ldots,a_g)`$ define

```math
\|a\|_r=\sum_{j=1}^{g}|a_j|r^j,
```

and its palindromic completion

```math
F_a(z)=1+\sum_{j=1}^{g}a_jz^j
          +\sum_{j=1}^{g-1}a_jz^{2g-j}+z^{2g}.
```

The central coefficient is included only once. The second sum is empty for
$`g=1`$. Work on the closed ball

```math
\mathcal B=\{a:\|a\|_r\le1/2\}.
```

For $`a\in\mathcal B`$,

```math
\begin{split}
\|F_a-1\|_r
&\le(1+r^2)\|a\|_r+r^{2g}\\
&\le\frac{65}{128}+\frac1{64}
 =\frac{67}{128}\lt \frac58.
\end{split}
```

Here $`r\le1/8`$ and $`r^{2g}\le1/64`$. The factor $`r^2`$ is justified by
$`r^{2g-j}/r^j=r^{2g-2j}\le r^2`$ for every $`j\le g-1`$.
For $`g=1`$, the direct bound is even smaller: $`1/2+r^2=33/64`$.

Differences obey

```math
\|F_a-F_b\|_r\le(1+r^2)\|a-b\|_r
                    \le\frac{65}{64}\|a-b\|_r.
```

The logarithm is the norm-convergent series

```math
\log F_a=\sum_{j\ge1}\frac{(-1)^{j+1}}j(F_a-1)^j.
```

For $`a,b\in\mathcal B`$, telescoping the powers gives

```math
\|\log F_a-\log F_b\|_r
\le\frac{8}{3}\|F_a-F_b\|_r.
```

Also

```math
\|\log F_a\|_r\le\log(8/3)\lt 1.
```

The final strict inequality follows, for example, from
$`\exp(1)>1+1+1/2+1/6+1/24=65/24>8/3`$.

For arbitrary $`H,G`$ in this algebra,

```math
\|\exp H-\exp G\|_r
\le\exp(\max(\|H\|_r,\|G\|_r))\|H-G\|_r.
```

This follows by telescoping $`H^j-G^j`$ in the exponential series; no pointwise
root separation or assertion about the roots of intermediate $`F_a`$ is needed.

## 4. The exact alias identity, including every scale factor

Write

```math
\log F(z)=\sum_{m\ge1}\ell_mz^m.
```

For the true polynomial, reciprocity gives

```math
\prod_{\zeta^n=1}F(p\zeta)
=\prod_i(1-\alpha_i^n/q^n)
=K_n/q^{gn}.
```

Since $`p\lt r`$, each logarithmic series is absolutely convergent. Summing over
the roots of unity filters the coefficients:

```math
\sum_{\zeta^n=1}\log F(p\zeta)
  =n\sum_{k\ge1}\ell_{nk}p^{nk}.
```

The sum is real because $`F`$ has real coefficients and the root-of-unity terms
pair under conjugation. Its exponential is the positive real number
$`K_n/q^{gn}`$. Consequently the sum equals its ordinary real logarithm; there
is no unresolved multiple of $`2\pi i`$.

Thus the supplied values determine

```math
y_n:=\frac{\log(K_n/q^{gn})}{np^n}
=\ell_n+\sum_{k\ge2}\ell_{nk}p^{n(k-1)}.
```

Define a linear operator from $`\mathcal A_r`$ to polynomials of degree at most $`g`$ by

```math
(A H)(z)=\sum_{n=1}^{g}\left(
           \sum_{k\ge2}h_{nk}p^{n(k-1)}\right)z^n.
```

The factor in the weighted norm is exactly

```math
|h_{nk}|p^{n(k-1)}r^n
=|h_m|r^m\kappa^{m-n},\qquad m=nk.
```

For a fixed $`m\ge2`$, each contributing $`n`$ is a proper divisor of $`m`$, with
$`n\le g`$ and $`n\le m/2`$. Hence

```math
\begin{split}
\|AH\|_r
&\le\sum_{m\ge2}|h_m|r^m
       \sum_{\substack{n\mid m\\1\le n\le g,\ n\lt m}}
                    \kappa^{m-n}\\
&\le\sum_{m\ge2}|h_m|r^m
       \sum_{n=1}^{\lfloor m/2\rfloor}\kappa^{m-n}\\
&\le\frac{\kappa}{1-\kappa}\|H\|_r
\le\frac1{31}\|H\|_r.
\end{split}
```

The last geometric sum starts at exponent $`\lceil m/2\rceil\ge1`$. This estimate counts
repeated uses of a coefficient across different divisors; it does not assume
that each $`h_m`$ appears only once.

If $`A^{(M)}`$ retains only summands with $`nk\le M`$, where $`M\ge g`$, a useful tail bound is

```math
\|(A-A^{(M)})H\|_r
\le g\kappa^{M+1-g}\|H\|_r.
```

Indeed, for every omitted $`m\ge M+1`$, there are at most $`g`$ contributing indices,
and $`m-n\ge M+1-g`$ for all of them. This is deliberately a loose bound.

## 5. Fixed point and its uniform constants

Let $`a_*`$ denote the first half of the true $`F`$; it satisfies
$`\lVert a_*\rVert_r\lt1/3`$. Set

```math
Y(z)=\sum_{n=1}^{g}y_nz^n
=\pi_g\log F_{a_*}+A\log F_{a_*}.
```

For $`a\in\mathcal B`$, define

```math
H_a=Y-A\log F_a,\qquad
T(a)=\pi_g\exp(H_a).
```

The expression for $`T`$ is interpreted as its vector of first $`g`$ coefficients.
Since those coefficients of an exponential depend only on the first $`g`$
coefficients of its exponent,

```math
T(a_*)=\pi_g\exp(\pi_g\log F_{a_*})=a_*.
```

The bounds established above give

```math
\|H_a-H_b\|_r
\le\frac1{31}\frac83\frac{65}{64}\|a-b\|_r
=\frac{65}{744}\|a-b\|_r.
```

Also

```math
\begin{split}
\|H_a-\pi_g\log F_{a_*}\|_r
&\le\frac{65}{744}\|a-a_*\|_r\\
&\lt \frac{65}{744}\left(\frac12+\frac13\right)
=\frac{325}{4464}\lt \frac18.
\end{split}
```

The true-polynomial bound from Section 2 gives

```math
\|\pi_g\log F_{a_*}\|_r\lt \log(3/2).
```

Consequently every $`H_a`$, for $`a\in\mathcal B`$, has norm less than
$`\log(3/2)+1/8`$. Its exponential norm is at most

```math
\frac32e^{1/8}\lt \frac32\frac{1}{1-1/8}=\frac{12}{7}.
```

Therefore

```math
\|T(a)-T(b)\|_r
\le\frac{12}{7}\frac{65}{744}\|a-b\|_r
=\frac{65}{434}\|a-b\|_r
\lt \frac16\|a-b\|_r.
```

This estimate is not circular: the domain bound on $`H_a`$ used the existence
and Weil bound of the promised true polynomial, not invariance of $`T`$.

Finally

```math
\|T(a)\|_r
\le\|a_*\|_r+\frac16\|a-a_*\|_r
\lt \frac13+\frac16\frac56=\frac{17}{36}\lt \frac12.
```

Thus $`T`$ maps $`\mathcal B`$ into itself and is a contraction there. Starting at zero,

```math
\|a^{(t)}-a_*\|_r\le\frac13\,6^{-t}.
```

If two promised Weil polynomials have the same first $`g`$ count values, their
vectors are fixed points of this same contraction in $`\mathcal B`$, and are equal.
This proves uniqueness under the stated hypotheses.

## 6. A finite, certified precision schedule

The letter $`\theta`$ below is a numerical tolerance, not the coefficient weight.

Set the following integers and rational number:

```math
\begin{split}
W&=(8gq)^g,\\
N&=\lceil\log_2(64W)\rceil,\qquad \theta=2^{-N},\\
u&=\lceil\log_2 g\rceil,\qquad
M=g+\left\lceil\frac{N+u+6}{5}\right\rceil,\\
B&=N+5,\qquad I=N.
\end{split}
```

These can all be computed with exact integer comparisons and bit lengths;
none requires a floating-point logarithm. In particular,
$`\theta\le1/(64W)\le1/64`$.

Compute each real logarithm $`L_n=\log(K_n/q^{gn})`$ once, as a rational dyadic
approximation $`\widehat L_n`$ with certified absolute error at most

```math
\varepsilon=\frac{\theta}{64gq^g}.
```

Concretely, obtain an enclosure of radius at most $`\varepsilon/2`$ and round its
center to denominator $`2^L`$, with $`L=\lceil\log_2(2/\varepsilon)\rceil`$. The additional
nearest-rounding error is at most $`\varepsilon/4`$. The resulting approximation
meets the stated allowance, with $`L=O(\log(1/\varepsilon))`$.

At every iteration use $`A^{(M)}`$ in place of $`A`$, calculate the exponential
through degree $`g`$ exactly for the resulting rational exponent, and round each
new **raw** coefficient $`c_j`$ to the nearest dyadic rational with denominator
$`2^B`$. The raw-coordinate formulas are given in Section 8.

The errors in this finite procedure have the following bounds, in the normalized
coefficient norm.

### 6.1 Error in the supplied logarithms

The contribution of the common error allowance to $`Y`$ has norm at most

```math
\sum_{n=1}^{g}\frac{p^{-n}}n\varepsilon r^n
\le gq^g\varepsilon=\theta/64.
```

Here $`p^{-n}r^n\le q^n\le q^g`$ is a deliberately loose bound.

### 6.2 Alias truncation

For every candidate in $`\mathcal B`$, $`\lVert\log F_a\rVert_r\lt1`$. The tail estimate and the choice
of $`M`$ give

```math
\begin{split}
\|(A-A^{(M)})\log F_a\|_r
&\lt g32^{-(M+1-g)}\\
&\le 2^u\,2^{-(N+u+11)}
=\theta/2048\lt \theta/64.
\end{split}
```

The strict positivity of $`M+1-g`$ follows directly from its definition.

### 6.3 Exponentiation and dyadic rounding

The finite exponent differs from $`H_a`$ in norm by less than $`\theta/32`$.
Both exponent norms are bounded above by

```math
\log(3/2)+1/8+\theta/32\lt \log(3/2)+1/4.
```

Their exponential Lipschitz factor is therefore less than
$`(3/2)\exp(1/4)\lt2`$. Consequently the error before dyadic rounding is less
than $`\theta/16`$.

The raw-coefficient norm has weight

```math
\rho=rp=\frac1{8g\sqrt q}\lt \frac18,
\qquad
\|c\|_\rho=\sum_{j=1}^{g}|c_j|\rho^j=\|a\|_r.
```

Rounding each raw coefficient to its nearest multiple of $`2^{-B}`$ changes this
norm by at most

```math
2^{-B-1}\sum_{j=1}^{g}\rho^j
\lt 2^{-B}/14=\theta/448\lt \theta/32.
```

Thus the entire finite step, including quantization, differs from its exact
map $`T`$ by less than $`\theta`$; the stronger bound $`\theta/8`$ is also available.

The approximate iterates remain in $`\mathcal B`$: an exact step has norm less than
$`17/36`$, and $`17/36+\theta\lt1/2`$, since $`\theta\le1/64\lt1/36`$.

## 7. Termination and exact integer recovery

Let $`\widehat a^{(t)}`$ denote the normalized version of the finite raw iterates,
starting from zero. The preceding section gives

```math
\|\widehat a^{(t+1)}-a_*\|_r
\le\frac16\|\widehat a^{(t)}-a_*\|_r+\theta.
```

After $`I=N`$ steps,

```math
\begin{split}
\|\widehat a^{(N)}-a_*\|_r
&\lt \frac13 6^{-N}+\frac65\theta\\
&\le\frac13\theta+\frac65\theta
=\frac{23}{15}\theta\lt 2\theta.
\end{split}
```

For $`j\le g`$, the raw coefficient error is therefore less than

```math
2\theta\rho^{-j}\le2\theta\rho^{-g}
=2\theta(8g\sqrt q)^g
\le2\theta W\le1/32.
```

Rounding each final raw coefficient to the nearest integer recovers its true
value uniquely. Exact reciprocity then supplies the remaining coefficients.
There are no uncertain power sums that are multiplied by growing coefficients
between iterations: the entire state is quantized afresh to the fixed dyadic
precision at the end of each step.

## 8. Entirely rational finite algorithm

For a raw vector $`c=(c_1,\ldots,c_g)`$, define

```math
P_c(T)=1+\sum_{j=1}^{g}c_jT^j
 +\sum_{j=1}^{g-1}q^{g-j}c_jT^{2g-j}+q^gT^{2g}.
```

Write its formal logarithm as

```math
\log P_c(T)=\sum_{m\ge1}b_mT^m.
```

Conjugating the normalized formulas by $`a_j=c_jq^{-j/2}`$ gives the **raw**
exponent

```math
Z_n=\frac{q^n}{n}\widehat L_n
 -\sum_{\substack{k\ge2\\nk\le M}}
          b_{nk}q^{-n(k-1)},\qquad1\le n\le g.
```

To check the scale: $`\ell_m=b_mq^{-m/2}`$, and multiplication of the normalized
exponent's $`n`$th coefficient by $`q^{n/2}`$ turns its alias term into
$`b_{nk}q^{-n(k-1)}`$, precisely as displayed. No square-root arithmetic remains.

One finite iteration is:

1. Complete the dyadic vector $`c`$ to $`P_c`$ using the displayed reciprocity.
2. Compute $`b_1,\ldots,b_M`$ by exact rational formal-series arithmetic.
3. Form $`Z_1,\ldots,Z_g`$ from the finite sums above.
4. Compute coefficients $`d_1,\ldots,d_g`$ of
   $`\exp\bigl(\sum_{n=1}^g Z_nT^n\bigr)`$ by exact rational arithmetic.
5. Replace every $`c_j`$ by the nearest multiple of $`2^{-B}`$ to $`d_j`$.

Useful exact recurrences are, with $`C_m=[T^m]P_c`$, $`C_0=1`$, and $`C_m=0`$ for
$`m>2g`$,

```math
b_m=C_m-\frac1m\sum_{j=1}^{m-1}j b_j C_{m-j},
```

and, with $`d_0=1`$,

```math
d_m=\frac1m\sum_{j=1}^{m}jZ_jd_{m-j}\qquad(m\le g).
```

These recurrences are just $`P_c'=P_c(\log P_c)'`$ and
$`(\exp Z)'=Z'\exp Z`$. They compute exact rational coefficients of the truncated
formal series, regardless of roots of the candidate polynomial. Their analytic
error bounds come from the norm argument already proved.

Initialize all raw $`c_j=0`$, perform $`N`$ steps, round the last vector to integers,
and complete by reciprocity.

## 9. Bit-complexity details and the role of quantization

Put $`b=\lceil\log_2 q\rceil`$ and

```math
\Lambda=g\bigl(b+\lceil\log_2(g+1)\rceil+1\bigr).
```

The parameters $`N`$, $`M`$, $`B`$, and the required logarithm precision in bits are
all $`O(\Lambda)`$. In particular the number of iterations and formal-series terms
is polynomial in $`g`$ and $`\log q`$.

### 9.1 Input sizes and certified logarithms

The Weil bound gives

```math
0\lt K_n\le(q^{n/2}+1)^{2g}\le2^{2g}q^{gn}.
```

Thus each requested integer has $`O(g^2 b)`$ bits and the complete transcript has
$`O(g^3 b)`$ bits. These are promised-input bounds, not a claim about the time
needed to read an arbitrary malformed integer of unbounded length.

For a positive rational $`x=K_n/q^{gn}`$, compute its exact binary range reduction
$`x=2^e u`$, $`1\le u\lt2`$. Let $`z=(u-1)/(u+1)`$, so $`0\le z\lt1/3`$. Evaluate

```math
\log x=e\log2+2\sum_{j\ge0}\frac{z^{2j+1}}{2j+1}
```

with the geometric tail bound

```math
\frac{2|z|^{2s+1}}{(2s+1)(1-z^2)}.
```

Compute $`\log u`$ and $`\log2`$ finely enough that multiplication by $`e`$ is included
in the error allowance, then round to a dyadic rational while preserving the
total error bound $`\varepsilon`$. The exponent has polynomial bit size (indeed its
magnitude is $`O(g)`$ on these Weil inputs, although that sharper bound is not
needed). The number of terms is
$`O(\log(1/\varepsilon)+\log(1+\lvert e\rvert))`$. Rational powers and their finite sums have
polynomial bit size in the input length and that term count. This provides a
deterministic, rational, certified logarithm computation, rather than a
unit-cost real-number oracle.

### 9.2 Uniform candidate sizes

Every stored low coefficient is a multiple of $`2^{-B}`$. Because all finite
iterates remain in the norm ball,

```math
|c_j|\le\tfrac12\rho^{-j}\le W\qquad(j\le g).
```

Every completed coefficient is bounded in magnitude by $`W^2`$, since
$`q^g\le W`$; its dyadic denominator divides $`2^B`$. Hence the numerators and
denominators supplied to one iteration have $`O(\Lambda)`$ bits.

### 9.3 Intermediate fractions inside one step

The formal identity

```math
\log(1+U)=\sum_{j=1}^{M}(-1)^{j+1}U^j/j\pmod {T^{M+1}}
```

shows that denominators of its first $`M`$ coefficients divide
$`2^{BM}\mathrm{lcm}(1,\ldots,M)`$. Coefficient magnitudes can be bounded by products of at
most $`M`$ input coefficients and the number of compositions of indices up to
$`M`$. Therefore their reduced numerator/denominator sizes are
$`O(M(B+\log W+\log M))`$, a polynomial bound. Exact recurrence computations with
fraction reduction respect a polynomial bound as well, including temporary
products and partial sums.

The alias sums introduce denominators dividing $`q^M`$; the dyadic input
logarithms and factors $`1/n`$ add polynomially many bits. Thus all $`Z_n`$ admit
a common denominator $`D`$ of polynomial bit length.
The first $`g`$ coefficients of $`\exp Z`$ have denominators dividing $`D^g g!`$, by
its finite power-series expansion through degree $`g`$. Their numerator lengths
are polynomial as well. A loose bound for the maximum intermediate bit length
is $`O(gM(\Lambda+\log M))`$, sufficient for the complexity claim.

**The final dyadic quantization of each iteration is essential for this
argument.** Without it, exact denominators from one nonlinear step could be
raised to powers in all subsequent steps, and merely counting iterations would
not establish polynomial bit complexity. With it, every iteration starts again
with denominator $`2^B`$ and the same polynomial input-size bound.

There are polynomially many rational additions, multiplications, divisions,
comparisons, and gcd reductions: for example, $`O(M^2+gM+g^2)`$ arithmetic
operations per iteration is a loose bound. Ordinary integer algorithms on the
polynomial-sized operands therefore prove deterministic polynomial bit time
and polynomial storage. No tight runtime exponent is asserted.

## 10. Verification and scope

An independent internal check rederived the alias weights, the global domain
bounds, the contraction constant, finite-series error, and integer-rounding
margin. It also checked the rational formulation for nonsquare $`q`$ and the role
of dyadic quantization in the bit-complexity argument.

The standard-library implementation reconstructs five supplied-polynomial
controls with genera 1, 2, 3, 4 and 8. These include repeated factors, nonsquare
$`q`$, equality at the sufficient threshold, and an irreducible degree-eight Weil
polynomial. All 41 coefficients agree exactly; all final unrounded low
coefficients satisfy the proved error budget. Two allowed logarithm displacement
runs also recover the polynomial. Independent full-degree companion determinants
agree on all 18 supplied values. See the experiment for the exact report.

The supplied controls are not asserted to be Jacobians. The finite controls
support the implementation, while the proof above establishes the uniform
claim. No hardware, quantum group-order acquisition, native point counter,
external author's program, or formal proof checker was used.

A one-unit corruption of a supplied count can be accepted and decoded to the
original polynomial; replaying its resultant detects the mismatch. The
promised-input theorem reconstructs the true polynomial. Successful decoding
alone does not authenticate a transcript or bind it to a claimed curve.

The constant 65,536 is sufficient, not sharp. Failure of its inequality is not
proof that first-g reconstruction fails. The theorem coexists with the
preserved sparse all-field guarantee; neither subsumes the other over the
entire parameter range. Manuscript preparation remains on hold.
