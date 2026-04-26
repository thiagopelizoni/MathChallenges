# Problem 131: https://projecteuler.net/problem=131

from itertools import count

from sympy import isprime


def solve():
    total = 0

    for k in count(1):
        p = 3 * k * k + 3 * k + 1
        if p >= 1_000_000:
            return total
        total += isprime(p)


if __name__ == "__main__":
    print(solve())
