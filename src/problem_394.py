# Problem 394: https://projecteuler.net/problem=394
from math import log


def expected_repetitions(x):
    return 7 / 9 + 2 * log(x) / 3 + 2 / (9 * x**3)


def solve():
    return f"{expected_repetitions(40):.10f}"


if __name__ == "__main__":
    print(solve())
