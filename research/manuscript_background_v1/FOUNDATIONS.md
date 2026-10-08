# Finite-field foundations and interpretation

Background checked on 28 September 2026 (Asia/Shanghai; 27 September UTC).
The [application note](../finite_field_application_v1/COROLLARIES.md) gives
the geometric corollaries and output bounds.

## 1. Fix the Frobenius and polynomial conventions

For an abelian variety $`A/\mathbb F_q`$ of dimension $`g\ge1`$, $`q`$ is a prime power.
Choose $`\ell\nmid q`$ and let $`V_\ell A=T_\ell A\otimes_{\mathbb Z_\ell}\mathbb Q_\ell`$.
Use the **$`q`$-power Frobenius endomorphism** $`\pi_A`$ acting on this Tate module:

```math
f_A(X)=\det(X-\pi_A\mid V_\ell A),\qquad
P_A(T)=T^{2g}f_A(1/T)=\det(1-T\pi_A\mid V_\ell A).
```

Thus $`f_A`$ is monic, whereas the repository's $`P_A`$ has constant coefficient
$`1`$. Its inverse roots are the roots $`\alpha_i`$ of $`f_A`$. Specifying the
endomorphism avoids an ambiguity about arithmetic versus geometric Galois
Frobenius. [MilneAV1986, Proposition 12.9 and Section 19][MilneAV1986] supports
this convention and gives

```math
P_A(T)=\prod_{i=1}^{2g}(1-\alpha_iT)\in\mathbb Z[T],\quad
|\alpha_i|=\sqrt q,\quad
c_{2g-j}=q^{g-j}c_j,
```

```math
\#A(\mathbb F_{q^m})=\prod_{i=1}^{2g}(1-\alpha_i^m).
```

The last identity is a cardinality formula: the geometric points fixed by
$`\pi_A^m`$ form the kernel of the separable isogeny $`1-\pi_A^m`$.
Integrality, reciprocity and the inverse-root modulus are standard input
facts. The abstract reconstruction results
also allow integers $`q\ge2`$ that are not prime powers; their geometric
interpretation does not.

## 2. Curves supply two different counting problems

Let $`C/\mathbb F_q`$ be smooth, projective and geometrically connected, with
genus $`g`$, and let $`J_C`$ be its Jacobian. [MilneJV1986, Theorem 11.1 and
Corollary 11.4][MilneJV1986] gives

```math
N_m:=\#C(\mathbb F_{q^m})=q^m+1-\sum_i\alpha_i^m,\qquad
Z_C(T)=\frac{P_{J_C}(T)}{(1-T)(1-qT)}.
```

By contrast, $`K_m=\#J_C(\mathbb F_{q^m})`$ is the product in Section 1.
The reconstruction inputs are the $`K_m`$. They count elements of a
$`g`$-dimensional abelian variety, rather than points of the curve.

The first $`g`$ values of $`N_m`$ already recover $`P_{J_C}`$ for every finite field:
convert them to power sums, apply Newton identities, then use reciprocity.
The [application note, Section 2](../finite_field_application_v1/COROLLARIES.md#2-curves-and-jacobians)
records this elementary derivation. The quadratic-threshold theorem instead
uses the product data $`K_m`$. The stated zeta identity holds for every curve
under the hypotheses above.

## 3. What the recovered invariant determines

[Tate1966, Theorem 1(c)][Tate1966] proves that two abelian varieties over the
same finite field are isogenous over that field exactly when their Frobenius
characteristic polynomials agree. Equivalently, all their extension-field
cardinalities agree. Reconstructing $`P_A`$ therefore identifies the
$`\mathbb F_q`$-isogeny class.

The compact output identifies an isogeny class, which can contain several
isomorphism classes. In the Jacobian application it also gives the curve's
zeta function.

For a variety $`X`$, the zeta function packages all extension counts as
$`\exp(\sum_{m\ge1}\#X(\mathbb F_{q^m})T^m/m)`$. For an abelian variety,
higher cohomology is obtained from exterior powers of degree-one cohomology;
hence $`P_A`$ determines the full $`Z_A`$. See [DupuyEtAl2021, Section 2.1][DupuyEtAl2021]
and [MilneAV1986, Corollary 19.4][MilneAV1986]. The compact curve formula above
must not be substituted for $`Z_{J_C}`$ when $`g>1`$.

The [application note, Section 3](../finite_field_application_v1/COROLLARIES.md#3-compact-output-versus-an-expanded-abelian-variety-zeta-function)
proves the relevant representation boundary: $`P_A`$ has polynomial output
length, while the fully expanded numerator and denominator of $`Z_A`$ each
have degree $`2^{2g-1}`$ and a leading coefficient with exponentially many bits.
Thus “reconstruct the zeta function in polynomial time” requires the compact
representation to be specified for general abelian varieties.

## 4. Algebraic controls do not automatically supply geometry

Honda–Tate theory classifies simple isogeny classes through conjugacy classes
of Weil numbers. A simple class has characteristic polynomial $`h^e`$, where
$`h`$ is irreducible and the prescribed exponent $`e`$ depends on local invariants.
Consequently, the root-modulus and integrality conditions alone do not certify
an arbitrary polynomial as an abelian-variety characteristic polynomial with
the proposed multiplicities. [DupuyEtAl2021, Section 2.3][DupuyEtAl2021] states
the exponent rule. Realization by a Jacobian is an additional issue.

The geometric corollaries start from an actual $`A`$ or $`J_C`$ and therefore
inherit the polynomial promises. The exact experimental controls instead start
from supplied polynomials and test recovery within that algebraic class;
identifying them with abelian varieties or Jacobians would require a separate
realization argument.

## 5. Scientific role of the supplied-count model

The project's question is how much selected cardinality information determines
the full Frobenius invariant, and how efficiently the information can be
converted. Its two sufficient regimes address different uses of that
information: fewer than $`2g`$ selected values for every $`q`$ when $`g\ge32`$,
and exactly the first $`g`$ values when $`q\ge65{,}536g^2`$.

This is an information-to-invariant reconstruction guarantee. To turn it into
an end-to-end point-counting algorithm for a presented curve or abelian variety,
one must additionally specify how the required $`K_m`$ are obtained and account
for their cost. The polynomial bit-time result here is the conversion cost
after those true exact integers are supplied. Fewer requested indices alone
do not prove a faster acquisition procedure, especially when the extension
degrees differ. Successful output also does not authenticate an untrusted
transcript.

## 6. Exact source locations

Page numbers for Milne refer to the corrected author PDFs, not the original
book pagination. Section and theorem numbering is retained by those versions.
The sources provide established geometry; the project's thresholds, decoder,
and output-size argument are cited to their own versioned notes.

| Stable key | Inspected material and use |
|---|---|
| `MilneAV1986` | Corrected 2 January 2022 author chapter: Proposition 12.9, p. 23 (Tate-module polynomial); Theorem 19.1 and its proof, pp. 40–41 (Frobenius and cardinality); Corollary 19.4, p. 42 (full zeta function). |
| `MilneJV1986` | Corrected 12 June 2021 author chapter: Theorem 11.1, p. 35, and Corollary 11.4, p. 37 (curve counts and zeta numerator). |
| `Tate1966` | Original article, Theorem 1(c), p. 139 (isogeny over the given finite field). |
| `DupuyEtAl2021` | arXiv:2003.05380v2, Sections 2.1–2.3, pp. 5–7 (cohomological convention, Weil polynomials, Honda–Tate multiplicities); publisher metadata gives 2021 and pp. 375–448 for the published chapter. |

[MilneAV1986]: https://www.jmilne.org/math/xnotes/AVs.pdf
[MilneJV1986]: https://www.jmilne.org/math/xnotes/JVs.pdf
[Tate1966]: https://pazuki.perso.math.cnrs.fr/index_fichiers/Tate66.pdf
[DupuyEtAl2021]: https://arxiv.org/html/2003.05380v2
