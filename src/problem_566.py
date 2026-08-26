# Problem 566: https://projecteuler.net/problem=566
from array import array
from math import isqrt, lcm

import numpy as np
from sympy.ntheory.modular import solve_congruence


def layouts(size, cuts):
    order = np.arange(size, dtype=np.min_scalar_type(size - 1))
    signs = np.ones(size, dtype=np.int8)
    targets = []
    for turn, cut in enumerate(cuts):
        order = np.concatenate((order[cut:], order[:cut][::-1]))
        signs = np.concatenate((signs[cut:], -signs[:cut][::-1]))
        if turn < 2:
            target = np.empty(size, dtype=np.int8)
            target[order] = signs
            targets.append(target)
    permutation = array("q")
    permutation.frombytes(order.astype(np.int64, copy=False).tobytes())
    compact_signs = array("b")
    compact_signs.frombytes(signs.tobytes())
    return permutation, compact_signs, targets


def cycle_solutions(perm, signs, targets):
    seen = bytearray(len(perm))
    congruences = [set() for _ in targets]
    possible = [True] * len(targets)
    for first in range(len(perm)):
        if seen[first]:
            continue
        cycle = array("q")
        j = first
        while not seen[j]:
            seen[j] = True
            cycle.append(j)
            j = perm[j]

        gauge = bytearray([1])
        for i in range(len(cycle) - 1):
            gauge.append(gauge[-1] if signs[cycle[i]] > 0 else not gauge[-1])
        initial = bytes(gauge)
        indices = np.frombuffer(cycle, dtype=np.int64)
        gauge_array = np.frombuffer(gauge, dtype=np.uint8)
        if bool(gauge[-1]) == (signs[cycle[-1]] > 0):
            extended = initial + initial
        else:
            opposite = np.logical_not(gauge_array).tobytes()
            extended = initial + opposite + initial
        period = extended.find(initial, 1)
        for i, target in enumerate(targets):
            if not possible[i]:
                continue
            wanted = (gauge_array == (target[indices] > 0)).tobytes()
            hit = extended.find(wanted)
            if hit < 0 or hit >= period:
                possible[i] = False
            else:
                congruences[i].add((hit, period))

    answers = []
    for valid, equations in zip(possible, congruences):
        answers.append(solve_congruence(*sorted(equations)) if valid else None)
    return answers


def rational_flips(a, b, numerator, denominator):
    size = lcm(a, b, denominator)
    cuts = [size // a, size // b, numerator * (size // denominator)]
    perm, signs, targets = layouts(size, cuts)
    results = cycle_solutions(perm, signs, [np.ones(size, dtype=np.int8)] + targets)
    answers = [3 * int(results[0][1])]
    for remainder, result in enumerate(results[1:], 1):
        if result is not None:
            answers.append(3 * int(result[0]) + remainder)
    return min(answers)


def fraction_period(scale, c):
    d = scale * scale * c
    floor_root = isqrt(d)
    whole = floor_root // c
    p = whole * c
    q = (d - p * p) // c
    first = p, q
    period = []
    while True:
        term = (p + floor_root) // q
        period.append(term)
        p = term * q - p
        q = (d - p * p) // q
        if (p, q) == first:
            return whole, period


def flips(a, b, c):
    root = isqrt(c)
    if root * root == c:
        return rational_flips(a, b, 1, root)

    scale = lcm(a, b)
    whole, period = fraction_period(scale, c)
    p0, p1 = 0, 1
    q0, q1 = 1, 0
    previous = None
    for term in [whole] + period:
        p = term * p1 + p0
        q = term * q1 + q0
        value = rational_flips(a, b, p, scale * q)
        if q > 1 and value == previous:
            return value
        previous = value
        p0, p1 = p1, p
        q0, q1 = q1, q
    return previous


def solve():
    n = 53
    total = 0
    for a in range(9, n - 1):
        for b in range(a + 1, n):
            for c in range(b + 1, n + 1):
                total += flips(a, b, c)
    return total


if __name__ == "__main__":
    print(solve())
