# Problem 378: https://projecteuler.net/problem=378

from math import isqrt

import numpy as np
from sympy import primerange


MOD = 10**18
DIVISOR_BLOCK = 1_000_000
COUNT_BLOCK = 100_000


def divisor_counts(limit):
    tau = np.empty(limit + 2, dtype=np.uint16)
    tau[0] = 0
    primes = list(primerange(2, isqrt(limit + 1) + 1))

    for start in range(1, limit + 2, DIVISOR_BLOCK):
        stop = min(start + DIVISOR_BLOCK, limit + 2)
        remaining = np.arange(start, stop, dtype=np.uint32)
        counts = np.ones(stop - start, dtype=np.uint16)

        for p in primes:
            if p * p >= stop:
                break
            first = (-start) % p
            values = remaining[first::p]
            values //= p
            exponent = np.ones(values.size, dtype=np.uint8)

            while True:
                divisible = values % p == 0
                if not divisible.any():
                    break
                values[divisible] //= p
                exponent[divisible] += 1

            counts[first::p] *= exponent + 1

        counts[remaining > 1] *= 2
        tau[start:stop] = counts

    return tau


def block_summary(values):
    unique, ranks = np.unique(values, return_inverse=True)
    rows = np.arange(values.size)
    grid = np.zeros((values.size, unique.size + 1), dtype=np.uint8)
    grid[rows, ranks + 1] = 1

    counts = np.cumsum(grid, axis=0, dtype=np.uint32)
    np.cumsum(counts, axis=1, out=counts)
    larger_left = rows + 1 - counts[rows, ranks + 1]
    smaller_right = counts[-1, ranks] - counts[rows, ranks]

    frequency = np.bincount(ranks, minlength=unique.size).astype(np.int64)
    pair_starts = np.bincount(ranks, weights=smaller_right).astype(np.int64)
    pair_ends = np.bincount(ranks, weights=larger_left).astype(np.int64)
    triples = int(
        np.dot(larger_left.astype(np.int64), smaller_right.astype(np.int64))
    )
    return unique, frequency, pair_starts, pair_ends, triples


def solve(limit=60_000_000):
    tau = divisor_counts(limit)
    value_limit = int(tau.max()) ** 2 + 1
    singles = np.zeros(value_limit, dtype=np.int64)
    pairs = np.zeros(value_limit, dtype=np.int64)
    total = 0

    for start in range(1, limit + 1, COUNT_BLOCK):
        stop = min(start + COUNT_BLOCK, limit + 1)
        n = np.arange(start, stop, dtype=np.intp)
        values = np.empty(n.size, dtype=np.uint32)
        even = n % 2 == 0
        odd = n % 2 == 1
        values[even] = tau[n[even] // 2].astype(np.uint32) * tau[n[even] + 1]
        values[odd] = tau[n[odd]].astype(np.uint32) * tau[(n[odd] + 1) // 2]

        unique, frequency, pair_starts, pair_ends, local = block_summary(values)
        larger_singles = singles.sum() - np.cumsum(singles)[unique]
        larger_pairs = pairs.sum() - np.cumsum(pairs)[unique]

        total += sum(int(a) * int(b) for a, b in zip(frequency, larger_pairs))
        total += sum(int(a) * int(b) for a, b in zip(pair_starts, larger_singles))
        total = (total + local) % MOD
        pairs[unique] += pair_ends + frequency * larger_singles
        singles[unique] += frequency

    return total


if __name__ == "__main__":
    print(solve())
