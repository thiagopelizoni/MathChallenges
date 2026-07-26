# Problem 451: https://projecteuler.net/problem=451

from math import isqrt

import numpy as np
from sympy import sieve


LIMIT = 20_000_000


def smallest_prime_factors(limit):
    spf = np.zeros(limit + 1, dtype=np.uint32)
    for p in sieve.primerange(2, isqrt(limit) + 1):
        multiples = spf[p * p :: p]
        multiples[multiples == 0] = p
    return spf


def largest_self_inverse(n, spf):
    roots = [n - 1]
    best = 1
    remaining = n

    while remaining > 1:
        p = int(spf[remaining]) or remaining
        prime_power = 1
        while remaining % p == 0:
            remaining //= p
            prime_power *= p

        if prime_power == 2:
            continue

        cofactor = n // prime_power
        projector = (
            cofactor
            * pow(cofactor % prime_power, -1, prime_power)
            % n
        )
        offsets = [2 * projector % n]
        if prime_power % 2 == 0 and prime_power >= 8:
            half = prime_power // 2
            offsets.extend(
                (half * projector % n, (half + 2) * projector % n)
            )

        count = len(roots)
        for i in range(count):
            root = roots[i]
            for offset in offsets:
                candidate = (root + offset) % n
                roots.append(candidate)
                if best < candidate < n - 1:
                    best = candidate

    return best


def solve():
    spf = smallest_prime_factors(LIMIT)
    return sum(
        largest_self_inverse(n, spf)
        for n in range(3, LIMIT + 1)
    )


if __name__ == "__main__":
    print(solve())
