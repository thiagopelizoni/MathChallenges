# Problem 530: https://projecteuler.net/problem=530

from math import isqrt

import numpy as np
from sympy import sieve


N = 10**15
LIM = isqrt(N)
SMALL = 2_000_000
BLOCK = 1_000_000


def D(n, pref):
    if n <= SMALL:
        return int(pref[n])
    m = isqrt(n)
    total = 0
    for start in range(1, m + 1, BLOCK):
        d = np.arange(start, min(start + BLOCK, m + 1), dtype=np.int64)
        total += int(np.sum(n // d))
    return 2 * total - m * m


def solve():
    phi = np.fromiter(sieve.totientrange(1, LIM + 1), dtype=np.int64, count=LIM)
    np.cumsum(phi, out=phi)

    tau = np.zeros(SMALL + 1, dtype=np.int64)
    for i in range(1, SMALL + 1):
        tau[i::i] += 1
    pref = np.cumsum(tau)

    total = 0
    t = 1
    while t <= LIM:
        q = N // (t * t)
        r = isqrt(N // q)
        if r > LIM:
            r = LIM
        s = int(phi[r - 1])
        if t > 1:
            s -= int(phi[t - 2])
        total += s * D(q, pref)
        t = r + 1
    return total


if __name__ == "__main__":
    print(solve())
