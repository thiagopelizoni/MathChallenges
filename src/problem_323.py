# Problem 323: https://projecteuler.net/problem=323

from decimal import Decimal, getcontext
from fractions import Fraction
from math import comb


BITS = 32


def solve():
    getcontext().prec = 50
    total = Fraction(0, 1)

    for j in range(1, BITS + 1):
        sign = 1 if j % 2 else -1
        total += sign * comb(BITS, j) * Fraction(2**j, 2**j - 1)

    ans = Decimal(total.numerator) / Decimal(total.denominator)
    return f"{ans:.10f}"


if __name__ == "__main__":
    print(solve())
