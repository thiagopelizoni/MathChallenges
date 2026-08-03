# Problem 493: https://projecteuler.net/problem=493

from decimal import Decimal
from fractions import Fraction
from math import comb


def solve():
    missing = Fraction(comb(60, 20), comb(70, 20))
    expectation = 7 * (1 - missing)
    value = Decimal(expectation.numerator) / expectation.denominator
    return f"{value:.9f}"


if __name__ == "__main__":
    print(solve())
