# Problem 210: https://projecteuler.net/problem=210
from math import isqrt

import numpy as np


def circle_count(s):
    r2 = 2 * s * s
    m = isqrt(r2 - 1)
    total = 0
    chunk = 1_000_000

    for start in range(0, m + 1, chunk):
        stop = min(m + 1, start + chunk)
        x = np.arange(start, stop, dtype=np.int64)
        rem = r2 - x * x - 1
        y = np.sqrt(rem).astype(np.int64)

        while True:
            mask = (y + 1) * (y + 1) <= rem
            if not mask.any():
                break
            y[mask] += 1

        while True:
            mask = y * y > rem
            if not mask.any():
                break
            y[mask] -= 1

        if start == 0:
            total += int(2 * y[0])
            y = y[1:]
        total += int((4 * y + 2).sum())

    return total - 2 * (s - 1)


def solve():
    r = 1_000_000_000
    return 3 * r * r // 2 + circle_count(r // 8)


if __name__ == "__main__":
    print(solve())
