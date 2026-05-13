# Problem 201: https://projecteuler.net/problem=201
import numpy as np


def unique_sum(values, size):
    max_sum = sum(sorted(values)[-size:])
    dp = np.zeros((size + 1, max_sum + 1), dtype=np.uint8)
    dp[0, 0] = 1

    for i, x in enumerate(values, 1):
        for k in range(min(i, size), 0, -1):
            row = dp[k, x:]
            np.add(row, dp[k - 1, :-x], out=row)
            np.minimum(row, 2, out=row)

    return int(np.flatnonzero(dp[size] == 1).sum())


def solve():
    return unique_sum([n * n for n in range(1, 101)], 50)


if __name__ == "__main__":
    print(solve())
