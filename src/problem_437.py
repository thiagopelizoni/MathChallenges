# Problem 437: https://projecteuler.net/problem=437

from math import isqrt

import numpy as np
from sympy import sieve
from sympy.ntheory.residue_ntheory import _sqrt_mod_prime_power


LIMIT = 100_000_000


def smallest_odd_prime_factors(limit):
    factors = np.zeros(limit // 2 + 1, dtype=np.int32)
    for prime in sieve.primerange(3, isqrt(limit) + 1):
        p = int(prime)
        multiples = factors[p * p // 2 :: p]
        multiples[multiples == 0] = p
    return factors


def solve():
    factors = smallest_odd_prime_factors((LIMIT - 1) // 2)
    total = 5

    for prime in sieve.primerange(7, LIMIT):
        p = int(prime)
        if p % 5 not in (1, 4):
            continue

        square_root = _sqrt_mod_prime_power(5, p, 1)[0]
        half_order = (p - 1) // 2
        inverse_two = (p + 1) // 2
        root = (1 + square_root) * inverse_two % p

        if pow(root, half_order, p) == 1:
            if p % 4 == 1:
                continue
            root = (1 - square_root) * inverse_two % p

        remainder = half_order
        while remainder % 2 == 0:
            remainder //= 2

        while remainder > 1:
            divisor = int(factors[remainder // 2]) or remainder
            if pow(root, (p - 1) // divisor, p) == 1:
                break
            while remainder % divisor == 0:
                remainder //= divisor
        else:
            total += p

    return total


if __name__ == "__main__":
    print(solve())
