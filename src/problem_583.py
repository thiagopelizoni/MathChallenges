# Problem 583: https://projecteuler.net/problem=583

from bisect import bisect_right
from math import gcd, isqrt

import numpy as np


def primitive_legs(bound):
    for m in range(2, isqrt(bound) + 2):
        for n in range(1, m):
            if (m - n) % 2 == 0 or gcd(m, n) != 1:
                continue
            a = m * m - n * n
            b = 2 * m * n
            if a + b < bound:
                yield a, b


def solve():
    limit = 10**7
    half = limit // 2
    xmax = half // 2
    size = 0

    for a, b in primitive_legs(half):
        perimeter = a + b
        size += min((half - 1) // perimeter, (xmax - 1) // a)
        size += min((half - 1) // perimeter, (xmax - 1) // b)

    pairs = np.empty(size, dtype=[("x", np.uint32), ("y", np.uint32)])
    pos = 0
    for a, b in primitive_legs(half):
        perimeter = a + b
        ka = min((half - 1) // perimeter, (xmax - 1) // a)
        for k in range(1, ka + 1):
            pairs[pos] = k * a, k * b
            pos += 1
        kb = min((half - 1) // perimeter, (xmax - 1) // b)
        for k in range(1, kb + 1):
            pairs[pos] = k * b, k * a
            pos += 1

    pairs.sort(order=("x", "y"))
    xs = pairs["x"]
    ends = np.flatnonzero(xs[1:] != xs[:-1]) + 1
    ends = np.append(ends, size)

    total = 0
    start = 0
    for end0 in ends:
        end = int(end0)
        if end - start > 1:
            x = int(xs[start])
            ys = pairs["y"][start:end].tolist()
            for t in ys:
                if 2 * t >= ys[-1]:
                    break
                l = isqrt(x * x + t * t)
                upper = half - x + t - l
                if upper <= 2 * t:
                    continue
                lo = bisect_right(ys, 2 * t)
                hi = bisect_right(ys, upper)
                for y in ys[lo:hi]:
                    h = y - t
                    q = 4 * x * x + h * h
                    if isqrt(q) ** 2 == q:
                        total += 2 * (x + h + l)
        start = end

    return total


if __name__ == "__main__":
    print(solve())
