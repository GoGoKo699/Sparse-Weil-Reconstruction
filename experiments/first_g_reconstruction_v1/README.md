# First-g contraction decoder: targeted experiment

This successor experiment implements the first-g reconstruction argument for
integral reciprocal $`q`$-Weil polynomials, under $`g\ge1`$ and
$`q\ge65{,}536g^2`$. It receives only $`q`$, $`g`$, and the true exact integers
$`K_1,\ldots,K_g`$. The input parameter $`q`$ may be any integer satisfying the bound;
the finite-field interpretation additionally requires a prime power.

The formal-logarithm correction is evaluated with exact fractions, bounded
alias truncation, range-reduced logarithm enclosures, and dyadic rounding after
each complete correction. The number of iterations and all precision choices
follow the written contraction argument; no convergence shortcut or supplied
factorization is used. This implementation is a research prototype, not a
claim of optimal resource use.

The inherited range-reduced logarithm routine is imported from
`../all_field_reconstruction_v1/reconstruct.py` and pinned by SHA256 and Git blob
identity. Each center is itself rounded to a dyadic rational within the allowed
logarithm error budget, preventing its long exact series denominator from
propagating through every iteration.

Run from the repository root:

```sh
python3 experiments/first_g_reconstruction_v1/verify.py
```

Python 3.10 or later; standard library only. Do not use `-O` or `-OO`.
The verifier checks source and dependency hashes, runs the controls in a fresh
temporary layout, and compares the exact output with `REPORT.json`. Observed
runtime is written separately to standard error and is not a reference value.

The five controls cover genera 1, 2, 3, 4, and 8; exact field-parameter
boundaries; nonsquare parameters; repeated factors; near-boundary inverse
roots; and an irreducible degree-8 polynomial. All 41 returned coefficients
agree exactly. All 18 requested resultants are computed by cyclic-shift
determinants and checked independently by full-degree companion powers and
fraction-free determinants. Products of quadratic factors also have separate
second-order count recurrences. The decoder receives none of those constructions.

For the irreducible example, the real polynomial
$`x^4-x^3-4x^2+4x+1`$ has four roots in $`(-2,2)`$, verified by exact signs on
four disjoint intervals. Its reduction modulo 2 has no linear or irreducible
quadratic factor, hence is irreducible. Its $`q`$-Weil transform is irreducible
because the quadratic discriminant is negative at every real embedding.

Every final unrounded coefficient differs from the known control coefficient
by less than $`1/32`$, verified with exact rational arithmetic. Two legal
logarithm-enclosure perturbations also recover the correct result, and seven
malformed inputs are rejected. The alteration of one supplied count is
accepted while retaining the original polynomial; independent resultant
replay finds the discrepancy. Reconstruction does not authenticate counts.

These are supplied-polynomial controls, not newly counted curves. Jacobian
realization, field-order acquisition, publication priority, and theorem-wide
correctness are not established by finite controls. The uniform conclusion
depends on the written analytic and bit-complexity proof.
