# Problem 158: https://projecteuler.net/problem=158
from math import comb


def solve():
    return max(comb(26, n) * (2**n - n - 1) for n in range(1, 27))


if __name__ == "__main__":
    print(solve())
