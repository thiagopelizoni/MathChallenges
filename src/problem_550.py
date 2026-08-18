# Problem 550: https://projecteuler.net/problem=550

import numpy as np
from sympy import primerange


LIMIT = 10_000_000
PILES = 10**12
MOD = 987_654_321


def grundy_values(length):
    grundy = [0] * (length + 1)

    for total in range(2, length + 1):
        moves = set()
        for a in range(1, total):
            for b in range(1, total):
                moves.add(grundy[a] ^ grundy[b])

        value = 0
        while value in moves:
            value += 1
        grundy[total] = value

    return grundy


def transform(values):
    width = 1
    while width < len(values):
        for start in range(0, len(values), 2 * width):
            for i in range(start, start + width):
                a = values[i]
                b = values[i + width]
                values[i] = (a + b) % MOD
                values[i + width] = (a - b) % MOD
        width *= 2


def solve():
    omega = np.zeros(LIMIT + 1, dtype=np.uint8)

    for p in primerange(2, LIMIT + 1):
        power = p
        while power <= LIMIT:
            omega[power::power] += 1
            power *= p

    frequency = np.bincount(omega[2:])
    grundy = grundy_values(len(frequency) - 1)
    size = 1
    while size <= max(grundy):
        size *= 2

    distribution = [0] * size
    for total in range(1, len(frequency)):
        distribution[grundy[total]] += int(frequency[total])

    transform(distribution)
    distribution = [pow(value, PILES, MOD) for value in distribution]
    transform(distribution)

    losing = distribution[0] * pow(size, -1, MOD) % MOD
    return (pow(LIMIT - 1, PILES, MOD) - losing) % MOD


if __name__ == "__main__":
    print(solve())
