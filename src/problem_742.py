# Problem 742: https://projecteuler.net/problem=742

from fractions import Fraction
from math import isqrt

import numpy as np


def solve(n=1000):
    k = n // 4 - 1
    if k == 0:
        return 1

    v = np.arange(1, k + 1)
    primitive = np.gcd.outer(v, v) == 1
    counts = primitive.cumsum(axis=0).cumsum(axis=1)
    pairs = []
    for a in range(1, k + 1):
        for b in range(1, k + 1):
            if primitive[a - 1, b - 1] and counts[a - 1, b - 1] <= k:
                pairs.append((a, b))

    selected = sorted(pairs, key=lambda p: (sum(p), p))[:k]
    selected.sort(key=lambda p: Fraction(p[1], p[0]))
    upper = 1
    x = 0
    for a, b in selected:
        upper += 2 * (a + b + a * b) + 4 * x * b
        x += a

    limit = (isqrt(2 * upper) - 1) // 2
    dp = np.full((k + 1, limit + 1), upper + 1, dtype=np.int64)
    dp[0, 0] = 1
    x = np.arange(limit + 1, dtype=np.int64)
    pairs.sort(key=lambda p: Fraction(p[1], p[0]))
    for a, b in pairs:
        cost = 4 * x[:limit + 1 - a] * b + 2 * (a + b + a * b)
        np.minimum(dp[1:, a:], dp[:-1, :limit + 1 - a] + cost, out=dp[1:, a:])

    return int(dp[k].min())


if __name__ == "__main__":
    print(solve())
