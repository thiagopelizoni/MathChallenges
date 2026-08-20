# Problem 553: https://projecteuler.net/problem=553

from sympy.discrete.convolutions import convolution_ntt
from sympy.ntheory.modular import crt1, crt2


LIMIT = 10_000
COMPONENTS = 10
MOD = 1_000_000_007
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
    inverse = [pow(values[0], -1, MOD)]

    while len(inverse) < limit:
        size = min(2 * len(inverse), limit)
        product = multiply(values[:size], inverse, size)
        correction = [0] * size
        correction[0] = (2 - product[0]) % MOD
        for i in range(1, len(product)):
            correction[i] = -product[i] % MOD
        inverse = multiply(inverse, correction, size)

    return inverse


def solve():
    factorial = [1] * (LIMIT + 1)
    for i in range(1, LIMIT + 1):
        factorial[i] = factorial[i - 1] * i % MOD

    inv_factorial = [1] * (LIMIT + 1)
    inv_factorial[LIMIT] = pow(factorial[LIMIT], -1, MOD)
    for i in range(LIMIT, 0, -1):
        inv_factorial[i - 1] = inv_factorial[i] * i % MOD

    families = []
    for n in range(LIMIT + 1):
        exponent = (pow(2, n, MOD - 1) - 1) % (MOD - 1)
        count = pow(2, exponent, MOD)
        families.append(count * inv_factorial[n] % MOD)

    inverse = inverse_series(families, LIMIT + 1)
    derivative = [n * families[n] % MOD for n in range(1, LIMIT + 1)]
    quotient = multiply(derivative, inverse, LIMIT)
    connected = [0] * (LIMIT + 1)
    for n in range(1, LIMIT + 1):
        connected[n] = quotient[n - 1] * pow(n, -1, MOD) % MOD
    connected[1] = (connected[1] - 1) % MOD

    power = [1]
    base = connected
    exponent = COMPONENTS
    while exponent:
        if exponent % 2:
            power = multiply(power, base, LIMIT + 1)
        exponent //= 2
        if exponent:
            base = multiply(base, base, LIMIT + 1)

    total = multiply(power, inv_factorial, LIMIT + 1)[LIMIT]
    return factorial[LIMIT] * total % MOD * inv_factorial[COMPONENTS] % MOD


if __name__ == "__main__":
    print(solve())
