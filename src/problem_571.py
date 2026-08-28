# Problem 571: https://projecteuler.net/problem=571
from itertools import permutations

import numpy as np


def pandigital(values, base):
    work = values.copy()
    seen = np.zeros((len(values), base), dtype=bool)
    rows = np.arange(len(values))

    while np.any(work):
        active = work > 0
        digits = work % base
        seen[rows[active], digits[active]] = True
        work //= base

    return values[np.all(seen, axis=1)]


def solve():
    base = 12
    wanted = 10
    tail_size = 8
    prefix_size = base - tail_size
    tail_orders = np.array(list(permutations(range(tail_size))), dtype=np.int8)
    weights = base ** np.arange(tail_size - 1, -1, -1, dtype=np.int64)
    place = base**tail_size
    found = []

    for prefix in permutations(range(base), prefix_size):
        if prefix[0] == 0:
            continue

        remaining = np.array([d for d in range(base) if d not in prefix], dtype=np.int64)
        prefix_value = 0
        for digit in prefix:
            prefix_value = prefix_value * base + digit

        values = prefix_value * place + remaining[tail_orders].dot(weights)
        for lower_base in range(base - 1, 1, -1):
            values = pandigital(values, lower_base)
            if not len(values):
                break

        found.extend(map(int, values[: wanted - len(found)]))
        if len(found) == wanted:
            return sum(found)


if __name__ == "__main__":
    print(solve())
