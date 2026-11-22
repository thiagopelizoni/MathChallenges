# Problem 782: https://projecteuler.net/problem=782

from itertools import combinations_with_replacement, product

import numpy as np


def solve(n=10**4):
    area = n * n
    seen = np.zeros(area + 1, dtype=bool)
    sizes = np.arange(n + 1)
    for k in (sizes**2, 2 * sizes * (n - sizes)):
        seen[k] = True
        seen[area - k] = True
    at_most_two = np.count_nonzero(seen)

    for a in range(1, n + 1):
        k = a * sizes
        seen[k] = True
        seen[area - k] = True

    pairs = tuple(combinations_with_replacement(range(3), 2))
    forms = set()
    for tail in product((0, 1), repeat=3**2 - 1):
        cells = (0,) + tail
        rows = tuple(cells[i:i + 3] for i in range(0, len(cells), 3))
        if len(set(rows).union(zip(*rows))) <= 3:
            weights = tuple(
                rows[i][i] if i == j else rows[i][j] + rows[j][i]
                for i, j in pairs
            )
            forms.add(weights)

    for a in range(n // 3 + 1):
        b = np.arange(a, (n - a) // 2 + 1)
        sizes = (a, b, n - a - b)
        terms = [sizes[i] * sizes[j] for i, j in pairs]
        for weights in forms:
            k = sum(w * term for w, term in zip(weights, terms) if w)
            seen[k] = True
            seen[area - k] = True

    return 4 * (area + 1) - np.count_nonzero(seen) - at_most_two - 2


if __name__ == "__main__":
    print(solve())
