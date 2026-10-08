# Problem 663: https://projecteuler.net/problem=663

from math import isqrt

import numpy as np


def summarize(block):
    sums = np.cumsum(block)
    minima = np.minimum.accumulate(np.r_[0, sums[:-1]])
    return sums[-1], sums.max(), sums[-1] - minima[-1], (sums - minima).max()


def solve(n=10_000_003, start=10_000_000, stop=10_200_000):
    values = np.zeros(n, dtype=np.int64)
    a, b, c = 0, 0, 1 % n
    for _ in range(start):
        values[a] += 2 * b - n + 1
        a, b, c = c, (a + b + c) % n, (a + 2 * b + 2 * c) % n

    size = isqrt(n)
    blocks = np.array([summarize(values[i:i + size]) for i in range(0, n, size)])
    answer = 0

    for _ in range(start, stop):
        values[a] += 2 * b - n + 1
        index = a // size
        left = index * size
        blocks[index] = summarize(values[left:left + size])
        best = int(blocks[:, 3].max())
        if len(blocks) > 1:
            ends = np.cumsum(blocks[:, 0])
            minima = np.minimum.accumulate(ends[:-1] - blocks[:-1, 2])
            best = max(best, int((ends[:-1] + blocks[1:, 1] - minima).max()))
        answer += best
        a, b, c = c, (a + b + c) % n, (a + 2 * b + 2 * c) % n

    return answer


if __name__ == "__main__":
    print(solve())
