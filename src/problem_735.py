# Problem 735: https://projecteuler.net/problem=735

from math import isqrt

import numpy as np
from sympy import integer_nthroot, sieve


def cone_sum(n):
    b = int(integer_nthroot(n, 3)[0])
    indices = np.arange(1, max(isqrt(n), 2 * b) + 1, dtype=np.int64)
    total = 0
    for j in range(1, b + 1):
        q = n // j
        s = isqrt(q)
        d = 2 * int((q // indices[:s]).sum()) - s * s
        total += 2 * d
        total -= int((q // indices[:j - 1]).sum())
        total -= int((q // indices[:2 * j - 1]).sum())

    for r in (1, 2):
        for g in range(1, n // (r * (b + 1) ** 2) + 1):
            q = n // g
            s = isqrt(q // r)
            count = s - b
            total += int((q // indices[b:s]).sum()) + count
            total -= r * (b + 1 + s) * count // 2
    return total


def solve(n=10**12):
    limit = isqrt(n)
    pairs = np.zeros(limit + 1, dtype=np.int64)
    for b in range(1, isqrt(limit) + 1):
        pairs[b * b::b] += 1
        pairs[2 * b * b::b] += 1
    small = np.zeros(limit + 1, dtype=np.int64)
    for g in range(1, limit + 1):
        small[g::g] += pairs[1:limit // g + 1]
    np.cumsum(small, out=small)

    total = 0
    for k, mu in enumerate(sieve.mobiusrange(1, limit + 1), 1):
        if k % 2 == 0 or mu == 0:
            continue
        q = n // (k * k)
        a = int(small[q]) if q <= limit else cone_sum(q)
        q //= 2
        b = int(small[q]) if q <= limit else cone_sum(q)
        total += mu * (a - b)
    return total


if __name__ == "__main__":
    print(solve())
