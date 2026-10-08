# Verification

Use Python 3.10 or later with the standard library. From the repository root:

```sh
python3 verify.py
```

The command checks all 17 entries in the
[integrity manifest](../provenance/import-manifest.json), then runs the three
experiment verifiers. Each checks its pinned source files and dependencies,
executes in temporary storage, and compares the resulting report exactly with
its reference. Python assertions are part of these checks; use ordinary Python
execution without `-O` or `-OO`.

For the manifest check alone:

```sh
python3 verify.py --integrity-only
```

## Checks and evidence

| Evidence | Where to read or run it |
|---|---|
| First-g coefficient recovery, independent determinants, rounding margins, and input controls | [First-g experiments](EXPERIMENTS.md#first-g-reconstruction) |
| Selected-support recovery, independent determinants, parameter bounds, and logarithm checks | [All-field experiments](EXPERIMENTS.md#all-field-reconstruction) |
| Irreducibility, exact resultants, logarithm perturbations, and count-corruption control | [Reconstruction audit](EXPERIMENTS.md#independent-reconstruction-audit) |
| Logarithm signs, contraction bounds, error margins, and rational denominators | [Proof and arithmetic checks](../research/consolidation_v1/AUDIT.md) |

The experiment guide gives the commands for individual packages and links to
all reference reports. The controls test implementations on supplied
polynomials. Uniform guarantees follow from the
[first-g proof](../research/first_g_reconstruction_v1/THEOREM.md) and
[all-field proof](ALL_FIELD_PROOF.md).

[Source and report integrity](../PROVENANCE.md) explains the manifests and
revision-specific verification records.
