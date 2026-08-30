# Problem 575: https://projecteuler.net/problem=575
from fractions import Fraction


def solve():
    n = 1000
    related_weight = 0
    fixed_weight = 0

    for k in range(1, n + 1):
        row, column = divmod(k * k - 1, n)
        degree = 4
        if row == 0 or row == n - 1:
            degree -= 1
        if column == 0 or column == n - 1:
            degree -= 1
        related_weight += degree + 1
        fixed_weight += degree

    related_total = n * n + 4 * n * (n - 1)
    fixed_total = 4 * n * (n - 1)
    probability = (Fraction(related_weight, related_total) + Fraction(fixed_weight, fixed_total)) / 2
    return f"{float(probability):.12f}"


if __name__ == "__main__":
    print(solve())
