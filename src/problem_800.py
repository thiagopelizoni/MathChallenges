# Problem 800: https://projecteuler.net/problem=800
from bisect import bisect_right
from math import log2

from sympy import sieve


def solve():
    n = 800800
    limit = n * log2(n)
    primes = list(sieve.primerange(int(limit) + 1))
    total = 0
    for i, p in enumerate(primes):
        log_p = log2(p)
        start = i + 1
        end = bisect_right(primes, limit, lo=start, key=lambda q: q * log_p + p * log2(q))
        if end == start:
            break
        total += end - start
    return total


if __name__ == "__main__":
    print(solve())
