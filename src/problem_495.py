# Problem 495: https://projecteuler.net/problem=495

from collections import Counter

import numpy as np
from sympy import primerange


N = 10_000
K = 30
MOD = 1_000_000_007


def factorial_exponents(n):
    exponents = []
    for p in primerange(2, n + 1):
        q = n
        exponent = 0
        while q:
            q //= p
            exponent += q
        exponents.append(exponent)
    return exponents


def count_factorizations(exponents, k):
    frequencies = Counter(exponents)
    limit = max(frequencies)
    inverses = tuple(pow(value, -1, MOD) for value in range(1, k + 1))
    initial = np.zeros(limit + 1, dtype=np.int64)
    initial[0] = 1
    total = 0

    def visit(remaining, smallest, coefficients, weight, previous, multiplicity):
        nonlocal total
        if remaining == 0:
            ways = 1
            for exponent, frequency in frequencies.items():
                ways *= pow(int(coefficients[exponent]), frequency, MOD)
                ways %= MOD
            total = (total + weight * ways) % MOD
            return

        for part in range(smallest, remaining + 1):
            updated = np.empty_like(coefficients)
            for residue in range(part):
                updated[residue::part] = np.cumsum(
                    coefficients[residue::part], dtype=np.int64
                ) % MOD

            count_equal = multiplicity + 1 if part == previous else 1
            factor = inverses[part - 1] * inverses[count_equal - 1] % MOD
            if part % 2 == 0:
                factor = -factor
            visit(
                remaining - part,
                part,
                updated,
                weight * factor % MOD,
                part,
                count_equal,
            )

    visit(k, 1, initial, 1, 0, 0)
    return total


def solve():
    return count_factorizations(factorial_exponents(N), K)


if __name__ == "__main__":
    print(solve())
