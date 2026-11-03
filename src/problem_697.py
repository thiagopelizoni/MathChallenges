# Problem 697: https://projecteuler.net/problem=697

from math import log

from scipy.special import gammainccinv


def solve():
    x = gammainccinv(10_000_000, 0.25)
    return f"{x / log(10):.2f}"


if __name__ == "__main__":
    print(solve())
