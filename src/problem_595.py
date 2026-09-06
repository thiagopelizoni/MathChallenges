# Problem 595: https://projecteuler.net/problem=595

from fractions import Fraction
from math import comb, factorial


def solve(n=52):
    counts = [0, 1]
    e = [Fraction(0), Fraction(0)]
    for m in range(2, n + 1):
        count = sum(
            (-1)**k * comb(m - 1, k) * factorial(m - k)
            for k in range(m)
        )
        counts.append(count)

        total = Fraction(factorial(m) - 1)
        for j in range(2, m):
            total += comb(m - 1, j - 1) * counts[j] * e[j]
        e.append(total / (factorial(m) - count))

    return f"{e[n]:.8f}"


if __name__ == "__main__":
    print(solve())
