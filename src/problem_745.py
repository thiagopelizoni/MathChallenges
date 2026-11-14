# Problem 745: https://projecteuler.net/problem=745

from math import isqrt

import numpy as np


def solve(n=10**14):
    mod = 1_000_000_007
    m = isqrt(n)
    squares = np.arange(1, m + 1, dtype=np.int64)
    squares *= squares
    counts = n // squares

    for k in range(m // 2, 0, -1):
        counts[k - 1] -= counts[2 * k - 1 :: k].sum()

    counts *= squares
    counts %= mod
    return int(counts.sum()) % mod


if __name__ == "__main__":
    print(solve())
