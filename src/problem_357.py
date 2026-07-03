# Problem 357: https://projecteuler.net/problem=357

from math import isqrt

import numpy as np
from sympy import sieve


N = 100_000_000


def solve():
    primes = np.fromiter(sieve.primerange(2, N + 2), dtype=np.int64)
    is_prime = np.zeros(N + 2, dtype=np.bool_)
    is_prime[primes] = True
    candidates = primes - 1
    candidates = candidates[candidates <= N]

    for d in range(2, isqrt(N) + 1):
        divisible = candidates % d == 0
        if np.any(divisible):
            keep = np.ones(len(candidates), dtype=np.bool_)
            keep[divisible] = is_prime[d + candidates[divisible] // d]
            candidates = candidates[keep]

    return int(candidates.sum())


if __name__ == "__main__":
    print(solve())
