# Problem 720: https://projecteuler.net/problem=720

import numpy as np


def solve(n=2**25):
    mod = 1_000_000_007
    p = np.array([1, 2], dtype=np.int32)
    digits = np.zeros(2, dtype=np.int32)

    while len(p) < n:
        m = len(p)
        q = np.empty(2 * m, dtype=np.int32)
        d = np.empty(2 * m, dtype=np.int32)
        q[:m] = 2 * p - 1
        q[m:] = 2 * p
        d[:m] = digits + p - 1
        d[m:] = digits
        if m > 2:
            q[m - 1], q[m] = q[m], q[m - 1]
            d[m - 1] = 0
            d[m] = m - 2
        p, digits = q, d

    ans = 1
    fact = 1
    for k, digit in enumerate(reversed(digits), 1):
        ans = (ans + int(digit) * fact) % mod
        fact = fact * k % mod
    return ans


if __name__ == "__main__":
    print(solve())
