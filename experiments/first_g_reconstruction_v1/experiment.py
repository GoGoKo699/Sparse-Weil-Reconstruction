"""Targeted exact controls for the first-g contraction prototype.

No factorization or polynomial is passed to the decoder. Controls are supplied
Weil polynomials, with no claim of Jacobian realization. Finite controls do not
prove the candidate uniform theorem.
"""
from fractions import Fraction as Q
from itertools import permutations
from math import comb
import json
import sys
import time

import reconstruct as subject


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def multiply(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            result[i + j] += u * v
    return result


def determinant_by_permutations(matrix):
    n = len(matrix)
    answer = 0
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        term = (-1) ** inversions
        for i, j in enumerate(perm):
            term *= matrix[i][j]
        answer += term
    return answer


def cyclic_resultant(polynomial, n):
    # chi(X)=X^(2g)P(1/X); det(chi(S_n))=K_n because deg(chi) is even.
    reduced = [0] * n
    for i, coefficient in enumerate(reversed(polynomial)):
        reduced[i % n] += coefficient
    return determinant_by_permutations([[reduced[(i - j) % n] for j in range(n)]
                                       for i in range(n)])


def matrix_product(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def companion_resultants(P, degree):
    """Independent full-degree companion powers and fraction-free determinants."""
    size = len(P) - 1
    C = [[0] * size for _ in range(size)]
    for j in range(size):
        C[j][-1] = -P[size - j]
        if j:
            C[j][j - 1] = 1
    identity = [[int(i == j) for j in range(size)] for i in range(size)]
    power = identity
    answers = {}
    for n in range(1, degree + 1):
        power = matrix_product(power, C)
        a = [[identity[i][j] - power[i][j] for j in range(size)] for i in range(size)]
        previous, sign = 1, 1
        zero = False
        for k in range(size - 1):
            pivot_row = next((r for r in range(k, size) if a[r][k]), None)
            if pivot_row is None:
                zero = True
                break
            if pivot_row != k:
                a[k], a[pivot_row] = a[pivot_row], a[k]
                sign = -sign
            pivot = a[k][k]
            for i in range(k + 1, size):
                for j in range(k + 1, size):
                    a[i][j], remainder = divmod(a[i][j] * pivot - a[i][k] * a[k][j], previous)
                    check(remainder == 0, 'nonexact companion Bareiss division')
                a[i][k] = 0
            previous = pivot
        answers[n] = 0 if zero else sign * a[-1][-1]
    return answers


def quadratic_orders(q, traces, n):
    result = 1
    for trace in traces:
        previous, current = 2, trace
        for _ in range(2, n + 1):
            previous, current = current, trace * current - q * previous
        result *= 1 + q ** n - current
    return result


def irreducible_control(q):
    # f=X^4-X^3-4X^2+4X+1 has four real roots in (-2,2).
    f = [1, 4, -4, -1, 1]
    evaluate = lambda x: sum(c * x ** j for j, c in enumerate(f))
    intervals = [(-2, -1), (-1, 0), (1, Q(3, 2)), (Q(3, 2), 2)]
    check(all(evaluate(a) * evaluate(b) < 0 for a, b in intervals), 'real root intervals')
    # Mod 2, f=X^4+X^3+1 has no linear factor and has nonzero remainder
    # modulo the only monic irreducible quadratic X^2+X+1 (remainder X).
    check(sum(c for c in f) % 2 == 1 and f[0] % 2 == 1, 'mod-2 linear factors')
    remainder = [c % 2 for c in f]
    for j in range(4, 1, -1):
        if remainder[j]:
            for k in range(3):
                remainder[j - 2 + k] ^= 1
    check(remainder[:2] == [0, 1], 'mod-2 quadratic factor')
    # All real conjugates t satisfy t^2<4<4q. Thus t^2-4q cannot be a
    # square in the totally real field Q(t): the Weil transform is irreducible.
    P = [0] * 9
    for j, coefficient in enumerate(f):
        for k in range(j + 1):
            P[4 - j + 2 * k] += coefficient * comb(j, k) * q ** k
    return P


def run():
    controls = []
    fixtures = []
    for g, traces in ((1, [511]), (2, [0, -17]), (3, [1, 1, -3]),
                      (8, [4095, -4095, 0, 0, 1, -1, 7, 17])):
        q = 65536 * g * g + (1 if g == 2 else 0)
        P = [1]
        for trace in traces:
            check(trace * trace <= 4 * q, 'quadratic Weil promise')
            P = multiply(P, [1, -trace, q])
        fixtures.append((f'quadratic_g{g}', q, g, P, traces))
    q = 65536 * 4 * 4 + 1
    fixtures.append(('irreducible_degree8', q, 4, irreducible_control(q), None))

    for name, q, g, P, traces in fixtures:
        orders = {n: cyclic_resultant(P, n) for n in range(1, g + 1)}
        check(all(K > 0 for K in orders.values()), 'positive supplied counts')
        check(orders == companion_resultants(P, g), 'independent companion determinants')
        if traces is not None:
            check(all(orders[n] == quadratic_orders(q, traces, n) for n in orders),
                  'independent quadratic-count calculation')
        start = time.monotonic()
        actual, details = subject.reconstruct(q, g, orders)
        elapsed = time.monotonic() - start
        check(actual == P, 'exact recovered coefficients: ' + name)
        max_error = max(abs(x - y) for x, y in zip(details['unrounded_low'], P))
        check(max_error < Q(1, 32), 'proved final raw coefficient budget: ' + name)
        row = dict(name=name, q=q, g=g, recovered_coefficients=len(actual),
                   max_input_bits=max(K.bit_length() for K in orders.values()),
                   iterations=details['iterations'], alias_cutoff=details['alias_cutoff'],
                   coefficient_bits=details['coefficient_bits'], log_bits=details['log_bits'],
                   max_intermediate_bits=details['max_intermediate_bits'],
                   final_error_less_than_one_over_32=True)
        print(f'{name}: {elapsed:.3f}s', file=sys.stderr, flush=True)
        controls.append(row)

    # Uniform allowed log-enclosure perturbations, on the mixed nonsquare q control.
    _, q, g, P, traces = fixtures[1]
    orders = {n: cyclic_resultant(P, n) for n in range(1, g + 1)}
    original = subject.baseline.log_enclosure
    displaced_runs = 0
    for sign in (-1, 1):
        def displaced(num, den, tol, sign=sign):
            box, metadata = original(num, den, tol)
            return subject.baseline.Interval(box.centre + sign * (tol - box.radius), tol), metadata
        subject.baseline.log_enclosure = displaced
        try:
            check(subject.reconstruct(q, g, orders)[0] == P, 'allowed log displacement')
        finally:
            subject.baseline.log_enclosure = original
        displaced_runs += 1

    malformed = [
        (65535, 1, {1: 65536}),
        (65536, 0, {}),
        (65536, 1, {}),
        (65536, 1, {1: 65536, 2: 1}),
        (65536, 1, {True: 65536}),
        (65536, 1, {1: 0}),
        (True, 1, {1: 1}),
    ]
    for q, g, counts in malformed:
        try:
            subject.reconstruct(q, g, counts)
        except subject.InvalidData:
            pass
        else:
            raise AssertionError('malformed input accepted')

    # Observe a malformed transcript without prescribing the decoder's response.
    # Either rejection or a returned polynomial with a replay mismatch is retained.
    _, q, g, P, _ = fixtures[1]
    corrupted = {n: cyclic_resultant(P, n) for n in range(1, g + 1)}
    corrupted[g] += 1
    try:
        returned, _ = subject.reconstruct(q, g, corrupted)
    except subject.InvalidData:
        corruption = dict(accepted=False)
    else:
        corruption = dict(accepted=True, original_polynomial_returned=returned == P,
                          supplied_resultants_match=companion_resultants(returned, g) == corrupted)

    return dict(scope='Targeted exact prototype controls; no curve realization or priority claim.',
                controls=controls, allowed_log_displacement_runs=displaced_runs,
                malformed_input_rejections=len(malformed), altered_count_observation=corruption,
                independent_companion_determinants=sum(row['g'] for row in controls))


if __name__ == '__main__':
    if not __debug__:
        raise SystemExit('Do not run with -O or -OO.')
    report = run()
    print(json.dumps(report, sort_keys=True, indent=2))
