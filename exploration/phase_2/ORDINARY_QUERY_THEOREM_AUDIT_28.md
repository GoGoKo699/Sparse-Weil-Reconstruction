# Ordinary-count reconstruction without a large-field hypothesis

For genus at least 32, a fixed set of fewer than 2g supplied cardinalities
reconstructs the Weil polynomial over every finite field. The decoder combines
normalized Mobius cancellation, Newton identities and endpoint equations with
a uniform tail bound and certified rational logarithms. The characteristic may
be two. The source comparison below attributes the reconstruction ingredients
and records the scope of the literature assessment.

## 1. The theorem and its exact input model

Let g>=32 and let q>=2 be an integer. Let

$$
P(T)=\prod_{j=1}^{2g}(1-\alpha_jT)=\sum_{j=0}^{2g}c_jT^j
$$

have integer coefficients, c_0=1, roots with |alpha_j|=sqrt(q), and reciprocity
c_(2g-j)=q^(g-j)c_j. Pair the alpha_j so that each pair has product q.
In the curve application, q is a prime power and P is the numerator of the zeta
function of a smooth projective geometrically connected genus-g curve.

Define K_m=product_j(1-alpha_j^m), and put h=g-2. Suppose the exact positive
integers K_m are supplied at the indices

$$
D_h=\{1,\ldots,h\}\cup\{2,4,\ldots,2h\}.
$$

**Theorem.** P is determined by these integers and can be reconstructed in time
polynomial in g and log(q). There are

$$
|D_h|=h+\lceil h/2\rceil<2g
$$

ordinary cardinality requests, and the largest requested degree is 2h=2g-4.
The requests are fixed, nonadaptive, and need not form an initial consecutive
sequence. This is a supplied-data / exact-cardinality-oracle theorem.

For g=32, this means 45 supplied counts, at degrees 1..30 and 32,34,..,60.
For g=64 it means 93 counts and maximum degree 124. The theorem includes q=2.
It does NOT assert that the first 45 counts suffice in the genus-32 example.
The constant 32 is a convenient sufficient threshold, not a lower bound.

## 2. Normalized Mobius reconstruction

Kedlaya [1, Section 8] does not require rounding each unnormalized power sum to
within one half. Previously recovered coefficients fix the next power sum
modulo its index through Newton identities. This means the error should be
controlled on S_n/n, where S_n=sum_j alpha_j^n. That is prior machinery, not a
new congruence principle.

His cutoff-dependent Mobius formula uses logarithms from the dense initial
part 1..h of D_h for low indices. At high indices two terms suffice because q^n
is large even when q itself is small. Combined with the final two endpoint
equations, this supplies the theorem above.

No extra query is hidden in the improvement. Put

$$
k_n=\max(2,\lfloor h/n\rfloor),\qquad
L_m=\log(K_m/q^{gm}).
$$

Every index ni with 1<=i<=k_n belongs to D_h. If floor(h/n)>=2, it is at most h;
otherwise only n and 2n are needed. Define

$$
A_n=-\frac{q^n}{n}\sum_{i=1}^{k_n}\frac{\mu(i)}{i}L_{ni}.
$$

This is the normalized, truncated Mobius statistic from [1], with a different
cutoff supported by a smaller selected data set.

## 3. Uniform analytic error proof

Reciprocity and the convergent logarithm series give

$$
L_m=-\sum_{r\ge1}\frac{S_{mr}}{r q^{mr}}.
$$

Consequently

$$
A_n=\frac{S_n}{n}+\frac{q^n}{n}\sum_{r>k_n}
   a_r\frac{S_{nr}}{r q^{nr}},\qquad
 a_r=\sum_{i\mid r,\ i\le k_n}\mu(i).
$$

The terms for 2<=r<=k_n vanish, |a_r|<=k_n, and |S_(nr)|<=2g q^(nr/2).
Thus, writing k=k_n,

$$
\left|A_n-\frac{S_n}{n}\right|
\le \frac{2gk}{n(k+1)}
       \frac{q^{-n(k-1)/2}}{1-q^{-n/2}}.
$$

Let rho=5/7. Since 1/sqrt(q)<=1/sqrt(2)<rho, an entirely rational upper bound is

$$
E_{g,n}=\frac{2gk}{n(k+1)}
       \frac{\rho^{n(k-1)}}{1-\rho^n}.
$$

We now prove E_(g,n)<1/3 for EVERY g>=32 and 1<=n<=h, rather than extrapolating
from a finite parameter table. Here h>=30 and g/h<=16/15.

**Case A: n>h/3.** Then k=2, so

$$
E_{g,n}<\frac{64}{15}\frac{\rho^{10}}{1-\rho^{10}}
 =\frac{15625000}{102266109}<\frac13.
$$

**Case B: h/6<n<=h/3.** Here k>=3. Because n>h/(k+1), we have
n(k-1)>h(k-1)/(k+1)>=h/2. Also 2g/n<12g/h<=64/5 and n>h/6>=5. Hence

$$
E_{g,n}<\frac{64}{5}\frac{\rho^{15}}{1-\rho^5}
 =\frac{195312500000}{1932413178409}<\frac13.
$$

**Case C: n<=h/6.** We have n(k-1)>h-2n>=2h/3. Moreover
1/[n(1-rho^n)]<=1/(1-rho)=7/2. Therefore

$$
E_{g,n}<7g\rho^{2(g-2)/3}
 \le224\rho^{20}
 =\frac{3051757812500000}{11398895185373143}<\frac13.
$$

The middle inequality holds uniformly: the logarithmic derivative of
x*rho^(2(x-2)/3) is 1/x-(2/3)log(7/5)<0 for x>=32, using
log(7/5)>=2/7. This finishes the analytic proof. The executable checks of the
three rational constants are supplementary, not the reason the bound holds
for arbitrarily large genus.

## 4. Integer reconstruction and clean numerical control

Assume c_1,..,c_(n-1) and S_1,..,S_(n-1) are known. Set

$$
B_n=\sum_{i=1}^{n-1}c_{n-i}S_i.
$$

Newton's identity gives c_n=-S_n/n-B_n/n. If A_n is evaluated with numerical
error at most 1/24, then

$$
-A_n-B_n/n
$$

lies within 1/3+1/24=3/8 of the INTEGER c_n. Certified interval rounding
therefore recovers c_n uniquely. Then S_n=-n*c_n-B_n is exact. This incorporates
Newton's residue information; rounding n*A_n directly to the nearest integer
would require a stronger error guarantee and is not the decoder used here.

Proceed through n=h=g-2. Since K_1=P(1) and K_2=P(1)P(-1), compute
T_1=P(-1)=K_2/K_1 by exact division; this is algebra, not a physical twist query.
With

$$
R_+=K_1-\sum_{i=0}^{g-2}(1+q^{g-i})c_i,\qquad
R_-=T_1-\sum_{i=0}^{g-2}(-1)^i(1+q^{g-i})c_i,
$$

and s=(-1)^(g-1), recover

$$
c_{g-1}=\frac{R_++sR_-}{2(q+1)},\qquad
c_g=\frac{R_+-sR_-}{2}.
$$

Reciprocity supplies the remaining coefficients. Reference [2] supplies the
direct low-genus predecessors of these endpoint equations.

### Logarithms must be range-reduced in small fields

The unscaled atanh series can converge extremely slowly when its positive
rational argument is tiny. Range reduction gives a polynomial-time small-field
implementation: for x>0, compute the exact decomposition x=2^e*u with 1<=u<2.
Then

$$
\log x=e\log2+2\sum_{j\ge0}\frac{z^{2j+1}}{2j+1},\qquad
z=(u-1)/(u+1),\quad |z|\le1/3.
$$

A truncated sum of m terms has tail at most
2*|z|^(2m+1)/[(2m+1)(1-z^2)]. Compute each L_j to absolute error at most

$$
\varepsilon=\frac{1}{24h q^h}.
$$

The resulting numerical error in A_n is at most
(q^n/n)*sum_(i<=k)|mu(i)|/i*epsilon <= q^h*h*epsilon=1/24.
Errors from e*log2 are included; logarithms are not treated as exact primitives.
The implementation uses Fraction arithmetic, with rational error radii.

Each input K_j has O(gj log q+g) bits by the Weil bounds, with j<=2h.
The required precision is O(h log q+log h) bits. Range reduction and the
geometric series therefore use polynomially many rational operations of
polynomial bit length. Newton identities and endpoint divisions also have
polynomial bit cost. No exponential candidate enumeration is needed.

## 5. Comparison with predecessor results

| Source | Exact relevant scope | Relation to this statement |
|---|---|---|
| Kedlaya [1], Sections 8-9 | Consecutive max(18,2g) count reconstruction; normalized Mobius cancellation and Newton residues; fewer-than-2g question | Supplies the proof ingredients and question, but not the selected D_h/all-field/g>=32 bound as a stated result |
| Sutherland [2], Section 4.1, Lemma 4 | Base endpoints determine genus at most three in its stated large-q range; exact genus-two formulas | Direct predecessor for low-genus endpoint reasoning, not a varying-genus theorem |
| Hillar-Levine [3], Theorem 1.1 and Conjecture 1.2 | Generic monic / palindromic polynomials, exponential sufficient initial segment; conjectured short initial segment | Different promises and first-sequence question; not an effective all-input Weil reconstruction theorem with this query set |
| Hillar [4], Theorem 1.1 | Characterization using the full nonzero cyclic-resultant sequence | Infinite-sequence uniqueness, not the present finite data/complexity guarantee |
| Roy-Saxena-Venkatesh [5], Lemma 2.10 | Invokes the consecutive max(18,2g) theorem for its certification framework | Confirms that cited ingredient, not priority of our pruning |

The inspected primary statements do not subsume the bound proved above.
The focused search and its limits are recorded in the companion SOURCES.md;
publication priority remains qualified by that scope.

This addresses Kedlaya's fewer-than-2g question for selected ordinary count
requests in the supplied-data reconstruction problem, for every field size once
g>=32. The selected set differs from the initial sequence in the generic
cyclic-resultant conjecture. Its cardinality is a sufficient query bound.

## 6. Exact verification controls

The standard-library decoder receives only q, g and the declared count map.
Seven supplied Weil-polynomial controls cover genera 32,33,48 and q=2,3,4,5,
including repeated roots and degree-64 or mixed higher-degree factors. Their
orders are generated from independently specified factor recurrences. All 489
recovered coefficients and 227 recovered traces agree exactly with the supplied
polynomials. No assertion is made that these
controls are Jacobians of curves.

The factorwise order generator is separately checked against 36 small companion-
determinant computations. Additional checks cover 4030 finite parameter pairs,
128 Mobius divisor identities, the three rational uniform proof constants,
seven range-reduced logarithms (including 2^4096 and its reciprocal), and eleven
malformed cases. Decimal logarithms are only a secondary numerical spot check;
the decoder and its error proof use exact rational enclosures. The two extreme
range reductions need 23 log2-series terms rather than a near-unit-ratio expansion.
The finite checks do not replace the uniform proof or authenticate arbitrary data.

Primary links and inspection records: [SOURCES.md](../../experiments/all_field_reconstruction_v1/SOURCES.md).
Executable source and reproduction: [README.md](../../experiments/all_field_reconstruction_v1/README.md).
