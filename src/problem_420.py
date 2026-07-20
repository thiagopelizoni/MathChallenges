# Problem 420: https://projecteuler.net/problem=420

from math import gcd, isqrt

import numpy as np


N = 10_000_000


def divisor_prefixes(limit):
    max_g = isqrt((2 * limit - 1) // 5)
    max_value = max_g * max_g // 4
    tau = np.zeros(max_value + 1, dtype=np.uint16)
    for d in range(1, max_value + 1):
        tau[d::d] += 1

    prefixes = [None] * (max_g + 1)
    for g in range(1, max_g + 1):
        values = np.zeros(g, dtype=np.int64)
        if g % 2 == 0:
            values[0] = tau[g * g // 4]
            z = np.arange(2, g, 2, dtype=np.int64)
        else:
            z = np.arange(1, g, 2, dtype=np.int64)
        values[z] = 2 * tau[(g * g - z * z) // 4]
        prefixes[g] = np.cumsum(values)
    return prefixes


def count_matrices(limit):
    prefixes = divisor_prefixes(limit)
    total = 0
    for g in range(1, len(prefixes)):
        bound = (2 * limit - 1) // (g * g)
        a = 1
        while a * a + (a + 1) ** 2 <= bound:
            b = a + 1
            while a * a + b * b <= bound:
                parity_ok = g % 2 == 0 or (a % 2 == 1 and b % 2 == 1)
                if parity_ok and gcd(a, b) == 1:
                    z = (g * a - 1) // b
                    total += int(prefixes[g][z])
                b += 1
            a += 1
    return total


def solve():
    return count_matrices(N)


if __name__ == "__main__":
    print(solve())
