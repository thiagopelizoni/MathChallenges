# Problem 614: https://projecteuler.net/problem=614

from math import isqrt

import numpy as np


def solve(n=10**7):
    mod = 10**9 + 7
    m = n // 4
    k = np.arange(1, isqrt(m) + 1, dtype=np.int64)
    squares = k * k
    signs = np.where(k % 2, 2, -2)
    b = np.zeros(m + 1, dtype=np.int64)
    b[0] = 1

    for i in range(1, m + 1):
        r = isqrt(i)
        b[i] = np.dot(signs[:r], b[i - squares[:r]]) % mod

    prefix = np.cumsum(b) % mod
    k = np.arange((isqrt(8 * n + 1) - 1) // 2 + 1, dtype=np.int64)
    triangular = k * (k + 1) // 2
    total = prefix[(n - triangular) // 4].sum()
    return int((total - 1) % mod)


if __name__ == "__main__":
    print(solve())
