# Problem 504: https://projecteuler.net/problem=504

from math import isqrt

import numpy as np


M = 100


def count_square_interiors(m):
    sides = np.arange(1, m + 1, dtype=np.int64)
    products = sides[:, None] * sides[None, :]
    edges = products - np.gcd(sides[:, None], sides[None, :])
    limit = 2 * m * m + 1
    squares = np.zeros(limit + 1, dtype=np.bool_)
    roots = np.arange(1, isqrt(limit) + 1, dtype=np.int64)
    squares[roots * roots] = True

    total = 0
    for a in range(m):
        last_edges = edges[:, a]
        for b in range(m):
            twice = (
                edges[a, b]
                + edges[b, :, None]
                + edges
                + last_edges[None, :]
            )
            total += int(squares[twice // 2 + 1].sum())
    return total


def solve():
    return count_square_interiors(M)


if __name__ == "__main__":
    print(solve())
