# Problem 478: https://projecteuler.net/problem=478

import numpy as np
from sympy import sieve


N = 10_000_000
MOD = 11**8


def mixture_subsets(n):
    mu = np.zeros(n + 1, dtype=np.int8)
    mu[1:] = np.fromiter(
        sieve.mobiusrange(1, n + 1), dtype=np.int8, count=n
    )
    mertens = memoryview(np.cumsum(mu, dtype=np.int32))

    phi = np.zeros(n + 1, dtype=np.int32)
    phi[1:] = np.fromiter(
        sieve.totientrange(1, n + 1), dtype=np.int32, count=n
    )
    phi = memoryview(phi)

    total = 0
    i = 1
    while i <= n:
        q = n // i
        j = n // q + 1
        total += (mertens[j - 1] - mertens[i - 1]) * ((q + 1) ** 3 - 1)
        i = j

    half = (total - 1) // 2
    central = pow(2, half, MOD)
    answer = pow(2, total, MOD) - 1
    previous = None
    power = None
    powers = {}

    for h in range(1, n + 1):
        rank = 0
        i = 1
        limit = n // h
        while i <= limit:
            q = n // i
            j = n // q + 1
            d = q // h
            points = d * (2 * q + 2 - h * (d + 1)) // 2
            rank += points * (mertens[j - 1] - mertens[i - 1])
            i = j

        if previous is None:
            power = pow(2, half - rank, MOD)
        else:
            delta = previous - rank
            factor = powers.get(delta)
            if factor is None:
                factor = pow(2, delta, MOD)
                powers[delta] = factor
            power = power * factor % MOD

        answer -= 6 * phi[h] * (central - power)
        previous = rank

    return answer % MOD


def solve():
    return mixture_subsets(N)


if __name__ == "__main__":
    print(solve())
