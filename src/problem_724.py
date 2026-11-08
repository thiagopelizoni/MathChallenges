# Problem 724: https://projecteuler.net/problem=724

from math import fsum


def solve():
    n = 10**8
    h = fsum(1 / k for k in range(1, n + 1))
    h2 = fsum(1 / (k * k) for k in range(1, n + 1))
    return round(n * (h * h + h2) / 2)


if __name__ == "__main__":
    print(solve())
