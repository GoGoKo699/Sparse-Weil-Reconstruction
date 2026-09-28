# Release sanity check

28 September 2026. Starting commit:
`cc560fa9bb26984bd5f8902f77b9d1386afee9bf`.

The internal pre-release review found no substantive mathematical,
implementation, attribution, or reproducibility blocker within the stated
two-theorem scope. The release changes concern navigation, discovery, and
citation; the scientific proofs and executable evidence are retained.

## Review scope

| Area | Result |
|---|---|
| First-g theorem | Checked normalization, alias multiplicities, contraction, invariant ball, finite precision, denominator growth, and the implementation against the proof. The quadratic sufficient threshold and rounding margins agree. |
| All-field theorem | Checked selected indices, the uniform three-region tail bound, exact Newton rounding, both endpoint signs, and rational bit complexity. |
| Finite-field applications | Checked reciprocity and Weil hypotheses, base-field isogeny interpretation, the Jacobian-to-curve-zeta corollary, and exponential expanded abelian-variety zeta output. |
| Code and verification | Reviewed the root verifier and all eight experiment Python files. Source hashes, fresh temporary reports, independent determinant/resultant checks, optimization guards, and promised-input contracts agree. Runtime uses the Python standard library and local imports. |
| Public claims | The overview and teaching pages retain true supplied counts, exact regimes, sufficient-bound qualification, prior first-g recovery and polynomiality, and the distinction between curve counts and Jacobian orders. |
| Sources | Rechecked Galbraith's online locators and Chidambaram–Keller v2. A bounded follow-up search found no additional matched theorem; irrelevant search results limit the strength of that negative evidence. |

The canonical details remain in the [first-g proof](../research/first_g_reconstruction_v1/THEOREM.md),
[all-field theorem](../exploration/phase_2/ORDINARY_QUERY_THEOREM_AUDIT_28.md),
[bit-complexity review](../exploration/phase_2/RECONSTRUCTION_PROOF_REVIEW_29.md),
and [application note](../research/finite_field_application_v1/COROLLARIES.md).

## Reproducibility and presentation

`python3 verify.py` passed with Python 3.12.14. It checked all 17 imported
files and reproduced all three exact reference reports in temporary storage.
Among the retained controls are 4,030 all-field parameter checks, 36 independent
all-field determinant checks, and first-g recovery of all 41 coefficients with
18 independently checked supplied counts. These finite controls check the
implementation; the written proofs establish the uniform statements.

The repository-wide check resolved 216 local Markdown/image references,
14 heading anchors, and all 21 raw-source paths in `llms.txt`. Both bibliographies
compiled together to 18 unique entries without warnings. Citation YAML parsed;
its required core fields and repository identity match the existing metadata.
The 55 other starting files remain byte-identical, including all scientific
proofs, experiments, background, and the license.

The live GitHub overview was inspected in a desktop browser: the diagram,
reading table, inline mathematics, and displayed formulas rendered. The reading
guide revealed a GitHub-disallowed `\operatorname{Pic}` macro, missed by the
earlier local conversion check; this pass replaces it with `\mathrm{Pic}`.
The other four teaching pages completed their live mathematics rendering
without reported formula errors or document-wide horizontal overflow.
The live checks supplement the historical [teaching check](VERIFICATION.md);
no mobile whole-page check is claimed.

## Surgical cleanup and discovery

- Replaced repeated checkpoint narratives in the work order with the current
  STATUS index and retained its operational requirements. Removed repeated
  manuscript-hold sentences within STATUS.
- Kept theorem hypotheses in standalone teaching pages, both complementary
  bibliography files, and independent determinant/resultant routines. These
  repetitions serve readers or validation; merging them would remove context
  or weaken independent evidence.
- Added [llms.txt](../llms.txt) with relevant retrieval questions, exact input
  conditions, source links, and attribution boundaries, and
  [CITATION.cff](../CITATION.cff) for software citation. This supplies discoverable
  context without promising search or model indexing.
- Corrected the reading guide's Picard notation to render on GitHub without
  changing its mathematical meaning.
- Preserved all versioned proofs, decoders, fixtures, reports, scientific
  background, and the license. One harmless historical comment in the pinned
  audit code abbreviates the positive-definiteness tests ambiguously; the
  executed matrices are correctly `(11/4)I + A` and `(11/4)I - A`.

## Source checkpoint and limits

The [current arXiv record](https://arxiv.org/abs/2606.28989) still identifies
Chidambaram–Keller v2, revised 14 July 2026. Its
[pinned PDF](https://arxiv.org/pdf/2606.28989v2), Theorem 1.1, Section 6, and
Remark 7.12 support the comparison's bound, polynomial bit complexity, and
open polynomial-threshold question. The PDF's internal 15 July date and the
HTML's internal 24 August date do not identify an additional arXiv revision.

Galbraith's [author page](https://www.math.auckland.ac.nz/~sgal018/crypto-book/crypto-book.html)
and [online Chapter 10](https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch10.pdf)
confirm the teaching locators and the online-versus-print numbering caveat;
the detailed mapping is in [SOURCES](SOURCES.md).

This is an internal release check, not external peer review or exhaustive
priority certification. It does not authenticate input counts, realize the
controls as Jacobians, prove optimal bounds, execute predecessor code or Lean,
or certify count acquisition. No manuscript or release tag is produced by this
check. Current scientific scope remains in [STATUS](../STATUS.md).
