# Problem 688: https://projecteuler.net/problem=688
from math import isqrt

import numpy as np


def S(N, mod=None):
    kmax = (isqrt(8 * N + 1) - 1) // 2
    total = 0
    step = 10**7
    for lo in range(1, kmax + 1, step):
        k = np.arange(lo, min(lo + step, kmax + 1), dtype=np.int64)
        m = N - k * (k - 1) // 2
        q = m // k
        r = m % k
        even = q % 2 == 0
        a = np.where(even, q // 2, q)
        b = np.where(even, q - 1, (q - 1) // 2)
        if mod is None:
            total += int(np.sum(k * a * b + q * (r + 1)))
        else:
            t = (a % mod) * (b % mod) % mod * k % mod
            t = (t + (q % mod) * (r + 1) % mod) % mod
            total = (total + int(t.sum() % mod)) % mod
    return total


def solve():
    return S(10**16, 10**9 + 7)


if __name__ == "__main__":
    print(solve())
