# Problem 805: https://projecteuler.net/problem=805
from math import gcd

from sympy import n_order


MOD = 1_000_000_007


def smallest_rotation(a, b):
    den = 10 * b - a
    if den <= 0:
        return 0

    min_length = 1
    while a * 10**min_length < 10 * b:
        min_length += 1

    best = None
    for digit in range(1, 10):
        q = den // gcd(den, digit * b)
        if gcd(q, 10) != 1:
            continue
        period = n_order(10, q) if q > 1 else 1
        length = (min_length + period - 1) // period * period

        excess = (digit + 1) * a - 10 * b
        if excess > 0:
            max_power = (10 * digit * b - 1) // excess
            if length >= len(str(max_power)):
                continue

        candidate = length, digit
        if best is None or candidate < best:
            best = candidate

    if best is None:
        return 0
    length, digit = best
    nines = pow(10, length, MOD * den) - 1
    return digit * b * nines // den % MOD


def solve(limit=200):
    total = 0
    for u in range(1, limit + 1):
        for v in range(1, limit + 1):
            if gcd(u, v) == 1:
                total += smallest_rotation(u**3, v**3)
    return total % MOD


if __name__ == "__main__":
    print(solve())
