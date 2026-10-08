# From Galbraith to sparse Weil reconstruction

[← Overview](../README.md) · [Sources](SOURCES.md) · [Foundations →](TUTORIAL.md)

The question is simple to state: **how much of a polynomial can we recover
from a few products formed from its inverse roots?** Over a finite field,
those products are cardinalities of an abelian variety over field extensions.
The polynomial packages the arithmetic information we want to recover.

The primary teaching anchor is Steven D. Galbraith's
[*Mathematics of Public Key Cryptography*](https://www.math.auckland.ac.nz/~sgal018/crypto-book/crypto-book.html).
Chidambaram–Keller's
[*Point counts of abelian varieties over finite fields determining their zeta function*](https://arxiv.org/pdf/2606.28989v2)
is the secondary anchor: it brings the reader from the textbook setting to
the same first-$`g`$ reconstruction question studied here.

## A first visit

Start with the three short notes below. Together they give a roughly
30-minute orientation; the linked textbook passages and full proofs support
slower study afterward.

| Read | Takeaway |
|---|---|
| [1. Foundations](TUTORIAL.md) | The polynomial; curve and Jacobian counts |
| [2. Reconstruction](RECONSTRUCTION.md) | Logarithms, correction, and convergence |
| [3. Comparison](COMPARISON.md) | The shared problem and the field-size guarantee |

The notes include worked examples and self-checks. The
[repository overview](../README.md) gives the exact theorem regimes and
reproduction command.

## The Galbraith reading path

All locators below refer to the **author's extended online edition**. Its
numbering may differ from the printed book.

| Passage | What to take into this project |
|---|---|
| [Chapter 2](https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch2.pdf), §§2.1–2.2 and §§2.10–2.11 | Bit operations, finite precision, polynomial arithmetic, and finite-field representation. |
| [Chapter 7](https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch7.pdf), §§7.7–7.8 | Principal divisors and divisor classes: the group behind a Jacobian. |
| [Chapter 10](https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch10.pdf), §10.5 | Jacobians, abelian varieties, and isogenies. |
| Chapter 10, §10.7 | The Weil polynomial, extension-field cardinalities, curve traces, Newton identities, and Tate's theorem. |

For an algorithm-oriented first reading, begin with §10.7 and consult the
other passages when a term is unfamiliar. Section 10.7 treats general curves
despite the chapter's hyperelliptic title. The useful landmarks are
Theorem 10.7.1, Theorem 10.7.5, Lemma 10.7.6, and Theorem 10.7.13.

The reconstruction arguments start from the resulting polynomial facts;
the Weil and Tate theorems can be taken as given while learning the algorithm.

## A notation guide

Our convention keeps the constant coefficient equal to one.

| Object | Galbraith | Here |
|---|---|---|
| Constant term one | $`L(t)`$ | $`P(T)`$ |
| Monic polynomial | $`P(T)`$ | $`\chi_A(X)`$ |

Here the two polynomial conventions are related by

```math
\begin{aligned}
P(T)&=\prod_i(1-\alpha_iT),\\
\chi_A(X)&=X^{2g}P(1/X).
\end{aligned}
```

Galbraith's ordinary curve cardinality $`\#C(\mathbb F_{q^m})`$ is $`N_m`$
in the tutorial. His Jacobian cardinality
$`\#\mathrm{Pic}^0_{\mathbb F_{q^m}}(C)`$ is $`K_m`$ when the promised
variety is $`J_C`$.

The tutorial uses $`S_m=\sum_i\alpha_i^m`$. Chidambaram–Keller instead use
inverse power sums $`s_m=\sum_i\alpha_i^{-m}`$; reciprocity gives
$`S_m=q^m s_m`$. Their $`c_m`$ denotes a count, which we call $`K_m`$;
our $`c_j`$ denotes a polynomial coefficient.

In [the reconstruction note](RECONSTRUCTION.md),
$`L_m=\log(q^{gm}/K_m)`$ is a logarithmic datum, not Galbraith's polynomial
$`L(t)`$. The canonical first-$`g`$ proof uses the opposite logarithm sign and
states that convention explicitly.

## Where the secondary anchor enters

After the textbook objects are familiar, read Chidambaram–Keller §§1–3 for
the reconstruction question and logarithmic identity, §§4–6 for their
algorithm, and Remark 7.12 for the field-size question. The
[comparison note](COMPARISON.md) explains the connection to our coefficient
iteration. It also locates the complementary sparse-count theorem within
Kedlaya's earlier reconstruction framework.

## Continue into the proofs

| Once you understand… | Continue with… |
|---|---|
| The coefficient correction and its fixed point | [First-$`g`$ theorem, §§2–5](../research/first_g_reconstruction_v1/THEOREM.md) |
| Why an approximation can determine an integer exactly | [Finite precision and rational implementation, §§6–9](../research/first_g_reconstruction_v1/THEOREM.md) |
| Cancellation using selected extension degrees | [All-field proof](ALL_FIELD_PROOF.md) and [bit complexity](ALL_FIELD_PROOF.md#6-explicit-numerical-bit-complexity-audit) |
| What the recovered polynomial says about a variety | [Finite-field corollaries](../research/finite_field_application_v1/COROLLARIES.md) |
| The mathematical argument and its data promises | [Exact executable controls](EXPERIMENTS.md) |

The [source map](SOURCES.md) records the editions and passage locations.
The broader [scientific background package](../research/manuscript_background_v1/README.md)
contains the claim-level citations and literature context.

---

[← Overview](../README.md) · [Sources](SOURCES.md) · [Foundations →](TUTORIAL.md)
