# Teaching integration checks

28 September 2026. Baseline: `088bf3118f8e881629c27f885b529b0d8b316264`.

This pass adds a Galbraith-led teaching path and a Chidambaram–Keller
comparison. The canonical proofs, decoders, fixtures, reference reports,
license, and versioned scientific background remain unchanged.

## Executed checks

- Ran `python3 verify.py` before and after the teaching changes. Both runs
  passed import integrity for all 17 preserved files and reproduced all
  three exact research reports.
- Compared 48 retained files byte for byte with the starting commit. Existing-file changes
  are confined to the root overview, status, and work order; new material
  is in `docs/`.
- Reviewed the exposition against the canonical proofs. The logarithm sign
  conversion, normalized and rational coefficient maps, contraction factor,
  truncation/rounding interpretation, and selected-support formula agree.
- Independently checked the two worked examples, the dimension-two inversion,
  and the selected-index counts. The small examples illustrate exact algebra;
  they do not test the general first-$g$ theorem outside its stated regime.
- Checked 99 local links, including four heading anchors, across the nine
  changed/new Markdown files,
  paired math/fence delimiters, and whitespace. Compiled the existing
  scientific bibliography together with the Galbraith supplement using
  BibTeX's plain style; all 18 unique entries compiled without warnings.
- Matched the cited Galbraith online locations and the pinned
  Chidambaram–Keller v2 passages to the [source map](SOURCES.md).

The independent teaching review found no substantive mathematical or
attribution issue. Its two presentation suggestions—removing a repeated
reading table and using one monic-polynomial symbol—were incorporated.
These checks concern the new exposition and retained reproducibility;
the [scientific audit](../research/consolidation_v1/AUDIT.md) records the
proof review.

## Presentation pass

The presentation pass starts from `2a1b261262d6fa909c85057b0b78a0c4692b591e`.
It adds the reconstruction diagram, a three-pass overview, compact reading
navigation, and consistent GitHub mathematical displays.

- All 39 pre-existing teaching display formulas were checked for equivalence
  after removing only layout wrappers, spacing, and line breaks. Two existing
  notation definitions were moved from a table into one additional display.
- The six reader-facing pages converted to 295 MathML expressions without
  parser warnings. Their 106 local links and image references, including four
  heading anchors, resolved. The SVG parsed and was rendered at 900 and 390
  pixels; visual inspection prompted a correction to formula spacing.
- `python3 verify.py` passed again, reproducing all three exact reports and
  verifying the 17-file import. The research proofs, decoders, fixtures,
  reference reports, and versioned background remain byte-identical.
- An independent presentation review found no scientific change or attribution
  issue. Its endpoint-label clarification was incorporated.

MathML conversion and SVG raster checks are local presentation checks.
A whole-page browser preview was unavailable because the browser download
endpoint returned an unavailable-site page; no live GitHub rendering check is
claimed. The pages use GitHub-native math fences and protected inline formulas.

## Research-note rendering repair

28 September 2026. Baseline: `51b1f1f343a42e1102ae2f9215d03a9de6c372be`.

Live GitHub inspection reproduced the cardinality-symbol failure in the
finite-field corollaries and further failures in the first-g proof. Ordinary
Markdown consumed TeX escapes and subscripts; the renderer also rejected
`\operatorname` and interpreted some strict inequalities as markup.

Nine research pages now use protected inline math and `math` display fences,
`\mathrm` for the affected named operators, and `\lt` for strict inequalities.
Independent comparison checked all 102 displays and 344 inline formulas against
the baseline. After normalizing only these typography changes and whitespace,
all mathematical payloads, surrounding prose, and code agree.

The 17 manifest-pinned files, all experiment files, and historical JSON receipts
remain byte-identical. The first-g theorem and application/background notes
received formatting repairs only. Hashes in earlier receipts identify their
dated checkpoint bytes; they have not been replaced with the reformatted hashes.

`python3 verify.py` passed, including import integrity and all three exact
reports. The corrected research pages were checked in GitHub's live renderer;
all 446 formulas completed rendering without reported math errors. The browser
check covers these nine pages, not every archived document. All 216 local links,
14 heading anchors, and 21 retrieval-guide source paths resolved.

## Inline notation and preserved reading editions

28 September 2026. Baseline: `ed82f91e404bd2a3762bf8f66dd0b3833d009ebf`.

Mathematical expressions in the first-g proof and consolidation notes now use
protected inline math. Roots, Greek letters, subscripts, superscripts, norms,
inequalities, and complexity expressions are typeset within the prose. Actual
code, identifiers, paths, and recorded hashes retain code formatting. The status,
background index, and claim map use the same inline convention.

Independent review checked the 170 first-g code-span translations and the
distinction between the coefficient ball and integer precision parameter.
All 55 existing display formulas in that proof, and all 13 displays in the
consolidation notes, remain byte-identical to the baseline.

The [all-field reading edition](ALL_FIELD_PROOF.md) presents the complete
mathematical argument of preserved Note 28, Sections 1–5, followed by Note 29,
Section 3. Independent comparison checked all 22 source displays and 133 inline
formulas. One former inline numerical error estimate is now the 23rd display.
The edition clarifies the inverse-root terminology and Jacobian input; historical
project context is omitted. Its mathematical hypotheses and arguments are retained.

The [experiment guide](EXPERIMENTS.md) provides typeset regimes, controls, and
reproduction commands for the three preserved experiment packages. An intermediate
check caught the first-g experiment README's own manifest constraint; that README
was restored before final verification. Every experiment file, all historical
JSON receipts, and all 17 import-manifest files remain byte-identical. No expected
report or manifest was regenerated to make a check pass.

`python3 verify.py` passed on the baseline and on the final scientific content,
reproducing all three exact reports. GitHub's live renderer completed all 538
formulas across the eight pages with new inline notation, without reported math
errors. A visual check confirmed the notation within proof paragraphs. All 247
local links, 28 heading anchors, and 23 retrieval-guide source paths resolved.
These presentation checks cover the current reading editions; preserved historical
records retain their original formatting and verification identities.

[Return to the reading guide](READING_GUIDE.md).
