# Problem 153: https://projecteuler.net/problem=153

from functools import cache
from math import gcd, isqrt


@cache
def divisor_sum(n):
    total = 0
    d = 1

    while d <= n:
        q = n // d
        e = n // q
        total += q * (d + e) * (e - d + 1) // 2
        d = e + 1

    return total


def solve():
    lim = 100_000_000
    total = divisor_sum(lim)

    for x in range(1, isqrt(lim) + 1):
        ymax = isqrt(lim - x * x)
        for y in range(1, ymax + 1):
            if gcd(x, y) == 1:
                total += 2 * x * divisor_sum(lim // (x * x + y * y))

    return total


if __name__ == "__main__":
    print(solve())
