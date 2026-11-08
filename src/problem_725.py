# Problem 725: https://projecteuler.net/problem=725

from math import comb


def solve(n=2020):
    mod = 10**16
    total = 0
    for d in range(1, 10):
        total += d * (2 * comb(n + d - 2, d) - (n - 1))
    repunit = (10**n - 1) // 9
    return total * repunit % mod


if __name__ == "__main__":
    print(solve())
