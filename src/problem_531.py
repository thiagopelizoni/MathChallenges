# Problem 531: https://projecteuler.net/problem=531

from math import gcd

from sympy import sieve


LOWER = 1_000_000
UPPER = 1_005_000


def solve():
    phi = list(sieve.totientrange(LOWER, UPPER))
    total = 0
    for i, n in enumerate(range(LOWER, UPPER)):
        a = phi[i]
        for j in range(i + 1, UPPER - LOWER):
            m = LOWER + j
            d = gcd(n, m)
            delta = phi[j] - a
            if delta % d == 0:
                q = m // d
                total += a + n * ((delta // d) * pow(n // d, -1, q) % q)
    return total


if __name__ == "__main__":
    print(solve())
