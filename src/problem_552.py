# Problem 552: https://projecteuler.net/problem=552

import numpy as np
from sympy import primerange


LIMIT = 300_000


def solve():
    primes = np.fromiter(primerange(2, LIMIT + 1), dtype=np.int64)
    residues = np.ones(len(primes), dtype=np.int64)
    products = np.full(len(primes), 2, dtype=np.int64)
    found = np.zeros(len(primes), dtype=np.bool_)

    for index in range(1, len(primes) - 1):
        p = int(primes[index])
        coefficient = (
            (index + 1 - int(residues[index]))
            * pow(int(products[index]), -1, p)
            % p
        )
        tail = slice(index + 1, None)
        residues[tail] = (
            residues[tail] + coefficient * products[tail]
        ) % primes[tail]
        products[tail] = products[tail] * p % primes[tail]
        np.logical_or(found[tail], residues[tail] == 0, out=found[tail])

    return int(primes[found].sum())


if __name__ == "__main__":
    print(solve())
