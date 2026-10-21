# Problem 682: https://projecteuler.net/problem=682
from math import lcm

import numpy as np
from sympy import interpolate


def f(n):
    total = 0
    for k in range(n // 4 + 1):
        m = n - 4 * k
        h = np.zeros(m + 1, dtype=np.int64)
        for c in range(min(k, m // 3) + 1):
            h[3 * c:min(2 * c + k, m) + 1] += 1
        total += int(np.dot(h, h[::-1]))
    return total


def solve(n=10**7):
    period = lcm(*range(1, 11))
    xs = [n % period + period * j for j in range(5)]
    return interpolate([(x, f(x)) for x in xs], n) % 1_000_000_007


if __name__ == "__main__":
    print(solve())
