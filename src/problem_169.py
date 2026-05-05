# Problem 169: https://projecteuler.net/problem=169
from functools import cache


@cache
def f(n):
    if n == 0:
        return 1
    if n % 2:
        return f(n // 2)
    return f(n // 2) + f(n // 2 - 1)


def solve():
    return f(10**25)


if __name__ == "__main__":
    print(solve())
