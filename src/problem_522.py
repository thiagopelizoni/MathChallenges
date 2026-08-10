# Problem 522: https://projecteuler.net/problem=522

from array import array

import numpy as np

N = 12_344_321
MOD = 135_707_531
CHUNK = 500_000


def mod_powers(start, stop):
    exponents = np.arange(start, stop - 1, -1, dtype=np.int64)
    bases = (exponents - 1) % MOD
    values = np.ones_like(exponents)
    limit = start
    while limit:
        odd = exponents % 2 == 1
        values[odd] = values[odd] * bases[odd] % MOD
        bases = bases * bases % MOD
        exponents //= 2
        limit //= 2
    return values


def solve():
    inverses = array("I", [0]) * (N + 1)
    inverses[1] = 1
    inverses[2] = (MOD + 1) // 2

    coefficient = N * (N - 1) // 2 % MOD
    cycles = 0
    d = 2
    while d <= N:
        end = min(d + CHUNK - 1, N)
        powers = mod_powers(N - d, N - end)
        for power in powers:
            cycles = (cycles + coefficient * int(power)) % MOD
            d += 1
            if d <= N:
                inverses[d] = MOD - MOD // d * inverses[MOD % d] % MOD
                coefficient = coefficient * (N - d + 1) % MOD * (d - 1) % MOD * inverses[d] % MOD

    zeros = N * (N - 1) % MOD * pow(N - 2, N - 1, MOD) % MOD
    return (zeros + cycles - coefficient) % MOD


if __name__ == "__main__":
    print(solve())
