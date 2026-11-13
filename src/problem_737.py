# Problem 737: https://projecteuler.net/problem=737

import numpy as np


def solve(loops=2020):
    target = 2 * np.pi * loops
    batch = loops**2
    start = 1
    h = 0.0
    angle = 0.0

    while True:
        n = np.arange(start, start + batch, dtype=float)
        harmonic = h + np.cumsum(1 / n)
        r = np.sqrt(n * harmonic)
        alpha = np.arccos(r / (2 * n))
        delta = np.arctan2(np.sin(alpha), r + np.cos(alpha))
        rotation = np.cumsum(delta)
        turns = angle + rotation - delta + alpha
        i = np.searchsorted(turns, target, side="right")
        if i < batch:
            return start + int(i) + 1
        h = harmonic[-1]
        angle += rotation[-1]
        start += batch


if __name__ == "__main__":
    print(solve())
