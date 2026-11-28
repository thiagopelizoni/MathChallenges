# Problem 814: https://projecteuler.net/problem=814

from itertools import product

import numpy as np


def solve(n=10**3):
    mod = 998244353
    states = list(product("LRO", repeat=2))
    transitions = []
    for i, (a, b) in enumerate(states):
        for j, (c, d) in enumerate(states):
            pairs = int(c == d == "O")
            pairs += a == "R" and c == "L"
            pairs += b == "R" and d == "L"
            transitions.append((i, j, pairs))

    size = len(states)
    paths = np.zeros((size, size, n + 1), dtype=np.int64)
    paths[:, :, 0] = np.eye(size, dtype=np.int64)
    for _ in range(2 * n):
        following = np.zeros_like(paths)
        for i, j, pairs in transitions:
            following[j, :, pairs:] += paths[i, :, :n + 1 - pairs]
        paths = following % mod

    total = 0
    for i, (a, b) in enumerate(states):
        j = states.index((b, a))
        total += paths[j, i, n]
    return int(total % mod)


if __name__ == "__main__":
    print(solve())
