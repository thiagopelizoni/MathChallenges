# Problem 791: https://projecteuler.net/problem=791

from math import isqrt

import numpy as np


def solve(n=10**8):
    w = np.arange(isqrt(2 * n) + 1, dtype=np.int64)
    bounds = w * (w + 1)
    squares = np.zeros(len(w) + 1, dtype=np.int64)
    squares[1:] = np.cumsum(w * w)

    total = 0
    for u in range(isqrt(n) + 1):
        v = np.arange(-u, u + 1, dtype=np.int64)
        offset = v * (v - 1)
        room = 2 * n - u * (u + 1) - offset
        stop = np.searchsorted(bounds, room, side="right")
        start = np.where(u * (u - 1) + offset == 0, max(u, 2), u)
        start = np.minimum(start, stop)
        terms = (stop - start) * (u * u + v * v)
        total += 2 * int(np.sum(terms + squares[stop] - squares[start]))

    return total % 433494437


if __name__ == "__main__":
    print(solve())
