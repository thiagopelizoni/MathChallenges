# Problem 115: https://projecteuler.net/problem=115

from functools import cache


LIMIT = 1_000_000
MIN_BLOCK = 50


@cache
def ways(m, n):
    if n < m:
        return 1
    return ways(m, n - 1) + sum(
        1 if k == n else ways(m, n - k - 1)
        for k in range(m, n + 1)
    )


def solve():
    n = MIN_BLOCK
    while ways(MIN_BLOCK, n) <= LIMIT:
        n += 1
    return n


if __name__ == "__main__":
    print(solve())
