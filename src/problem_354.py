# Problem 354: https://projecteuler.net/problem=354

from bisect import bisect_right
from math import isqrt

import numpy as np
from sympy import integer_nthroot, sieve


MAX_L = 5 * 10**11
LIMIT = MAX_L * MAX_L // 3


def root4(n):
    return integer_nthroot(n, 4)[0]


def one_mod_three_primes():
    maxp = isqrt(LIMIT // (7**4 * 13**4))
    return [p for p in sieve.primerange(2, maxp + 1) if p % 3 == 1]


def allowed_prefix(ymax):
    ok = np.ones(ymax + 1, dtype=np.bool_)
    ok[0] = False

    for p in sieve.primerange(2, ymax + 1):
        if p == 3 or p % 3 == 1:
            ok[p::p] = False

    return np.cumsum(ok, dtype=np.int64)


def square_multiplier_count(prefix, n):
    total = 0

    while n:
        total += int(prefix[isqrt(n)])
        n //= 3

    return total


def products_24_2(primes):
    for p in primes:
        p24 = p**24
        if p24 * 7**2 > LIMIT:
            break

        for q in primes[: bisect_right(primes, isqrt(LIMIT // p24))]:
            if q != p:
                yield p24 * q**2


def products_14_4(primes):
    for p in primes:
        p14 = p**14
        if p14 * 7**4 > LIMIT:
            break

        for q in primes[: bisect_right(primes, root4(LIMIT // p14))]:
            if q != p:
                yield p14 * q**4


def products_4_4_2(primes):
    p4 = [p**4 for p in primes]

    for i, p in enumerate(primes):
        if p > 7 and p4[i] * 13**4 * 19**2 > LIMIT:
            break

        for j in range(i + 1, len(primes)):
            pq = p4[i] * p4[j]
            if pq * 7**2 > LIMIT:
                break

            for k in range(bisect_right(primes, isqrt(LIMIT // pq))):
                if k != i and k != j:
                    yield pq * primes[k] ** 2


def solve():
    primes = one_mod_three_primes()
    ymax = isqrt(LIMIT // (7**4 * 13**4 * 19**2))
    prefix = allowed_prefix(ymax)
    total = 0

    for gen in (products_24_2, products_14_4, products_4_4_2):
        for a in gen(primes):
            total += square_multiplier_count(prefix, LIMIT // a)

    return total


if __name__ == "__main__":
    print(solve())
