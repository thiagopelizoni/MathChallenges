# Problem 388: https://projecteuler.net/problem=388

import numpy as np
from sympy import sieve


PREFIX_LIMIT = 1_000_000


def solve(limit=10**10):
    cutoff = min(PREFIX_LIMIT, limit)

    phi = np.zeros(cutoff + 1, dtype=np.uint64)
    phi[1:] = np.fromiter(
        sieve.totientrange(1, cutoff + 1), dtype=np.uint64, count=cutoff
    )

    jordan = np.arange(cutoff + 1, dtype=np.uint64)
    jordan *= jordan
    for p in sieve.primerange(2, cutoff + 1):
        jordan[p::p] -= jordan[p::p] // (p * p)

    phi = np.cumsum(phi, dtype=np.uint64)
    jordan = np.cumsum(jordan, dtype=np.uint64)
    memo = {}

    def sums(n):
        if n <= cutoff:
            return int(phi[n]), int(jordan[n])
        if n in memo:
            return memo[n]

        s1 = n * (n + 1) // 2
        s2 = n * (n + 1) * (2 * n + 1) // 6
        left = 2

        while left <= n:
            q = n // left
            right = n // q
            sub1, sub2 = sums(q)
            count = right - left + 1
            s1 -= count * sub1
            s2 -= count * sub2
            left = right + 1

        memo[n] = (s1, s2)
        return memo[n]

    s1, s2 = sums(limit)
    digits = str(1 + 3 * (s1 + s2))
    return digits[:9] + digits[-9:]


if __name__ == "__main__":
    print(solve())
