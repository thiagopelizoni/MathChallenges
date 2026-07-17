# Problem 407: https://projecteuler.net/problem=407

from math import isqrt

import numpy as np


N = 10**7
BLOCK = 1_000_000


def sum_idempotents(limit):
    best = np.ones(limit + 1, dtype=np.int32)
    best[:2] = 0

    for d in range(2, isqrt(limit) + 1):
        residues = np.arange(1, d, dtype=np.int64)
        units = residues[np.gcd(residues, d) == 1]
        inverse = np.zeros(d, dtype=np.int64)
        inverse[units] = [pow(int(r), -1, d) for r in units]

        stop = limit // d + 1
        for start in range(d + 1, stop, BLOCK):
            e = np.arange(start, min(start + BLOCK, stop), dtype=np.int64)
            s = inverse[e % d]
            valid = s > 0
            e = e[valid]
            s = s[valid]
            n = d * e
            a = e * s
            candidate = np.maximum(a, n + 1 - a)
            best[n] = np.maximum(best[n], candidate)

    return int(np.sum(best, dtype=np.int64))


def solve():
    return sum_idempotents(N)


if __name__ == "__main__":
    print(solve())
