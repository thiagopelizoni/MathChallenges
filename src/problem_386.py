# Problem 386: https://projecteuler.net/problem=386

from math import isqrt

import numpy as np
from sympy import primerange


FACTOR_BLOCK = 1_000_000
SEARCH_BLOCK = 1_000_000


def prime_factor_counts(limit):
    counts = np.zeros(limit + 1, dtype=np.uint8)
    primes = list(primerange(2, isqrt(limit) + 1))

    for start in range(1, limit + 1, FACTOR_BLOCK):
        stop = min(start + FACTOR_BLOCK, limit + 1)
        remaining = np.arange(start, stop, dtype=np.uint32)
        degrees = np.zeros(stop - start, dtype=np.uint8)

        for p in primes:
            if p * p >= stop:
                break
            first = (-start) % p
            values = remaining[first::p]
            if values.size == 0:
                continue

            values //= p
            exponent = np.ones(values.size, dtype=np.uint8)
            while True:
                divisible = values % p == 0
                if not divisible.any():
                    break
                values[divisible] //= p
                exponent[divisible] += 1
            degrees[first::p] += exponent

        degrees[remaining > 1] += 1
        counts[start:stop] = degrees

    return counts


def count_products(left, right, limit):
    total = 0
    for start in range(0, left.size, SEARCH_BLOCK):
        values = left[start : start + SEARCH_BLOCK]
        bounds = limit // values
        total += int(np.searchsorted(right, bounds, side="right").sum())
    return total


def solve(limit=10**8):
    degrees = prime_factor_counts(limit)
    maximum = int(degrees.max())
    current = (np.flatnonzero(degrees[1:] == 0) + 1).astype(np.uint32)
    total = 0

    for degree in range(maximum + 1):
        total += count_products(current, current, limit)
        if degree == maximum:
            break

        following = (
            np.flatnonzero(degrees[1:] == degree + 1) + 1
        ).astype(np.uint32)
        total += count_products(current, following, limit)
        current = following

    return total


if __name__ == "__main__":
    print(solve())
