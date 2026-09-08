# Problem 599: https://projecteuler.net/problem=599

from math import comb


def solve():
    n = 10
    corners = 8
    asymmetric = (n**3 - n) // 3
    total = asymmetric + n
    return comb(total + corners - 1, corners) + 2 * comb(
        asymmetric + corners - 1, corners
    )


if __name__ == "__main__":
    print(solve())
