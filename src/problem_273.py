# Problem 273: https://projecteuler.net/problem=273

from math import isqrt

import numpy as np


LIMIT = 150


def is_prime(n):
    for p in range(2, isqrt(n) + 1):
        if n % p == 0:
            return False
    return n > 1


def prime_rep(p):
    for a in range(1, isqrt(p) + 1):
        b = isqrt(p - a * a)
        if a * a + b * b == p:
            return a, b


def states(reps):
    out = []

    def search(i, a, b):
        if i == len(reps):
            out.append((a, b))
            return

        x, y = reps[i]
        search(i + 1, a, b)
        search(i + 1, a * x - b * y, a * y + b * x)
        search(i + 1, a * x + b * y, b * x - a * y)

    search(0, 1, 0)
    return np.array(out, dtype=np.int64)


def solve():
    reps = [prime_rep(p) for p in range(5, LIMIT, 4) if is_prime(p)]
    left = states(reps[:8])
    right = states(reps[8:])
    rr, ri = right[:, 0], right[:, 1]

    total = 0
    for a, b in left:
        re = a * rr - b * ri
        im = a * ri + b * rr
        total += int(np.minimum(np.abs(re), np.abs(im)).sum())

    return total // 2


if __name__ == "__main__":
    print(solve())
