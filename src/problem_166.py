# Problem 166: https://projecteuler.net/problem=166
from collections import Counter
from itertools import product


def rows_by_sum():
    rows = [[] for _ in range(37)]
    for row in product(range(10), repeat=4):
        rows[sum(row)].append(row)
    return rows


def solve():
    total = 0

    for s, rows in enumerate(rows_by_sum()):
        lower = Counter()
        for i, j, k, l in rows:
            for m, n, o, p in rows:
                lower[i + m, j + n, k + o, l + p, k + p, j + m] += 1

        for a, b, c, d in rows:
            for e, f, g, h in rows:
                total += lower[
                    s - a - e,
                    s - b - f,
                    s - c - g,
                    s - d - h,
                    s - a - f,
                    s - d - g,
                ]

    return total


if __name__ == "__main__":
    print(solve())
