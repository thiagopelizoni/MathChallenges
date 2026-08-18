# Problem 549: https://projecteuler.net/problem=549

from math import isqrt

import numpy as np


LIMIT = 100_000_000


def valuation(n, p):
    total = 0
    while n:
        n //= p
        total += n
    return total


def solve():
    root = isqrt(LIMIT)
    prime = np.ones(LIMIT + 1, dtype=np.bool_)
    prime[:2] = False

    for p in range(2, root + 1):
        if prime[p]:
            prime[p * p::p] = False

    primes = np.flatnonzero(prime)
    del prime
    values = np.zeros(LIMIT + 1, dtype=np.uint32)
    small_end = np.searchsorted(primes, root, side="right")

    for p0 in primes[:small_end]:
        p = int(p0)
        power = p
        exponent = 1
        m = p

        while power <= LIMIT:
            while valuation(m, p) < exponent:
                m += p
            multiples = values[power::power]
            np.maximum(multiples, m, out=multiples)
            power *= p
            exponent += 1

    large = primes[small_end:]
    for k in range(1, root + 1):
        end = np.searchsorted(large, LIMIT // k, side="right")
        p = large[:end]
        values[p * k] = p

    return int(values[2:].sum(dtype=np.uint64))


if __name__ == "__main__":
    print(solve())
