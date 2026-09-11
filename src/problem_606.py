# Problem 606: https://projecteuler.net/problem=606

from math import isqrt

import numpy as np
from sympy import integer_nthroot, primerange


def cube_sum(values, mod):
    values = values % (2 * mod)
    triangular = values * (values + 1) // 2 % mod
    return (triangular * triangular - 1) % mod


def solve(n=10**36):
    mod = 10**9
    limit = int(integer_nthroot(n, 3)[0])
    root = isqrt(limit)
    indices = np.arange(1, root + 1, dtype=np.int64)
    quotients = limit // indices
    small = cube_sum(np.arange(root + 1, dtype=np.int64), mod)
    large = cube_sum(quotients, mod)
    primes = list(primerange(2, root + 1))

    for p in primes:
        weight = p**3 % mod
        previous = small[p - 1]
        count = min(root, limit // (p * p))
        split = min(count, limit // ((root + 1) * p))
        large[:split] -= weight * (large[indices[:split] * p - 1] - previous)
        large[:split] %= mod
        large[split:count] -= weight * (small[quotients[split:count] // p] - previous)
        large[split:count] %= mod
        if p * p <= root:
            small[p * p:] -= weight * (small[indices[p * p - 1:] // p] - previous)
            small[p * p:] %= mod

    total = 0
    for p in primes:
        total += p**3 * (int(large[p - 1]) - int(small[p]))
    return total % mod


if __name__ == "__main__":
    print(solve())
