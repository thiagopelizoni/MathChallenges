# Problem 199: https://projecteuler.net/problem=199
from math import sqrt


def tangent(a, b, c):
    return a + b + c + 2 * sqrt(a * b + a * c + b * c)


def fill(a, b, c, depth):
    if depth == 0:
        return 0.0

    k = tangent(a, b, c)
    return (
        1 / (k * k)
        + fill(k, a, b, depth - 1)
        + fill(k, a, c, depth - 1)
        + fill(k, b, c, depth - 1)
    )


def solve():
    r = 2 * sqrt(3) - 3
    k = 1 / r
    covered = 3 * r * r + fill(k, k, k, 10) + 3 * fill(-1, k, k, 10)
    return f"{1 - covered:.8f}"


if __name__ == "__main__":
    print(solve())
