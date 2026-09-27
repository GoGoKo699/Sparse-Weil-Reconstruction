"""Prototype: first-g cyclic-resultant reconstruction under q>=65536*g^2.

This is an internally checked research prototype for a candidate theorem.
Only q, g and the promised true first g counts reach the reconstruction routine.
Supplying malformed counts can yield arbitrary output: decoding is not authentication.
"""
from __future__ import annotations

from fractions import Fraction as Q
from pathlib import Path
from typing import Mapping
import importlib.util
import sys

DEPENDENCY = Path(__file__).resolve().parent.parent / 'all_field_reconstruction_v1/reconstruct.py'
spec = importlib.util.spec_from_file_location('first_g_baseline_logs', DEPENDENCY)
baseline = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = baseline
spec.loader.exec_module(baseline)
InvalidData = baseline.InvalidData


def ceil_log2(n: int) -> int:
    return (n - 1).bit_length()


def dyadic_nearest(x: Q, bits: int) -> Q:
    scaled = x * (1 << bits)
    return Q((2 * scaled.numerator + scaled.denominator) // (2 * scaled.denominator),
             1 << bits)


def reciprocal_completion(low: list[Q], q: int) -> list[Q]:
    g = len(low) - 1
    return low + [q ** (g - i) * low[i] for i in range(g - 1, -1, -1)]


def log_series(coefficients: list[Q], degree: int) -> list[Q]:
    """Exact formal coefficients of log(P); no roots are computed."""
    out = [Q(0)]
    for n in range(1, degree + 1):
        cn = coefficients[n] if n < len(coefficients) else Q(0)
        previous = sum((j * out[j] * coefficients[n - j]
                        for j in range(max(1, n - len(coefficients) + 1), n)), Q(0))
        out.append(cn - previous / n)
    return out


def exp_series(logarithm: list[Q]) -> list[Q]:
    out = [Q(1)]
    for n in range(1, len(logarithm)):
        out.append(sum((j * logarithm[j] * out[n - j] for j in range(1, n + 1)), Q(0)) / n)
    return out


def reconstruct(q: int, g: int, supplied_orders: Mapping[int, int]) -> tuple[list[int], dict]:
    baseline.integer(g, 'genus', 1)
    baseline.integer(q, 'field-size parameter', 2)
    if q < 65536 * g * g:
        raise InvalidData('q must be at least 65536*g^2 for this decoder')
    data = dict(supplied_orders)
    if any(type(n) is not int for n in data) or set(data) != set(range(1, g + 1)):
        raise InvalidData('order keys differ from the first-g query set')
    for v in data.values():
        baseline.integer(v, 'supplied cardinality', 1)

    W = (8 * g * q) ** g
    N = ceil_log2(64 * W)
    B = N + 5
    M = g + (N + ceil_log2(g) + 10) // 5
    tolerance = Q(1, (1 << N) * 64 * g * q ** g)
    log_bits = ceil_log2(2 * tolerance.denominator)
    Y = [Q(0)]
    logs = []
    for n in range(1, g + 1):
        box, metadata = baseline.log_enclosure(data[n], q ** (g * n), tolerance / 2)
        centre = dyadic_nearest(box.centre, log_bits)
        error = box.radius + abs(centre - box.centre)
        if error > tolerance:
            raise InvalidData('log center exceeded its allowance')
        Y.append(Q(q ** n, n) * centre)
        logs.append(dict(n=n, log_error_numerator=error.numerator,
                         log_error_denominator=error.denominator, **metadata))

    low = [Q(1)] + [Q(0)] * g
    max_intermediate_bits = 0
    for _ in range(N):
        b = log_series(reciprocal_completion(low, q), M)
        corrected = [Q(0)]
        for n in range(1, g + 1):
            alias = sum((b[n * k] / q ** (n * (k - 1))
                         for k in range(2, M // n + 1)), Q(0))
            corrected.append(Y[n] - alias)
        exact = exp_series(corrected)
        max_intermediate_bits = max(max_intermediate_bits,
            max(max(x.numerator.bit_length(), x.denominator.bit_length()) for x in b + exact))
        low = [Q(1)] + [dyadic_nearest(x, B) for x in exact[1:]]

    rounded = [int(dyadic_nearest(x, 0)) for x in low]
    result = reciprocal_completion(rounded, q)
    # The metadata retains the unrounded low coefficients for validation only.
    return result, dict(query_count=g, max_degree=g, iterations=N, coefficient_bits=B,
                        alias_cutoff=M, log_bits=log_bits, log_rows=logs,
                        max_intermediate_bits=max_intermediate_bits,
                        unrounded_low=low)
