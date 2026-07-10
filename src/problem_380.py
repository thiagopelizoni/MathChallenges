# Problem 380: https://projecteuler.net/problem=380

from math import fsum, log10, pi

import numpy as np


def solve(m=100, n=500):
    rows = 2 - 2 * np.cos(pi * np.arange(m) / m)
    columns = 2 - 2 * np.cos(pi * np.arange(n) / n)
    eigenvalues = rows[:, None] + columns
    eigenvalues[0, 0] = 1

    logarithm = fsum(np.log10(eigenvalues).flat) - log10(m * n)
    exponent = int(logarithm)
    mantissa = 10 ** (logarithm - exponent)
    return f"{mantissa:.4f}e{exponent}"


if __name__ == "__main__":
    print(solve())
