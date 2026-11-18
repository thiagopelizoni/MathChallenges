# Problem 763: https://projecteuler.net/problem=763
from math import isqrt

import numpy as np


def solve(n=10_000):
    if n == 0:
        return 1

    mod = 10**9
    width = isqrt(n)
    edges = np.arange(width + 1)
    straight = np.arange(1, width)
    bent, run = np.tril_indices(width - 1, k=-1)
    bent += 1
    run += 1

    ways = np.zeros((width + 1, width + 1, width + 1), dtype=np.int64)
    ways[0, 0, 0] = 1
    for remaining in range(1, n):
        following = ways[(remaining - edges - 1) % len(ways), edges]
        current = ways[remaining % len(ways)]
        current[0, 0] = 3 * (following[0, 0] + following[1, 1]) % mod

        m = straight
        current[m, m] = (
            following[m - 1, m - 1]
            + 2 * (following[m, m] + following[m, 1])
            + following[m + 1, m + 1] + 2 * following[m + 1, 1]
        ) % mod

        m = bent
        current[m, run] = (
            following[m - 1, run]
            + following[m, run] + following[m, run + 1] + following[m, 1]
            + following[m + 1, run + 1] + following[m + 1, 1]
        ) % mod

    return int(ways[(n - 1) % len(ways), 0, 0])


if __name__ == "__main__":
    print(solve())
