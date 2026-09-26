# Problem 637: https://projecteuler.net/problem=637

from itertools import combinations

import numpy as np


def depths(limit, base):
    digit_sum = np.zeros(limit + 1, dtype=np.uint8)
    powers = [1]
    while powers[-1] <= limit:
        place = powers[-1]
        for digit in range(1, base):
            start = digit * place
            if start > limit:
                break
            end = min(start + place, limit + 1)
            digit_sum[start:end] = digit_sum[:end - start] + digit
        powers.append(place * base)

    steps = np.full(limit + 1, 2, dtype=np.uint8)
    steps[digit_sum < base] = 1
    steps[:base] = 0
    remaining = np.flatnonzero(
        np.logical_and(digit_sum >= base, digit_sum[digit_sum] >= base)
    )

    length = len(powers) - 1
    patterns = []
    for k in range(length):
        for cuts in combinations(range(1, length), k):
            edges = (0,) + cuts + (length,)
            spans = tuple((a, b - a) for a, b in zip(edges, edges[1:]))
            patterns.append(spans)
    patterns.sort(key=lambda spans: (max(w for a, w in spans), len(spans)))

    for spans in patterns:
        if not remaining.size:
            break
        sums = digit_sum[remaining].astype(np.int64)
        for a, w in spans:
            if w > 1:
                block = remaining // powers[a] % powers[w]
                sums += block - digit_sum[block]
        remaining = remaining[digit_sum[sums] >= base]
    steps[remaining] = 3
    return steps


def solve(limit=10**7):
    decimal = depths(limit, 10)
    ternary = depths(limit, 3)
    return int(np.flatnonzero(decimal == ternary).sum())


if __name__ == "__main__":
    print(solve())
