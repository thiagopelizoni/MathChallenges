# Problem 197: https://projecteuler.net/problem=197
from math import floor


def f(x):
    return floor(2 ** (30.403243784 - x * x)) * 1e-9


def solve():
    u = -1.0
    for _ in range(1_000):
        u = f(u)
    return f"{u + f(u):.9f}"


if __name__ == "__main__":
    print(solve())
