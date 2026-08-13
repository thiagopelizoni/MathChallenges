# Problem 535: https://projecteuler.net/problem=535

from functools import cache
from math import isqrt


LIMIT = 10**18
MOD = 10**9


def sqrt_sum(n):
    if n == 0:
        return 0
    r = isqrt(n)
    k = r - 1
    return k * (k + 1) * (4 * k + 5) // 6 + r * (n - r * r + 1)


def noncircles(n):
    lo, hi = 0, n // 2
    while lo < hi:
        m = (lo + hi + 1) // 2
        if m + root_sum(m) <= n:
            lo = m
        else:
            hi = m - 1
    return lo


@cache
def root_sum(n):
    if n == 0:
        return 0
    m = noncircles(n)
    return root_sum(m) + sqrt_sum(n - m)


def solve():
    n = LIMIT
    total = 0
    while n:
        m = noncircles(n)
        q = n - m
        total += q * (q + 1) // 2
        n = m
    return total % MOD


if __name__ == "__main__":
    print(solve())
