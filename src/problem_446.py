# Problem 446: https://projecteuler.net/problem=446

import numpy as np
from sympy import sieve, sqrt_mod


N = 10_000_000
MOD = 1_000_000_007


def solve():
    values = np.arange(N + 2, dtype=np.uint64)
    values *= values
    values += 1
    sigma = np.ones(N + 2, dtype=np.uint64)
    values[1::2] //= 2

    for prime in sieve.primerange(5, N + 2):
        p = int(prime)
        if p % 4 != 1:
            continue
        root = int(sqrt_mod(-1, p))
        for residue in (root, p - root):
            remaining = values[residue::p]
            factors = sigma[residue::p]
            remaining //= p
            factors[:] = factors * (p + 1) % MOD

            exponent = 1
            while True:
                selected = remaining % p == 0
                if not selected.any():
                    break
                remaining[selected] //= p
                exponent += 1
                old = (pow(p, exponent - 1, MOD) + 1) % MOD
                new = (pow(p, exponent, MOD) + 1) % MOD
                ratio = new * pow(old, -1, MOD) % MOD
                factors[selected] = factors[selected] * ratio % MOD

    selected = values > 1
    sigma[selected] = sigma[selected] * ((values[selected] + 1) % MOD) % MOD

    unitary = sigma[:N] * sigma[2 : N + 2] % MOD
    unitary[1::2] = unitary[1::2] * 5 % MOD
    unitary_sum = int(unitary.sum(dtype=np.uint64) % MOD)
    fourth_powers = N * (N + 1) * (2 * N + 1) * (3 * N * N + 3 * N - 1) // 30
    return (unitary_sum - fourth_powers - 4 * N) % MOD


if __name__ == "__main__":
    print(solve())
