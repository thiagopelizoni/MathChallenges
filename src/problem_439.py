# Problem 439: https://projecteuler.net/problem=439

from functools import cache

import numpy as np
from sympy import sieve


N = 10**11
MOD = 10**9
MOBIUS_LIMIT = 3_000_000
SIGMA_LIMIT = 10_000_000


def interval_sum(first, last):
    return (first + last) * (last - first + 1) // 2


def mobius_table():
    values = np.zeros(MOBIUS_LIMIT + 1, dtype=np.int64)
    values[1:] = np.fromiter(
        sieve.mobiusrange(1, MOBIUS_LIMIT + 1),
        dtype=np.int64,
        count=MOBIUS_LIMIT,
    )
    values *= np.arange(MOBIUS_LIMIT + 1, dtype=np.int64)
    np.cumsum(values, out=values)
    np.remainder(values, MOD, out=values)
    return values


def sigma_table():
    values = np.zeros(SIGMA_LIMIT + 1, dtype=np.int64)
    for divisor in range(1, SIGMA_LIMIT + 1):
        values[divisor::divisor] += divisor
    np.cumsum(values, out=values)
    np.remainder(values, MOD, out=values)
    return values


def solve():
    weighted_mu = mobius_table()
    sigma = sigma_table()

    @cache
    def weighted_mertens(n):
        if n <= MOBIUS_LIMIT:
            return int(weighted_mu[n])
        total = 1
        first = 2
        while first <= n:
            quotient = n // first
            last = n // quotient
            total -= (
                interval_sum(first, last) % MOD
            ) * weighted_mertens(quotient)
            first = last + 1
        return total % MOD

    def summatory_sigma(n):
        if n <= SIGMA_LIMIT:
            return int(sigma[n])
        total = 0
        first = 1
        while first <= n:
            quotient = n // first
            last = n // quotient
            total += quotient * (interval_sum(first, last) % MOD)
            first = last + 1
        return total % MOD

    total = 0
    first = 1
    previous = 0
    while first <= N:
        quotient = N // first
        last = N // quotient
        current = weighted_mertens(last)
        sigma_sum = summatory_sigma(quotient)
        total += (current - previous) * sigma_sum * sigma_sum
        previous = current
        first = last + 1

    return total % MOD


if __name__ == "__main__":
    print(solve())
