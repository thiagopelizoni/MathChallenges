# Problem 448: https://projecteuler.net/problem=448

from math import isqrt

import numpy as np
from sympy import sieve


N = 99_999_999_019
MOD = 999_999_017
LIMIT = 5_000_000
INV2 = pow(2, -1, MOD)
INV6 = pow(6, -1, MOD)


def interval_sum(first, last):
    return (
        (first % MOD + last % MOD)
        * ((last - first + 1) % MOD)
        % MOD
        * INV2
        % MOD
    )


def weighted_totient_tables():
    small = np.empty(LIMIT + 1, dtype=np.int64)
    small[0] = 0
    small[1:] = np.fromiter(
        sieve.totientrange(1, LIMIT + 1),
        dtype=np.int64,
        count=LIMIT,
    )
    small *= np.arange(LIMIT + 1, dtype=np.int64)
    np.remainder(small, MOD, out=small)
    np.cumsum(small, out=small)
    np.remainder(small, MOD, out=small)

    cap = N // (LIMIT + 1)
    large = np.zeros(cap + 1, dtype=np.int64)
    for i in range(cap, 0, -1):
        n = N // i
        root = isqrt(n)
        cut = min(root, cap // i)
        a = n % MOD
        total = (
            a
            * ((n + 1) % MOD)
            % MOD
            * ((2 * n + 1) % MOD)
            % MOD
            * INV6
            % MOD
        )

        if cut >= 2:
            k = np.arange(2, cut + 1, dtype=np.int64)
            total -= int(
                np.sum(k * large[i * k] % MOD, dtype=np.int64) % MOD
            )

        if cut < root:
            k = np.arange(max(2, cut + 1), root + 1, dtype=np.int64)
            total -= int(
                np.sum(k * small[n // k] % MOD, dtype=np.int64) % MOD
            )

        q = np.arange(1, n // (root + 1) + 1, dtype=np.int64)
        high = n // q
        low = n // (q + 1)
        coefficients = interval_sum(low + 1, high)
        total -= int(
            np.sum(coefficients * small[q] % MOD, dtype=np.int64) % MOD
        )
        large[i] = total % MOD

    return small, large


def solve():
    small, large = weighted_totient_tables()
    total = 0
    first = 1
    while first <= N:
        quotient = N // first
        last = N // quotient
        weighted_phi = (
            int(large[first])
            if quotient > LIMIT
            else int(small[quotient])
        )
        reduced_residues = (weighted_phi + 1) * INV2 % MOD
        total += (last - first + 1) % MOD * reduced_residues
        total %= MOD
        first = last + 1
    return total


if __name__ == "__main__":
    print(solve())
