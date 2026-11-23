# Problem 788: https://projecteuler.net/problem=788

from math import comb


def solve(n=2022):
    mod = 1_000_000_007
    total = 0
    for k in range((n - 1) // 2 + 1):
        placements = comb(n + 1, k + 1) - comb(2 * k + 1, k + 1)
        total += placements * pow(9, k + 1, mod)
    return total % mod


if __name__ == "__main__":
    print(solve())
