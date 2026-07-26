# Problem 454: https://projecteuler.net/problem=454

from math import isqrt

from sympy import sieve


LIMIT = 10**12


def floor_sum_segment(x, low, high):
    total = 0
    i = low + 1
    while i <= high:
        quotient = x // i
        if quotient == 0:
            break
        last = min(high, x // quotient)
        total += quotient * (last - i + 1)
        i = last + 1
    return total


def count_solutions(limit):
    root = isqrt(limit)
    total = 0
    for d, mu in enumerate(sieve.mobiusrange(1, root + 1), 1):
        if mu == 0:
            continue
        square = d * d
        for k in range(2, root // d + 1):
            x = limit // (square * k)
            total += mu * floor_sum_segment(x, k, 2 * k - 1)
    return total


def solve():
    return count_solutions(LIMIT)


if __name__ == "__main__":
    print(solve())
