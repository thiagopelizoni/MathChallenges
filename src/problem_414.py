# Problem 414: https://projecteuler.net/problem=414

import numpy as np
from scipy.sparse import csr_array
from scipy.sparse.csgraph import shortest_path


MOD = 10**18


def kaprekar_sum(b):
    x, y = np.tril_indices(b)
    x = x[1:].astype(np.int64, copy=False)
    y = y[1:].astype(np.int64, copy=False)
    gap = x - y
    mult = np.where(
        y == 0,
        20 * x - 10,
        np.where(gap == 0, 30 * y - 10, 120 * gap * y - 20),
    )
    weight = (b - x) * mult

    digits = np.stack(
        (
            np.where(y == 0, x - 1, x),
            np.where(y == 0, b - 1, y - 1),
            np.full(x.size, b - 1, dtype=np.int64),
            np.where(y == 0, b - 1, b - y - 1),
            b - x,
        )
    )
    digits.sort(axis=0)
    nx = digits[4] - digits[0]
    ny = digits[3] - digits[1]
    nxt = nx * (nx + 1) // 2 + ny - 1

    nodes = np.arange(x.size)
    reverse = csr_array(
        (np.ones(x.size, dtype=np.int8), (nxt, nodes)),
        shape=(x.size, x.size),
    )
    cx, cy = 2 * b // 3, b // 3
    root = cx * (cx + 1) // 2 + cy - 1
    dist = shortest_path(reverse, directed=True, indices=root, unweighted=True)
    return int(np.sum(weight * (dist.astype(np.int64) + 1), dtype=np.int64)) - 1


def solve():
    return sum(kaprekar_sum(6 * k + 3) for k in range(2, 301)) % MOD


if __name__ == "__main__":
    print(solve())
