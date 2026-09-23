# Problem 630: https://projecteuler.net/problem=630

import numpy as np


def solve(n=2500):
    s = 290797
    points = []
    for _ in range(n):
        s = s * s % 50515093
        x = s % 2000 - 1000
        s = s * s % 50515093
        y = s % 2000 - 1000
        points.append((x, y))

    points = np.array(sorted(set(points)), dtype=np.int64)
    n = len(points)
    lines = np.empty((n * (n - 1) // 2, 3), dtype=np.int64)
    start = 0

    for i, (x, y) in enumerate(points[:-1]):
        dx = points[i + 1:, 0] - x
        dy = points[i + 1:, 1] - y
        d = np.gcd(dx, dy)
        dx //= d
        dy //= d
        stop = start + len(dx)
        lines[start:stop, 0] = dx
        lines[start:stop, 1] = dy
        lines[start:stop, 2] = dx * y - dy * x
        start = stop

    lines = np.unique(lines, axis=0)
    _, counts = np.unique(lines[:, :2], axis=0, return_counts=True)
    return len(lines) ** 2 - int(np.sum(counts * counts))


if __name__ == "__main__":
    print(solve())
