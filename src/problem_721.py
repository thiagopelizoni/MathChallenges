# Problem 721: https://projecteuler.net/problem=721

from math import isqrt

import numpy as np


def solve(n=5_000_000):
    mod = 999_999_937
    total = 0
    for b in range(1, isqrt(n - 1) + 2):
        lo = (b - 1) ** 2 + 1
        hi = min(b * b, n)
        a = np.arange(lo, hi + 1, dtype=np.int64)
        e = a * a
        x = np.ones_like(a)
        y = np.zeros_like(a)
        place = 1
        while place <= hi * hi:
            place *= 2
        place //= 2
        while place:
            xx = (x * x + a * (y * y % mod)) % mod
            yy = 2 * x * y % mod
            odd = e // place % 2 != 0
            x = np.where(odd, (b * xx + a * yy) % mod, xx)
            y = np.where(odd, (xx + b * yy) % mod, yy)
            place //= 2
        total += int(np.sum((2 * x - (a != b * b)) % mod))
    return total % mod


if __name__ == "__main__":
    print(solve())
