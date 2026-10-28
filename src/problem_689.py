# Problem 689: https://projecteuler.net/problem=689
from math import pi

import numpy as np


def solve():
    a = 0.5
    s = pi * pi / 6
    y = a - s / 2
    k = np.arange(1, 1001)
    t = 2 * pi * k / s
    psi = np.ones(len(k))
    for i in range(1, 10001):
        psi *= np.cos(t / (2 * i * i))
    cdf = 0.5 + y / s + (psi * np.sin(t * y) / k).sum() / pi
    return f"{1 - cdf:.8f}"


if __name__ == "__main__":
    print(solve())
