# Problem 559: https://projecteuler.net/problem=559
from math import isqrt

from sympy import isprime
from sympy.discrete.convolutions import convolution_ntt
from sympy.ntheory.modular import crt1, crt2


LIMIT = 50_000
MOD = 1_000_000_123

NTT_LENGTH = 1
while NTT_LENGTH < 2 * LIMIT:
    NTT_LENGTH *= 2

CRT_BOUND = LIMIT * (MOD - 1) ** 2
NTT_PRIMES = []
prime_product = 1
multiple = MOD // NTT_LENGTH
while prime_product <= CRT_BOUND:
    candidate = multiple * NTT_LENGTH + 1
    if isprime(candidate):
        NTT_PRIMES.append(candidate)
        prime_product *= candidate
    multiple -= 1

NTT_PRIMES = tuple(NTT_PRIMES)
CRT_DATA = crt1(NTT_PRIMES)


def multiply(a, b, limit):
    residues = []
    for p in NTT_PRIMES:
        values = convolution_ntt(a, b, prime=p)
        residues.append(values[:limit])

    result = []
    for values in zip(*residues):
        value, _ = crt2(NTT_PRIMES, values, *CRT_DATA)
        result.append(value % MOD)
    return result


def reciprocal(values):
    result = [1]

    while len(result) < len(values):
        size = min(2 * len(result), len(values))
        product = multiply(values[:size], result, size)
        correction = [0] * size
        correction[0] = (2 - product[0]) % MOD
        for i in range(1, len(product)):
            correction[i] = -product[i] % MOD
        result = multiply(result, correction, size)

    return result


def direct_reciprocal(values):
    result = [0] * len(values)
    result[0] = 1

    for i in range(1, len(values)):
        value = 0
        for j in range(1, i + 1):
            value -= values[j] * result[i - j]
        result[i] = value % MOD

    return result


def solve():
    factorial = [1] * (LIMIT + 1)
    for i in range(1, LIMIT + 1):
        factorial[i] = factorial[i - 1] * i % MOD

    inv_factorial = [1] * (LIMIT + 1)
    inv_factorial[LIMIT] = pow(factorial[LIMIT], -1, MOD)
    for i in range(LIMIT, 0, -1):
        inv_factorial[i - 1] = inv_factorial[i] * i % MOD

    weights = []
    for value in inv_factorial:
        weights.append(pow(value, LIMIT, MOD))

    common = pow(factorial[LIMIT], LIMIT, MOD)
    total = 0
    direct_limit = isqrt(LIMIT)

    for k in range(1, LIMIT + 1):
        blocks, remainder = divmod(LIMIT, k)
        denominator = [1]
        for length in range(1, blocks + 1):
            value = weights[length * k]
            if length % 2:
                value = -value % MOD
            denominator.append(value)

        if blocks <= direct_limit:
            coefficients = direct_reciprocal(denominator)
        else:
            coefficients = reciprocal(denominator)

        if remainder == 0:
            count = coefficients[blocks]
        else:
            count = 0
            for complete in range(blocks + 1):
                length = blocks - complete
                term = coefficients[complete] * weights[length * k + remainder]
                if length % 2:
                    count -= term
                else:
                    count += term
            count %= MOD

        total = (total + common * count) % MOD

    return total


if __name__ == "__main__":
    print(solve())
