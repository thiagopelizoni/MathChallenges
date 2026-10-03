# Problem 654: https://projecteuler.net/problem=654

from math import comb

import numpy as np
from sympy.discrete.convolutions import convolution_int


def solve(n=5000, m=10**12):
    mod = 1_000_000_007
    d = n - 1
    values = []
    v = np.ones(d, dtype=np.int64)
    if m % 2:
        v = np.cumsum(v)[::-1] % mod

    for _ in range(d):
        v = np.cumsum(v)[::-1] % mod
        values.append(int(v.sum() % mod))
        v = np.cumsum(v)[::-1] % mod

    q = [(-1) ** k * comb(d + k, 2 * k) % mod for k in range(d + 1)]
    p = [value % mod for value in convolution_int(values, q)[:d]]
    index = (m - 2) // 2

    while index:
        negative = [value if k % 2 == 0 else -value for k, value in enumerate(q)]
        numerator = convolution_int(p, negative)
        denominator = convolution_int(q, negative)
        p = [value % mod for value in numerator[index % 2::2]]
        q = [value % mod for value in denominator[::2]]
        index //= 2

    return p[0]


if __name__ == "__main__":
    print(solve())
