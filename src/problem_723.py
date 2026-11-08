# Problem 723: https://projecteuler.net/problem=723

from itertools import product
from math import comb, prod

from sympy import factorint


def count(exponents):
    n = prod(e + 1 for e in exponents)
    t = h = 1
    for e in exponents:
        ways = [min(j + 1, 2 * e - j + 1) for j in range(2 * e + 1)]
        t *= sum(w * w for w in ways)
        h *= sum(ways[::2])
    k = 2 * n
    return k * (k - 1) ** 2 - comb(k, 2) + 4 * (t - h - n * n + n)


def solve():
    factors = factorint(1411033124176203125)
    ranges = [range(e + 1) for e in factors.values()]
    return sum(count(exponents) for exponents in product(*ranges))


if __name__ == "__main__":
    print(solve())
