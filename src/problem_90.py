# Problem 90: https://projecteuler.net/problem=90

from itertools import combinations


def can_show(cube, d):
    return d in cube or (d in (6, 9) and (6 in cube or 9 in cube))


def solve():
    squares = [(0, 1), (0, 4), (0, 9), (1, 6), (2, 5), (3, 6), (4, 9), (6, 4), (8, 1)]
    cubes = list(combinations(range(10), 6))
    total = 0

    for i, a in enumerate(cubes):
        for b in cubes[i:]:
            if all(
                can_show(a, x) and can_show(b, y)
                or can_show(a, y) and can_show(b, x)
                for x, y in squares
            ):
                total += 1

    return total


if __name__ == "__main__":
    print(solve())
