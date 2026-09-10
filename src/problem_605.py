# Problem 605: https://projecteuler.net/problem=605

from math import gcd


def product(n, k, mod):
    m = n * n
    y = pow(2, n, m) - 1
    g = gcd((k - 1) * y + n, y * y, m)

    m = mod * g
    y = pow(2, n, m) - 1
    p = pow(2, n - k, m) * ((k - 1) * y + n) % m
    q = y * y % m
    return (p // g) * (q // g) % mod


def solve():
    return product(10**8 + 7, 10**4 + 7, 10**8)


if __name__ == "__main__":
    print(solve())
