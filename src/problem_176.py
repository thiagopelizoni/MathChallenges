# Problem 176: https://projecteuler.net/problem=176
from math import prod


def solve():
    factors = (19, 13, 11, 7, 5)
    primes = (2, 3, 5, 7, 11)
    m = prod(p ** ((f - 1) // 2) for p, f in zip(primes, factors))
    return 2 * m


if __name__ == "__main__":
    print(solve())
