# Problem 430: https://projecteuler.net/problem=430

import numpy as np


N = 10_000_000_000
TURNS = 4_000
CUTOFF = 30_000_000
CHUNK = 1_000_000


def solve():
    total = 0.0
    denominator = float(N * N)

    # Position i is flipped by 2*i*(N + 1 - i) - 1 ordered pairs.
    # Symmetry supplies the matching contribution from the other end.
    for start in range(1, CUTOFF + 1, CHUNK):
        stop = min(start + CHUNK, CUTOFF + 1)
        positions = np.arange(start, stop, dtype=np.float64)
        flip_probability = (
            2.0 * positions * (N + 1.0 - positions) - 1.0
        ) / denominator
        total += float(
            np.sum(np.power(1.0 - 2.0 * flip_probability, TURNS))
        )

    # Beyond the cutoff, the omitted geometric tail is less than 0.00005.
    return f"{N / 2.0 + total:.2f}"


if __name__ == "__main__":
    print(solve())
