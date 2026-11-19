# Problem 769: https://projecteuler.net/problem=769

from collections import defaultdict
from math import isqrt

from sympy import sieve


def count(limit):
    disc = 5**2 - 4 * 3
    root = 5 * pow(2, -1, disc) % disc
    weights = defaultdict(int)
    for d, mu in enumerate(sieve.mobiusrange(1, isqrt(limit // 2) + 1), 1):
        if mu and d % disc:
            weights[limit // (d * d)] += mu

    total = 0
    for bound, weight in weights.items():
        if not weight:
            continue
        points = 0
        for b in range(1, isqrt(bound // 2) + 1):
            bb = b * b
            low = isqrt(3 * bb)
            residue = root * b
            delta = disc * bb - 4 * bound
            high = (5 * b - 1 - isqrt(max(0, delta - 1))) // 2
            if high > low:
                excluded = (high - residue) // disc - (low - residue) // disc
                points += high - low - excluded

            high = (isqrt(disc * bb + 4 * bound) - 5 * b) // 2
            if high > low:
                excluded = (high + residue) // disc - (low + residue) // disc
                points += high - low - excluded
        total += weight * points
    return total


def solve():
    return count(10**14)


if __name__ == "__main__":
    print(solve())
