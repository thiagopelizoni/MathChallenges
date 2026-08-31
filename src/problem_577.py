# Problem 577: https://projecteuler.net/problem=577
from math import comb


def solve():
    n = 12345
    total = 0

    for side_sum in range(1, n // 3 + 1):
        total += side_sum * comb(n - 3 * side_sum + 3, 3)

    return total


if __name__ == "__main__":
    print(solve())
