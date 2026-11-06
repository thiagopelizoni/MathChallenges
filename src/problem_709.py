# Problem 709: https://projecteuler.net/problem=709

import numpy as np


def solve():
    n = 24680
    mod = 1020202009
    row = np.array([1], dtype=np.int64)
    for m in range(2, n + 1):
        prev = row
        row = np.empty(m, dtype=np.int64)
        row[0] = 0
        row[1:] = np.cumsum(prev[::-1]) % mod
    return int(row.sum() % mod)


if __name__ == "__main__":
    print(solve())
