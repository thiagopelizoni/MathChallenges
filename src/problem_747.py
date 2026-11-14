# Problem 747: https://projecteuler.net/problem=747

from math import comb, isqrt

import numpy as np


def solve(m=10**8):
    mod = 1_000_000_007
    total = comb(m, 3) + 3 * (m - 1) * (m - 2)
    block = isqrt(m)
    extra = 0

    for x in range(1, (isqrt(m) - 1) // 2 + 1):
        c = 4 * m * x * (m - 1) * (x + 1)
        r = isqrt(c)
        end = m - 1 - x + 2 * m * x - r - (r * r < c)

        for start in range(x, end + 1, block):
            z = np.arange(start, min(start + block, end + 1), dtype=np.int64)
            a = 4 * x * (x + 1) * z * (z + 1)
            s = np.sqrt(a).astype(np.int64)
            s -= s * s > a
            s += (s + 1) * (s + 1) <= a
            ways = 2 * (m - x - z - 1 - 2 * x * z - s) + (s * s == a)
            extra += 2 * int(ways.sum())
            if start == x:
                extra -= int(ways[0])

    return (total + 3 * extra) % mod


if __name__ == "__main__":
    print(solve())
