# Analytic and algorithmic background

28 September 2026. Background and attribution for a future manuscript;
manuscript drafting remains on hold. The existing theorems, precision schedules,
and executable controls are unchanged.

This note separates standard algebra and numerical analysis from the estimates
specific to this reconstruction problem. The guarantee is deterministic
polynomial **bit** time on the promised inputs, with both $g$ and $\log q$
variable. It is not a count of unit-cost real arithmetic operations.

## 1. Which ingredients need attribution

| Ingredient | Role and attribution |
|---|---|
| Logarithms of normalized resultants, truncated Möbius cancellation, and Newton residue information | The reconstruction framework of [Kedlaya2006], Section 8; see the [preserved derivation](../../exploration/phase_2/ORDINARY_QUERY_THEOREM_AUDIT_28.md). |
| Formal logarithm/exponential identities and Newton identities | Elementary identities recalled below, with no separate novelty claim. |
| Weighted $\ell^1$ coefficient algebra and contraction principle | Standard tools; the needed facts are proved below. |
| Range reduction and logarithm series | Standard multiple-precision methods; [BrentZimmermann2010], Sections 4.3–4.4, especially printed p. 141. |
| Integer arithmetic, division, and gcd reduction | Standard bit-cost accounting; [BrentZimmermann2010], Sections 1.2, 1.3.1, 1.4.1, and 1.6.1. |
| Sparse support and all-field tail estimates | Repository-specific statements in [Note 28](../../exploration/phase_2/ORDINARY_QUERY_THEOREM_AUDIT_28.md), with endpoint attribution retained there. |
| Palindromic completion, alias bound, invariant ball, and quadratic field threshold | Repository-specific estimates in [the first-$g$ theorem](../first_g_reconstruction_v1/THEOREM.md), Sections 2–5. |
| Certified finite iteration, precision allocation, and denominator bounds | Theorem Sections 6–9 and the [consolidation audit](../consolidation_v1/AUDIT.md), Section 3. |

The first-$g$ and polynomial-time precedents belong in the separate predecessor
comparison. None of the standard tools in this table establishes the new
field-size threshold by itself.

## 2. Formal identities and the meaning of the logarithmic data

Put $s_m=\sum_i\alpha_i^m$. In the formal power-series ring over a
characteristic-zero field,

$$
\log P(T)=-\sum_{m\ge1}\frac{s_m}{m}T^m.
$$

Differentiating and using $P'=P(\log P)'$ gives

$$
n c_n=-\sum_{j=1}^{n}c_{n-j}s_j,\qquad c_0=1.
$$

Thus a known power-sum prefix determines the corresponding coefficients by
Newton identities. A resultant $K_n$ does not directly supply $s_n$: under
the reciprocal Weil promises its normalized real logarithm is

$$
L_n=\log(K_n/q^{gn})
   =-\sum_{k\ge1}\frac{s_{nk}}{kq^{nk}}.
$$

The sum converges absolutely because $|\alpha_i/q|=q^{-1/2}<1$.
Positivity and the absence of a logarithm-branch ambiguity are established in
the [audit](../consolidation_v1/AUDIT.md), Section 2. This distinction between
a power sum and its mixture with higher indices is the reconstruction problem.

For a cutoff $k_0$, substitution into
$-q^n\sum_{i=1}^{k_0}\mu(i)L_{ni}/(ni)$ makes the coefficient of the
$s_{nr}$ term proportional to
$\sum_{i\mid r,\ i\le k_0}\mu(i)$. The usual divisor identity makes this
sum zero for $2\le r\le k_0$. What remains to prove is the support condition,
the tail bound, and an exact recovery margin. These are the specific tasks in
Note 28, not new Möbius inversion or new Newton identities.

The finite first-$g$ algorithm also uses only formal identities. If
$\log P_c=\sum b_mT^m$ and $\exp Z=\sum d_mT^m$, then
$P_c'=P_c(\log P_c)'$ and $(\exp Z)'=Z'\exp Z$ give the exact recurrences
in theorem Section 8. Their coefficients are computed rationally, without
finding the roots of any candidate polynomial.

## 3. The weighted algebra and what contraction contributes

For $r>0$, the space

$$
\mathcal A_r=\left\{\sum_{m\ge0}h_mz^m:
               \sum_{m\ge0}|h_m|r^m<\infty\right\}
$$

is isometric to $\ell^1$ under $h_m\mapsto h_mr^m$, so it is complete.
Its Cauchy product satisfies

$$
\|HG\|_r
\le\sum_{i,j\ge0}|h_i|r^i|g_j|r^j
=\|H\|_r\|G\|_r.
$$

Coefficient truncation has norm at most one. If
$\|U\|_r,\|V\|_r\le s<1$, telescoping $U^j-V^j$ inside the logarithm
series gives

$$
\|\log(1+U)-\log(1+V)\|_r
\le\frac{\|U-V\|_r}{1-s}.
$$

Similarly, for $\|H\|_r,\|G\|_r\le R$, the exponential series gives
$\|\exp H-\exp G\|_r\le e^R\|H-G\|_r$.
These elementary bounds require no theorem about the roots of intermediate
polynomials and no root-separation hypothesis.

A contraction $T$ with factor $0\le\lambda<1$ on a closed invariant ball
has a unique fixed point: successive differences form a geometric bound,
completeness gives a limit, continuity makes it fixed, and
$\|a-b\|\le\lambda\|a-b\|$ proves uniqueness. When a true fixed point
$a_*$ is already supplied by the problem's promise, the error calculation is
even more direct. If each computed step has norm error at most $\eta$, then

$$
E_{t+1}\le\lambda E_t+\eta,
\qquad
E_t\le\lambda^tE_0+
\frac{1-\lambda^t}{1-\lambda}\eta,
$$

provided the computed iterates stay in the ball.

The research work is the construction of the map and proof of those
conditions. Theorem Sections 2–7 supply $r=1/(8g)$, the palindromic completion,
the alias estimate, a factor below $1/6$, a strict ball margin, and finite
errors compatible with that margin when $q\ge65536g^2$.
The [method-boundary proposition](../consolidation_v1/METHOD_BOUNDARY.md)
concerns this particular norm architecture. It is not a general obstruction
to reconstruction below a quadratic field size.

## 4. A certified logarithm is a finite rational computation

Brent–Zimmermann's argument-reduction discussion and odd-power logarithm
series provide standard numerical background [BrentZimmermann2010]. The
repository uses the following explicit specialization, whose error and operand
sizes are proved in theorem Section 9.1 and [Note 29](../../exploration/phase_2/RECONSTRUCTION_PROOF_REVIEW_29.md), Section 3.

For positive rational $x$, exact comparisons give $x=2^eu$ with $1\le u<2$.
Set $z=(u-1)/(u+1)$, so $0\le z<1/3$. Then

$$
\log x=e\log2+
  2\sum_{j=0}^{s-1}\frac{z^{2j+1}}{2j+1}+R_s,
\qquad
|R_s|\le\frac{2|z|^{2s+1}}{(2s+1)(1-z^2)}.
$$

The bound follows by replacing all remaining odd denominators by $2s+1$
and summing a geometric series. The same formula at $z=1/3$ encloses
$\log2$. Its error must be multiplied by $|e|$ when the two enclosures are
combined. All displayed finite terms and tail bounds are rational.

Dyadic rounding of the enclosure center adds a separately budgeted error.
No call to a floating-point logarithm is needed for the guarantee. Faster
elementary-function algorithms are not required, and their asymptotic
complexities are not being claimed for this implementation.

## 5. Why iteration count alone is not a complexity proof

With $b=\lceil\log_2q\rceil$ and
$\Lambda=g(b+\lceil\log_2(g+1)\rceil+1)$, the first-$g$ proof uses
$O(\Lambda)$ iterations, series cutoff, and stored precision. It also proves
polynomial bit length for every intermediate fraction. This second part is
essential: exact nonlinear iterations can repeatedly raise old denominators
to powers even when the number of iterations is small.

Here every completed step resets the low coefficients to denominator
$2^B$. If $M$ is the formal-log cutoff and $L$ is the dyadic input-log
precision, the audit gives a common denominator

$$
D=2^{BM+L}\operatorname{lcm}(1,\ldots,M)q^M
$$

for the corrected exponent coefficients. A degree-$j$ exponential coefficient
has denominator dividing $D^j j!$. The coefficient-magnitude estimates bound
the numerators too. Reduced fraction arithmetic keeps temporary operations
within polynomial bit length; dyadic quantization prevents those bounds from
compounding without control across iterations.

Standard integer arithmetic then turns the polynomial number of operations
into polynomial bit time; [BrentZimmermann2010], Chapter 1, gives the
arithmetic background. The repository does not require fast multiplication,
an optimal exponent, or a unit-cost real-number model.

The input transcript also has to fit this accounting. The Weil bound gives
$K_n\le2^{2g}q^{gn}$; both schedules use $O(g)$ indices of size $O(g)$,
so promised transcripts have $O(g^3\log q)$ bits. Each coefficient has
$O(g\log q)$ bits, and the polynomial output has $O(g^2\log q)$ bits.
See the [application note](../finite_field_application_v1/COROLLARIES.md)
for why a fully expanded abelian-variety zeta function is a different,
potentially exponential-sized output.

## 6. Wording to preserve when drafting resumes

- State the true-count, integrality, reciprocity, modulus, genus, and field-size
  promises with the theorem. The parameter-only runtime bound applies to
  promised transcripts, not arbitrary malformed integers of unbounded length.
- Describe the analytic normalization as a proof device. The finite algorithm
  works in raw rational coefficients and does not compute $\sqrt q$.
- Retain the invariant-ball and bit-length arguments. A contraction estimate
  or an arithmetic-operation count alone does not establish the stated decoder.
- Cite standard machinery as standard. Attribute the threshold, sparse support,
  and their certified recovery bounds only to the corresponding repository
  statements; first-$g$ recovery itself has a predecessor.
- Keep count acquisition, authentication, geometric realization, and expanded
  zeta output separate from reconstruction. Numerical controls support the
  implementation; they do not replace the uniform proof.

## Sources inspected for this note

**[Kedlaya2006]** Kiran S. Kedlaya, *Quantum computation of zeta functions
of curves*, Computational Complexity 15 (2006), 1–19.
[Primary preprint, v3](https://arxiv.org/pdf/math/0411623v3), Section 8,
printed pp. 11–12. Used here only for the classical reconstruction machinery.

**[BrentZimmermann2010]** Richard P. Brent and Paul Zimmermann,
*Modern Computer Arithmetic*, Cambridge University Press, 2010.
[Author page](https://members.loria.fr/PZimmermann/mca/pub226.html);
[author-hosted version 0.5.9, 7 October 2010](https://www.loria.fr/~zimmerma/mca/mca-cup-0.5.9.pdf).
The locators above refer to printed page numbers in that version, whose
pagination differs from the PDF viewer's page count. The author-hosted text
and relevant sections were inspected; no third-party code or source text
was imported.
