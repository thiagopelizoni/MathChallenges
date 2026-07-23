# Problem 436: https://projecteuler.net/problem=436

from math import e


def solve():
    probability = (1 + 14 * e - 5 * e**2) / 4
    return f"{probability:.10f}"


if __name__ == "__main__":
    print(solve())
