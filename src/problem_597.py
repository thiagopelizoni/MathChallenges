# Problem 597: https://projecteuler.net/problem=597

from fractions import Fraction
from functools import cache


def solve(n=13, length=1800):
    @cache
    def parity(n, l):
        if n == 0:
            return Fraction(1)
        total = Fraction(0)
        for k in range(n):
            total += (-1) ** k * (l - k) * parity(k, k) * parity(n - k - 1, l - k - 1)
        return total / (n * l - n * (n - 1) // 2)

    p = (1 + parity(n, Fraction(length, 40))) / 2
    return f"{float(p):.10f}"


if __name__ == "__main__":
    print(solve())
