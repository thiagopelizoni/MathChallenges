# Problem 636: https://projecteuler.net/problem=636

from collections import Counter
from math import factorial, prod

import numpy as np
from sympy import primerange
from sympy.ntheory import multiplicity_in_factorial
from sympy.utilities.iterables import multiset_partitions


def solve(n=10**6):
    mod = 1_000_000_007
    weights = (2, 2, 3, 3, 3, 4, 4, 4, 4)
    terms = Counter()
    for blocks in multiset_partitions(len(weights)):
        pattern = []
        coefficient = 1
        for block in blocks:
            pattern.append(sum(weights[i] for i in block))
            size = len(block)
            coefficient *= (-1) ** (size - 1) * factorial(size - 1)
        terms[tuple(sorted(pattern))] += coefficient

    exponents = Counter()
    for p in primerange(2, n + 1):
        exponents[int(multiplicity_in_factorial(p, n))] += 1

    total = 0
    for pattern, coefficient in terms.items():
        ways = np.ones(max(exponents) + 1, dtype=np.int64)
        for w in pattern:
            for r in range(w):
                ways[r::w] = np.cumsum(ways[r::w]) % mod
        count = 1
        for e, frequency in exponents.items():
            count = count * pow(int(ways[e]), frequency, mod) % mod
        total = (total + coefficient * count) % mod

    permutations = prod(factorial(k) for k in range(2, 5))
    return total * pow(permutations, -1, mod) % mod


if __name__ == "__main__":
    print(solve())
