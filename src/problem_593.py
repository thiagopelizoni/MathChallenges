# Problem 593: https://projecteuler.net/problem=593

import numpy as np
from scipy.ndimage import rank_filter
from sympy import sieve


def solve(n=10**7, k=10**5):
    s = np.fromiter(
        (pow(p, i, 10007) for i, p in enumerate(sieve[1:n + 1], 1)),
        dtype=np.int64,
        count=n,
    )
    s2 = s + s[np.arange(1, n + 1) // 10000]

    total = 0
    for rank in ((k - 1) // 2, k // 2):
        medians = rank_filter(s2, rank, size=k)
        total += int(medians[k // 2:n - (k - 1) // 2].sum())

    return f"{total / 2:.1f}"


if __name__ == "__main__":
    print(solve())
