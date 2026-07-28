# Problem 464: https://projecteuler.net/problem=464

import numpy as np
from scipy.stats._stats import _kendall_dis
from sympy import sieve


LIMIT = 20_000_000


def count_intervals(limit):
    mu = np.fromiter(
        sieve.mobiusrange(1, limit + 1),
        dtype=np.int8,
        count=limit,
    )
    mu_squared = mu * mu
    increments = (199 * mu.astype(np.int16) + mu_squared) // 2

    x = np.empty(limit + 1, dtype=np.int64)
    x[0] = 0
    np.cumsum(increments, dtype=np.int64, out=x[1:])
    y = np.empty(limit + 1, dtype=np.int64)
    y[0] = 0
    np.cumsum(mu_squared, dtype=np.int64, out=y[1:])
    y -= x
    del mu, mu_squared, increments

    order = np.lexsort((y, x))
    x_sorted = x[order]
    y_sorted = y[order]
    y_sorted -= y_sorted.min() - 1
    del x, y, order

    discordant = int(_kendall_dis(x_sorted, y_sorted))
    return limit * (limit + 1) // 2 - discordant


def solve():
    return count_intervals(LIMIT)


if __name__ == "__main__":
    print(solve())
