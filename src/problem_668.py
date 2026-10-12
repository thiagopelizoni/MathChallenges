# Problem 668: https://projecteuler.net/problem=668
from math import isqrt

import numpy as np
from sympy import primerange


def solve(N=10**10):
    r = isqrt(N)
    small = np.arange(r + 1, dtype=np.int64) - 1
    small[0] = 0
    large = np.zeros(r + 1, dtype=np.int64)
    large[1:] = N // np.arange(1, r + 1, dtype=np.int64) - 1

    for p in range(2, r + 1):
        if small[p] == small[p - 1]:
            continue
        sp = small[p - 1]
        p2 = p * p
        m = min(r, N // p2)
        i = np.arange(1, m + 1, dtype=np.int64)
        d = i * p
        sub = np.where(d <= r, large[np.minimum(d, r)], small[N // np.maximum(d, r + 1)])
        large[1:m + 1] -= sub - sp
        if p2 <= r:
            v = np.arange(p2, r + 1)
            small[p2:] -= small[v // p] - sp

    bad = sum(primerange(2, r + 1))
    k = 1
    while N // k > r:
        bad += int(large[k] - small[r])
        k += 1
    return N - bad


if __name__ == "__main__":
    print(solve())
