# Problem 590: https://projecteuler.net/problem=590
from collections import Counter
from math import comb

import numpy as np
from sympy import primerange, totient
from sympy.ntheory.modular import crt


def solve():
    limit = 50000
    mod = 10**9
    even_mod = 2**9
    odd_mod = mod // even_mod
    period = int(totient(odd_mod))

    counts = Counter()
    for p in primerange(2, limit + 1):
        a = 0
        power = p
        while power <= limit:
            a += 1
            power *= p
        counts[a] += 1

    ones = counts.pop(1)
    terms = [(1, 1)]
    for a, count in counts.items():
        choices = []
        for k in range(count + 1):
            exponent = pow(a, k, period) * pow(a + 1, count - k, period) % period
            weight = comb(count, k)
            if k % 2:
                weight = -weight
            choices.append((exponent, weight))

        next_terms = []
        for exponent, weight in terms:
            for factor, coefficient in choices:
                next_terms.append((exponent * factor % period, weight * coefficient % odd_mod))
        terms = next_terms

    powers = np.fromiter((pow(2, exponent, odd_mod) for exponent, _ in terms), dtype=np.int64)
    weights = np.fromiter((weight for _, weight in terms), dtype=np.int64)

    total = 0
    choose = 1
    sign = -1 if ones % 2 else 1
    for j in range(ones + 1):
        inner = int(np.dot(weights, powers) % odd_mod)
        total = (total + sign * (choose % odd_mod) * inner) % odd_mod
        if j < ones:
            choose = choose * (ones - j) // (j + 1)
            sign = -sign
            powers = powers * powers % odd_mod

    return int(crt((even_mod, odd_mod), (0, total))[0])


if __name__ == "__main__":
    print(solve())
