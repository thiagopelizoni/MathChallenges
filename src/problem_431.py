# Problem 431: https://projecteuler.net/problem=431

from math import ceil, cos, floor, pi, sin, sqrt, tan

from scipy.integrate import quad
from scipy.optimize import brentq


RADIUS = 6
SLOPE = tan(40 * pi / 180)


def volume(x):
    def ray_cube(theta):
        reach = -x * cos(theta) + sqrt(
            RADIUS**2 - x**2 * sin(theta) ** 2
        )
        return reach**3

    return SLOPE * quad(ray_cube, 0, 2 * pi, epsabs=1e-11, epsrel=1e-13)[0] / 3


def solve():
    first = ceil(sqrt(volume(0)))
    last = floor(sqrt(volume(RADIUS)))
    roots = (
        brentq(lambda x: volume(x) - n**2, 0, RADIUS, xtol=1e-13)
        for n in range(first, last + 1)
    )
    return f"{sum(roots):.9f}"


if __name__ == "__main__":
    print(solve())
