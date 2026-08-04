# Problem 501: https://projecteuler.net/problem=501

from functools import cache, lru_cache
from math import isqrt

import numpy as np
from sympy import integer_nthroot, primerange


LIMIT = 10**12
SIEVE_LIMIT = 20_000_000
PRIMES = np.fromiter(primerange(2, SIEVE_LIMIT + 1), dtype=np.int64)
PRIME_COUNTS = np.zeros(SIEVE_LIMIT + 1, dtype=np.int32)
PRIME_COUNTS[PRIMES] = 1
np.cumsum(PRIME_COUNTS, out=PRIME_COUNTS)


@lru_cache(maxsize=5_000_000)
def phi(x, a):
    if a == 0:
        return x
    if a == 1:
        return x - x // 2
    if a == 2:
        return x - x // 2 - x // 3 + x // 6
    if x <= SIEVE_LIMIT and int(PRIMES[a - 1]) ** 2 > x:
        return int(PRIME_COUNTS[x]) - a + 1
    return phi(x, a - 1) - phi(x // int(PRIMES[a - 1]), a - 1)


def prime_count(x):
    if x <= SIEVE_LIMIT:
        return int(PRIME_COUNTS[x])
    return lehmer_prime_count(x)


@cache
def lehmer_prime_count(x):
    a = prime_count(isqrt(isqrt(x)))
    b = prime_count(isqrt(x))
    c = prime_count(integer_nthroot(x, 3)[0])
    total = phi(x, a) + (b + a - 2) * (b - a + 1) // 2

    for i in range(a, b):
        w = x // int(PRIMES[i])
        total -= prime_count(w)
        if i < c:
            for j in range(i, prime_count(isqrt(w))):
                total -= prime_count(w // int(PRIMES[j])) - j
    return total


def count_eight_divisors(limit):
    total = prime_count(integer_nthroot(limit, 7)[0])

    for value in PRIMES:
        p = int(value)
        if 2 * p**3 > limit:
            break
        q_limit = limit // p**3
        total += prime_count(q_limit) - int(p <= q_limit)

    for i, value in enumerate(PRIMES):
        p = int(value)
        if p**3 > limit:
            break
        q_end = prime_count(isqrt(limit // p))
        for j in range(i + 1, q_end):
            q = int(PRIMES[j])
            total += prime_count(limit // (p * q)) - j - 1
    return total


def solve():
    return count_eight_divisors(LIMIT)


if __name__ == "__main__":
    print(solve())
