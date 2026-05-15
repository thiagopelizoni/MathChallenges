# Problem 211: https://projecteuler.net/problem=211
from math import isqrt

import numpy as np


def sigma2(limit):
    sig = np.zeros(limit, dtype=np.uint64)
    block = 1_000_000

    for d in range(1, isqrt(limit - 1) + 1):
        d2 = d * d
        sig[d * d] += d2
        qmax = (limit - 1) // d

        for start in range(d + 1, qmax + 1, block):
            stop = min(qmax + 1, start + block)
            q = np.arange(start, stop, dtype=np.uint64)
            sig[d * q] += q * q + d2

    return sig


def solve():
    limit = 64_000_000
    sig = sigma2(limit)
    total = 0
    block = 1_000_000

    for start in range(1, limit, block):
        stop = min(limit, start + block)
        s = sig[start:stop]
        r = np.sqrt(s).astype(np.uint64)
        mask = (r * r == s) | ((r + 1) * (r + 1) == s)
        total += int(np.nonzero(mask)[0].sum() + start * int(mask.sum()))

    return total


if __name__ == "__main__":
    print(solve())
