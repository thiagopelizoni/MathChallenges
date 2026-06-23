# Problem 325: https://projecteuler.net/problem=325

from functools import cache
from math import isqrt


N = 10**16
MOD = 7**10


def lower(n):
    return (isqrt(5 * n * n) - n) // 2


def p1(n):
    return n * (n + 1) // 2


def p2(n):
    return n * (n + 1) * (2 * n + 1) // 6


@cache
def sums(n):
    if n == 0:
        return 0, 0, 0

    m = lower(n)
    a, b, x = sums(m)
    sm = p1(m)
    qm = p2(m)

    an = m * n - sm - a
    bn = n * m * m - (2 * qm - sm) - (2 * x - a)
    xn = m * p1(n) - (qm + 2 * x + b + sm + a) // 2

    return an, bn, xn


def total(n):
    m = lower(n)
    a, b, x = sums(m)
    left = 2 * x + (b + a) // 2

    c = n - m
    sx = p1(n) - p1(m)
    sx2 = p2(n) - p2(m)
    right = ((2 * n - 1) * sx - 3 * sx2 + c * n * (n + 1)) // 2

    return left + right


def solve():
    return total(N) % MOD


if __name__ == "__main__":
    print(solve())
