# Problem 640: https://projecteuler.net/problem=640

from itertools import combinations_with_replacement

import numpy as np
from scipy.sparse import csr_matrix, eye
from scipy.sparse.linalg import spsolve


def solve(sides=6):
    cards = 2 * sides
    size = 2**cards
    states = np.arange(size)
    places = 2 ** np.arange(cards)
    up = states[:, None] // places % 2
    neighbors = states[:, None] + (1 - 2 * up) * places
    rolls = list(combinations_with_replacement(range(1, sides + 1), 2))
    options = np.array([(x - 1, y - 1, x + y - 1) for x, y in rolls])
    probabilities = np.array([1 if x == y else 2 for x, y in rolls]) / sides**2
    targets = neighbors[:, options]
    rows = np.repeat(states[1:], len(rolls))
    data = np.tile(probabilities, size - 1)
    rhs = np.ones(size)
    rhs[0] = 0
    values = up.sum(axis=1).astype(float)

    while True:
        actions = values[targets].argmin(axis=2)
        chosen = np.take_along_axis(targets, actions[:, :, None], axis=2)[:, :, 0]
        transition = csr_matrix((data, (rows, chosen[1:].ravel())), shape=(size, size))
        values = spsolve(eye(size, format="csr") - transition, rhs)
        best = 1 + values[targets[1:]].min(axis=2) @ probabilities
        residual = np.max(np.abs(values[1:] - best))
        if residual < 1:
            lower = f"{values[-1] / (1 + residual):.6f}"
            upper = f"{values[-1] / (1 - residual):.6f}"
            if lower == upper:
                return lower


if __name__ == "__main__":
    print(solve())
