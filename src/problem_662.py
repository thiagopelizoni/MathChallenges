# Problem 662: https://projecteuler.net/problem=662

from math import isqrt

import numpy as np


def solve(width=10_000, height=10_000):
    mod = 1_000_000_007
    moves = []
    f, g = 1, 2
    while f * f <= width * width + height * height:
        for x in range(min(width, f) + 1):
            y = isqrt(f * f - x * x)
            if y <= height and x * x + y * y == f * f:
                moves.append((x, y))
        f, g = g, f + g

    diagonals = [np.array([1], dtype=np.int32)]
    for s in range(1, width + height + 1):
        low = max(0, s - height)
        high = min(width, s)
        counts = np.zeros(high - low + 1, dtype=np.int64)

        for x, y in moves:
            t = s - x - y
            if t < 0:
                continue
            previous = diagonals[t]
            start = max(0, t - height)
            left = max(low, start + x)
            right = min(high, start + len(previous) - 1 + x)
            if left <= right:
                counts[left - low:right - low + 1] += previous[left - x - start:right - x - start + 1]

        diagonals.append((counts % mod).astype(np.int32))

    return int(diagonals[-1][0])


if __name__ == "__main__":
    print(solve())
