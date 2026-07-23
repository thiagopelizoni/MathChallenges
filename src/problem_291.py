# Problem 291: https://projecteuler.net/problem=291

from math import isqrt

import numpy as np
from sympy import sieve
from sympy.ntheory.residue_ntheory import _sqrt_mod_prime_power


LIMIT = 5_000_000_000_000_000


def value(n):
    return 2 * n * n + 2 * n + 1


def solve():
    max_n = (isqrt(2 * LIMIT - 2) - 1) // 2
    composite = np.zeros(max_n + 1, dtype=np.bool_)

    for prime in sieve.primerange(5, isqrt(value(max_n)) + 1):
        p = int(prime)
        if p % 4 != 1:
            continue

        r = _sqrt_mod_prime_power(p - 1, p, 1)[0]
        inverse_two = (p + 1) // 2
        roots = (
            (r - 1) * inverse_two % p,
            (-r - 1) * inverse_two % p,
        )
        for root in roots:
            first = root or p
            if value(first) == p:
                first += p
            if first <= max_n:
                composite[first::p] = True

    return int(np.count_nonzero(np.logical_not(composite[1:])))


if __name__ == "__main__":
    print(solve())
