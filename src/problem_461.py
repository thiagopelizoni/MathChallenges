# Problem 461: https://projecteuler.net/problem=461

from math import log1p, pi

import numpy as np


N = 10_000
CHUNK_SIZE = 1_000_000


def make_pair_sums(values):
    limits = np.searchsorted(values, pi - values, side="right")
    starts = np.arange(len(values))
    counts = np.maximum(limits - starts, 0)
    pairs = np.empty(int(np.sum(counts)), dtype=np.float64)

    offset = 0
    for i, limit in enumerate(limits):
        size = max(0, int(limit) - i)
        if size:
            pairs[offset : offset + size] = values[i] + values[i:limit]
            offset += size
    pairs.sort()
    return pairs


def closest_pair_sums(pairs):
    stop = int(np.searchsorted(pairs, pi / 2, side="right"))
    best_error = pi
    best = (0.0, 0.0)

    for start in range(0, stop, CHUNK_SIZE):
        left = pairs[start : min(start + CHUNK_SIZE, stop)]
        positions = np.searchsorted(pairs, pi - left)
        for indices in (
            np.minimum(positions, len(pairs) - 1),
            np.maximum(positions - 1, 0),
        ):
            errors = np.abs(left + pairs[indices] - pi)
            index = int(np.argmin(errors))
            if errors[index] < best_error:
                best_error = float(errors[index])
                best = float(left[index]), float(pairs[indices[index]])
    return best


def recover_indices(values, target):
    for i, value in enumerate(values):
        position = int(np.searchsorted(values, target - value))
        for j in range(max(i, position - 1), min(position + 2, len(values))):
            if value + values[j] == target:
                return i, j


def solve(n=N):
    maximum = int(n * log1p(pi))
    values = np.expm1(np.arange(maximum + 1, dtype=np.float64) / n)
    pairs = make_pair_sums(values)
    left, right = closest_pair_sums(pairs)
    indices = recover_indices(values, left) + recover_indices(values, right)
    return sum(index * index for index in indices)


if __name__ == "__main__":
    print(solve())
