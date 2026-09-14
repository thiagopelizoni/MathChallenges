# Problem 613: https://projecteuler.net/problem=613

from math import log1p, pi


def solve():
    r = 30 / 40
    probability = 1 / 2 - (log1p(r * r) / r + r * log1p(1 / (r * r))) / (4 * pi)
    return f"{probability:.10f}"


if __name__ == "__main__":
    print(solve())
