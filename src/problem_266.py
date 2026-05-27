# Problem 266: https://projecteuler.net/problem=266

from bisect import bisect_right
from math import prod, isqrt

from sympy import primerange


MOD = 10**16


def subset_products(values):
    ps = [1]
    for n in values:
        ps += [p * n for p in ps]
    return ps


def solve():
    primes = list(primerange(2, 190))
    target = isqrt(prod(primes))
    mid = len(primes) // 2
    left = subset_products(primes[:mid])
    right = sorted(subset_products(primes[mid:]))
    best = 0

    for a in left:
        if a > target:
            continue
        b = right[bisect_right(right, target // a) - 1]
        best = max(best, a * b)

    return best % MOD


if __name__ == "__main__":
    print(solve())
