# Problem 564: https://projecteuler.net/problem=564
from math import comb, factorial, fsum, pi

import numpy as np
from sympy.utilities.iterables import partitions


def expected_area(n):
    records = list(partitions(n - 3))
    counts = np.zeros((len(records), n - 2), dtype=np.float64)
    weights = np.empty(len(records), dtype=np.float64)
    longest = np.empty(len(records), dtype=np.int64)
    fact = factorial(n)

    for row, part in enumerate(records):
        used = sum(part.values())
        counts[row, 0] = n - used
        divisor = factorial(n - used)
        top = 1
        for extra, amount in part.items():
            counts[row, extra] = amount
            divisor *= factorial(amount)
            top = max(top, extra + 1)
        weights[row] = fact // divisor
        longest[row] = top

    sides = np.arange(1, n - 1, dtype=np.float64)
    rows = np.arange(len(records))
    high = 1.0 / longest
    ratios = np.minimum(sides / longest[:, None], 1)
    total = np.sum(counts * np.arcsin(ratios), axis=1)
    inside = total >= pi
    low = np.zeros_like(high)

    while np.any(high - low > np.spacing(high)):
        middle = (low + high) / 2
        ratios = np.minimum(sides * middle[:, None], 1)
        angles = np.arcsin(ratios)
        total = np.sum(counts * angles, axis=1)
        equation = np.where(inside, total - pi, 2 * angles[rows, longest - 1] - total)
        positive = equation >= 0
        high = np.where(positive, middle, high)
        low = np.where(positive, low, middle)

    t = (low + high) / 2
    ratios = np.minimum(sides * t[:, None], 1)
    triangles = sides * np.sqrt(1 - ratios * ratios) / (4 * t[:, None])
    areas = np.sum(counts * triangles, axis=1)
    areas = np.where(inside, areas, areas - 2 * triangles[rows, longest - 1])

    weighted = fsum(areas * weights)
    return weighted / comb(2 * n - 4, n - 1)


def solve():
    return f"{fsum(expected_area(n) for n in range(3, 51)):.6f}"


if __name__ == "__main__":
    print(solve())
