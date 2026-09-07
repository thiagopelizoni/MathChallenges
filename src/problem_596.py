# Problem 596: https://projecteuler.net/problem=596

from math import isqrt

import numpy as np


def sigma_sum(n, mod):
    m = isqrt(n)
    step = max(1, isqrt(m))
    total = -m * m * (m + 1) // 2
    for start in range(1, m + 1, step):
        d = np.arange(start, min(start + step, m + 1), dtype=np.int64)
        q = n // d
        total += int((d * q % mod).sum())
        q %= mod
        total += int((q * (q + 1) // 2 % mod).sum())
    return total % mod


def solve(r=10**8):
    mod = 1000000007
    n = r * r
    total = sigma_sum(n, mod) - 4 * sigma_sum(n // 4, mod)
    return (1 + 8 * total) % mod


if __name__ == "__main__":
    print(solve())
