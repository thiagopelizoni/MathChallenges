# Problem 545: https://projecteuler.net/problem=545

from math import gcd, lcm

import numpy as np
from sympy import divisors, factorint, isprime


PRIMES = set(factorint(20_010))
BASE = lcm(*(p - 1 for p in PRIMES))
FACTORS = [int(d) for d in divisors(BASE)]


def find(index):
    bad = np.zeros(4_000_000, dtype=bool)
    found = 0

    for n in range(1, len(bad)):
        if bad[n]:
            continue

        extra = False
        for g in FACTORS:
            if gcd(n, BASE // g) > 1:
                continue
            p = g * n + 1
            if p not in PRIMES and isprime(p):
                extra = True
                break

        if extra:
            bad[n::n] = True
            continue

        found += 1
        if found == index:
            return BASE * n


def solve():
    return find(100_000)


if __name__ == "__main__":
    print(solve())
