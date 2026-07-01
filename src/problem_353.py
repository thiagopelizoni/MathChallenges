# Problem 353: https://projecteuler.net/problem=353

from collections import defaultdict
from functools import cache
from heapq import heappop, heappush
from math import acos, ceil, inf, isqrt, pi, sqrt

from sympy import factorint, sqrt_mod


NEIGHBOR_FACTOR = 3.0


def gmul(z, w):
    a, b = z
    c, d = w
    return (a * c - b * d, a * d + b * c)


def gpow(z, e):
    out = (1, 0)

    for _ in range(e):
        out = gmul(out, z)

    return out


@cache
def prime_square_sum(p):
    if p == 2:
        return (1, 1)

    a, b = p, min(sqrt_mod(p - 1, p, all_roots=True))
    while b * b > p:
        a, b = b, a % b

    y = isqrt(p - b * b)
    return (b, y)


@cache
def two_square_pairs(n):
    if n == 0:
        return ((0, 0),)

    scale = 1
    choices = [(1, 0)]

    for p, e in factorint(n).items():
        if p % 4 == 3:
            if e % 2:
                return ()
            scale *= p ** (e // 2)
        elif p == 2:
            z = gpow((1, 1), e)
            choices = [gmul(w, z) for w in choices]
        else:
            z = prime_square_sum(p)
            conjugate = (z[0], -z[1])
            factors = [
                gmul(gpow(z, k), gpow(conjugate, e - k)) for k in range(e + 1)
            ]
            choices = [gmul(w, v) for w in choices for v in factors]

    pairs = set()
    for a, b in choices:
        a, b = abs(a * scale), abs(b * scale)
        if a < b:
            a, b = b, a
        pairs.add((a, b))

    return tuple(pairs)


def signed_pairs(a, b):
    out = set()

    for x, y in ((a, b), (b, a)):
        xs = (0,) if x == 0 else (-x, x)
        ys = (0,) if y == 0 else (-y, y)
        for sx in xs:
            for sy in ys:
                out.add((sx, sy))

    return out


@cache
def sphere_points(r):
    rr = r * r
    points = []

    for z in range(-r, r + 1):
        for a, b in two_square_pairs(rr - z * z):
            for x, y in signed_pairs(a, b):
                points.append((x, y, z))

    return tuple(dict.fromkeys(points))


def cells(points, cell):
    grid = defaultdict(list)

    for i, (x, y, z) in enumerate(points):
        grid[(x // cell, y // cell, z // cell)].append(i)

    return grid


def risk(r):
    points = sphere_points(r)
    n = len(points)
    rr = r * r
    start = points.index((0, 0, r))
    target = points.index((0, 0, -r))
    spacing = sqrt(4.0 * pi * r * r / n)
    radius = min(2.0 * r, max(2.0, NEIGHBOR_FACTOR * spacing))
    cell = max(1, int(radius))
    delta = ceil(radius / cell)
    radius2 = radius * radius
    grid = cells(points, cell)
    dist = [inf] * n
    seen = [False] * n
    dist[start] = 0.0
    heap = [(0.0, start)]

    while heap:
        du, u = heappop(heap)
        if seen[u]:
            continue
        if u == target:
            return du

        seen[u] = True
        ux, uy, uz = points[u]
        cx, cy, cz = ux // cell, uy // cell, uz // cell

        for dx in range(-delta, delta + 1):
            for dy in range(-delta, delta + 1):
                for dz in range(-delta, delta + 1):
                    for v in grid.get((cx + dx, cy + dy, cz + dz), ()):
                        if seen[v] or v == u:
                            continue

                        x, y, z = points[v]
                        d2 = (ux - x) ** 2 + (uy - y) ** 2 + (uz - z) ** 2
                        if d2 > radius2:
                            continue

                        dot = ux * x + uy * y + uz * z
                        a = acos(max(-1.0, min(1.0, dot / rr))) / pi
                        nd = du + a * a
                        if nd < dist[v]:
                            dist[v] = nd
                            heappush(heap, (nd, v))


def solve():
    total = sum(risk(2**n - 1) for n in range(1, 16))
    return f"{total:.10f}"


if __name__ == "__main__":
    print(solve())
