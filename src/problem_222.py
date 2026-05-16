# Problem 222: https://projecteuler.net/problem=222
from math import sqrt


def gap(a, b):
    return sqrt((a + b) ** 2 - (100 - a - b) ** 2)


def solve():
    rs = list(range(50, 29, -2)) + list(range(31, 50, 2))
    length = rs[0] + rs[-1] + sum(gap(a, b) for a, b in zip(rs, rs[1:]))
    return round(1000 * length)


if __name__ == "__main__":
    print(solve())
