# Problem 456: https://projecteuler.net/problem=456

import numpy as np


N = 2_000_000


def coordinates(multiplier, modulus, shift, n):
    value = 1
    for _ in range(n):
        value = value * multiplier % modulus
        yield value - shift


def choose_three(n):
    return n * (n - 1) * (n - 2) // 6


def count_triangles(n):
    x = np.fromiter(
        coordinates(1248, 32323, 16161, n),
        dtype=np.int64,
        count=n,
    )
    y = np.fromiter(
        coordinates(8421, 30103, 15051, n),
        dtype=np.int64,
        count=n,
    )
    keep = np.logical_or(x != 0, y != 0)
    x = x[keep]
    y = y[keep]
    size = x.size

    divisors = np.gcd(np.abs(x), np.abs(y))
    dx = x // divisors
    dy = y // divisors
    canonical = np.logical_or(
        dx > 0,
        np.logical_and(dx == 0, dy > 0),
    )
    line_x = np.where(canonical, dx, -dx)
    line_y = np.where(canonical, dy, -dy)
    keys = (line_x + 16161) * 40000 + line_y + 15051
    order = np.argsort(keys)
    keys = keys[order]
    sides = canonical[order].astype(np.int64)
    starts = np.r_[
        0,
        np.flatnonzero(keys[1:] != keys[:-1]) + 1,
    ]
    counts = np.diff(np.r_[starts, size])
    a = np.add.reduceat(sides, starts)
    b = counts - a
    total_on_line = a + b
    boundary = int(
        np.sum(
            a * b * (size - total_on_line)
            + choose_three(total_on_line)
            - choose_three(a)
            - choose_three(b),
            dtype=np.int64,
        )
    )

    angles = np.arctan2(y, x)
    order = np.argsort(angles)
    x = x[order]
    y = y[order]

    outside = 0
    j = 1
    for i in range(size):
        j = max(j, i + 1)
        xi = int(x[i])
        yi = int(y[i])
        while j < i + size:
            index = j if j < size else j - size
            xj = int(x[index])
            yj = int(y[index])
            cross = xi * yj - yi * xj
            dot = xi * xj + yi * yj
            if cross > 0 or cross == 0 and dot > 0:
                j += 1
            else:
                break
        count = j - i - 1
        outside += count * (count - 1) // 2

    return choose_three(size) - outside - boundary


def solve():
    return count_triangles(N)


if __name__ == "__main__":
    print(solve())
