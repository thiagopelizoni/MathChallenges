# Problem 517: https://projecteuler.net/problem=517

from array import array
from math import isqrt

from sympy import primerange

A = 10_000_000
B = 10_010_000
MOD = 1_000_000_007


def solve():
    fact = array("I", [1]) * (B + 1)
    for n in range(1, B + 1):
        fact[n] = fact[n - 1] * n % MOD

    invfact = array("I", [1]) * (B + 1)
    invfact[B] = pow(fact[B], MOD - 2, MOD)
    for n in range(B, 0, -1):
        invfact[n - 1] = invfact[n] * n % MOD

    total = 0
    for p in primerange(A + 1, B):
        total += 1
        for r in range(1, isqrt(p) + 1):
            n = p - isqrt(r * r * p) - 1 + r
            total += fact[n] * invfact[r] % MOD * invfact[n - r] % MOD
        total %= MOD
    return total


if __name__ == "__main__":
    print(solve())
