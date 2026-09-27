# Problem 638: https://projecteuler.net/problem=638

from math import comb


def c(a, b, k, mod):
    if k == 1:
        return comb(a + b, a) % mod

    numerator = denominator = 1
    upper = pow(k, a, mod)
    lower = 1
    for _ in range(b):
        upper = upper * k % mod
        lower = lower * k % mod
        numerator = numerator * (upper - 1) % mod
        denominator = denominator * (lower - 1) % mod
    return numerator * pow(denominator, -1, mod) % mod


def solve():
    mod = 1_000_000_007
    total = 0
    for k in range(1, 8):
        n = 10**k + k
        total += c(n, n, k, mod)
    return total % mod


if __name__ == "__main__":
    print(solve())
