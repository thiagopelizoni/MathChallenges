# Problem 780: https://projecteuler.net/problem=780
from functools import cache
from math import isqrt

from sympy import sieve


def divisor_pairs(n):
    r = isqrt(n)
    return 2 * sum(n // d for d in range(1, r + 1)) - r * r


def aligned_tilings(m, mu):
    @cache
    def lattice_points(n):
        total = 0
        for x in range(1, isqrt(n) + 1):
            total += (isqrt(4 * n - 3 * x * x) - x) // 2 + 1
        return total

    @cache
    def primitive_no_three(n):
        if not n:
            return 0
        total = 0
        for d in range(1, isqrt(n) + 1):
            if mu[d]:
                total += mu[d] * lattice_points(n // (d * d))
        return total - primitive_no_three(n // 3)

    limit = m // 2
    total, previous, q = 0, 0, 1
    while q <= limit:
        pairs = limit // q
        hi = limit // pairs
        count = primitive_no_three(hi)
        total += (count - previous) * divisor_pairs(pairs)
        previous, q = count, hi + 1
    return 2 * total


def floor_sum(n, a, b, modulus):
    total = 0
    while n:
        qa, a = divmod(a, modulus)
        qb, b = divmod(b, modulus)
        total += qa * n * (n - 1) // 2 + qb * n
        n, b = divmod(a * n + b, modulus)
        a, modulus = modulus, a
    return total


def oblique_seams(m, lim, mu):
    scale = 2 * m * m
    root = isqrt(3 * scale * scale)
    total = 0
    for t in range(1, lim + 1):
        k = m // t
        bound = isqrt((k * k) // (3 * t * t))
        for d in range(1, isqrt(bound) + 1):
            if not mu[d]:
                continue
            uv = bound // (d * d)
            slope = root * t * d * d
            count = 0
            for u in range(1, isqrt(uv) + 1):
                n = uv // u - u + 1
                step = slope * u
                start = step * u
                count += 2 * (n * k - floor_sum(n, step, start, scale))
                count -= k - start // scale
            total += mu[d] * count
    return 4 * total


def tilings(n):
    m = n // 2
    lim = isqrt(isqrt((m * m) // 3))
    mu = (0, *sieve.mobiusrange(1, lim + 1))
    return 2 * divisor_pairs(m) + oblique_seams(m, lim, mu) - 2 * aligned_tilings(m, mu)


def solve():
    return tilings(10**9) % 1_000_000_007


if __name__ == "__main__":
    print(solve())
