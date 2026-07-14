# Problem 389: https://projecteuler.net/problem=389

from fractions import Fraction


def solve():
    mean = Fraction(5, 2)
    variance = Fraction(5, 4)

    for sides in (6, 8, 12, 20):
        die_mean = Fraction(sides + 1, 2)
        die_variance = Fraction(sides * sides - 1, 12)
        variance = die_variance * mean + die_mean * die_mean * variance
        mean *= die_mean

    return f"{float(variance):.4f}"


if __name__ == "__main__":
    print(solve())
