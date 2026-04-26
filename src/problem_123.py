# Problem 123: https://projecteuler.net/problem=123

from itertools import count

from sympy import nextprime


LIMIT = 10**10


def solve():
    p = 1
    for n in count(1):
        p = nextprime(p)
        if n % 2 and 2 * n * p > LIMIT:
            return n


if __name__ == "__main__":
    print(solve())
