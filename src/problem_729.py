# Problem 729: https://projecteuler.net/problem=729

import numpy as np


def words(n):
    w = [0]
    while w:
        if len(w) == n:
            yield bytes(w)
        k = len(w)
        w.extend(w[i % k] for i in range(n - k))
        while w and w[-1] == 1:
            w.pop()
        if w:
            w[-1] += 1


def solve(limit=25, places=4):
    dtype = np.longdouble
    eps = np.finfo(dtype).eps
    tol = dtype(10) ** (-places - 2) / limit
    lower = upper = dtype(0)
    for n in range(2, limit + 1):
        signs = np.frombuffer(b"".join(words(n)), dtype=np.int8)
        signs = 1 - 2 * signs.reshape(-1, n).T
        lo = np.zeros(signs.shape[1], dtype=dtype)
        hi = np.full_like(lo, np.sqrt(dtype(2 * n)))
        while 2 * n * np.sum(hi - lo) > tol:
            for s in signs[::-1]:
                error = 8 * eps * (np.abs(lo) + 2)
                lo = (lo + s * np.sqrt(lo * lo + 4)) / 2 - error
                error = 8 * eps * (np.abs(hi) + 2)
                hi = (hi + s * np.sqrt(hi * hi + 4)) / 2 + error
        lower += 2 * n * np.sum(lo)
        upper += 2 * n * np.sum(hi)
    a = np.format_float_positional(lower, precision=places, unique=False)
    b = np.format_float_positional(upper, precision=places, unique=False)
    assert a == b
    return a


if __name__ == "__main__":
    print(solve())
