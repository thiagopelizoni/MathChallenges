# Problem 607: https://projecteuler.net/problem=607

from math import nextafter, sqrt, ulp

from scipy.optimize import brentq


def solve():
    distance = 100 / sqrt(2)
    outside = (distance - 50) / 2
    widths = [outside] + [10] * 5 + [outside]
    speeds = [10, 9, 8, 7, 6, 5, 10]

    def displacement(p):
        return sum(
            w * p * v / sqrt(1 - (p * v)**2)
            for w, v in zip(widths, speeds)
        ) - distance

    upper = 1 / max(speeds)
    p = brentq(displacement, 0, nextafter(upper, 0), xtol=ulp(upper))
    time = sum(
        w / (v * sqrt(1 - (p * v)**2))
        for w, v in zip(widths, speeds)
    )
    return f"{time:.10f}"


if __name__ == "__main__":
    print(solve())
