# Problem 589: https://projecteuler.net/problem=589

from math import fsum

import numpy as np


def expected_time(m, n):
    lo = n + 5
    hi = m + 5
    width = m - n + 1
    size = hi - 1
    g0 = 2 * size
    g1 = g0 + 1

    a = np.eye(2 * size + 2)
    b = np.zeros(2 * size + 2)
    chance = 1 / width
    times = range(lo, hi + 1)

    for r in range(1, size + 1):
        tied = r - 1
        leading = size + tied
        b[tied] = fsum(min(t, r) for t in times) * chance
        b[leading] = b[tied]

        for t in times:
            if t < r:
                a[tied, size + r - t - 1] -= chance
            elif t > r:
                a[tied, size + t - r - 1] -= chance
                a[leading, t - r - 1] -= chance
            else:
                a[tied, g0] -= chance
                a[leading, g1] -= chance

    fresh = np.arange(lo, hi + 1)
    pair_min = np.minimum.outer(fresh, fresh).sum()
    a[g0, g0] = width * width - width
    a[g1, g1] = width * width - width
    b[g0] = pair_min
    b[g1] = pair_min

    for d in range(1, width):
        a[g0, size + d - 1] -= 2 * (width - d)
        a[g1, d - 1] -= width - d

    value = np.linalg.solve(a, b)
    first = np.arange(n, m + 1)
    total = np.minimum.outer(first, first).sum() + width * value[g0]

    for d in range(1, width):
        total += 2 * (width - d) * value[size + d - 1]

    return total / (width * width)


def solve():
    total = fsum(expected_time(m, n) for m in range(2, 100 + 1) for n in range(1, m))
    return f"{total:.2f}"


if __name__ == "__main__":
    print(solve())
