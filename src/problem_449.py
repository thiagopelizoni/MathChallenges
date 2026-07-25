# Problem 449: https://projecteuler.net/problem=449

from math import asinh, atan, pi, sqrt


def chocolate_volume(a, b):
    c = sqrt(a * a - b * b)
    surface = 2 * pi * (
        a * a + a * b * b * asinh(c / b) / c
    )
    mean_curvature = 2 * pi * (
        b + a * a * atan(c / b) / c
    )
    return surface + mean_curvature + 4 * pi / 3


def solve():
    return f"{chocolate_volume(3, 1):.8f}"


if __name__ == "__main__":
    print(solve())
