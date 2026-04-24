# Problem 112: https://projecteuler.net/problem=112

from itertools import pairwise


def bouncy(n):
    digits = str(n)
    return not (
        all(a <= b for a, b in pairwise(digits))
        or all(a >= b for a, b in pairwise(digits))
    )


def solve():
    count = 0
    n = 99

    while True:
        n += 1
        count += bouncy(n)
        if 100 * count == 99 * n:
            return n


if __name__ == "__main__":
    print(solve())
