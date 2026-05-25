# Problem 255: https://projecteuler.net/problem=255
from decimal import Decimal, getcontext

import numpy as np


DIGITS = 14


def next_values(x, n):
    return (x + (n + x - 1) // x) // 2


def solve():
    lo = 10 ** (DIGITS - 1)
    hi = 10**DIGITS - 1
    x0 = 7 * 10 ** ((DIGITS - 2) // 2)

    a = np.array([lo], dtype=np.int64)
    b = np.array([hi], dtype=np.int64)
    x = np.array([x0], dtype=np.int64)
    total = 0
    k = 0

    while a.size:
        k += 1
        ya = next_values(x, a)
        yb = next_values(x, b)
        cnt = yb - ya + 1
        na = []
        nb = []
        nx = []

        if a.size == 1 and cnt[0] > 1000:
            y = np.arange(int(ya[0]), int(yb[0]) + 1, dtype=np.int64)
            xx = x[0]
            l = np.maximum(a[0], (2 * y - xx - 1) * xx + 1)
            r = np.minimum(b[0], (2 * y + 1 - xx) * xx)
            fixed = y == xx
            total += k * int((r[fixed] - l[fixed] + 1).sum())
            keep = ~fixed
            a = l[keep]
            b = r[keep]
            x = y[keep]
            continue

        for off in range(int(cnt.max())):
            m = cnt > off
            y = ya[m] + off
            xx = x[m]
            l = np.maximum(a[m], (2 * y - xx - 1) * xx + 1)
            r = np.minimum(b[m], (2 * y + 1 - xx) * xx)
            fixed = y == xx

            if fixed.any():
                total += k * int((r[fixed] - l[fixed] + 1).sum())

            keep = ~fixed
            if keep.any():
                na.append(l[keep])
                nb.append(r[keep])
                nx.append(y[keep])

        if na:
            a = np.concatenate(na)
            b = np.concatenate(nb)
            x = np.concatenate(nx)
        else:
            a = np.array([], dtype=np.int64)
            b = a
            x = a

    getcontext().prec = 30
    return f"{Decimal(total) / Decimal(hi - lo + 1):.10f}"


if __name__ == "__main__":
    print(solve())
