# Problem 114: https://projecteuler.net/problem=114

from functools import cache


@cache
def ways(n):
    if n < 3:
        return 1
    return ways(n - 1) + sum(
        1 if m == n else ways(n - m - 1)
        for m in range(3, n + 1)
    )


def solve():
    return ways(50)


if __name__ == "__main__":
    print(solve())
