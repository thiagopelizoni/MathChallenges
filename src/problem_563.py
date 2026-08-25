# Problem 563: https://projecteuler.net/problem=563
from bisect import bisect_right
from math import isqrt

import numpy as np
from sympy import primerange


def smooth_numbers(primes, limit):
    values = []

    def visit(i, value):
        if i == len(primes):
            values.append(value)
            return
        p = primes[i]
        while value <= limit:
            visit(i + 1, value)
            value *= p

    visit(0, 1)
    return np.array(sorted(values), dtype=np.int64)


def find_minima(primes, limit, minima, targets):
    values = smooth_numbers(primes, isqrt(11 * limit // 10))
    root = isqrt(limit)
    ranges = []
    total = 0

    for i, value in enumerate(values):
        a = int(value)
        if a > root:
            break
        high = min(11 * a // 10, limit // a)
        j = bisect_right(values, high, i)
        ranges.append((i, j))
        total += j - i

    products = np.empty(total, dtype=np.int64)
    pos = 0
    for i, j in ranges:
        size = j - i
        products[pos:pos + size] = values[i] * values[i:j]
        pos += size

    products.sort()
    starts = np.flatnonzero(np.r_[True, products[1:] != products[:-1]])
    counts = np.diff(np.append(starts, len(products)))
    for area, count in zip(products[starts], counts):
        count = int(count)
        if count in targets and count not in minima:
            minima[count] = int(area)


def solve():
    primes = tuple(primerange(2, 26))
    targets = set(range(2, 101))
    minima = {}
    limit = 1

    while minima.keys() != targets:
        find_minima(primes, limit, minima, targets)
        limit *= 2

    return sum(minima.values())


if __name__ == "__main__":
    print(solve())
