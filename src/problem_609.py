# Problem 609: https://projecteuler.net/problem=609

from collections import Counter
from math import prod

import numpy as np
from sympy import sieve


def solve(n=10**8):
    mod = 1000000007
    primes = np.fromiter(sieve.primerange(2, n + 1), dtype=np.int64)
    size = len(primes)
    gaps = np.diff(np.append(primes, n + 1)) - 1
    prime = np.zeros(size + 1, dtype=bool)
    prime[primes[primes <= size]] = True
    pi = np.cumsum(prime, dtype=np.int32)
    current = np.arange(1, size + 1, dtype=np.int32)
    counts = np.zeros_like(current)
    totals = Counter()

    while current.size:
        counts += np.logical_not(prime[current])
        for k, value in enumerate(np.bincount(counts)):
            totals[k] += int(value)
        for k, value in enumerate(np.bincount(counts, weights=gaps)):
            totals[k + 1] += int(value)
        current = pi[current]
        active = current > 0
        current = current[active]
        counts = counts[active]
        gaps = gaps[active]

    return prod(value for value in totals.values() if value) % mod


if __name__ == "__main__":
    print(solve())
