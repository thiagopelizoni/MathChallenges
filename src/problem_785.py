# Problem 785: https://projecteuler.net/problem=785

from math import isqrt

import numpy as np


def solve(limit=10**9):
    total = 0
    for d in (1, 19):
        for n in range(1, isqrt(d * limit // 5) + 1):
            lo = (isqrt(19 * n * n) - 2 * n) // 5 + 1
            hi = min((3 * n - 1) // 2, (isqrt(n * n + 3 * d * limit) - 4 * n) // 3)
            if d == 19:
                lo += (3 * n * pow(2, -1, d) - lo) % d
            if lo > hi:
                continue

            m = np.arange(lo, hi + 1, d, dtype=np.int64)
            if d == 1:
                m = m[(2 * m - 3 * n) % 19 != 0]
            m = m[np.gcd(m, n) == 1]
            total += 8 * int((m * m + m * n + n * n).sum()) // d
    return total


if __name__ == "__main__":
    print(solve())
