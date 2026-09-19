# Problem 623: https://projecteuler.net/problem=623

import numpy as np


def solve(limit=2000):
    mod = 1_000_000_007
    inner = np.zeros(1, dtype=np.int64)
    for depth in range((limit - 1) // 5, -1, -1):
        row = np.zeros(limit - 5 * depth + 1, dtype=np.int64)
        row[1] = depth
        for size in range(4, len(row)):
            if size >= 6:
                row[size] = inner[size - 5]
            products = row[1 : size - 2] * row[size - 3 : 0 : -1]
            row[size] += (products % mod).sum()
            row[size] %= mod
        inner = row
    return int(inner.sum() % mod)


if __name__ == "__main__":
    print(solve())
