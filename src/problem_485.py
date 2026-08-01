# Problem 485: https://projecteuler.net/problem=485
import math

import numpy as np

U = 100_000_000
K = 100_000


def divisor_counts(u):
    d = np.zeros(u + 1, dtype=np.uint16)
    s = math.isqrt(u)
    for i in range(1, s + 1):
        d[i * i] += 1
        start = i * (i + 1)
        if start <= u:
            d[start::i] += 2
    return d


def window_max_sum(arr, k):
    n = len(arr)
    j = int(math.floor(math.log2(k)))
    span = 1
    for _ in range(j):
        span *= 2

    cur = arr.copy()
    step = 1
    while step < span:
        right = cur[step : step + (n - step)].copy()
        np.maximum(cur[: n - step], right, out=cur[: n - step])
        step *= 2

    m1 = cur[: n - k + 1]
    m2 = cur[k - span : k - span + (n - k + 1)]
    return int(np.maximum(m1, m2).sum())


def solve():
    d = divisor_counts(U)
    return window_max_sum(d[1:], K)


if __name__ == "__main__":
    print(solve())
