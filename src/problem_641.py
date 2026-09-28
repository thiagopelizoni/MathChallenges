# Problem 641: https://projecteuler.net/problem=641

from functools import cache
from math import isqrt

import numpy as np
from sympy import integer_nthroot, sieve


def solve(limit=10**36):
    maximum = int(integer_nthroot(limit, 4)[0])
    cutoff = int(integer_nthroot(maximum**2, 3)[0])
    mu = np.zeros(cutoff + 1, dtype=np.int64)
    mu[1:] = list(sieve.mobiusrange(1, cutoff + 1))
    prefix = np.cumsum(mu)
    squarefree = np.cumsum(mu != 0)
    indices = np.arange(1, isqrt(maximum) + 1, dtype=np.int64)
    squares = indices * indices

    @cache
    def mertens(n):
        root = isqrt(n)
        small = indices[:root]
        total = 1 - int(np.dot(prefix[1:root + 1], n // small - n // (small + 1)))
        split = n // (cutoff + 1)
        stop = n // (root + 1)
        total -= int(prefix[n // indices[split:stop]].sum())
        for d in range(2, split + 1):
            total -= mertens(n // d)
        return total

    total = 0
    a = 1
    while a**6 <= limit:
        b = int(integer_nthroot(limit // a**6, 4)[0])
        end = int(integer_nthroot(limit // b**4, 6)[0])
        if b <= cutoff:
            count = (int(squarefree[b]) + int(prefix[b])) // 2
        else:
            root = isqrt(b)
            count = (int(np.dot(mu[1:root + 1], b // squares[:root])) + mertens(b)) // 2
        total += (end - a + 1) * count
        a = end + 1
    return total


if __name__ == "__main__":
    print(solve())
