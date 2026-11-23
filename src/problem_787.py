# Problem 787: https://projecteuler.net/problem=787

from functools import cache


@cache
def coprime_pairs(n):
    odds = (n + 2) // 4
    total = odds * (n + 1 - 2 * odds)
    d = 3
    while 2 * d <= n:
        q = n // d
        count = (n // q - d) // 2 + 1
        total -= count * coprime_pairs(q)
        d += 2 * count
    return total


def solve():
    return 2 * coprime_pairs(10**9) - 1


if __name__ == "__main__":
    print(solve())
