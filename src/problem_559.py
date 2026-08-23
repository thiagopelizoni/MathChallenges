# Problem 559: https://projecteuler.net/problem=559
from sympy.discrete.convolutions import convolution_ntt
from sympy.ntheory.modular import crt1, crt2


LIMIT = 50_000
MOD = 1_000_000_123
DIRECT_LIMIT = 5_000
NTT_PRIMES = (998_244_353, 1_004_535_809, 469_762_049)
CRT_DATA = crt1(NTT_PRIMES)


def multiply(a, b, limit):
    residues = []
    for p in NTT_PRIMES:
        residues.append(convolution_ntt(a, b, prime=p)[:limit])

    result = []
    for values in zip(*residues):
        value, _ = crt2(NTT_PRIMES, values, *CRT_DATA)
        result.append(value % MOD)
    return result


def inverse_series(values, limit):
    inverse = [1]

    while len(inverse) < limit:
        size = min(2 * len(inverse), limit)
        product = multiply(values[:size], inverse, size)
        correction = [0] * size
        correction[0] = (2 - product[0]) % MOD
        for i in range(1, len(product)):
            correction[i] = -product[i] % MOD
        inverse = multiply(inverse, correction, size)

    return inverse


def direct_inverse(values):
    inverse = [0] * len(values)
    inverse[0] = 1

    for i in range(1, len(values)):
        value = 0
        for j in range(1, i + 1):
            value -= values[j] * inverse[i - j]
        inverse[i] = value % MOD

    return inverse


def solve():
    factorial = [1] * (LIMIT + 1)
    for i in range(1, LIMIT + 1):
        factorial[i] = factorial[i - 1] * i % MOD

    inv_factorial = [1] * (LIMIT + 1)
    inv_factorial[LIMIT] = pow(factorial[LIMIT], -1, MOD)
    for i in range(LIMIT, 0, -1):
        inv_factorial[i - 1] = inv_factorial[i] * i % MOD

    weight = []
    for value in inv_factorial:
        weight.append(pow(value, LIMIT, MOD))

    common = pow(factorial[LIMIT], LIMIT, MOD)
    total = 0

    for k in range(1, LIMIT + 1):
        blocks, last = divmod(LIMIT, k)
        denominator = [1]
        for length in range(1, blocks + 1):
            value = weight[length * k]
            if length % 2:
                value = -value % MOD
            denominator.append(value)

        if blocks > DIRECT_LIMIT:
            coefficients = inverse_series(denominator, blocks + 1)
        else:
            coefficients = direct_inverse(denominator)

        if last == 0:
            count = coefficients[blocks]
        else:
            count = 0
            for complete in range(blocks + 1):
                length = blocks - complete
                term = coefficients[complete] * weight[length * k + last]
                if length % 2:
                    count -= term
                else:
                    count += term
            count %= MOD

        total += common * count
        total %= MOD

    return total


if __name__ == "__main__":
    print(solve())
