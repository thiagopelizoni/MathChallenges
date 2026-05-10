# Problem 190: https://projecteuler.net/problem=190
from math import prod


def p_floor(m):
    num = prod((2 * i) ** i for i in range(1, m + 1))
    den = (m + 1) ** (m * (m + 1) // 2)
    return num // den


def solve():
    return sum(p_floor(m) for m in range(2, 16))


if __name__ == "__main__":
    print(solve())
