# Problem 642: https://projecteuler.net/problem=642

from itertools import accumulate
from math import isqrt

import numpy as np
from sympy import sieve


def solve(n=201820182018):
    mod = 10**9
    root = isqrt(n)
    primes = list(sieve.primerange(root + 1))
    prefix = list(accumulate(primes, initial=0))
    values = np.concatenate((n // np.arange(1, root + 1),
                             np.arange(n // root - 1, 0, -1)))
    size = len(values)
    a = values.copy()
    b = values + 1
    even = a % 2 == 0
    a[even] //= 2
    b[np.logical_not(even)] //= 2
    sums = ((a % mod) * (b % mod) - 1) % mod

    for i, p in enumerate(primes):
        square = p * p
        stop = n // square if square > root else size - square + 1
        divided = values[:stop] // p
        indices = np.where(divided <= root, size - divided, n // divided - 1)
        sums[:stop] = (sums[:stop] - p * (sums[indices] - prefix[i])) % mod

    sums = sums.tolist()

    def total(x, start):
        index = size - x if x <= root else n // x - 1
        result = sums[index] - prefix[start]
        for i in range(start, len(primes)):
            p = primes[i]
            if p * p > x:
                break
            result += total(x // p, i)
        return result % mod

    return total(n, 0)


if __name__ == "__main__":
    print(solve())
