# Problem 415: https://projecteuler.net/problem=415

from math import isqrt

import numpy as np
from sympy import sieve


MOD = 10**8
PERIOD = 312_500
LIMIT = 5_000_000
N = 10**11
MODS = (MOD, 2 * MOD, MOD)


def power_sum(n, j, mod):
    n = np.asarray(n, dtype=np.int64)
    if j == 0:
        return n % mod
    if j == 1:
        m = 2 * mod
        return (n % m * ((n + 1) % m) % m) // 2
    m = 6 * mod
    return (n % m * ((n + 1) % m) % m * ((2 * n + 1) % m) % m) // 6


def dot_power(values, x, j, mod):
    coeff = np.ones(x.size, dtype=np.int64) if j == 0 else x % mod
    if j == 2:
        coeff = coeff * coeff % mod
    return int(np.sum(coeff * values % mod, dtype=np.int64) % mod)


def totient_tables():
    phi = np.empty(LIMIT + 1, dtype=np.int64)
    phi[0] = 0
    phi[1:] = np.fromiter(
        sieve.totientrange(1, LIMIT + 1), dtype=np.int64, count=LIMIT
    )
    k = np.arange(LIMIT + 1, dtype=np.int64)
    small = []
    values = phi

    for j, mod in enumerate(MODS):
        if j:
            values = values * (k % mod) % mod
        prefix = np.cumsum(values, dtype=np.int64) % mod
        small.append(prefix.astype(np.uint32))

    cap = N // (LIMIT + 1)
    large = [np.zeros(cap + 1, dtype=np.uint32) for _ in range(3)]

    for i in range(cap, 0, -1):
        n = N // i
        h = isqrt(n)
        cut = min(h, cap // i)
        tri = n * (n + 1) // 2
        result = [
            tri % MOD,
            n * (n + 1) * (2 * n + 1) // 6 % (2 * MOD),
            tri * tri % MOD,
        ]

        if cut >= 2:
            x = np.arange(2, cut + 1, dtype=np.int64)
            indices = i * x
            for j, mod in enumerate(MODS):
                result[j] -= dot_power(large[j][indices], x, j, mod)

        if cut < h:
            x = np.arange(max(2, cut + 1), h + 1, dtype=np.int64)
            q = n // x
            for j, mod in enumerate(MODS):
                result[j] -= dot_power(small[j][q], x, j, mod)

        q = np.arange(1, n // (h + 1) + 1, dtype=np.int64)
        hi = n // q
        lo = n // (q + 1)
        for j, mod in enumerate(MODS):
            coeff = (power_sum(hi, j, mod) - power_sum(lo, j, mod)) % mod
            result[j] -= int(
                np.sum(coeff * small[j][q] % mod, dtype=np.int64) % mod
            )

        for j, mod in enumerate(MODS):
            large[j][i] = result[j] % mod

    return small, large


def coefficient_tables():
    c = np.empty(PERIOD, dtype=np.int64)
    p = pow(2, 8, MOD)
    for i in range(PERIOD):
        c[i] = (p - 1) % MOD
        p = 2 * p % MOD

    d = np.arange(9, 9 + PERIOD, dtype=np.int64)
    prefix = []
    values = c
    for j in range(3):
        if j:
            values = values * (d % MOD) % MOD
        sums = np.empty(PERIOD + 1, dtype=np.uint32)
        sums[0] = 0
        sums[1:] = (np.cumsum(values, dtype=np.int64) % MOD).astype(np.uint32)
        prefix.append(sums)

    initial = []
    for j in range(3):
        sums = [0]
        for d in range(1, 9):
            sums.append((sums[-1] + (2 ** (d - 1) - 1) * d**j) % MOD)
        initial.append(sums)

    return initial, prefix, tuple(int(sums[-1]) for sums in prefix)


def coefficient_prefix(n, initial, prefix, totals):
    if n <= 8:
        return tuple(sums[n] for sums in initial)

    q, r = divmod(n - 8, PERIOD)
    shift = q * PERIOD
    t1 = q * (q - 1) // 2
    t2 = q * (q - 1) * (2 * q - 1) // 6
    partial = tuple(int(sums[r]) for sums in prefix)
    return (
        (initial[0][8] + q * totals[0] + partial[0]) % MOD,
        (
            initial[1][8]
            + q * totals[1]
            + PERIOD * totals[0] * t1
            + partial[1]
            + shift * partial[0]
        )
        % MOD,
        (
            initial[2][8]
            + q * totals[2]
            + 2 * PERIOD * totals[1] * t1
            + PERIOD**2 * totals[0] * t2
            + partial[2]
            + 2 * shift * partial[1]
            + shift**2 * partial[0]
        )
        % MOD,
    )


def titanic_sets(n, small, large, coefficients):
    initial, prefix, totals = coefficients

    def coefficient_range(lo, hi):
        a = coefficient_prefix(hi, initial, prefix, totals)
        b = coefficient_prefix(lo - 1, initial, prefix, totals)
        return tuple((a[j] - b[j]) % MOD for j in range(3))

    side = n + 1
    c0, c1, _ = coefficient_range(2, n)
    bad = 1 + side * side + 2 * side * (side * c0 - c1)
    nonaxis = 0
    lo = 2

    while lo <= n:
        m = n // lo
        hi = n // m
        c0, c1, c2 = coefficient_range(lo, hi)
        phi = (
            tuple(int(small[j][m]) for j in range(3))
            if m <= LIMIT
            else tuple(int(large[j][lo]) for j in range(3))
        )
        pairs = (2 * phi[0] - 1) % MOD
        coordinates = (1 + 3 * ((phi[1] - 1) % (2 * MOD)) // 2) % MOD
        nonaxis += (
            side * side * pairs * c0
            - 2 * side * coordinates * c1
            + phi[2] * c2
        )
        nonaxis %= MOD
        lo = hi + 1

    return (pow(2, side * side, MOD) - bad - 2 * nonaxis) % MOD


def solve():
    small, large = totient_tables()
    coefficients = coefficient_tables()
    return titanic_sets(N, small, large, coefficients)


if __name__ == "__main__":
    print(solve())
