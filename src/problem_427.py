# Problem 427: https://projecteuler.net/problem=427

from array import array
from math import isqrt

import numpy as np


N = 7_500_000
MOD = 1_000_000_009
CHUNK = 200_000


def tables():
    factorial = array("I", [1])
    powers_n = array("I", [1])
    powers_r = array("I", [1])
    r = (1 - N) % MOD
    for i in range(1, N + 1):
        factorial.append(factorial[-1] * i % MOD)
        powers_n.append(powers_n[-1] * N % MOD)
        powers_r.append(powers_r[-1] * r % MOD)

    inverse_factorial = array("I", [0]) * (N + 1)
    inverse_factorial[N] = pow(factorial[N], -1, MOD)
    for i in range(N, 0, -1):
        inverse_factorial[i - 1] = inverse_factorial[i] * i % MOD

    return tuple(
        np.frombuffer(values, dtype=np.uint32)
        for values in (
            factorial,
            inverse_factorial,
            powers_n,
            powers_r,
        )
    )


def solve():
    factorial, inverse_factorial, powers_n, powers_r = tables()

    def terms(i, exponent):
        values = powers_n[exponent].astype(np.int64) * powers_r[i] % MOD
        values = values * factorial[exponent + i] % MOD
        values = values * inverse_factorial[i] % MOD
        values = values * inverse_factorial[exponent] % MOD
        return int(values.sum(dtype=np.int64) % MOD)

    lower = upper = 0
    root = isqrt(N)
    for k in range(1, root + 1):
        maximum = N // k
        for start in range(1, maximum + 1, CHUNK):
            stop = min(maximum + 1, start + CHUNK)
            i = np.arange(start, stop, dtype=np.int64)
            exponent = N - i * k
            lower = (lower + terms(i, exponent)) % MOD
            if stop - 1 < maximum:
                upper = (upper + terms(i, exponent - k)) % MOD
            elif start < maximum:
                upper = (upper + terms(i[:-1], exponent[:-1] - k)) % MOD

    for i in range(1, N // (root + 1) + 1):
        maximum = N // i
        for start in range(root + 1, maximum + 1, CHUNK):
            stop = min(maximum + 1, start + CHUNK)
            k = np.arange(start, stop, dtype=np.int64)
            lower = (lower + terms(i, N - i * k)) % MOD

        maximum = N // (i + 1)
        for start in range(root + 1, maximum + 1, CHUNK):
            stop = min(maximum + 1, start + CHUNK)
            k = np.arange(start, stop, dtype=np.int64)
            upper = (upper + terms(i, N - (i + 1) * k)) % MOD

    geometric = (pow(N, N, MOD) - 1) * pow(N - 1, -1, MOD) % MOD
    return (geometric + upper - lower) % MOD


if __name__ == "__main__":
    print(solve())
