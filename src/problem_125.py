# Problem 125: https://projecteuler.net/problem=125

from math import isqrt


def palindrome(n):
    s = str(n)
    return s == s[::-1]


def solve():
    lim = 10**8
    squares = [n * n for n in range(1, isqrt(lim) + 1)]
    vals = set()

    for i, first in enumerate(squares):
        total = first
        for j in range(i + 1, len(squares)):
            total += squares[j]
            if total >= lim:
                break
            if palindrome(total):
                vals.add(total)

    return sum(vals)


if __name__ == "__main__":
    print(solve())
