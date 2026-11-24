# Problem 795: https://projecteuler.net/problem=795

from math import isqrt

import numpy as np
from sympy import sieve


def solve(limit=12_345_678):
    square_root = np.ones(limit + 1, dtype=int)
    for p in sieve.primerange(2, isqrt(limit) + 1):
        power = p * p
        while power <= limit:
            square_root[power::power] *= p
            power *= p * p

    total = -(((limit + 1) // 2) ** 2)
    for d, phi in enumerate(sieve.totientrange(1, limit + 1), 1):
        if d % 2 == 0:
            count = limit // d
            total += phi * int(square_root[d]) * count * (count + 1) // 2
    return total


if __name__ == "__main__":
    print(solve())
