# Problem 352: https://projecteuler.net/problem=352

import numpy as np


SIZE = 10_000


def expected_tests(size, p):
    q = 1.0 - p
    qpow = np.power(q, np.arange(size + 1, dtype=np.float64))
    unknown = np.zeros(size + 1)
    positive = np.zeros(size + 1)
    pooled = np.zeros(size + 1)
    unknown[1] = pooled[1] = 1.0

    for n in range(2, size + 1):
        nonempty = 1.0 - qpow[n]
        left_q = qpow[1:n]
        right_q = qpow[n - 1 : 0 : -1]
        pos = (1.0 - left_q) / nonempty
        neg = left_q * (1.0 - right_q) / nonempty

        positive[n] = (
            1.0
            + pos * (positive[1:n] + unknown[n - 1 : 0 : -1])
            + neg * positive[n - 1 : 0 : -1]
        ).min()
        pooled[n] = 1.0 + nonempty * positive[n]
        unknown[n] = (pooled[1 : n + 1] + unknown[n - 1 :: -1]).min()

    return unknown[size]


def solve():
    total = sum(expected_tests(SIZE, p / 100.0) for p in range(1, 51))
    return f"{total:.6f}"


if __name__ == "__main__":
    print(solve())
