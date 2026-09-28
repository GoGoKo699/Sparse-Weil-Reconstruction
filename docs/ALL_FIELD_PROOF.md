# All-field reconstruction: a typeset proof

This reading edition presents the complete selected-count argument from
Sections 1–5 of the [preserved theorem](../exploration/phase_2/ORDINARY_QUERY_THEOREM_AUDIT_28.md),
followed by the explicit bit-complexity analysis from Section 3 of the
[preserved proof audit](../exploration/phase_2/RECONSTRUCTION_PROOF_REVIEW_29.md).
The mathematical hypotheses, bounds, rounding argument, and complexity estimates
are unchanged. The original records retain their historical context and exact
verification identities.

## 1. The theorem and its exact input model

Let $`g\ge32`$ and let $`q\ge2`$ be an integer. Let

```math
P(T)=\prod_{j=1}^{2g}(1-\alpha_jT)=\sum_{j=0}^{2g}c_jT^j
```

have integer coefficients, $`c_0=1`$, inverse roots with
$`|\alpha_j|=\sqrt q`$, and reciprocity
$`c_{2g-j}=q^{g-j}c_j`$. Pair the $`\alpha_j`$ so that each pair has product
$`q`$. In the curve application, $`q`$ is a prime power and $`P`$ is the
numerator of the zeta function of a smooth projective geometrically connected
genus-$`g`$ curve. The supplied cardinalities then count its Jacobian, rather
than the curve itself.

Define $`K_m=\prod_j(1-\alpha_j^m)`$, and put $`h=g-2`$. Suppose the exact
positive integers $`K_m`$ are supplied at the indices

```math
D_h=\{1,\ldots,h\}\cup\{2,4,\ldots,2h\}.
```

**Theorem.** $`P`$ is determined by these integers and can be reconstructed in
time polynomial in $`g`$ and $`\log q`$. There are

```math
|D_h|=h+\lceil h/2\rceil\lt 2g
```

cardinality requests, and the largest requested degree is $`2h=2g-4`$.
The requests are fixed, nonadaptive, and need not form an initial consecutive
sequence. This is a supplied-data / exact-cardinality-oracle theorem.

For $`g=32`$, this means 45 supplied counts, at degrees $`1,\ldots,30`$ and
$`32,34,\ldots,60`$. For $`g=64`$ it means 93 counts and maximum degree 124.
The theorem includes $`q=2`$. It does not assert that the first 45 counts
suffice in the genus-32 example. The constant 32 is a convenient sufficient
threshold, not a lower bound.

The separate large-field guarantee and low-genus endpoint results retain their
own regimes. No uniform all-field claim for genera $`3,\ldots,31`$ is added here.

## 2. Möbius cancellation on the selected indices

[Kedlaya, Section 8][Kedlaya] does not require rounding each unnormalized power
sum to within one half. Previously recovered coefficients fix the next power
sum modulo its index through Newton identities. This means the error should be
controlled on $`S_n/n`$, where $`S_n=\sum_j\alpha_j^n`$. That is prior
machinery, not a new congruence principle.

His cutoff-dependent Möbius formula permits more than two logarithms. For low
indices those extra logarithms lie in the dense initial part $`1,\ldots,h`$ of
$`D_h`$, already queried. At high indices two terms suffice because $`q^n`$ is
large even when $`q`$ itself is small. This observation, combined with the final
two endpoint equations, supplies the theorem above.

No extra query is hidden in the improvement. For $`1\le n\le h`$, put

```math
k_n=\max(2,\lfloor h/n\rfloor),\qquad
L_m=\log(K_m/q^{gm}).
```

Every index $`ni`$ with $`1\le i\le k_n`$ belongs to $`D_h`$. If
$`\lfloor h/n\rfloor\ge2`$, it is at most $`h`$; otherwise only $`n`$ and
$`2n`$ are needed. Define

```math
A_n=-\frac{q^n}{n}\sum_{i=1}^{k_n}\frac{\mu(i)}{i}L_{ni}.
```

This is the normalized, truncated Möbius statistic from [Kedlaya][Kedlaya],
with a different cutoff supported by a smaller selected data set.

## 3. Uniform analytic error proof

Reciprocity and the convergent logarithm series give

```math
L_m=-\sum_{r\ge1}\frac{S_{mr}}{r q^{mr}}.
```

Consequently

```math
A_n=\frac{S_n}{n}+\frac{q^n}{n}\sum_{r>k_n}
   a_r\frac{S_{nr}}{r q^{nr}},\qquad
 a_r=\sum_{i\mid r,\ i\le k_n}\mu(i).
```

The terms for $`2\le r\le k_n`$ vanish, $`|a_r|\le k_n`$, and
$`|S_{nr}|\le2gq^{nr/2}`$. Thus, writing $`k=k_n`$,

```math
\left|A_n-\frac{S_n}{n}\right|
\le \frac{2gk}{n(k+1)}
       \frac{q^{-n(k-1)/2}}{1-q^{-n/2}}.
```

Let $`\rho=5/7`$. Since $`1/\sqrt q\le1/\sqrt2\lt\rho`$, an entirely
rational upper bound is

```math
E_{g,n}=\frac{2gk}{n(k+1)}
       \frac{\rho^{n(k-1)}}{1-\rho^n}.
```

We now prove $`E_{g,n}\lt1/3`$ for every $`g\ge32`$ and $`1\le n\le h`$,
rather than extrapolating from a finite parameter table. Here $`h\ge30`$ and
$`g/h\le16/15`$.

**Case A: $`n>h/3`$.** Then $`k=2`$, so

```math
E_{g,n}\lt\frac{64}{15}\frac{\rho^{10}}{1-\rho^{10}}
 =\frac{15625000}{102266109}\lt\frac13.
```

**Case B: $`h/6\lt n\le h/3`$.** Here $`k\ge3`$. Because
$`n>h/(k+1)`$, we have $`n(k-1)>h(k-1)/(k+1)\ge h/2`$.
Also $`2g/n\lt12g/h\le64/5`$ and $`n>h/6\ge5`$. Hence

```math
E_{g,n}\lt\frac{64}{5}\frac{\rho^{15}}{1-\rho^5}
 =\frac{195312500000}{1932413178409}\lt\frac13.
```

**Case C: $`n\le h/6`$.** We have $`n(k-1)>h-2n\ge2h/3`$.
Moreover $`1/[n(1-\rho^n)]\le1/(1-\rho)=7/2`$. Therefore

```math
E_{g,n}\lt7g\rho^{2(g-2)/3}
 \le224\rho^{20}
 =\frac{3051757812500000}{11398895185373143}\lt\frac13.
```

The middle inequality holds uniformly: the logarithmic derivative of
$`x\rho^{2(x-2)/3}`$ is $`1/x-(2/3)\log(7/5)\lt0`$ for $`x\ge32`$,
using $`\log(7/5)\ge2/7`$. This finishes the analytic proof. The executable
checks of the three rational constants are supplementary, not the reason the
bound holds for arbitrarily large genus.

## 4. Integer reconstruction and numerical control

Assume $`c_1,\ldots,c_{n-1}`$ and $`S_1,\ldots,S_{n-1}`$ are known. Set

```math
B_n=\sum_{i=1}^{n-1}c_{n-i}S_i.
```

Newton's identity gives $`c_n=-S_n/n-B_n/n`$. If $`A_n`$ is evaluated with
numerical error at most $`1/24`$, then

```math
-A_n-B_n/n
```

lies within $`1/3+1/24=3/8`$ of the integer $`c_n`$. Certified interval
rounding therefore recovers $`c_n`$ uniquely. Then $`S_n=-nc_n-B_n`$ is exact.
This incorporates Newton's residue information; rounding $`nA_n`$ directly to
the nearest integer would require a stronger error guarantee and is not the
decoder used here.

Proceed through $`n=h=g-2`$. Since $`K_1=P(1)`$ and $`K_2=P(1)P(-1)`$,
compute $`T_1=P(-1)=K_2/K_1`$ by exact division. This uses no additional count.
With

```math
R_+=K_1-\sum_{i=0}^{g-2}(1+q^{g-i})c_i,\qquad
R_-=T_1-\sum_{i=0}^{g-2}(-1)^i(1+q^{g-i})c_i,
```

and $`s=(-1)^{g-1}`$, recover

```math
c_{g-1}=\frac{R_++sR_-}{2(q+1)},\qquad
c_g=\frac{R_+-sR_-}{2}.
```

Reciprocity supplies the remaining coefficients. These are the established
endpoint equations; [Sutherland][Sutherland] supplies their direct low-genus
predecessors.

### Range reduction for logarithms

An unscaled inverse-hyperbolic-tangent series can converge extremely slowly
when its positive rational argument is tiny. A polynomial-time small-field
implementation therefore uses range reduction. For $`x>0`$, first compute the
exact decomposition $`x=2^eu`$ with $`1\le u\lt2`$. Then

```math
\log x=e\log2+2\sum_{j\ge0}\frac{z^{2j+1}}{2j+1},\qquad
z=(u-1)/(u+1),\quad |z|\le1/3.
```

A truncated sum of $`m`$ terms has tail at most
$`2|z|^{2m+1}/[(2m+1)(1-z^2)]`$. Compute each $`L_j`$ to absolute error at most

```math
\varepsilon=\frac{1}{24h q^h}.
```

The resulting numerical error in $`A_n`$ is at most

```math
\frac{q^n}{n}\sum_{i=1}^{k}\frac{|\mu(i)|}{i}\varepsilon
\le q^hh\varepsilon=\frac1{24}.
```

Errors from $`e\log2`$ are included; logarithms are not treated as exact
primitives. The implementation uses `Fraction` arithmetic, with rational error
radii.

Each input $`K_j`$ has $`O(gj\log q+g)`$ bits by the Weil bounds, with
$`j\le2h`$. The required precision is $`O(h\log q+\log h)`$ bits. Range
reduction and the geometric series therefore use polynomially many rational
operations of polynomial bit length. Newton identities and endpoint divisions
also have polynomial bit cost. No exponential candidate enumeration is needed.
Section 6 gives the explicit size accounting.

## 5. Predecessors and the scope of the result

| Source | Exact relevant scope | Relation to this statement |
|---|---|---|
| [Kedlaya][Kedlaya], Sections 8–9 | Consecutive $`\max(18,2g)`$ count reconstruction; normalized Möbius cancellation and Newton residues; fewer-than-$`2g`$ question | Supplies the proof ingredients and question, but not the selected $`D_h`$/all-field/$`g\ge32`$ bound as a stated result |
| [Sutherland][Sutherland], Section 4.1, Lemma 4 | Base endpoints determine genus at most three in its stated large-$`q`$ range; exact genus-two formulas | Direct predecessor for low-genus endpoint reasoning, not a varying-genus theorem |
| [Hillar–Levine][HillarLevine], Theorem 1.1 and Conjecture 1.2 | Generic monic / palindromic polynomials, exponential sufficient initial segment; conjectured short initial segment | Different promises and first-sequence question; not an effective all-input Weil reconstruction theorem with this query set |
| [Hillar][Hillar], Theorem 1.1 | Characterization using the full nonzero cyclic-resultant sequence | Infinite-sequence uniqueness, not the present finite data/complexity guarantee |
| [Roy–Saxena–Venkatesh][RoySaxenaVenkatesh], Lemma 2.10 | Invokes the consecutive $`\max(18,2g)`$ theorem for its certification framework | Confirms that cited ingredient, not priority of the selected-support refinement |

The primary statements inspected in the original comparison do not subsume the
bound proved above. This is not equivalent to proving that no paper, thesis,
implementation or unpublished argument contains it. The literature search was
focused and its exact scope is recorded in the [source record](../experiments/all_field_reconstruction_v1/SOURCES.md).
The proved statement is a candidate contribution, not established publication
priority. The [current background comparison](../research/manuscript_background_v1/WEIL_RECONSTRUCTION.md)
and [cyclic-resultant background](../research/manuscript_background_v1/CYCLIC_RESULTANTS.md)
record the subsequent literature checks and qualifications.

The relationship to Kedlaya's question is precise: this gives fewer than $`2g`$
selected cardinality requests for the supplied-data reconstruction problem,
for every field size once $`g\ge32`$. It is not a theorem about the first
$`g+1`$ cyclic resultants, a global minimum-query result, or arbitrary complex
polynomials. It does not turn parameter counting into an information-theoretic
lower bound for discrete, variable-bit-length integer answers.

## 6. Explicit numerical bit-complexity audit

The following size accounting makes polynomial bit time checkable without
treating logarithms or rational arithmetic as unit-cost operations. Put
$`b=\lceil\log_2q\rceil`$, and $`B=b+\lceil\log_2(g+1)\rceil+1`$.

For $`j\le2h`$, the Weil estimate gives

```math
0\lt K_j\le2^{2g}q^{gj}.
```

Thus every input count has $`O(g^2b)`$ bits, and the complete supplied transcript
has $`O(g^3b)`$ bits. The bounds apply on promised inputs; malformed inputs with
arbitrary length cannot be read in time polynomial only in $`g`$ and $`b`$.

There is also a useful range-reduction bound independent of $`j`$:

```math
2^{-4g}\lt K_j/q^{gj}\lt2^{2g}.
```

Indeed $`1-1/\sqrt2>1/4`$ and $`1+1/\sqrt2\lt2`$. The exact exponent $`e`$
in $`K_j/q^{gj}=2^eu`$, $`1\le u\lt2`$, therefore satisfies
$`-4g\le e\lt2g`$.

Let $`\varepsilon=1/(24hq^h)`$. Each series used for $`\log u`$ or
$`\log2`$ has argument $`z\in[0,1/3]`$, and after $`M`$ terms its remainder
is at most $`(3/4)9^{-M}`$. The implementation's smallest local error allowance
is at least $`\varepsilon/(8g)`$. Consequently the uniform term cap

```math
M=\left\lceil\log_2(192 g h q^h)\right\rceil+1=O(gB)
```

suffices. It covers the multiplier $`e`$ of $`\log2`$, not only the mantissa's
logarithm.

If $`z=a/v`$ in lowest terms and its operands have $`O(g^2B)`$ bits, a common
denominator for the truncated series divides $`v^{2M+1}`$ times a product of
$`O(M)`$ positive integers at most $`2M+1`$. The rational tail denominator adds
only the factor $`v^2-a^2`$ and a linear term index. Hence each log centre and
error radius has

```math
O\bigl(M(g^2B+\log M)\bigr)=O(g^3B^2)
```

bits. Reduction of intermediate fractions prevents representing an
unnecessarily larger common denominator; even the temporary product before a
gcd obeys the same polynomial bound up to a constant factor.

A sum of at most $`g`$ such log fractions has at most $`O(g^4B^2)`$ bits,
including the weights $`q^n/(ni)`$. These bounds also cover rational radii and
cancellation in $`A_n`$. Each coefficient step is then rounded to an integer;
its denominators do not propagate multiplicatively through all later coefficient
steps. Coefficient and power-sum integers themselves have polynomial bit size by
the Weil bounds and Newton's identity. The endpoint divisions and final output
are polynomial-sized.

There are $`O(g^2B)`$ rational arithmetic operations under a loose count of all
series, log combinations and Newton sums. Ordinary exact integer addition,
multiplication, division and gcd on these polynomial-sized operands have
polynomial bit cost. This proves the claimed polynomial decoder time and
storage. These are upper bounds for an intentionally simple implementation,
not new optimal arithmetic bounds or hardware resource estimates.

[Kedlaya]: ../experiments/all_field_reconstruction_v1/SOURCES.md#1-kiran-s-kedlaya
[Sutherland]: ../experiments/all_field_reconstruction_v1/SOURCES.md#2-andrew-v-sutherland
[HillarLevine]: ../experiments/all_field_reconstruction_v1/SOURCES.md#3-christopher-j-hillar-and-lionel-levine
[Hillar]: ../experiments/all_field_reconstruction_v1/SOURCES.md#4-christopher-j-hillar
[RoySaxenaVenkatesh]: ../experiments/all_field_reconstruction_v1/SOURCES.md#5-diptajit-roy-nitin-saxena-and-madhavan-venkatesh
