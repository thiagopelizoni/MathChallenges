# Problem 777: https://projecteuler.net/problem=777

from decimal import Decimal
from math import lcm

from sympy import sieve


def multiples(m, d):
    n = m // d
    s = d * n * (n + 1) // 2
    if d == 1:
        return n - 1, s - 1
    return n, s


def s4(m):
    total = 0
    for d, mu in enumerate(sieve.mobiusrange(1, m + 1), 1):
        if not mu:
            continue

        n, s = multiples(m, d)
        weight = 8 * s * s - 12 * n * s

        for r, t in ((10, 1), (2, 5)):
            na, sa = multiples(m, lcm(d, r))
            nb, sb = multiples(m, lcm(d, t))
            correction = -6 * sa * sb + 3 * (sa * nb + sb * na) + 4 * na * nb
            weight += 2 * correction

        total += mu * weight
    return total


def solve():
    ans = Decimal(s4(10**6)) / 4
    return f"{ans:.9e}".replace("e+", "e")


if __name__ == "__main__":
    print(solve())
