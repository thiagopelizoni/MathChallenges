# Problem 332: https://projecteuler.net/problem=332

from math import fsum, isqrt

import numpy as np


TRIU = {}


def points(r):
    pts = []
    rr = r * r

    for x in range(-r, r + 1):
        x2 = x * x

        for y in range(-r, r + 1):
            z2 = rr - x2 - y * y
            if z2 < 0:
                continue

            z = isqrt(z2)
            if z * z == z2:
                pts.append((x, y, z))
                if z:
                    pts.append((x, y, -z))

    return np.array(pts, dtype=np.int64)


def triu_indices(n):
    idx = TRIU.get(n)
    if idx is None:
        idx = np.triu_indices(n, 1)
        TRIU[n] = idx
    return idx


def area(r):
    p = points(r)
    n = len(p)
    rr = r * r
    g = p @ p.T
    best = float("inf")

    for i in range(n - 2):
        rest = p[i + 1 :]
        rows, cols = triu_indices(n - i - 1)

        det = np.abs((np.cross(p[i], rest) @ rest.T)[rows, cols])
        mask = det != 0
        if not np.any(mask):
            continue

        da = g[i, i + 1 :]
        den = (r * (rr + da[:, None] + g[i + 1 :, i + 1 :] + da[None, :]))[
            rows, cols
        ]
        vals = 2 * rr * np.arctan2(
            det[mask].astype(np.float64),
            den[mask].astype(np.float64),
        )
        best = min(best, float(vals.min()))

    return best


def solve():
    return f"{fsum(area(r) for r in range(1, 51)):.6f}"


if __name__ == "__main__":
    print(solve())
