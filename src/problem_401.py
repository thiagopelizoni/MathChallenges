# Problem 401: https://projecteuler.net/problem=401

from math import isqrt

import numpy as np


N = 10**15
MOD = 10**9
BLOCK = 1_000_000


def square_sum_mod(n):
    a = n.copy()
    b = n + 1
    c = 2 * n + 1

    even = a % 2 == 0
    a[even] //= 2
    b[np.logical_not(even)] //= 2

    divisible = a % 3 == 0
    a[divisible] //= 3
    remaining = np.logical_not(divisible)
    divisible = np.logical_and(remaining, b % 3 == 0)
    b[divisible] //= 3
    c[np.logical_and(remaining, np.logical_not(divisible))] //= 3

    return (a % MOD) * (b % MOD) % MOD * (c % MOD) % MOD


def summatory_sigma_2(n):
    limit = isqrt(n)
    square_sum = limit * (limit + 1) * (2 * limit + 1) // 6 % MOD
    total = 0

    for start in range(1, limit + 1, BLOCK):
        d = np.arange(start, min(start + BLOCK, limit + 1), dtype=np.int64)
        q = n // d
        direct = d * d % MOD * (q % MOD) % MOD
        grouped = (square_sum_mod(q) - square_sum) % MOD
        total = (total + int(np.sum((direct + grouped) % MOD))) % MOD

    return total


def solve():
    return summatory_sigma_2(N)


if __name__ == "__main__":
    print(solve())
