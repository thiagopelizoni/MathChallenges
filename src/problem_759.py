# Problem 759: https://projecteuler.net/problem=759

from functools import cache
from math import comb


def solve(n=10**16):
    mod = 1_000_000_007

    @cache
    def moment(n, a, b):
        if n == 0:
            return int(a == 0 and b == 0)

        total = 2**a * moment(n // 2, a, b)
        for i in range(a + 1):
            for j in range(b + 1):
                total += comb(a, i) * 2**i * comb(b, j) * moment((n - 1) // 2, i, j)
        return total % mod

    return moment(n, 2, 2)


if __name__ == "__main__":
    print(solve())
