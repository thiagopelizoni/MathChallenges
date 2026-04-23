# Problem 106: https://projecteuler.net/problem=106

from math import comb


def solve():
    n = 12
    return sum(
        comb(n, 2 * k) * (comb(2 * k, k) // 2 - comb(2 * k, k) // (k + 1))
        for k in range(2, n // 2 + 1)
    )


if __name__ == "__main__":
    print(solve())
