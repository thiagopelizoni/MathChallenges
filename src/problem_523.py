# Problem 523: https://projecteuler.net/problem=523

from decimal import Decimal
from fractions import Fraction


def solve():
    expected = Fraction()
    for n in range(2, 31):
        expected += Fraction(2 ** (n - 1) - 1, n)
    value = Decimal(expected.numerator) / Decimal(expected.denominator)
    return f"{value:.2f}"


if __name__ == "__main__":
    print(solve())
