# Problem 738: https://projecteuler.net/problem=738

from functools import cache
from math import isqrt

import numpy as np
from sympy import integer_nthroot


def solve(n=10**10):
    k = n
    mod = 1_000_000_007

    @cache
    def pairs(m, lo, r):
        xs = np.arange(lo, isqrt(m) + 1, dtype=np.int64)
        total = int(np.sum(m // xs - xs + 1)) * (k - r - 1)
        for x in range(lo, int(integer_nthroot(m, 3)[0]) + 1):
            total += pairs(m // x, x, r + 1)
        return total

    return (n * k + pairs(n, 2, 0)) % mod


if __name__ == "__main__":
    print(solve())
