# Problem 632: https://projecteuler.net/problem=632

from math import comb, isqrt, prod

import numpy as np
from sympy import primerange


def solve(n=10**16):
    mod = 1_000_000_007
    lim = isqrt(n)
    remaining = np.arange(lim + 1, dtype=np.int32)
    omega = np.zeros(lim + 1, dtype=np.uint8)

    for p in primerange(2, isqrt(lim) + 1):
        remaining[p::p] //= p
        omega[p::p] += 1
        remaining[p * p::p * p] = 0

    omega[remaining > 1] += 1
    omega[remaining == 0] = 0
    del remaining

    counts = [n]
    for k in range(1, int(omega.max()) + 1):
        d = np.flatnonzero(omega == k)
        counts.append(int(np.sum(n // (d * d))))

    for k in range(len(counts) - 1, -1, -1):
        counts[k] -= sum(comb(j, k) * counts[j] for j in range(k + 1, len(counts)))

    return prod(c for c in counts if c) % mod


if __name__ == "__main__":
    print(solve())
