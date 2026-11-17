# Problem 757: https://projecteuler.net/problem=757

from math import isqrt

import numpy as np


def solve(limit=10**14):
    bounds = []
    i = 1
    while (i * (i + 1)) ** 2 <= limit:
        p = i * (i + 1)
        bounds.append((isqrt(1 + 4 * (limit // p)) - 1) // 2)
        i += 1

    size = sum(j - i + 1 for i, j in enumerate(bounds, 1))
    if size == 0:
        return 0

    values = np.empty(size, dtype=np.int64)
    start = 0
    for i, j in enumerate(bounds, 1):
        k = np.arange(i, j + 1, dtype=np.int64)
        end = start + len(k)
        values[start:end] = i * (i + 1) * k * (k + 1)
        start = end

    values.sort()
    return 1 + int(np.count_nonzero(values[1:] != values[:-1]))


if __name__ == "__main__":
    print(solve())
