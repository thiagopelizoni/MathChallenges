# Problem 804: https://projecteuler.net/problem=804

from math import isqrt


def solve(n=10**16):
    limit = 4 * n
    d = 4 * 41 - 1
    total = isqrt(n)

    for y in range(1, isqrt(limit // d) + 1):
        r = isqrt(limit - d * y * y)
        total += r + 1 - (r - y) % 2

    return 2 * total


if __name__ == "__main__":
    print(solve())
