# Problem 718: https://projecteuler.net/problem=718

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra


def solve(p=6):
    a, b, c = 17**p, 19**p, 23**p
    mod = 1_000_000_007
    residues = np.arange(a, dtype=np.int32)
    cols = np.empty(2 * a, dtype=np.int32)
    cols[0::2] = (residues + b) % a
    cols[1::2] = (residues + c) % a
    weights = np.empty(2 * a)
    weights[0::2] = b
    weights[1::2] = c
    rows = np.arange(0, 2 * a + 1, 2, dtype=np.int32)
    graph = csr_matrix((weights, cols, rows), shape=(a, a))
    distances = dijkstra(graph, directed=True, indices=0)

    total = 0
    for d in distances:
        q, r = divmod(int(d) + a + b + c, a)
        total += q * r + a * q * (q - 1) // 2
    return total % mod


if __name__ == "__main__":
    print(solve())
