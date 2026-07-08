# Problem 373: https://projecteuler.net/problem=373

import numpy as np
from sympy import sieve


N = 10_000_000


def triangle_counts(n):
    a = np.ones(n + 1, dtype=np.int64)
    b = np.ones(n + 1, dtype=np.int64)
    c = np.ones(n + 1, dtype=np.int64)

    for p in sieve.primerange(5, n + 1):
        if p % 4 != 1:
            continue

        power = p
        e = 1
        prev_a = prev_b = prev_c = 1
        while power <= n:
            cur_a = 3 * e * e + 3 * e + 1
            cur_b = 2 * e + 1
            cur_c = 2 * (e // 2) + 1

            a[power::power] = a[power::power] // prev_a * cur_a
            b[power::power] = b[power::power] // prev_b * cur_b
            c[power::power] = c[power::power] // prev_c * cur_c

            prev_a, prev_b, prev_c = cur_a, cur_b, cur_c
            power *= p
            e += 1

    return (2 * a - 3 * b + 3 * c - 2) // 6


def s(n):
    counts = triangle_counts(n)
    radii = np.arange(n + 1, dtype=np.int64)
    return int(np.dot(radii, counts))


def solve():
    return s(N)


if __name__ == "__main__":
    print(solve())
