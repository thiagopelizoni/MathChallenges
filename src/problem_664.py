# Problem 664: https://projecteuler.net/problem=664
import math

import numpy as np
from scipy.special import logsumexp


def solve():
    n = 1234567
    phi = (1 + math.sqrt(5)) / 2
    d = np.arange(1, 10 * n, dtype=np.float64)
    s = logsumexp(n * np.log(d) - d * math.log(phi)) / math.log(phi)
    return math.ceil(4 + s) - 1


if __name__ == "__main__":
    print(solve())
