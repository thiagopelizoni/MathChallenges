# Problem 129: https://projecteuler.net/problem=129

from itertools import count
from math import gcd


LIMIT = 10**6


def exceeds(n):
    r = 0
    for _ in range(LIMIT):
        r = (10 * r + 1) % n
        if r == 0:
            return False
    return True


def solve():
    for n in count(LIMIT + 1):
        if gcd(n, 10) == 1 and exceeds(n):
            return n


if __name__ == "__main__":
    print(solve())
