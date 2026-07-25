# Problem 450: https://projecteuler.net/problem=450

from itertools import product
from math import gcd, isqrt

import numpy as np
from sympy import integer_nthroot, sieve


N = 1_000_000


def axis_total(n):
    mu = np.zeros(n + 1, dtype=np.int64)
    mu[1:] = np.fromiter(
        sieve.mobiusrange(1, n + 1), dtype=np.int64, count=n
    )
    phi = np.zeros(n + 1, dtype=np.int64)
    phi[1:] = np.fromiter(
        sieve.totientrange(1, n + 1), dtype=np.int64, count=n
    )

    k = np.arange(n + 1, dtype=np.int64)
    m = (k - 1) // 2
    triangular = m * (m + 1) // 2
    coprime_sums = np.zeros(n + 1, dtype=np.int64)
    for d in np.flatnonzero(mu):
        coprime_sums[d::d] += (
            mu[d] * d * triangular[1 : n // d + 1]
        )

    p = np.arange(3, n + 1, dtype=np.int64)
    counts = phi[3:] // 2
    contributions = 4 * p * counts
    odd = p % 2 == 1
    twice_odd = p % 4 == 2
    contributions[odd] -= 2 * coprime_sums[3:][odd]
    contributions[twice_odd] -= 4 * coprime_sums[3:][twice_odd]
    scales = n // p
    return int(
        np.sum(
            contributions * scales * (scales + 1) // 2,
            dtype=np.int64,
        )
    )


def primitive_triples(limit):
    for m in range(2, isqrt(limit - 1) + 1):
        for n in range(1, m):
            c = m * m + n * n
            if c > limit:
                break
            if (m - n) % 2 == 1 and gcd(m, n) == 1:
                yield m * m - n * n, 2 * m * n, c


def gaussian_power(re, im, exponent):
    x, y = 1, 0
    for _ in range(exponent):
        x, y = x * re - y * im, x * im + y * re
    return x, y


def non_axis_total(n):
    total = 0
    e = 2
    while (limit := integer_nthroot(n, e)[0]) >= 5:
        triples = tuple(primitive_triples(limit))
        for q in range(1, e):
            if gcd(e, q) != 1:
                continue
            p = e + q
            for a, b, c in triples:
                denominator = c**e
                scale = c ** (e - q)
                for u, v in ((a, b), (b, a)):
                    for sx, sy in product((-1, 1), repeat=2):
                        re, im = sx * u, sy * v
                        xe, ye = gaussian_power(re, im, e)
                        xq, yq = gaussian_power(re, im, q)
                        nx = e * xq * scale + q * xe
                        ny = e * yq * scale - q * ye
                        common = gcd(
                            denominator,
                            gcd(abs(nx), abs(ny)),
                        )
                        required = denominator // common
                        count = n // (p * required)
                        norm = abs(nx // common) + abs(ny // common)
                        total += norm * count * (count + 1) // 2
        e += 1
    return total


def solve():
    return axis_total(N) + non_axis_total(N)


if __name__ == "__main__":
    print(solve())
