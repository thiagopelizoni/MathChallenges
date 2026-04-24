# Problem 113: https://projecteuler.net/problem=113

from math import comb


def solve():
    n = 100
    return comb(n + 10, 10) + comb(n + 9, 9) - 10 * n - 2


if __name__ == "__main__":
    print(solve())
