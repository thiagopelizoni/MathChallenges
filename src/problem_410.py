# Problem 410: https://projecteuler.net/problem=410

from math import isqrt

import numpy as np
from sympy import primerange


R = 10**8
X = 10**9
BLOCK = 1_000_000


def circle_tangencies(r, x):
    limit = min(r, x)
    primes = tuple(primerange(3, isqrt(limit) + 1))
    odd = 0
    even = 0

    for start in range(1, limit + 1, 2 * BLOCK):
        stop = min(start + 2 * BLOCK, limit + 1)
        numbers = np.arange(start, stop, 2, dtype=np.int64)
        residual = numbers.copy()
        weight = np.ones(len(numbers), dtype=np.int64)

        for p in primes:
            if p * p >= stop:
                break
            first = ((start + p - 1) // p) * p
            if first % 2 == 0:
                first += p
            if first >= stop:
                continue

            offset = (first - start) // 2
            target = residual[offset::p]
            weight[offset::p] *= 2
            target //= p
            while True:
                divisible = target % p == 0
                if not np.any(divisible):
                    break
                target[divisible] //= p

        weight[residual > 1] *= 2
        a = r // numbers
        b = x // numbers
        odd += int(np.sum(weight * a * b, dtype=np.int64))

        power = 2
        while power <= limit:
            valid = numbers <= limit // power
            if not np.any(valid):
                break
            q = numbers[valid] * power
            a = r // q
            b = x // q
            pairs = (a // 2) * (b // 2) + ((a + 1) // 2) * ((b + 1) // 2)
            even += int(np.sum(weight[valid] * pairs, dtype=np.int64))
            power *= 2

    odd = (odd - r * x) // 2
    return 2 * r * x + 4 * (odd + even)


def solve():
    return 2 * circle_tangencies(R, X)


if __name__ == "__main__":
    print(solve())
