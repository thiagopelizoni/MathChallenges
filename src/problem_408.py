# Problem 408: https://projecteuler.net/problem=408

from array import array
from math import gcd, isqrt

import numpy as np


N = 10_000_000
MOD = 1_000_000_007


def factorial_tables(n):
    fact = array("I", [1]) * (n + 1)
    value = 1
    for k in range(1, n + 1):
        value = value * k % MOD
        fact[k] = value

    inv = array("I", [1]) * (n + 1)
    value = pow(fact[n], -1, MOD)
    inv[n] = value
    for k in range(n, 0, -1):
        value = value * k % MOD
        inv[k - 1] = value

    return np.frombuffer(fact, dtype=np.uint32), np.frombuffer(inv, dtype=np.uint32)


def binomial_mod(n, k, fact, inv):
    result = np.multiply(fact[n], inv[k], dtype=np.uint64) % MOD
    return np.multiply(result, inv[n - k], dtype=np.uint64) % MOD


def inadmissible_points(n):
    limit = isqrt(n)
    points = []

    for u in range(2, isqrt(2 * limit) + 2):
        for v in range(1, u):
            if (u - v) % 2 == 0 or gcd(u, v) != 1:
                continue

            a = u * u - v * v
            b = 2 * u * v
            for k in range(1, limit // max(a, b) + 1):
                x = (k * a) ** 2
                y = (k * b) ** 2
                points.extend(((x, y), (y, x)))

    return sorted(points, key=lambda p: p[0] + p[1])


def admissible_paths(n):
    fact, inv = factorial_tables(2 * n)
    points = inadmissible_points(n)
    xy = np.array(points, dtype=np.int64)
    ways = np.zeros(len(points), dtype=np.int64)

    for i, (x, y) in enumerate(points):
        direct = int(binomial_mod(x + y, x, fact, inv))
        if i:
            dx = x - xy[:i, 0]
            dy = y - xy[:i, 1]
            valid = np.logical_and(dx >= 0, dy >= 0)
            paths = binomial_mod(
                dx[valid] + dy[valid], dx[valid], fact, inv
            ).astype(np.int64)
            direct -= int(
                np.sum(ways[:i][valid] * paths % MOD, dtype=np.int64)
            )
        ways[i] = direct % MOD

    answer = int(binomial_mod(2 * n, n, fact, inv))
    if points:
        dx = n - xy[:, 0]
        dy = n - xy[:, 1]
        paths = binomial_mod(dx + dy, dx, fact, inv).astype(np.int64)
        answer -= int(np.sum(ways * paths % MOD, dtype=np.int64))
    return answer % MOD


def solve():
    return admissible_paths(N)


if __name__ == "__main__":
    print(solve())
