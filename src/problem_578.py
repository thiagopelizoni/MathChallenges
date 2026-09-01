# Problem 578: https://projecteuler.net/problem=578
from bisect import bisect_right
from math import isqrt

import numpy as np
from sympy import primerange, sieve


def count_decreasing(limit):
    root = isqrt(limit)
    primes = list(primerange(2, root + 1))
    mu = np.fromiter(sieve.mobiusrange(1, root + 1), dtype=np.int8, count=root)
    squares = np.arange(1, root + 1, dtype=np.int64)
    squares *= squares
    cache_limit = bisect_right(primes, isqrt(root))
    memo = [dict() for _ in range(cache_limit + 1)]

    def squarefree(x):
        r = isqrt(x)
        return int(np.sum(mu[:r] * (x // squares[:r]), dtype=np.int64))

    def rough(x, excluded):
        if excluded == 0:
            return squarefree(x)

        p = primes[excluded - 1]
        if p > x:
            return 1
        if p * p > x:
            return 1 + bisect_right(primes, x) - excluded

        saved = memo[excluded].get(x)
        if saved is not None:
            return saved

        value = rough(x, excluded - 1) - rough(x // p, excluded)
        memo[excluded][x] = value
        return value

    total = squarefree(limit)

    def visit(start, remaining, max_exponent):
        nonlocal total
        stop = bisect_right(primes, isqrt(remaining))

        for i in range(start, stop):
            p = primes[i]
            power = p * p
            exponent = 2

            while exponent <= max_exponent and power <= remaining:
                rest = remaining // power
                total += rough(rest, i + 1)
                visit(i + 1, rest, exponent)
                power *= p
                exponent += 1

    visit(0, limit, limit)
    return total


def solve():
    return count_decreasing(10**13)


if __name__ == "__main__":
    print(solve())
