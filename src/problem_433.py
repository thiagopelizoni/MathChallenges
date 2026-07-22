# Problem 433: https://projecteuler.net/problem=433

from math import isqrt

import numpy as np
from sympy import sieve


def floor_total(n, m, a, b, weights):
    total = 0
    sums = np.zeros(len(n), dtype=np.int64)
    while len(n):
        q = a // m
        sums += n * (n - 1) * q // 2
        a %= m
        q = b // m
        sums += n * q
        b %= m
        top = a * n + b
        keep = top >= m
        done = np.logical_not(keep)
        total += int((sums[done] * weights[done]).sum())
        if not np.any(keep):
            break
        sums = sums[keep]
        weights = weights[keep]
        n = top[keep] // m[keep]
        b = top[keep] % m[keep]
        a, m = m[keep], a[keep]
    return total


def lattice_count(v):
    root = isqrt(v)
    total = 0
    for x in range(2, root + 1):
        y = np.arange(1, x, dtype=np.int64)
        t = v // (x + y)
        delta = v - t * x
        h1 = delta // x
        valid = t <= root
        h2 = np.where(valid, root - t, 0)
        h = np.concatenate((h1, h2))
        m = np.tile(y, 2)
        weights = np.concatenate(
            (np.full(len(y), 2, dtype=np.int64), np.full(len(y), -1, dtype=np.int64))
        )
        floors = floor_total(
            h,
            m,
            np.full(len(h), x, dtype=np.int64),
            np.concatenate((delta - x * h1, delta - x * h2)),
            weights,
        )
        base = np.where(valid, t * (t - 1) // 2, root * (root - 1) // 2)
        total += int((t * (t - 1)).sum()) - int(base.sum()) + floors
    return total


def total_steps(n):
    mu = np.fromiter(sieve.mobiusrange(1, n + 1), dtype=np.int8, count=n)
    prefix = np.empty(n + 1, dtype=np.int64)
    prefix[0] = 0
    np.cumsum(mu, out=prefix[1:])

    correction = 0
    left = 1
    while left <= n:
        q = n // left
        right = n // q
        weight = int(prefix[right] - prefix[left - 1])
        if weight and q >= 5:
            correction += weight * lattice_count(q)
        left = right + 1

    lower = n * (n - 1) // 2 + (n - 1) ** 2 // 4 + 2 * correction
    return 2 * lower + n * (n + 1) // 2


def solve():
    return total_steps(5_000_000)


if __name__ == "__main__":
    print(solve())
