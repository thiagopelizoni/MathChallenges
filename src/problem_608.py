# Problem 608: https://projecteuler.net/problem=608

from math import factorial, isqrt

import numpy as np
from sympy import factorint


def solve(m=200, n=10**12):
    mod = 10**9 + 7
    lim = isqrt(n)
    small = np.arange(lim + 1, dtype=np.int64)
    i = small[1:]
    low = small.copy()
    high = n // i % mod
    scale = 1

    for p, e in factorint(factorial(m)).items():
        c = e * pow(e + 2, -1, mod) % mod
        scale = scale * ((e + 1) * (e + 2) // 2) % mod
        q = n // (p * i)
        count = min(lim, n // (p * (lim + 1)))
        values = low[np.minimum(q, lim)]
        values[:count] = high[p * i[:count] - 1]
        high = (high - c * values) % mod
        low = (low - c * low[small // p]) % mod

    total = int(((low[1:] - low[:-1]) * (n // i % mod) % mod).sum())
    total += int(high.sum()) - lim * int(low[-1])
    return scale * (total % mod) % mod


if __name__ == "__main__":
    print(solve())
