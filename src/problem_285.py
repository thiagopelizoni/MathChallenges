# Problem 285: https://projecteuler.net/problem=285

from math import asin, fsum, pi, sqrt


LIMIT = 10**5
ROOT2 = sqrt(2)


def area(r):
    if r <= ROOT2:
        return 0.0

    strip = 0.5 * (sqrt(r * r - 1) + r * r * asin(1 / r))
    return pi * r * r / 4 - 2 * strip + 1


def solve():
    total = fsum(
        (area(k + 0.5) - area(k - 0.5)) / k
        for k in range(1, LIMIT + 1)
    )
    return f"{total:.5f}"


if __name__ == "__main__":
    print(solve())
