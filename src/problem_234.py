# Problem 234: https://projecteuler.net/problem=234
from math import isqrt

from sympy import nextprime, primerange


LIMIT = 999_966_663_333


def sum_multiples(m, lo, hi):
    a = (lo + m - 1) // m
    b = hi // m
    if a > b:
        return 0
    return m * (a + b) * (b - a + 1) // 2


def solve():
    r = isqrt(LIMIT)
    ps = list(primerange(2, r + 1))
    ps.append(nextprime(ps[-1]))

    total = 0
    for p, q in zip(ps, ps[1:]):
        lo = p * p + 1
        hi = min(q * q - 1, LIMIT)
        if lo > LIMIT:
            break
        total += sum_multiples(p, lo, hi)
        total += sum_multiples(q, lo, hi)
        total -= 2 * sum_multiples(p * q, lo, hi)
    return total


if __name__ == "__main__":
    print(solve())
