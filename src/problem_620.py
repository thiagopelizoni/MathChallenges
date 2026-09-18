# Problem 620: https://projecteuler.net/problem=620

import numpy as np


def solve(n=500):
    total = 0
    for s in range(5, n):
        for p in range(5, (n - s - 1) // 2 + 1):
            q = np.arange(p + 1, n - s - p + 1, dtype=np.float64)
            a = s + q
            b = s + p
            d = p + q - 2 * np.pi
            alpha = np.arccos((d * d + a * a - b * b) / (2 * d * a))
            beta = np.arccos((a * a - b * b - d * d) / (2 * d * b))
            total += int(np.floor((a * alpha + b * beta) / np.pi).sum())
    return total


if __name__ == "__main__":
    print(solve())
