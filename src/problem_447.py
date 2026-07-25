# Problem 447: https://projecteuler.net/problem=447

from math import isqrt

import numpy as np
from sympy import sieve


N = 10**14
MOD = 1_000_000_007
BLOCK = 1_000_000


def summatory_sigma(n):
    root = isqrt(n)
    total = 0
    for start in range(1, root + 1, BLOCK):
        indexes = np.arange(
            start,
            min(root + 1, start + BLOCK),
            dtype=np.uint64,
        )
        quotients = n // indexes
        terms = quotients % MOD
        terms *= indexes
        terms %= MOD

        parity = quotients % 2
        halves = (quotients + 1) // 2
        halves %= MOD
        quotients += 1
        quotients -= parity
        quotients %= MOD
        terms += halves * quotients % MOD
        terms %= MOD
        total += int(terms.sum(dtype=np.uint64) % MOD)

    overlap = root * root * (root + 1) // 2
    return (total - overlap) % MOD


def solve():
    limit = isqrt(N)
    mu = np.fromiter(
        sieve.mobiusrange(1, limit + 1),
        dtype=np.int8,
        count=limit,
    )
    weighted = np.arange(1, limit + 1, dtype=np.int64)
    weighted *= mu
    prefix = np.empty(limit + 1, dtype=np.int64)
    prefix[0] = 0
    np.cumsum(weighted, out=prefix[1:])

    total = 0
    k = 1
    while k <= limit:
        quotient = N // (k * k)
        end = isqrt(N // quotient)
        coefficient = int(prefix[end] - prefix[k - 1])
        total = (total + coefficient * summatory_sigma(quotient)) % MOD
        k = end + 1

    return (total - N * (N + 1) // 2) % MOD


if __name__ == "__main__":
    print(solve())
