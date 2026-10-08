# Scientific consolidation audit

27 September 2026. Audited commit:
`08a1199cfc52befc3bd47bf1f758612cdf650445`, tree
`94bacb3dabbdc5f7642fb6513fe825c18731fba4`.

**Outcome:** no substantive correctness or implementation gap was found in the
first-g theorem. The focused primary-source comparison continues to support the
quadratic sufficient threshold as the candidate main contribution. The current
two-theorem scope is ready for consolidation; an additional discovery is not a
prerequisite.

This is a fresh internal AI review, divided between mathematical and finite
arithmetic audits, with the findings checked together. It is not external peer
review or proof-assistant verification. The audit preserves the first-g proof,
decoder, fixtures, and reports, as well as all 17 imported baseline files.

## 1. Scope of the conclusion

The [first-g theorem](../first_g_reconstruction_v1/THEOREM.md) assumes integer
$`g\ge1`$, integer $`q\ge65{,}536g^2`$, integral coefficients, $`q`$-reciprocity, inverse
roots of modulus $`\sqrt q`$, and the true exact values $`K_1,\ldots,K_g`$. It gives
uniqueness and deterministic polynomial bit-time reconstruction. It does not
acquire or authenticate counts. For curves, the supplied counts are Jacobian
cardinalities. Abstract polynomial controls are not asserted to be Jacobians.

The all-field selected-data theorem remains a complementary result for $`g\ge32`$.
Neither the minimum number of queries nor the necessary field-size threshold
is established. No quantum advantage or practical runtime improvement is claimed.

## 2. Independent analytic checks

The following rederivations address possible failure points in Sections 1–7,
rather than relying on agreement of finite controls.

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

## 3. Finite arithmetic and implementation

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

One reporting qualification is now explicit: the historical metadata field
`max_intermediate_bits` samples stored formal-logarithm and exponential
coefficients. It does not measure corrected exponents, fraction-operation
temporaries, or logarithm preprocessing. It is not an observed global memory
maximum. The polynomial bit-complexity proof does not rely on that diagnostic.

The runtime and correctness guarantees concern promised inputs. Arbitrary
positive malformed counts need not keep iterates in the invariant ball. The
prototype is not a total defensive validator with the same parameter-only
runtime guarantee outside that promise.

## 4. Literature and the bounded extension question

The [fresh source record](SOURCES.md) confirms the current first-g predecessor
and its still-open polynomial-threshold question. Its polynomial bit-time
algorithm and its proposed $`g^{O(g)}`$ threshold refinement are included in the
comparison. The candidate contribution is the quadratic sufficient threshold,
not the first use of $`g`$ counts or the first efficient decoder.

The [method-boundary note](METHOD_BOUNDARY.md) proves that the current
single-radius, whole-algebra small-norm argument inherently requires a
quadratic field-size scale. This closes the bounded extension probe with a
precise limitation of the estimates. It proves neither failure of the actual
iteration below the threshold nor ambiguity of the data. It is an elementary
supporting observation, not a separate publication-priority claim.

## 5. Scientific decision and remaining limits

The quadratic-threshold theorem should lead the mathematical account; the
all-field sparse guarantee supplies the complementary regime. No new theorem,
constant optimization, lower bound, actual-curve fixture, or large simulation
is presently necessary to support this scope. No substantive correction was
identified in this audit, so the versioned decoder and its reference outputs
were left unchanged.

The focused search found no statement subsuming the new guarantee. That is a
bounded originality assessment, not a certificate against every thesis or
unpublished argument. External review remains unperformed. Query optimality,
an all-field first-g theorem, and practical scalability remain optional research
questions outside the present scope.

The [verification receipt](VERIFICATION.json) records the actual before/after
runs and preserved scientific file identities. Further scientific work should
respond to a concrete gap, competing theorem, or consequential extension,
rather than repeat this audit without new evidence.
