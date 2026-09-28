# From Galbraith to the reconstruction problem

The starting point is Steven Galbraith's
[*Mathematics of Public Key Cryptography*](https://www.math.auckland.ac.nz/~sgal018/crypto-book/crypto-book.html).
This page develops the short algebraic bridge from its finite-field background
to the question studied here: **which selected cardinalities determine a Weil
polynomial, and how can we recover its coefficients efficiently?**

You need polynomial arithmetic, complex absolute values, and elementary linear
algebra. The geometric interpretation explains why the inputs matter; once the
polynomial promises are stated, the reconstruction question is algebraic.

## 1. From the textbook notation

Read Galbraith's online §10.7 alongside this page. The
[reading guide](READING_GUIDE.md) gives the supporting passages and edition
information. Galbraith writes $L(t)$ for our constant-term-one polynomial
$P(T)$; his monic Frobenius polynomial is $\chi_A(X)=X^{2g}P(1/X)$ in our
notation.

The derivations and numerical illustrations below are written for this
tutorial. The textbook supplies the foundation, and the versioned research
notes hold the local proofs.

## 2. The unknown has only g free coefficients

Let $q\ge2$ and $g\ge1$ be integers. The unknown is

$$
P(T)=\prod_{i=1}^{2g}(1-\alpha_iT)
    =1+c_1T+\cdots+c_{2g}T^{2g}.
$$

The numbers $\alpha_i$ are called **inverse roots**: the roots of $P$ itself
are $1/\alpha_i$. They are complex algebraic numbers, not elements of the
finite field. Our promised polynomial has integer coefficients, satisfies
$|\alpha_i|=\sqrt q$, and obeys

$$
c_{2g-j}=q^{g-j}c_j\qquad(0\le j\le g),\qquad c_0=1.
$$

This reciprocity determines the second half of the coefficients from the
first. In particular, $c_{2g}=q^g$. For $g=2$ the whole polynomial is

$$
P(T)=1+c_1T+c_2T^2+qc_1T^3+q^2T^4.
$$

Thus the output is specified by $c_1,\ldots,c_g$. Having $g$ unknown integers
suggests looking for $g$ measurements, but it does not prove that an arbitrary
choice of $g$ measurements determines them.

In the geometric application, $q$ is a prime power and $g$ is the dimension
of an abelian variety $A/\mathbb F_q$. For a Jacobian $A=J_C$, it is also the
genus of the curve $C$. The abstract polynomial problem allows any integer
$q\ge2$; a finite-field interpretation requires a prime power.

## 3. Two ways to count give different data

Write the power sums as

$$
S_m=\sum_{i=1}^{2g}\alpha_i^m.
$$

For a smooth, projective, geometrically connected curve $C/\mathbb F_q$ and
its Jacobian $J_C$, the two relevant cardinalities are

$$
N_m:=\#C(\mathbb F_{q^m})=q^m+1-S_m,
$$

$$
K_m:=\#J_C(\mathbb F_{q^m})
    =\prod_{i=1}^{2g}(1-\alpha_i^m).
$$

$N_m$ counts points on the curve. $K_m$ counts elements of its Jacobian,
whose group interpretation comes from degree-zero divisor classes. For a
general abelian variety, the same product gives $\#A(\mathbb F_{q^m})$.
These standard interpretations are collected in the
[finite-field application note](../research/finite_field_application_v1/COROLLARIES.md).

The research inputs are selected **true exact integers $K_m$**, together with
$q$ and $g$. The decoder's task begins after they have been supplied.

Knowing $N_m$ immediately gives $S_m$ by subtraction. Knowing $K_m$ gives a
product instead. For example, $K_1=P(1)$ mixes every coefficient. Recovering
the individual coefficients from several such products is the problem here.

Once the Jacobian polynomial is known, the curve zeta function is

$$
Z_C(T)=\frac{P(T)}{(1-T)(1-qT)}.
$$

This is the zeta function of $C$. For $g>1$, the zeta function of the
higher-dimensional variety $J_C$ has a different expression; the
[application note](../research/finite_field_application_v1/COROLLARIES.md#3-compact-output-versus-an-expanded-abelian-variety-zeta-function)
explains what its compact representation means.

## 4. If the power sums were known: Newton identities

Differentiate the product for $P$ and expand at $T=0$:

$$
\frac{P'(T)}{P(T)}
=-\sum_i\frac{\alpha_i}{1-\alpha_iT}
=-\sum_{m\ge1}S_mT^{m-1}.
$$

Multiplying by $P(T)$ and comparing the coefficient of $T^{j-1}$ gives

$$
jc_j=-\sum_{m=1}^{j}c_{j-m}S_m.
$$

This is a triangular calculation: compute $c_1$, then $c_2$, and continue.
The first two steps are

$$
c_1=-S_1,\qquad c_2=\frac{S_1^2-S_2}{2}.
$$

Hence $S_1,\ldots,S_g$ determine $c_1,\ldots,c_g$, and reciprocity finishes
the polynomial. This explains why the first $g$ ordinary curve counts $N_m$
already suffice over every finite field. Our selected-$K_m$ problem asks how
to reach these coefficients from the product data.

## 5. Work it out in dimension one

For $g=1$,

$$
P(T)=1+c_1T+qT^2,\qquad K_1=P(1)=1+c_1+q.
$$

Therefore $c_1=K_1-q-1$: one subtraction recovers the only unknown coefficient.
As an algebraic example, let $q=5$ and suppose $K_1=4$. Then

$$
c_1=-2,\qquad P(T)=1-2T+5T^2,\qquad S_1=2.
$$

The corresponding monic polynomial is $X^2-2X+5$, with roots $1\pm2i$;
both have modulus $\sqrt5$, as required. This example needs no construction
of a curve. In the elliptic-curve application, the curve and its Jacobian
have the same cardinalities, so the two input types coincide in this dimension.

## 6. Work it out in dimension two

There is also a direct formula for $g=2$. Factor each term of $K_2$:

$$
K_2=\prod_i(1-\alpha_i^2)
    =\prod_i(1-\alpha_i)(1+\alpha_i)
    =P(1)P(-1).
$$

Since $K_1\ne0$ under the root-modulus promise, put $R=K_2/K_1=P(-1)$.
The reciprocal form from Section 2 yields

$$
K_1=1+(q+1)c_1+c_2+q^2,
$$

$$
R=1-(q+1)c_1+c_2+q^2.
$$

Subtract and add these equations:

$$
c_1=\frac{K_1-K_2/K_1}{2(q+1)},\qquad
c_2=\frac{K_1+K_2/K_1}{2}-1-q^2.
$$

For a concrete supplied-polynomial illustration, choose $q=5$ and

$$
P(T)=(1+5T^2)^2=1+10T^2+25T^4.
$$

Its inverse roots are $i\sqrt5$ and $-i\sqrt5$, each twice. Thus
$S_1=0$ and $S_2=-20$. Newton identities give $c_1=0$ and $c_2=10$.
Independently, its supplied products are

$$
K_1=36,\qquad K_2=36^2=1296.
$$

The product-data formulas recover

$$
c_1=\frac{36-36}{12}=0,\qquad
c_2=\frac{36+36}{2}-1-25=10.
$$

This is an illustration within the promised polynomial class; no Jacobian
realization is asserted. The dimension-two inversion works for every $q\ge2$.
It is a special exact calculation, not evidence that the general first-$g$
theorem holds outside its stated sufficient regime $q\ge65{,}536g^2$.

## 7. Check your understanding

<details>
<summary>1. Which supplied data immediately reveal the power sums: curve counts or Jacobian counts?</summary>

Curve counts: $S_m=q^m+1-N_m$. Jacobian counts $K_m$ are products and require
the reconstruction step developed next.

</details>

<details>
<summary>2. If S₁ = 3 and S₂ = −7, what do Newton identities give for c₁ and c₂?</summary>

$c_1=-3$ and $c_2=(9+7)/2=8$. This arithmetic alone does not check all the
promises of a Weil polynomial.

</details>

<details>
<summary>3. Does the dimension-two example prove that the general field-size threshold can be removed?</summary>

No. Its two direct equations give a special low-dimensional inversion. The
general theorem controls a reconstruction algorithm uniformly in $g$ under
its stated field-size bound.

</details>

Continue to [Reconstruction: from the supplied products to the local results](RECONSTRUCTION.md).
That bridge introduces logarithms and explains the two reconstruction
methods. The [comparison](COMPARISON.md) then connects the first-$g$ method
to the secondary anchor, Chidambaram–Keller.
