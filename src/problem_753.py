# Problem 753: https://projecteuler.net/problem=753

from math import isqrt

from sympy import sieve


def solve():
    limit = 6_000_000
    trace = [0] * limit
    bound = 4 * (limit - 1)

    for m in range(1, isqrt(bound // 27) + 1):
        q = 27 * m * m
        start = 1 if m % 2 else 2
        for a in range(start, isqrt(bound - q) + 1, 2):
            if a % 3 == 0:
                continue
            p = (a * a + q) // 4
            trace[p] = a if a % 3 == 1 else -a

    total = 0
    for p in sieve.primerange(limit):
        if p % 3 == 1:
            total += (p - 1) * (p - 8 + trace[p])
        else:
            total += (p - 1) * (p - 2)
    return total


if __name__ == "__main__":
    print(solve())
