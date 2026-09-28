# Teaching anchors and passage map

Checked 28 September 2026. The guide uses Galbraith as its primary textbook
and Chidambaram–Keller as the secondary research anchor. The existing
[scientific bibliography](../research/manuscript_background_v1/REFERENCES.bib)
and [claim map](../research/manuscript_background_v1/CLAIM_MAP.md) retain the
broader primary-literature context.

## Galbraith: the primary anchor

Steven D. Galbraith, *Mathematics of Public Key Cryptography*, Cambridge
University Press, 2012. [Author's book page and extended text](https://www.math.auckland.ac.nz/~sgal018/crypto-book/crypto-book.html).
Citation key: `Galbraith2012`; [BibTeX entry](GALBRAITH.bib).
This one-entry teaching supplement can be used alongside the existing
17-entry scientific bibliography, without duplicating its references.

The inspected chapter PDFs are the extended online text. The author explicitly
notes that their section, theorem, and page numbers can differ from the print
edition. All tutorial locators use the online numbering.

| Passage inspected | Use in the reading path |
|---|---|
| [Chapter 2](https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch2.pdf), §§2.1–2.2, §§2.10–2.11 | Arithmetic model, finite precision, polynomials, and finite fields |
| [Chapter 7](https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch7.pdf), §§7.7–7.8 | Principal divisors and divisor classes |
| [Chapter 10](https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch10.pdf), §10.5 | Jacobians, abelian varieties, isogenies |
| Theorem 10.7.1 | Weil polynomial and extension-field Jacobian cardinalities |
| Theorem 10.7.5 and Lemma 10.7.6 | Curve counts, power sums, and Newton identities |
| Definition 10.7.10 and surrounding discussion | Monic Frobenius polynomial versus constant-term-one polynomial |
| Theorem 10.7.13 | Isogeny interpretation |

The new worked calculations are derived in the tutorial. The textbook supplies
the established setting; the reconstruction proofs are linked to their
canonical repository notes.

## Chidambaram–Keller: the secondary anchor

Shiva Chidambaram and Timo Keller, *Point counts of abelian varieties over
finite fields determining their zeta function*, arXiv:2606.28989v2.
[Version record](https://arxiv.org/abs/2606.28989v2) ·
[Pinned PDF](https://arxiv.org/pdf/2606.28989v2).
Citation key: `ChidambaramKeller2026`.

| Passage inspected | Use in the comparison |
|---|---|
| Theorem 1.1 | First-$g$ determination and the stated sufficient threshold |
| §2 | Reciprocity, Weil bounds, integrality, and Newton identities |
| §3 | Supplied counts as logarithmic mixtures of inverse power sums |
| §§4–6 | Reconstruction argument and polynomial bit complexity |
| Remark 7.12 | Refined threshold discussion and the polynomial-threshold question |

The version record dates v2 to 14 July 2026. The pinned PDF's internal date is
15 July 2026. The HTML rendering inspected on this pass displays a different
internal date (24 August 2026), while retaining the v2 header. The reading path
therefore links the pinned PDF and uses section/theorem locators; it does not
infer a new revision from the HTML date.

## Claims supported by our proofs

| Exposition | Canonical mathematical source |
|---|---|
| Coefficient contraction, its invariant domain, and quadratic sufficient threshold | [First-$g$ theorem, §§1–5](../research/first_g_reconstruction_v1/THEOREM.md) |
| Truncation, logarithm error, quantization, exact rounding, and polynomial bit time | [First-$g$ theorem, §§6–9](../research/first_g_reconstruction_v1/THEOREM.md) |
| Sparse selected indices and uniform all-field tail bound | [Note 28](../exploration/phase_2/ORDINARY_QUERY_THEOREM_AUDIT_28.md) and [Note 29](../exploration/phase_2/RECONSTRUCTION_PROOF_REVIEW_29.md) |
| Geometric applications and compact-output distinction | [Finite-field corollaries](../research/finite_field_application_v1/COROLLARIES.md) |

Kedlaya's reconstruction framework and the endpoint precedents remain
attributed in the [existing source comparison](../research/manuscript_background_v1/WEIL_RECONSTRUCTION.md).
They support the literature record without becoming additional required
teaching anchors. Primary papers and book chapters are linked, not redistributed.

[Return to the reading guide](READING_GUIDE.md).
