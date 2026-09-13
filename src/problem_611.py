# Problem 611: https://projecteuler.net/problem=611

from math import isqrt

import numpy as np
from sympy import sieve


def solve(n=10**12):
    lim = isqrt(n)
    small = np.arange(lim + 1, dtype=np.int64)
    i = small[1:]
    low1 = (small - 1) // 4
    low1[0] = 0
    low3 = (small + 1) // 4
    high1 = (n // i - 1) // 4
    high3 = (n // i + 1) // 4
    primes = list(sieve.primerange(3, lim + 1))

    for p in primes:
        base1, base3 = low1[p - 1], low3[p - 1]
        end = min(lim, n // (p * p))
        q = n // (p * i[:end])
        count = min(end, n // (p * (lim + 1)))
        values1 = low1[np.minimum(q, lim)]
        values3 = low3[np.minimum(q, lim)]
        values1[:count] = high1[p * i[:count] - 1]
        values3[:count] = high3[p * i[:count] - 1]
        if p % 4 == 1:
            high1[:end] -= values1 - base1
            high3[:end] -= values3 - base3
        else:
            high1[:end] -= values3 - base3
            high3[:end] -= values1 - base1

        if p * p <= lim:
            q = small[p * p:] // p
            values1, values3 = low1[q], low3[q]
            if p % 4 == 1:
                low1[p * p:] -= values1 - base1
                low3[p * p:] -= values3 - base3
            else:
                low1[p * p:] -= values3 - base3
                low3[p * p:] -= values1 - base1

    primes = [p for p in primes if p % 4 == 1]
    signs = np.ones(lim + 1, dtype=np.int8)
    for p in primes:
        power = p
        while power <= lim:
            signs[power::power] *= -1
            power *= p

    total = 0
    for factor in (1, 2):
        bound = isqrt(n // factor)
        squares = factor * small[1:bound + 1] ** 2
        q = n // squares
        counts = low1[np.minimum(q, lim)]
        large = q > lim
        counts[large] = high1[squares[large] - 1]
        total += int(counts.sum())
        total += int(np.count_nonzero(signs[1:bound + 1] == -1))

        for p in primes:
            bound = isqrt(n // (factor * p))
            if p > bound:
                break
            power = p
            while power <= bound:
                total -= bound // power - bound // (power * p)
                power *= p * p

    return total


if __name__ == "__main__":
    print(solve())
