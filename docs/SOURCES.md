# Teaching anchors and passage map

[← Comparison](COMPARISON.md) · [Reading guide](READING_GUIDE.md) · [Overview →](../README.md)

The guide uses Galbraith as its primary textbook and Chidambaram–Keller as
the secondary research anchor. The
[scientific bibliography](../research/manuscript_background_v1/REFERENCES.bib)
and [claim map](../research/manuscript_background_v1/CLAIM_MAP.md) retain the
broader primary-literature context.

## Galbraith: the primary anchor

Steven D. Galbraith, *Mathematics of Public Key Cryptography*, Cambridge
University Press, 2012. [Author's book page and extended text](https://www.math.auckland.ac.nz/~sgal018/crypto-book/crypto-book.html).
Citation key: `Galbraith2012`; [BibTeX entry](GALBRAITH.bib).
The entry supplements the scientific bibliography.

The chapter PDFs are the extended online text. Their section, theorem, and
page numbers can differ from the print edition; all tutorial locators use
the online numbering.

| Passage | Use in the reading path |
|---|---|
| [Chapter 2](https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch2.pdf), §§2.1–2.2, §§2.10–2.11 | Arithmetic model, finite precision, polynomials, and finite fields |
| [Chapter 7](https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch7.pdf), §§7.7–7.8 | Principal divisors and divisor classes |
| [Chapter 10](https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch10.pdf), §10.5 | Jacobians, abelian varieties, isogenies |
| Theorem 10.7.1 | Weil polynomial and extension-field Jacobian cardinalities |
| Theorem 10.7.5 and Lemma 10.7.6 | Curve counts, power sums, and Newton identities |
| Definition 10.7.10 and surrounding discussion | Monic Frobenius polynomial versus constant-term-one polynomial |
| Theorem 10.7.13 | Isogeny interpretation |

## Chidambaram–Keller: the secondary anchor

Shiva Chidambaram and Timo Keller, *Point counts of abelian varieties over
finite fields determining their zeta function*, arXiv:2606.28989v2.
[Version record](https://arxiv.org/abs/2606.28989v2) ·
[Pinned PDF](https://arxiv.org/pdf/2606.28989v2).
Citation key: `ChidambaramKeller2026`.

| Passage | Use in the comparison |
|---|---|
| Theorem 1.1 | First-$`g`$ determination and the stated sufficient threshold |
| §2 | Reciprocity, Weil bounds, integrality, and Newton identities |
| §3 | Supplied counts as logarithmic mixtures of inverse power sums |
| §§4–6 | Reconstruction argument and polynomial bit complexity |
| Remark 7.12 | Refined threshold discussion and the polynomial-threshold question |

The locators refer to the pinned v2 PDF (version record: 14 July 2026;
internal PDF date: 15 July 2026).

## Claims supported by our proofs

| Exposition | Canonical mathematical source |
|---|---|
| Coefficient contraction, its invariant domain, and quadratic sufficient threshold | [First-$`g`$ theorem, §§1–5](../research/first_g_reconstruction_v1/THEOREM.md) |
| Truncation, logarithm error, quantization, exact rounding, and polynomial bit time | [First-$`g`$ theorem, §§6–9](../research/first_g_reconstruction_v1/THEOREM.md) |
| Sparse selected indices, uniform all-field tail bound, and bit complexity | [All-field reading edition](ALL_FIELD_PROOF.md), from [Note 28](../exploration/phase_2/ORDINARY_QUERY_THEOREM_AUDIT_28.md) and [Note 29](../exploration/phase_2/RECONSTRUCTION_PROOF_REVIEW_29.md) |
| Geometric applications and compact-output distinction | [Finite-field corollaries](../research/finite_field_application_v1/COROLLARIES.md) |

Kedlaya's reconstruction framework and the endpoint precedents are described
in the [source comparison](../research/manuscript_background_v1/WEIL_RECONSTRUCTION.md).

---

[← Comparison](COMPARISON.md) · [Reading guide](READING_GUIDE.md) · [Overview →](../README.md)
