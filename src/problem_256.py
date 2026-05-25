# Problem 256: https://projecteuler.net/problem=256
from math import isqrt

import numpy as np


LIMIT = 86_000_000
TARGET = 200


def add_interval(cnt, a, b0, b1, step):
    if b0 <= b1:
        cnt[a * b0 : a * b1 + 1 : a * step] += 1


def counts(limit):
    cnt = np.zeros(limit + 1, dtype=np.uint16)

    for a in range(1, isqrt(limit) + 1):
        bmax = limit // a
        if bmax < a:
            continue

        if a & 1:
            if a == 1:
                continue

            p = (a - 1) // 2
            for k in range(p - 1):
                b0 = max(a, 2 * (k * (p + 1) + 1))
                b1 = min(bmax, 2 * ((k + 1) * p - 1))
                add_interval(cnt, a, b0 + (b0 & 1), b1, 2)

        else:
            k = 1
            while True:
                b0 = k * (a + 1) + 2
                b1 = (k + 1) * (a - 1) - 2
                if b0 > b1 or b0 > bmax:
                    break

                add_interval(cnt, a, max(a, b0), min(bmax, b1), 1)
                k += 1

    return cnt


def solve():
    return int(np.flatnonzero(counts(LIMIT) == TARGET)[0])


if __name__ == "__main__":
    print(solve())
