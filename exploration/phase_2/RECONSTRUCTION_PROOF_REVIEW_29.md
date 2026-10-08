# Reconstruction theorem: proof and bit-complexity audit

This internal mathematical and implementation audit checks the all-field
reconstruction theorem by a fresh proof derivation, explicit bit-size analysis,
and an independently constructed irreducible-polynomial control. The analysis
supports its stated genus threshold, query set, and mathematical hypotheses.
The source comparison and its search scope appear in Section 6.

## 1. The audited statement

For g>=32, q>=2 an integer, and a reciprocal integral q-Weil polynomial

$$
P(T)=\prod_{i=1}^{2g}(1-\alpha_iT),\qquad |\alpha_i|=\sqrt q,
$$

with constant coefficient 1 and c_(2g-i)=q^(g-i)c_i, put h=g-2 and

$$
D_h=\{1,\ldots,h\}\cup\{2,4,\ldots,2h\}.
$$

The exact integers K_m=product_i(1-alpha_i^m), for m in D_h, determine P and
permit deterministic reconstruction in polynomial time in g and log q. The
cardinalities are supplied inputs; no group-order computation is performed by
the decoder. There are h+ceil(h/2) requests and maximum degree 2g-4. In the curve
application q is a prime power, but primality/prime-power recognition and curve
realizability are not tasks of this reconstruction theorem.

The natural application is an unknown curve's Jacobian cardinality data, NOT
ordinary curve point counts. Given the first g curve point counts, the usual
Newton reconstruction is already a different, simpler input problem.

The sufficient query bound applies to the selected set D_h, rather than the
first h+ceil(h/2) indices.

## 2. Proof audit

### Root conventions, positivity, and logarithm branches

The alpha_i are the inverse roots of P, not its roots as a polynomial in T.
The monic characteristic polynomial is chi(X)=X^(2g)P(1/X). Reciprocity makes the
multiset of alpha_i invariant under alpha -> q/alpha. The product is q^g.
Hence

$$
\frac{K_m}{q^{gm}}=\prod_i(1-\alpha_i^{-m}).
$$

Each alpha_i^-m has modulus <1. Conjugate factors pair, and the real factors
1-alpha_i^-m are positive. The analytic logarithm defined by its convergent power
series therefore sums to the ordinary real logarithm of the positive product.
There is no omitted complex-argument multiple of 2*pi*i. Integrality of K_m also
follows from the resultant of the integral monic chi with X^m-1. Nonvanishing is
forced by |alpha_i|>1. These properties need not be tested by approximate roots.

It follows exactly that

$$
L_m:=\log(K_m/q^{gm})=-\sum_{r\ge1}\frac{S_{mr}}{r q^{mr}},
\qquad S_j=\sum_i\alpha_i^j.
$$

### Cancellation and support

For k=max(2,floor(h/n)), expand

$$
A_n=-\frac{q^n}{n}\sum_{i=1}^k\frac{\mu(i)}{i}L_{ni}.
$$

Regrouping the absolutely convergent series assigns coefficient
sum_(i|r,i<=k) mu(i) to its r-th term. This is 1 at r=1 and 0 at 2<=r<=k.
Every used ni is in D_h: it is at most h when floor(h/n)>=2, and otherwise it is
n or 2n. Thus the proof does not consume an unlisted count.

The remainder has magnitude at most

$$
\frac{2gk}{n(k+1)}\frac{q^{-n(k-1)/2}}{1-q^{-n/2}}.
$$

The factor n in the denominator is essential: the approximated object is S_n/n.
The q^n prefactor and the exponent n(k-1) both survive the rederivation.

### Uniform bound and boundaries

Replacing q^-1/2 by rho=5/7 enlarges the bound, since (5/7)^2>1/2.
At h>=30, g/h<=16/15. The three regions in Note 28 include their boundaries
correctly: n>h/3; h/6<n<=h/3; n<=h/6. The corresponding genus-independent
upper bounds are

$$
\frac{64}{15}\frac{\rho^{10}}{1-\rho^{10}},\qquad
\frac{64}{5}\frac{\rho^{15}}{1-\rho^5},\qquad
224\rho^{20}.
$$

All are strictly below 1/3. In the third region the remaining quantity
7g*rho^(2(g-2)/3) decreases for g>=32: its logarithmic derivative is at most
1/32-4/21<0, using log(7/5)>=2/7. Thus checking the three rational constants is
not an extrapolation from finite genera. The value 32 is a sufficient genus
threshold.

### Exact induction rather than floating-point error propagation

Assuming earlier coefficients and power sums already recovered exactly, Newton's
identity gives

$$
c_n=-S_n/n-B_n/n,\qquad
B_n=\sum_{i=1}^{n-1}c_{n-i}S_i.
$$

The exact integer B_n incurs no approximation error. A numerical enclosure of
A_n of radius at most 1/24, enlarged by the analytic error bound <1/3, gives an
interval for c_n with radius <3/8 and length <3/4. It contains the true integer
and cannot contain a second one. Recovering S_n=-n*c_n-B_n then resets the next
stage to exact integers. Large earlier coefficients do NOT multiply uncertain
power sums, because no uncertain power sum is retained.

Finally K_2/K_1=P(-1). With c_0 through c_(g-2) known, the two endpoint equations
have coefficient matrix with determinant of absolute value 2(q+1), which is
nonzero. Their exact divisions recover c_(g-1),c_g, and reciprocity gives the
remaining coefficients. This step is algebraic and requires no physical twist.

**No incorrect step was found in this proof chain under the declared promises.**
The conclusion does not authenticate those promises for arbitrary input data.

## 3. Explicit numerical bit-complexity audit

The original note asserts polynomial bit time. The following size accounting
makes that assertion checkable without treating logarithms or rational arithmetic
as unit-cost operations. Put b=ceil(log2 q), and B=b+ceil(log2(g+1))+1.

For j<=2h, the Weil estimate gives

$$
0<K_j\le2^{2g}q^{gj}.
$$

Thus every input count has O(g^2 b) bits, and the complete supplied transcript has
O(g^3 b) bits. The bounds apply on promised inputs; malformed inputs with arbitrary
length cannot be read in time polynomial only in g and b.

There is also a useful range-reduction bound independent of j:

$$
2^{-4g}<K_j/q^{gj}<2^{2g}.
$$

Indeed 1-1/sqrt(2)>1/4 and 1+1/sqrt(2)<2. The exact exponent e in
K_j/q^(gj)=2^e u, 1<=u<2, therefore satisfies -4g<=e<2g.

Let epsilon=1/(24 h q^h). Each series used for log(u) or log(2) has argument
z in [0,1/3], and after M terms its remainder is at most (3/4)*9^-M.
The inherited implementation's smallest local error allowance is at least
epsilon/(8g). Consequently the uniform term cap

$$
M=\left\lceil\log_2(192 g h q^h)\right\rceil+1=O(gB)
$$

suffices. It covers the multiplier e of log(2), not only the mantissa's logarithm.

If z=a/v in lowest terms and its operands have O(g^2 B) bits, a common denominator
for the truncated series divides v^(2M+1) times a product of O(M) positive integers
at most 2M+1. The rational tail denominator adds only the factor v^2-a^2 and a
linear term index. Hence each log centre and error radius has

$$
O\bigl(M(g^2B+\log M)\bigr)=O(g^3B^2)
$$

bits. Reduction of intermediate fractions prevents representing an unnecessarily
larger common denominator; even the temporary product before a gcd obeys the same
polynomial bound up to a constant factor.

A sum of at most g such log fractions has at most O(g^4 B^2) bits, including the
weights q^n/(ni). These bounds also cover rational radii and cancellation in A_n.
Each coefficient step is then rounded to an integer; its denominators do not
propagate multiplicatively through all later coefficient steps. Coefficient and
power-sum integers themselves have polynomial bit size by the Weil bounds and
Newton's identity. The endpoint divisions and final output are polynomial-sized.

There are O(g^2 B) rational arithmetic operations under a loose count of all series,
log combinations and Newton sums. Ordinary exact integer addition, multiplication,
division and gcd on these polynomial-sized operands have polynomial bit cost.
This proves polynomial decoder time and storage for the implementation.

## 4. A structurally different, independently checked control

An irreducible polynomial of degree 64 at q=2, g=32 tests the decoder on a
structurally different input from quadratic products and cyclotomic-shaped
factors.

Take the integer symmetric tridiagonal matrix A with off-diagonal entries 1 and
the 32 diagonal entries recorded in CONTROL.json. Let F(Y)=det(YI-A). A standard
three-term determinant recurrence gives its integer coefficients. All 64 leading
principal minors of (11/4)I+A and (11/4)I-A are positive, checked exactly.
Therefore every root t of F lies in (-11/4,11/4), strictly inside (-2sqrt(2),2sqrt(2)).

The degree-32 reduction of F modulo 7 is irreducible. The independent finite-field
check verifies Y^(7^32)=Y mod F and gcd(F,Y^(7^16)-Y)=1; these are the complete
Rabin tests since 2 is the only prime dividing 32. Hence F is irreducible over Q.

Set

$$
\chi(X)=X^{32}F(X+2/X),\qquad P(T)=T^{64}\chi(1/T).
$$

For each root t, X^2-tX+2 has conjugate roots of magnitude sqrt(2). Thus chi is a
2-Weil polynomial. Moreover Q(t) is totally real and t^2-8 is negative at every
real embedding, so this discriminant is not a square in Q(t). Since t=alpha+2/alpha,
chi has degree 64 and is irreducible over Q. This proof certifies the polynomial
class without floating-point roots, not curve or abelian-variety realizability.

The 45 K-values were first generated by SymPy 1.14.0 resultants. The standalone
audit instead derives every value by a separately implemented exact circulant
determinant det(chi(S_m)), where S_m is the cyclic shift matrix. The resulting
integer list matches the stored fingerprint of the SymPy calculation. No SymPy
installation is needed to replay the audit. All 589310 Bareiss divisions were
exact. The inherited decoder receives only q,g and these count values, and
recovers all 65 coefficients and 30 required power sums exactly.

Four further runs shift each rational logarithm centre to different edges of
its permitted numerical enclosure while enlarging its radius accordingly. The
output is unchanged in all four. These test the error interface. The log
computations used at most 13 terms versus the proved cap 49 for this control.

## 5. Reconstruction and input authenticity

Replacing just K_60 by K_60+1 still lets the inherited decoder return the same P.
Its log change is too small to affect the integer rounding, and the endpoints
K_1,K_2 are unchanged. Exact resultant replay from the returned polynomial detects
that one-unit discrepancy.

Thus successful reconstruction and divisibility checks are not a test of the
input's authenticity. An optional all-query resultant replay can enforce internal
transcript consistency; even that would not bind a transcript to a separately
claimed curve. The theorem correctly receives TRUE values as a promise. The
experiment therefore distinguishes reconstruction from authentication.

## 6. Priority and significance after direct source comparison

The primary documents reread were Kedlaya [1], Sutherland [2], Hillar-Levine [3],
Hillar [4], and Roy-Saxena-Venkatesh [5]. The precise access and search scope is in
SOURCES.md. The comparison does not identify an earlier statement that supplies
the same selected-query, all-field, varying-genus polynomial-time guarantee.

The attribution remains important. Kedlaya supplies the normalized Mobius and
Newton-residue framework and asks about fewer order-oracle calls. Sutherland is
a direct predecessor for low-genus endpoint reasoning. Hillar's infinite-sequence
uniqueness and Hillar-Levine's generic finite-sequence results do not by themselves
give this uniform Weil decoder. In particular, the existence of a short polynomial
recurrence whose coefficients depend on the unknown polynomial is not an efficient
reconstruction procedure from that many supplied observations. Scaling a q-Weil
polynomial to roots on the unit circle also changes the observed resultants and
integer coefficient lattice; it does not silently turn their palindromic question
into ours. The later preprint's use of the consecutive bound is not a priority
certificate for our improvement.

The search is limited to the sources and access scope recorded in SOURCES.md;
it does not establish publication priority.

The contribution is a deterministic reconstruction query theorem for a structured
integer-polynomial class, with exact implementation and a comparison to the known
sufficient bound. Its scope is unbounded in genus and includes every field size.

[Audit source, fixture and verifier](../../experiments/reconstruction_audit_v1/README.md).
[Primary-source inspection record](../../experiments/reconstruction_audit_v1/SOURCES.md).
