# Problem 728: https://projecteuler.net/problem=728

from math import isqrt

import numpy as np
from sympy import sieve


def solve(n=10**7):
    mod = 1_000_000_007
    c = np.zeros(n + 1, dtype=np.int64)
    c[1:] = np.fromiter(sieve.totientrange(1, n + 1), dtype=np.int64, count=n)
    c[2::2] *= 2
    c[3::2] = c[3::2] // 2 * 3

    powers = np.empty(n + 1, dtype=np.int64)
    powers[0] = 1
    length = 1
    while length <= n:
        end = min(2 * length, n + 1)
        q = int(powers[length - 1]) * 2 % mod
        powers[length:end] = powers[:end - length] * q % mod
        length = end

    total = 2 * n
    cut = isqrt(n)
    for m in range(2, cut + 1):
        q = int(powers[m - 1])
        count = n // m
        if q == 1:
            s = count
        else:
            s = q * (pow(q, count, mod) - 1) * pow(q - 1, -1, mod) % mod
        total = (total + int(c[m]) * s) % mod

    for d in range(1, n // (cut + 1) + 1):
        end = n // d
        terms = c[cut + 1:end + 1] * powers[d * cut:d * end:d] % mod
        total = (total + int(terms.sum())) % mod
    return total


if __name__ == "__main__":
    print(solve())
