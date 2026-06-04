# Problem 287: https://projecteuler.net/problem=287

import numpy as np


N = 24


def pair_count(limit, d):
    sq = d * d
    return int(np.searchsorted(sq, limit - sq, side="right").sum())


def solve():
    c = 1 << (N - 1)
    r2 = c * c
    internal = 1

    for k in range(1, N):
        s = 1 << k
        h = c // s
        a = np.arange(h, dtype=np.int64)

        dmin = np.empty(2 * h, dtype=np.int64)
        dmin[0::2] = a * s
        dmin[1::2] = a * s + 1

        a += 1
        dmax = np.empty(2 * h, dtype=np.int64)
        dmax[0::2] = a * s - 1
        dmax[1::2] = a * s

        internal += pair_count(r2, dmin) - pair_count(r2, dmax)

    return 7 * internal + 2


if __name__ == "__main__":
    print(solve())
