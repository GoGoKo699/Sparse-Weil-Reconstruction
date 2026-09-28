# Reproducing the exact experiments

The three experiment packages check the reconstruction algorithms using supplied
Weil polynomials and independently computed counts. Their source files, manifests,
READMEs, and reference reports are preserved. This guide provides a typeset reading
route to those records.

Use Python 3.10 or later; only the standard library is required. From the
repository root, run all three packages and the 17-file preservation check with

```sh
python3 verify.py
```

Each verifier checks its pinned files, runs in temporary storage, and compares
the regenerated report with the preserved reference. It does not overwrite the
expected evidence. Do not use `-O` or `-OO`.

## First-g reconstruction

The [first-$`g`$ proof](../research/first_g_reconstruction_v1/THEOREM.md) applies
to integral reciprocal $`q`$-Weil polynomials with $`g\ge1`$ and
$`q\ge65{,}536g^2`$. The decoder receives only $`q`$, $`g`$, and the true exact
integers $`K_1,\ldots,K_g`$. A geometric finite-field interpretation additionally
requires $`q`$ to be a prime power.

```sh
python3 experiments/first_g_reconstruction_v1/verify.py
```

The correction uses exact fractions, bounded alias truncation, certified
range-reduced logarithms, and dyadic rounding. Five controls at
$`g=1,2,3,4,8`$ cover field-parameter boundaries, nonsquare parameters, repeated
factors, near-boundary inverse roots, and an irreducible degree-eight polynomial.
All 41 coefficients recover exactly. Independent companion determinants check
all 18 supplied resultants; quadratic-product controls also have separate count
recurrences. The decoder receives none of these constructions.

For the irreducible example, $`x^4-x^3-4x^2+4x+1`$ has four roots in
$`(-2,2)`$, verified by exact signs on disjoint intervals. Its reduction modulo
2 has no linear or irreducible quadratic factor, so it is irreducible. Its
$`q`$-Weil transform is irreducible because the quadratic discriminant is
negative at every real embedding.

Every final unrounded coefficient has error $`\lt1/32`$, checked with exact
rational arithmetic. Two allowed logarithm perturbations retain the correct
output, and seven malformed inputs are rejected. Runtime is reported separately
from the pinned output; the prototype makes no optimal-resource claim.

[Decoder](../experiments/first_g_reconstruction_v1/reconstruct.py) ·
[Controls](../experiments/first_g_reconstruction_v1/experiment.py) ·
[Report](../experiments/first_g_reconstruction_v1/REPORT.json) ·
[Manifest](../experiments/first_g_reconstruction_v1/MANIFEST.json) ·
[Preserved README](../experiments/first_g_reconstruction_v1/README.md)

## All-field reconstruction

The [all-field proof](ALL_FIELD_PROOF.md) applies for $`g\ge32`$ and every
integer $`q\ge2`$. With $`h=g-2`$, the supplied indices are
$`D_h=\{1,\ldots,h\}\cup\{2,4,\ldots,2h\}`$, giving
$`h+\lceil h/2\rceil\lt2g`$ counts and maximum index $`2g-4`$.

```sh
python3 experiments/all_field_reconstruction_v1/verify.py
```

The decoder combines Möbius cancellation, Newton rounding, endpoint completion,
and range-reduced rational logarithms. Seven supplied-polynomial controls at
genera $`32,33,48`$ and parameters $`q=2,3,4,5`$ recover all 489 coefficients and
227 traces exactly, including higher-degree and repeated-root factors.

The checks include 36 independent companion determinants, 4,030 finite parameter
pairs, 128 Möbius identities, the three uniform proof constants, seven logarithm
cases, a residue-rounding control, and eleven malformed cases. Decimal logarithms
serve only as secondary spot checks; reconstruction uses exact rational enclosures.

[Decoder](../experiments/all_field_reconstruction_v1/reconstruct.py) ·
[Controls](../experiments/all_field_reconstruction_v1/checks.py) ·
[Report](../experiments/all_field_reconstruction_v1/REPORT.json) ·
[Manifest](../experiments/all_field_reconstruction_v1/MANIFEST.json) ·
[Preserved README](../experiments/all_field_reconstruction_v1/README.md)

## Independent reconstruction audit

This package checks an irreducible degree-64 $`2`$-Weil polynomial at
$`q=2`$, $`g=32`$, using exact real-root bounds and a modulo-7 irreducibility
test. It retains the all-field decoder and its theorem's threshold.

```sh
python3 experiments/reconstruction_audit_v1/verify.py
```

All 45 supplied counts are reconstructed by exact circulant determinants and
checked against a preserved fingerprint of a separate SymPy resultant
calculation. SymPy is not required for replay. The decoder receives only $`q`$,
$`g`$, and the counts, and recovers all 65 coefficients and 30 traces exactly.
Four permitted logarithm-centre displacements leave the output unchanged.
The associated [bit-complexity audit](ALL_FIELD_PROOF.md#6-explicit-numerical-bit-complexity-audit)
provides the uniform size bounds supporting the algorithm.

[Audit source](../experiments/reconstruction_audit_v1/audit.py) ·
[Fixture](../experiments/reconstruction_audit_v1/CONTROL.json) ·
[Report](../experiments/reconstruction_audit_v1/REPORT.json) ·
[Manifest](../experiments/reconstruction_audit_v1/MANIFEST.json) ·
[Preserved README](../experiments/reconstruction_audit_v1/README.md)

## What the controls establish

These finite checks support the implementations; the written proofs establish
the uniform theorems. The controls are supplied polynomials, with no claim that
they are Jacobians of curves. Count acquisition and authentication remain separate
tasks. Both the first-$`g`$ experiment and the independent audit include an altered
count that decoding accepts while exact resultant replay detects the discrepancy.
Successful reconstruction therefore does not authenticate the input transcript.
The controls do not establish external peer review, publication priority, optimal
thresholds, or minimum query counts.
