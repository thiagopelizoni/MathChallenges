# Problem 768: https://projecteuler.net/problem=768

from collections import defaultdict
from itertools import product

from sympy import Poly, Symbol


def solve():
    sockets, candles = 360, 20
    rows, columns = 3, 5
    rings = sockets // (2 * rows * columns)
    x = Poly(Symbol("x"))
    by_difference = defaultdict(int)

    for column in product((-1, 0, 1), repeat=rows):
        difference = tuple(entry - column[0] for entry in column[1:])
        zeros = column.count(0)
        by_difference[difference] += x ** (rows - zeros) * (1 + x**2) ** zeros

    ring = sum(choices**columns for choices in by_difference.values())
    return (ring**rings).nth(candles)


if __name__ == "__main__":
    print(solve())
