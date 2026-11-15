# Problem 748: https://projecteuler.net/problem=748

from math import isqrt

import numpy as np


def solve(limit=10**16):
    mod = 10**9
    cmax = isqrt(isqrt(2 * limit * limit // 13))
    total = 0
    for m in range(1, isqrt(26 * cmax) + 1):
        lo = 5 * m - isqrt(26 * m * m)
        hi = (isqrt(13 * m * m) - 3 * m) // 2
        step = 1
        if m * m > 2 * cmax:
            step = 13
            residue = -3 * m * pow(2, -1, 13) % 13
            lo += (residue - lo) % 13
        n = np.arange(lo, hi + 1, step, dtype=np.int64)
        n = n[np.gcd(m, n) == 1]
        a = 2 * (m * m - n * n) - 6 * m * n
        b = 3 * (m * m - n * n) + 4 * m * n
        c = m * m + n * n
        d = np.gcd(np.gcd(a, b), c)
        a, b, c = a // d, b // d, c // d
        valid = c <= cmax
        a, b, c = a[valid], b[valid], c[valid]
        x, y, z = a * c, b * c, a * b
        valid = np.logical_and(y <= limit, z <= limit)
        total += int(np.sum((x[valid] + y[valid] + z[valid]) % mod))
    return total % mod


if __name__ == "__main__":
    print(solve())
