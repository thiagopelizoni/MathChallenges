# Problem 206: https://projecteuler.net/problem=206
from math import isqrt


def fits(n):
    return str(n * n)[::2] == "1234567890"


def solve():
    lo = isqrt(1_020_304_050_607_080_900)
    hi = isqrt(1_929_394_959_697_989_990) + 1

    for n in range(hi - hi % 100 + 70, lo, -100):
        if fits(n):
            return n
        if fits(n - 40):
            return n - 40


if __name__ == "__main__":
    print(solve())
