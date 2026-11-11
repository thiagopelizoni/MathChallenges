# Problem 732: https://projecteuler.net/problem=732

from math import isqrt

import numpy as np


def solve(n=1000):
    r = []
    s = 1
    for _ in range(3 * n):
        r.append(s % 101 + 50)
        s = s * 5 % (10**9 + 7)

    trolls = sorted(zip(r[::3], r[1::3], r[2::3]), key=lambda t: t[0] + t[1])
    total = sum(h for h, l, q in trolls)
    limit = total - isqrt(total * total // 2) - 1
    size = limit + max(h + l for h, l, q in trolls) + 1
    dp = np.full(size, -sum(q for h, l, q in trolls) - 1, dtype=np.int64)
    dp[0] = 0

    for h, l, q in trolls:
        end = limit + l + 1
        np.maximum(dp[h:h + end], dp[:end] + q, out=dp[h:h + end])

    return int(dp.max())


if __name__ == "__main__":
    print(solve())
