# Problem 445: https://projecteuler.net/problem=445

from array import array
from math import isqrt

import numpy as np
from sympy import sieve


N = 10_000_000
MOD = 1_000_000_007


def solve():
    spf_array = np.zeros(N + 1, dtype=np.uint32)
    for p in sieve.primerange(2, isqrt(N) + 1):
        multiples = spf_array[p * p :: p]
        multiples[multiples == 0] = p
    spf = memoryview(spf_array)

    exponents = bytearray(N + 1)
    offsets = array("I", [0]) * (N + 1)
    terms = array("I")
    inverses = array("I")
    for prime in sieve.primerange(2, N + 1):
        p = int(prime)
        offsets[p] = len(terms)
        power = 1
        limit = N
        while limit >= p:
            limit //= p
            power *= p
            term = power + 1
            terms.append(term)
            inverses.append(pow(term, -1, MOD))

    product = 1
    total = 0
    half = N // 2
    for k in range(1, half + 1):
        value = N - k + 1
        while value > 1:
            p = spf[value]
            if not p:
                p = value
            count = 0
            while value % p == 0:
                value //= p
                count += 1

            old = exponents[p]
            offset = offsets[p]
            if old:
                product = product * inverses[offset + old - 1] % MOD
            new = old + count
            exponents[p] = new
            product = product * terms[offset + new - 1] % MOD

        value = k
        while value > 1:
            p = spf[value]
            if not p:
                p = value
            count = 0
            while value % p == 0:
                value //= p
                count += 1

            old = exponents[p]
            offset = offsets[p]
            product = product * inverses[offset + old - 1] % MOD
            new = old - count
            exponents[p] = new
            if new:
                product = product * terms[offset + new - 1] % MOD

        total += product if N % 2 == 0 and k == half else 2 * product
        if total >= 10**30:
            total %= MOD

    binomial_sum = pow(2, N, MOD) - 2
    return (total - binomial_sum) % MOD


if __name__ == "__main__":
    print(solve())
