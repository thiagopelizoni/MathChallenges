# Problem 180: https://projecteuler.net/problem=180
from fractions import Fraction
from math import isqrt


def rational_sqrt(q):
    a = isqrt(q.numerator)
    b = isqrt(q.denominator)
    if a * a == q.numerator and b * b == q.denominator:
        return Fraction(a, b)
    return None


def solve():
    k = 35
    rationals = {Fraction(a, b) for b in range(2, k + 1) for a in range(1, b)}
    sums = set()

    for x in rationals:
        for y in rationals:
            for z in (x + y, x * y / (x + y)):
                if z in rationals:
                    sums.add(x + y + z)

            z = rational_sqrt(x * x + y * y)
            if z is not None:
                if z in rationals:
                    sums.add(x + y + z)
                w = x * y / z
                if w in rationals:
                    sums.add(x + y + w)

    total = sum(sums, Fraction(0))
    return total.numerator + total.denominator


if __name__ == "__main__":
    print(solve())
