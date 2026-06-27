# Problem 338: https://projecteuler.net/problem=338

from math import isqrt

import numpy as np
from sympy import integer_nthroot


N = 10**12
MOD = 10**8


def divisor_sum(n):
    total = 0
    i = 1

    while i <= n:
        q = n // i
        j = n // q
        total += q * (j - i + 1)
        i = j + 1

    return total


def product_sum(n):
    total = 0
    i = 2

    while i <= n:
        a = n // i
        b = n // (i - 1)
        j = min(n // a, n // b + 1, n)
        total = (total + (j - i + 1) * (a % MOD) * (b % MOD)) % MOD
        i = j + 1

    return total


def ordered_triples(n):
    total = 0
    lim = integer_nthroot(n, 3)[0]

    for a in range(1, lim + 1):
        hi = isqrt(n // a)
        b = np.arange(a, hi + 1, dtype=np.int64)
        c = n // (a * b)
        vals = 3 + 6 * (c - b)
        vals[0] = 1 + 3 * (c[0] - a)
        total += int(vals.sum())

    return total


def solve():
    return (product_sum(N) - ordered_triples(N) + divisor_sum(N)) % MOD


if __name__ == "__main__":
    print(solve())
