# Finite-field corollaries and output size

27 September 2026 (UTC). Application and output clarification for the two
existing supplied-count reconstruction theorems.

The statements below are standard finite-field consequences of those theorems,
not additional novelty claims or improvements to their thresholds. They make
the input promises and the representation of the recovered object explicit.
The original proofs, decoders, and reference reports are retained unchanged.

## 1. Abelian varieties

Let $`q`$ be a prime power and let $`A/\mathbb F_q`$ be an abelian variety of known
dimension $`g\ge1`$. For a prime $`\ell`$ not dividing $`q`$, write

```math
P_A(T)=\det(1-T\pi_A\mid V_\ell A)
      =\prod_{i=1}^{2g}(1-\alpha_iT)
      =\sum_{j=0}^{2g}c_jT^j,
```

where $`V_\ell A`$ is the rational Tate module and $`\pi_A`$ is the $`q`$-power
Frobenius endomorphism. This convention specifies the endomorphism directly,
without an arithmetic/geometric Galois convention. The usual monic Frobenius
characteristic polynomial is $`X^{2g}P_A(1/X)`$.

The standard Frobenius properties give

```math
P_A\in\mathbb Z[T],\quad c_0=1,\quad
|\alpha_i|=\sqrt q,\quad
c_{2g-j}=q^{g-j}c_j\quad(0\le j\le g),
```

and, for every $`m\ge1`$,

```math
K_m:=\#A(\mathbb F_{q^m})=\prod_{i=1}^{2g}(1-\alpha_i^m).
```

These are precisely the algebraic promises of the reconstruction theorems.
See [Milne, AVs, Theorem 19.1][avs] for the Frobenius and cardinality facts.
Reciprocity follows from the Frobenius pairing $`\alpha\leftrightarrow q/\alpha`$
and $`\prod_i\alpha_i=q^g`$.

**Corollary.** Given $`q`$, $`g`$, and the indicated **true exact cardinalities**,
either of the following regimes permits unique deterministic reconstruction of
$`P_A`$ in time polynomial in $`g`$ and $`\log q`$:

| Regime | Supplied indices | Number of supplied values |
|---|---|---:|
| $`g\ge1`$, $`q\ge65{,}536g^2`$ | $`1,\ldots,g`$ | $`g`$ |
| $`g\ge32`$, every prime-power $`q`$ | $`D_{g-2}=\{1,\ldots,g-2\}\cup\{2,4,\ldots,2g-4\}`$ | $`g-2+\lceil(g-2)/2\rceil\lt 2g`$ |

**Proof.** Substitute the displayed Frobenius properties and cardinality
identity into the [first-$`g`$ theorem](../first_g_reconstruction_v1/THEOREM.md)
or the [preserved all-field theorem](../../exploration/phase_2/ORDINARY_QUERY_THEOREM_AUDIT_28.md).
Their supplied indices, hypotheses, and bit-complexity conclusions apply
without alteration. In the second regime the largest supplied index is
$`2g-4`$. Unlike the abstract algebraic theorems, this geometric application
requires $`q`$ to be a prime power. No simplicity, ordinarity, squarefreeness,
genericity, or polarization-as-input assumption is needed. $`\square`$

By [Tate, Theorem 1(c)][tate], $`P_A`$ determines the **$`\mathbb F_q`$-isogeny
class** of $`A`$. This is a statement about the invariant recovered: the decoder
does not construct an equation for $`A`$, an isogeny, or an isomorphism class.
It neither acquires nor authenticates the counts. An input promised to arise
from an abelian variety needs no further realizability test for this corollary;
the decoder does not certify that arbitrary data have such an origin.

## 2. Curves and Jacobians

Let $`C/\mathbb F_q`$ be a smooth, projective, geometrically connected curve of
genus $`g\ge1`$, and put $`A=J_C`$. Then

```math
Z_C(T):=\exp\left(\sum_{m\ge1}\#C(\mathbb F_{q^m})\frac{T^m}{m}\right)
       =\frac{P_{J_C}(T)}{(1-T)(1-qT)}.
```

This is the standard curve zeta identity; see [Milne, JVs, Theorem 11.1 and
Corollary 11.4][jvs]. Thus, in either regime of Section 1, the supplied
**Jacobian cardinalities** $`K_m=\#J_C(\mathbb F_{q^m})`$ recover the curve zeta
function as an ordinary rational function with integer coefficients, in
deterministic polynomial bit time. The denominator is known and the numerator
has degree $`2g`$. No rational point on $`C`$, hyperellipticity assumption, or curve
equation is required. The curve itself is not reconstructed up to isomorphism.

The input distinction matters. If instead the first $`g`$ **ordinary curve point
counts** $`N_m=\#C(\mathbb F_{q^m})`$ are supplied, then for every prime-power $`q`$
the standard trace formula gives

```math
s_m=\sum_i\alpha_i^m=q^m+1-N_m\qquad(1\le m\le g).
```

Newton identities recover the first half of the numerator by

```math
c_0=1,\qquad
jc_j=-\sum_{m=1}^{j}c_{j-m}s_m\qquad(1\le j\le g),
```

and reciprocity recovers the other half. This uses only polynomially many
integer operations on polynomially bounded bit lengths. Consequently, the
quadratic field-size theorem is a result about supplied **Jacobian/abelian
cardinalities**, not a new first-$`g`$ reconstruction theorem for ordinary curve
point counts. The case $`g=0`$ has numerator $`1`$ and requires no reconstruction.

## 3. Compact output versus an expanded abelian-variety zeta function

For $`P_A`$, the Weil coefficient bound

```math
|c_j|\le {2g\choose j}q^{j/2}\qquad(0\le j\le2g)
```

gives $`O(g\log q)`$ bits per coefficient and $`O(g^2\log q)`$ bits for the
entire coefficient list. Also,
$`1\le K_m\le(1+q^{m/2})^{2g}`$, so each supplied cardinality has
$`O(gm\log q)`$ bits. Both schedules contain $`O(g)`$ indices of size $`O(g)`$,
and hence have total input length $`O(g^3\log q)`$.

The full zeta function of a higher-dimensional abelian variety is a different
output object. For $`S\subseteq\{1,\ldots,2g\}`$ put
$`\alpha_S=\prod_{i\in S}\alpha_i`$, including $`\alpha_\varnothing=1`$, and set

```math
E_k(T)=\prod_{|S|=k}(1-\alpha_ST),\qquad 0\le k\le2g.
```

These polynomials have integer coefficients: their coefficients are symmetric
integer polynomials in the $`\alpha_i`$, hence integer polynomials in the
elementary symmetric functions defining $`P_A`$. Their degrees are
$`\binom{2g}{k}`$. Expanding the point-count product gives

```math
K_m=\sum_{S\subseteq\{1,\ldots,2g\}}(-1)^{|S|}\alpha_S^m.
```

Taking formal logarithms therefore yields the standard identity
([Milne, AVs, Corollary 19.4][avs])

```math
Z_A(T):=\exp\left(\sum_{m\ge1}K_m\frac{T^m}{m}\right)
       =\frac{U(T)}{V(T)},\qquad
U(T)=\prod_{k\text{ odd}}E_k(T),\quad
V(T)=\prod_{k\text{ even}}E_k(T).
```

**Output-size observation.** In this fraction $`U(0)=V(0)=1`$, there is no
cancellation, and for $`g\ge1`$,

```math
\deg U=\deg V=2^{2g-1},\qquad
\mathrm{lc}(U)=\mathrm{lc}(V)=q^{\,g2^{2g-2}}.
```

**Proof.** Every inverse root $`\alpha_S`$ of $`E_k`$ has modulus $`q^{k/2}`$.
Since $`q>1`$, factors belonging to different $`k`$ have disjoint root moduli.
In particular the odd and even products have no common root. The sum of the
binomial coefficients of either parity is $`2^{2g-1}`$, giving the two degrees.
For each fixed index $`i`$, exactly $`2^{2g-2}`$ subsets of either parity contain
$`i`$: among the remaining $`2g-1`$ indices, either parity occurs equally often.
Each leading coefficient is consequently
$`(-1)^{2^{2g-1}}(\prod_i\alpha_i)^{2^{2g-2}} =q^{g2^{2g-2}}`$. $`\square`$

Thus a dense coefficient list for $`U,V`$ has exponentially many entries.
Even an ordinary sparse representation with binary integer coefficients must
write a leading coefficient of bit length
$`\lfloor g2^{2g-2}\log_2q\rfloor+1`$.
Neither expanded representation can be output in time polynomial in $`g`$ and
$`\log q`$. This elementary size argument does not prohibit compressed powers,
arithmetic circuits, or the defining recipe above.

The precise algorithmic claim is therefore recovery of the degree-$`2g`$
polynomial $`P_A`$. It is a compact description determining $`Z_A`$ and the
$`\mathbb F_q`$-isogeny class. For a Jacobian it also gives the compact **curve**
zeta function $`Z_C`$, which differs from $`Z_{J_C}`$ when $`g>1`$.
For $`g=1`$ the two formulas agree.

## 4. Scope and sources

This application check closes the distinction between the abstract polynomial
theorems and their geometric interpretation. It changes neither field/genus
threshold and supplies no new count-acquisition or authentication algorithm.
The preserved polynomial controls are still not asserted to be Jacobians.
The internal checks are recorded in [VERIFICATION.json](VERIFICATION.json);
they do not constitute external peer review.

The following primary/author sources were inspected for these standard facts
on 27 September 2026 (UTC). No new literature-priority claim is made here.

- J. S. Milne, *Abelian Varieties*, corrected 2022 chapter: Theorem 19.1,
  pp. 40–41, and Corollary 19.4, p. 42, for Frobenius, counts, and the full
  abelian-variety zeta function.
- J. S. Milne, *Jacobian Varieties*, corrected 2021 chapter: Section 11,
  Theorem 11.1 and Corollary 11.4, pp. 35–37, for the curve trace and zeta
  formulas.
- J. Tate, *Endomorphisms of Abelian Varieties over Finite Fields*,
  Invent. Math. **2** (1966), 134–144, Theorem 1(c), p. 139, for determination
  of the isogeny class over the given finite field.

[avs]: https://www.jmilne.org/math/xnotes/AVs.pdf
[jvs]: https://www.jmilne.org/math/xnotes/JVs.pdf
[tate]: https://pazuki.perso.math.cnrs.fr/index_fichiers/Tate66.pdf
