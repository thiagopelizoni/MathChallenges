# Problem 532: https://projecteuler.net/problem=532

from math import asin, pi, sin, tan

from scipy.integrate import quad

theta0 = asin(0.999)


def path_length(n):
    s = sin(pi / n)

    def integrand(theta):
        half = asin(sin(theta) * s)
        return tan(theta) / tan(half)

    return quad(integrand, 0.0, theta0)[0]


def solve():
    n = 3
    while path_length(n) <= 1000.0:
        n += 1
    return f"{n * path_length(n):.2f}"


if __name__ == "__main__":
    print(solve())
