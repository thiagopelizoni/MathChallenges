# Problem 281: https://projecteuler.net/problem=281

from functools import cache
from math import factorial


LIMIT = 10**15


def divisors(n):
    out = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
        d += 1
    return out


@cache
def phi(n):
    ans = n
    p = 2
    q = n
    while p * p <= q:
        if q % p == 0:
            while q % p == 0:
                q //= p
            ans -= ans // p
        p += 1
    if q > 1:
        ans -= ans // q
    return ans


def f(m, n):
    total = 0
    for d in divisors(n):
        total += phi(d) * factorial(m * n // d) // factorial(n // d) ** m
    return total // (m * n)


def solve():
    ans = 0
    m = 2

    while f(m, 1) <= LIMIT:
        n = 1
        while True:
            v = f(m, n)
            if v > LIMIT:
                break
            ans += v
            n += 1
        m += 1

    return ans


if __name__ == "__main__":
    print(solve())
