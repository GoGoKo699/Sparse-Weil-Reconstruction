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
proof review. Manuscript preparation remains on hold.

[Return to the reading guide](READING_GUIDE.md).
