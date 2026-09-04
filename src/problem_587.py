# Problem 587: https://projecteuler.net/problem=587

from math import asin, pi, sqrt


def solve():
    l_section = 1 - pi / 4
    n = 1

    while True:
        x = n * (n + 1 - sqrt(2 * n)) / (n * n + 1)
        u = x - 1
        area = x * x / (2 * n) + 1 - x
        area += (u * sqrt(1 - u * u) + asin(u)) / 2

        if area / l_section < 0.001:
            return n
        n += 1


if __name__ == "__main__":
    print(solve())
