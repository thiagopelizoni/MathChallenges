# Problem 460: https://projecteuler.net/problem=460

from math import isqrt, sqrt

import numpy as np


DISTANCE = 10_000
BAND = 6


def fastest_time(distance):
    half = distance // 2
    points = {(0, y) for y in range(1, isqrt(distance) + 1)}
    for x in range(half + 1):
        height = round(sqrt(1 + distance * x - x * x))
        for y in range(max(1, height - BAND), height + BAND + 1):
            points.add((x, y))

    points = sorted(points, key=lambda point: (sum(point), point))
    x_values = np.array([point[0] for point in points], dtype=np.float64)
    y_values = np.array([point[1] for point in points], dtype=np.float64)
    times = np.full(len(points), np.inf)
    start = points.index((0, 1))
    times[start] = 0.0

    for i, (x, y) in enumerate(points):
        if i == start:
            continue
        dx = x - x_values[:i]
        dy = y - y_values[:i]
        costs = np.hypot(dx, dy)
        horizontal = dy == 0
        costs[horizontal] = dx[horizontal] / y
        diagonal = np.logical_not(horizontal)
        costs[diagonal] *= (
            np.log(y / y_values[:i][diagonal]) / dy[diagonal]
        )
        valid = np.logical_and(x_values[:i] <= x, y_values[:i] <= y)
        times[i] = np.min(np.where(valid, times[:i] + costs, np.inf))

    return 2 * min(
        times[i]
        for i, point in enumerate(points)
        if point[0] == half
    )


def solve():
    return f"{fastest_time(DISTANCE):.9f}"


if __name__ == "__main__":
    print(solve())
