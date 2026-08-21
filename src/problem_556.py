# Problem 556: https://projecteuler.net/problem=556
from math import isqrt

import numpy as np
from sympy import integer_nthroot, primerange


def gaussian_mobius(limit):
    mu = np.ones(limit + 1, dtype=np.int16)
    mu[0] = 0

    for p in primerange(2, limit + 1):
        if p == 2:
            mu[p::p] *= -1
            mu[p * p::p * p] = 0
        elif p % 4 == 1:
            mu[p::p] *= -2
            pp = p * p
            if pp <= limit:
                mu[pp::pp] //= -2
                ppp = pp * p
                if ppp <= limit:
                    mu[ppp::ppp] = 0
        else:
            pp = p * p
            mu[p::p] = 0
            if pp <= limit:
                mu[pp::pp] = -mu[1:limit // pp + 1].copy()

    return mu


def proper_count(limit):
    total = 0
    for a in range(1, isqrt(limit) + 1):
        total += isqrt(limit - a * a) + 1
    return total


def solve(limit=10**14):
    root = isqrt(limit)
    mu = gaussian_mobius(root)
    cut = integer_nthroot(limit, 3)[0]
    small_limit = limit // ((cut + 1) ** 2)
    small = np.zeros(small_limit + 1, dtype=np.int64)

    for a in range(1, isqrt(small_limit) + 1):
        aa = a * a
        for b in range(isqrt(small_limit - aa) + 1):
            small[aa + b * b] += 1
    small = np.cumsum(small)

    total = 0
    for n in range(1, cut + 1):
        if mu[n]:
            total += int(mu[n]) * proper_count(limit // (n * n))
    for n in range(cut + 1, root + 1):
        if mu[n]:
            total += int(mu[n]) * int(small[limit // (n * n)])

    return total


if __name__ == "__main__":
    print(solve())
