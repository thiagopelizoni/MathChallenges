# Problem 639: https://projecteuler.net/problem=639

from math import comb, isqrt

import numpy as np
from sympy import primerange


def solve(limit=10**12, count=50):
    mod = 1_000_000_007
    primes = list(primerange(2, isqrt(limit) + 1))
    bases = np.array(primes, dtype=np.int64)
    powers = np.ones(len(primes), dtype=np.int64)
    factors = np.empty((len(primes), count), dtype=np.int64)
    for k in range(count):
        powers = powers * bases % mod
        factors[:, k] = powers * (1 - powers) % mod

    ones = np.ones(count, dtype=np.int64)
    weights = {limit: ones.copy()}

    def visit(n, start, coefficient):
        for i in range(start, len(primes)):
            p = primes[i]
            q = n // (p * p)
            if q == 0:
                break
            next_coefficient = coefficient * factors[i] % mod
            while q:
                if q in weights:
                    weights[q] += next_coefficient
                else:
                    weights[q] = next_coefficient.copy()
                visit(q, i + 1, next_coefficient)
                q //= p

    visit(limit, 0, ones)
    values = np.array(list(weights), dtype=np.int64) % mod
    coefficients = np.array(list(weights.values()), dtype=np.int64) % mod
    sums = [values]
    bases = (values + 1) % mod
    powers = bases.copy()
    total = 0
    for k in range(1, count + 1):
        powers = powers * bases % mod
        s = (powers - 1) % mod
        for j in range(k):
            s = (s - (comb(k + 1, j) % mod) * sums[j]) % mod
        s = s * pow(k + 1, -1, mod) % mod
        sums.append(s)
        total += int(np.sum(coefficients[:, k - 1] * s % mod))
    return total % mod


if __name__ == "__main__":
    print(solve())
