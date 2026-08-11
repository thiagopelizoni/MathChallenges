# Problem 525: https://projecteuler.net/problem=525

from math import cos, pi, sin, sqrt

from scipy.integrate import quad


def curve_length(a, b):
    def speed(t):
        x = cos(t) ** 2
        y = sin(t) ** 2
        return sqrt((a**4 * x + b**4 * y) / (a * a * x + b * b * y))

    return 4 * quad(speed, 0, pi / 2, epsabs=1e-13, epsrel=1e-13)[0]


def solve():
    return f"{curve_length(1, 4) + curve_length(3, 4):.8f}"


if __name__ == "__main__":
    print(solve())
