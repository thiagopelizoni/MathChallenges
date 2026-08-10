# Problem 521: https://projecteuler.net/problem=521

from math import isqrt

import numpy as np

N = 10**12
MOD = 10**9


def solve():
    r = isqrt(N)
    high = N // np.arange(1, r + 1, dtype=np.int64)
    cutoff = int(high[-1])
    values = np.concatenate((high, np.arange(cutoff - 1, 0, -1, dtype=np.int64)))
    size = len(values)

    counts = values - 1
    even = values % 2 == 0
    a = np.where(even, values // 2, values) % MOD
    b = np.where(even, values + 1, (values + 1) // 2) % MOD
    sums = (a * b - 1) % MOD

    total = 0
    for p in range(2, r + 1):
        ip = size - p
        before = ip + 1
        if counts[ip] == counts[before]:
            continue

        total = (total + p * (counts[p - 1] - counts[before])) % MOD
        square = p * p
        limit = size - square + 1 if square <= cutoff else N // square
        q = values[:limit] // p
        indices = np.where(q <= cutoff, size - q, N // q - 1)
        counts[:limit] -= counts[indices] - counts[before]
        sums[:limit] = (sums[:limit] - p * ((sums[indices] - sums[before]) % MOD)) % MOD

    return int((total + sums[0]) % MOD)


if __name__ == "__main__":
    print(solve())
