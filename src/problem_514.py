# Problem 514: https://projecteuler.net/problem=514

from math import gcd

import numpy as np

N = 100


def solve():
    n = N
    rho = 1 / (n + 1)
    emp = 1 - rho
    g = (n + 1) ** 2
    pe = np.empty(g + 1)
    pe[0] = 1.0
    for i in range(1, g + 1):
        pe[i] = pe[i - 1] * emp

    xs = np.arange(n + 1)
    ys = np.arange(n + 1)
    xx, yy = np.meshgrid(xs, ys, indexing="ij")
    xx = xx.ravel()
    yy = yy.ravel()

    fmax = 2 * n * n
    off = fmax
    size = 2 * fmax + 1
    total = 0.0

    for dx in range(-n, n + 1):
        for dy in range(-n, n + 1):
            if dx == 0 and dy == 0:
                continue
            mid = gcd(abs(dx), abs(dy)) - 1
            fvals = dx * yy - dy * xx
            cnt = np.bincount(fvals + off, minlength=size)
            less = np.cumsum(cnt) - cnt

            x0, x1 = max(0, -dx), min(n, n - dx)
            y0, y1 = max(0, -dy), min(n, n - dy)
            px = np.arange(x0, x1 + 1)
            py = np.arange(y0, y1 + 1)
            if px.size == 0 or py.size == 0:
                continue
            px, py = np.meshgrid(px, py, indexing="ij")
            px = px.ravel()
            py = py.ravel()
            det = px * dy - py * dx
            keep = det != 0
            if not np.any(keep):
                continue
            det = det[keep]
            fp = dx * py[keep] - dy * px[keep]
            r = less[fp + off]
            total += float(np.dot(det.astype(float), pe[r + mid]))

    return f"{0.5 * rho * rho * total:.5f}"


if __name__ == "__main__":
    print(solve())
