# Problem 314: https://projecteuler.net/problem=314

from math import hypot


SIDE = 500
H = 128
STEPS = (
    (1, 11),
    (1, 7),
    (1, 5),
    (1, 4),
    (2, 7),
    (1, 3),
    (1, 3),
    (2, 5),
    (3, 7),
    (1, 2),
    (1, 2),
    (1, 2),
    (4, 7),
    (2, 3),
    (2, 3),
    (3, 4),
    (3, 4),
    (6, 7),
    (1, 1),
    (1, 1),
    (1, 1),
    (1, 1),
    (1, 1),
    (1, 1),
    (7, 6),
    (4, 3),
    (4, 3),
    (3, 2),
    (3, 2),
    (7, 4),
    (2, 1),
    (2, 1),
    (2, 1),
    (7, 3),
    (5, 2),
    (3, 1),
    (3, 1),
    (7, 2),
    (4, 1),
    (5, 1),
    (7, 1),
    (11, 1),
)


def corner():
    x = 0
    y = H
    area = 0
    length = 0

    for dx, dy in STEPS:
        nx = x + dx
        ny = y - dy
        area += (nx * y - x * ny) / 2
        length += hypot(dx, dy)
        x, y = nx, ny

    return area, length


def solve():
    cut, length = corner()
    area = SIDE * SIDE - 4 * cut
    perimeter = 4 * SIDE - 8 * H + 4 * length

    return f"{area / perimeter:.8f}"


if __name__ == "__main__":
    print(solve())
