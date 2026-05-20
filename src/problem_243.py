# Problem 243: https://projecteuler.net/problem=243
from fractions import Fraction

from sympy import nextprime


TARGET = Fraction(15499, 94744)


def solve():
    d = 1
    phi = 1
    p = 2

    while Fraction(phi, d) >= TARGET:
        d *= p
        phi *= p - 1
        p = nextprime(p)

    m = 1
    while Fraction(phi * m, d * m - 1) >= TARGET:
        m += 1

    return d * m


if __name__ == "__main__":
    print(solve())
