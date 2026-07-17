# Problem 404: https://projecteuler.net/problem=404

from math import isqrt

import numpy as np


N = 10**17
SCALES = (1, 4, 25, 100)


def count_triplets(limit):
    bounds = np.zeros(101, dtype=np.int64)
    for scale in SCALES:
        bounds[scale] = isqrt(isqrt(scale * limit // 10)) + 1

    total = 0
    for m in range(1, int(bounds[100]) + 1):
        lo = (m + isqrt(10 * m * m) + 3) // 3
        n = np.arange(lo, 2 * m, dtype=np.int64)
        by_five = (n - 2 * m) % 5 == 0
        both_odd = np.logical_and(m % 2 == 1, n % 2 == 1)
        scale = np.where(by_five, 25, 1) * np.where(both_odd, 4, 1)
        viable = m <= bounds[scale]
        n = n[viable]
        by_five = by_five[viable]
        both_odd = both_odd[viable]

        coprime = np.gcd(n, m) == 1
        n = n[coprime]
        by_five = by_five[coprime]
        both_odd = both_odd[coprime]
        if not n.size:
            continue

        u = n * n + m * n - m * m
        v = m * m + 4 * m * n - n * n
        u //= np.where(by_five, 5, 1)
        v //= np.where(by_five, 5, 1) * np.where(both_odd, 4, 1)
        valid = u <= limit // v
        total += int(np.sum(limit // (u[valid] * v[valid])))

    return total


def solve():
    return count_triplets(N)


if __name__ == "__main__":
    print(solve())
