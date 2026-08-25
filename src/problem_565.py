# Problem 565: https://projecteuler.net/problem=565
from math import isqrt

import numpy as np
from sympy import primerange


def triangle(n):
    return n * (n + 1) // 2


def solve():
    n = 10**11
    q = 2017
    root = isqrt(n)
    small_primes = list(primerange(2, root + 1))

    changes = []
    for p in small_primes:
        options = []
        power = 1
        sigma = 1
        good_before = True
        while power <= n // p:
            power *= p
            sigma = (sigma * p + 1) % q
            good = sigma != 0
            if good != good_before:
                options.append((power, int(good) - int(good_before)))
            good_before = good
        if options:
            changes.append((p, options))

    coefficients = {1: 1}
    for _, options in changes:
        previous = list(coefficients.items())
        for d, coefficient in previous:
            for power, delta in options:
                if d <= n // power:
                    value = d * power
                    coefficients[value] = coefficients.get(value, 0) + coefficient * delta

    allowed_sum = 0
    for d, coefficient in coefficients.items():
        allowed_sum += coefficient * d * triangle(n // d)
    small_bad_sum = triangle(n) - allowed_sum

    allowed = np.ones(root + 1, dtype=np.bool_)
    for p, _ in changes:
        power = 1
        sigma = 1
        while power <= root // p:
            power *= p
            sigma = (sigma * p + 1) % q
            if sigma == 0:
                next_power = power * p
                multiples = np.arange(power, root + 1, power, dtype=np.int64)
                multiples = multiples[multiples % next_power != 0]
                allowed[multiples] = False

    last_k = (n + 1) // q
    candidates = np.ones(last_k + 1, dtype=np.bool_)
    candidates[0] = False
    for p in small_primes:
        if p != q:
            candidates[pow(q, -1, p) :: p] = False

    large_primes = q * np.flatnonzero(candidates) - 1
    large_primes = large_primes[large_primes > root]
    prime_sums = np.empty(len(large_primes) + 1, dtype=np.int64)
    prime_sums[0] = 0
    np.cumsum(large_primes, out=prime_sums[1:])

    cofactors = np.arange(1, root + 1, dtype=np.int64)
    positions = np.searchsorted(large_primes, n // cofactors, side="right")
    large_bad_sum = 0
    for a in np.flatnonzero(allowed[1:]) + 1:
        large_bad_sum += int(a) * int(prime_sums[positions[a - 1]])

    return small_bad_sum + large_bad_sum


if __name__ == "__main__":
    print(solve())
