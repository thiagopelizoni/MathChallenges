# Problem 163: https://projecteuler.net/problem=163
from collections import defaultdict
from itertools import combinations
from math import gcd

SCALE = 18


def normalized(dx, dy):
    g = gcd(abs(dx), abs(dy))
    dx //= g
    dy //= g
    if dx < 0 or (dx == 0 and dy < 0):
        dx = -dx
        dy = -dy
    return dx, dy


def cross(d, p):
    return d[0] * p[1] - d[1] * p[0]


def dot(d, p):
    return d[0] * p[0] + d[1] * p[1]


def intersection(d1, c1, d2, c2):
    den = d1[0] * d2[1] - d1[1] * d2[0]
    x = c1 * d2[0] - d1[0] * c2
    y = c1 * d2[1] - d1[1] * c2
    return x // den, y // den


def build_lines(n):
    lines = defaultdict(lambda: defaultdict(list))

    def add(p, q):
        d = normalized(q[0] - p[0], q[1] - p[1])
        c = cross(d, p)
        a, b = sorted((dot(d, p), dot(d, q)))
        lines[d][c].append((a, b))

    def add_triangle(a, b, c):
        add(a, b)
        add(a, c)
        add(b, c)
        add(a, ((b[0] + c[0]) // 2, (b[1] + c[1]) // 2))
        add(b, ((a[0] + c[0]) // 2, (a[1] + c[1]) // 2))
        add(c, ((a[0] + b[0]) // 2, (a[1] + b[1]) // 2))

    for i in range(n):
        for j in range(n - i):
            add_triangle(
                (SCALE * i, SCALE * j),
                (SCALE * (i + 1), SCALE * j),
                (SCALE * i, SCALE * (j + 1)),
            )
    for i in range(n - 1):
        for j in range(n - 1 - i):
            add_triangle(
                (SCALE * (i + 1), SCALE * j),
                (SCALE * i, SCALE * (j + 1)),
                (SCALE * (i + 1), SCALE * (j + 1)),
            )

    for by_c in lines.values():
        for c, intervals in by_c.items():
            intervals.sort()
            merged = []
            for a, b in intervals:
                if merged and a <= merged[-1][1]:
                    if b > merged[-1][1]:
                        merged[-1] = (merged[-1][0], b)
                else:
                    merged.append((a, b))
            by_c[c] = merged
    return lines


def count_triangles(n):
    lines = build_lines(n)

    def covered(d, p, q):
        c = cross(d, p)
        a, b = sorted((dot(d, p), dot(d, q)))
        for x, y in lines[d].get(c, ()):
            if x <= a and b <= y:
                return True
            if x > a:
                return False
        return False

    total = 0
    for d1, d2, d3 in combinations(lines, 3):
        for c1 in lines[d1]:
            for c2 in lines[d2]:
                p12 = intersection(d1, c1, d2, c2)
                for c3 in lines[d3]:
                    p13 = intersection(d1, c1, d3, c3)
                    p23 = intersection(d2, c2, d3, c3)
                    if p12 == p13 or p12 == p23 or p13 == p23:
                        continue
                    if (
                        covered(d1, p12, p13)
                        and covered(d2, p12, p23)
                        and covered(d3, p13, p23)
                    ):
                        total += 1
    return total


def solve():
    return count_triangles(36)


if __name__ == "__main__":
    print(solve())
