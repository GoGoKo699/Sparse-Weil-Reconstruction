# Proof and arithmetic checks

These internal analytic and implementation checks supplement the
[first-g proof](../first_g_reconstruction_v1/THEOREM.md). They address logarithm
signs, contraction bounds, finite-error margins, and rational denominator growth.
The theorem applies to the true supplied counts under its stated Weil-polynomial
and field-size hypotheses.

## 1. Analytic checks

The following rederivations check Sections 1–7 of the proof.

### Input signs and the logarithm

Let $`\chi(X)=X^{2g}P(1/X)`$. It is monic and integral, and

```math
K_n=\mathrm{Res}(\chi,X^n-1)\in\mathbb Z.
```

The sign is positive in this equality because the degree is even. Reciprocity
gives the inverse-root multiset identity
$`\{\alpha_i\}=\{q/\alpha_i\}`$ and the product $`\prod_i\alpha_i=q^g`$. For the true
normalized polynomial $`F(z)=P(z/\sqrt q)`$ and $`p=q^{-1/2}`$,

```math
\prod_{\zeta^n=1}F(p\zeta)=K_n/q^{gn}.
```

The convergent logarithm series has real coefficients. Pairing root-of-unity
arguments under conjugation makes the sum of their logarithms real. Its
exponential is the displayed product. This proves positivity of $`K_n`$ and
identifies the sum with its ordinary real logarithm, without a branch ambiguity.
Repeated roots and the real Weil endpoints do not require an extra assumption.

### Completion, divisors, and invariance

The central coefficient is counted once in palindromic completion. Every other
reflected coefficient has weight ratio at most $`r^2`$, so the completion
Lipschitz factor is at most $`65/64`$ for $`r=1/(8g)`$.

For $`\kappa=p/r`$, a fixed coefficient of degree $`m`$ contributes at every proper
divisor $`n\le g`$ of $`m`$. Its total relative weight is bounded by

```math
\sum_{\substack{n\mid m\\n\le g,\ n\lt m}}\kappa^{m-n}
\le\sum_{j=\lceil m/2\rceil}^{m-1}\kappa^j
\le\frac{\kappa}{1-\kappa}.
```

This checks the potentially repeated use of each coefficient. The resulting
constants independently reproduce as

```math
\mathrm{Lip}(H)\le\frac{65}{744},\qquad
\mathrm{Lip}(T)\le\frac{65}{434}\lt \frac16.
```

The exponent bound uses the promised true polynomial before invariance is
asserted; the argument is not circular. The image norm is below $`17/36`$, inside
the radius-$`1/2`$ ball. Two promised polynomials giving the same transcript would
be fixed points of the same contraction, so they coincide. Integrality enters
the final recovery step, not this analytic uniqueness argument.

### Finite error and boundary cases

With the theorem's precision parameters, the exact integer inequality
$`5(M+1-g)\ge N+u+11`$ gives alias error below $`\theta/2048`$. Input-logarithm error
is at most $`\theta/64`$. The conservative exponential and quantization errors
are below $`\theta/16`$ and $`\theta/448`$, respectively. A complete step therefore
has error below $`29\theta/448\lt\theta/8`$, within the stated $`\theta`$ allowance.

The ball margin is $`1/36>\theta`$. The final norm error is below
$`23\theta/15\lt2\theta`$, and every low raw coefficient has error below $`1/32`$.
Nearest-integer recovery is therefore unique. The empty completion sum for
$`g=1`$, nonsquare $`q`$, repeated roots, and equality at the field-size threshold
introduce no uncovered case.

## 2. Finite arithmetic and implementation

The [decoder](../../experiments/first_g_reconstruction_v1/reconstruct.py) matches
Sections 6–9 of the theorem. The code's cutoff
`g + (N+u+10)//5` equals $`g+\lceil(N+u+6)/5\rceil`$. It obtains logarithm enclosures
of radius at most $`\varepsilon/2`$ and rounds the centers with an additional error
at most $`\varepsilon/4`$. Binary range reduction, including a negative exponent,
is handled by the pinned inherited logarithm routine.

The raw exponent uses exactly

```math
Z_n=\frac{q^n}{n}\widehat L_n
 -\sum_{\substack{k\ge2\\nk\le M}}b_{nk}q^{-n(k-1)}.
```

Both formal-series recurrences match the proof. All stored low coefficients
are quantized after every iteration; the final rounding convention is harmless
because the final error is strictly below $`1/32`$. No square-root arithmetic is
needed by the implementation.

An explicit common denominator sharpens the bookkeeping in Section 9 without
changing its conclusion. Write

```math
R=\mathrm{lcm}(1,\ldots,M),\qquad
L=\texttt{log\_bits},\qquad D=2^{BM+L}R q^M.
```

Every $`Z_n`$ has denominator dividing $`D`$: formal-logarithm denominators divide
$`2^{BM}R`$, alias powers add denominators dividing $`q^M`$, and the input logarithms
and division by $`n`$ are covered by $`2^L R`$. Consequently the degree-$`j`$
exponential coefficient has denominator dividing $`D^j j!`$.

The exponential recurrence's temporary products and partial sums also have
polynomial bit length. Before the final division by $`j`$, their reduced denominators divide
$`D^j(j-1)!`$. The numerator bounds follow from the candidate-size bounds and
finite composition counts in the theorem. Quantization then resets all stored
denominators to divisors of $`2^B`$. Thus repeated nonlinear iterations do not
cause an uncontrolled denominator tower.

The experiment metadata field
`max_intermediate_bits` samples stored formal-logarithm and exponential
coefficients. It does not measure corrected exponents, fraction-operation
temporaries, or logarithm preprocessing. It is not an observed global memory
maximum. The polynomial bit-complexity proof does not rely on that diagnostic.

The runtime and correctness guarantees concern promised inputs. Arbitrary
positive malformed counts need not keep iterates in the invariant ball. The
prototype is not a total defensive validator with the same parameter-only
runtime guarantee outside that promise.

## 3. The norm-method boundary

The [method-boundary proposition](METHOD_BOUNDARY.md) shows why the single-radius,
whole-algebra small-norm argument requires a quadratic field-size scale. Its
necessity statement concerns those estimates; it is not a lower bound on
reconstruction from the first $`g`$ counts.
