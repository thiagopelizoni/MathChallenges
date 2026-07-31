# Problem 476: https://projecteuler.net/problem=476

from math import fsum, pi

import numpy as np


def average_area(n):
    sums = []
    count = 0

    for a in range(1, n // 2 + 1):
        bases = np.arange(a, n - a + 1, dtype=np.float64)
        b = np.repeat(bases, a)
        c = b + np.tile(np.arange(a, dtype=np.float64), bases.size)
        s = (a + b + c) / 2
        sa = s - a
        sb = s - b
        sc = s - c
        radius_squared = sa * sb * sc / s
        sin_a = np.sqrt(sb * sc / (b * c))
        sin_b = np.sqrt(sa * sc / (a * c))
        ratio_a = (1 - sin_a) / (1 + sin_a)
        ratio_b = (1 - sin_b) / (1 + sin_b)
        third = np.maximum(ratio_b, ratio_a * ratio_a)
        covered = radius_squared * (
            1 + ratio_a * ratio_a + third * third
        )
        sums.append(float(np.sum(covered)))
        count += b.size

    return pi * fsum(sums) / count


def solve():
    return f"{average_area(1803):.5f}"


if __name__ == "__main__":
    print(solve())
