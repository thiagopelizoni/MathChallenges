# Problem 539: https://projecteuler.net/problem=539

from functools import cache


def solve():
    @cache
    def p(n):
        if n == 1:
            return 1
        return 2 * (n // 2 + 1 - p(n // 2))

    @cache
    def s(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        m = n // 2
        if n % 2 == 1:
            return 1 + 2 * m * m + 6 * m - 4 * s(m)
        return 2 * m * m + 4 * m - 1 - 4 * s(m) + 2 * p(m)

    return s(10**18) % 987654321


if __name__ == "__main__":
    print(solve())
