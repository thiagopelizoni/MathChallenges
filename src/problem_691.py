# Problem 691: https://projecteuler.net/problem=691
from math import isqrt

import numpy as np


def sequence(n):
    a = np.zeros(1, dtype=np.int64)
    while len(a) < n:
        t = np.empty(2 * len(a), dtype=np.int64)
        t[0::2] = a
        t[1::2] = 1 - a
        a = t
    a = a[:n]
    f = np.array([(isqrt(5 * m * m) - m) // 2 for m in range(n + 1)], dtype=np.int64)
    b = f[1:] - f[:-1]
    return a + b - 2 * a * b


def solve(n=5_000_000):
    c = sequence(n)

    r = c.copy()
    h = 1
    while True:
        r2 = np.zeros(n, dtype=np.int64)
        r2[:n - h] = r[h:] + 1
        key = r * (n + 1) + r2
        sa = np.argsort(key, kind="stable")
        key = key[sa]
        r = np.empty(n, dtype=np.int64)
        r[sa] = np.concatenate(([0], np.cumsum(key[1:] != key[:-1])))
        if r[sa[-1]] == n - 1:
            break
        h *= 2

    s = c.tolist()
    sa = sa.tolist()
    rank = r.tolist()
    lcp = [0] * n
    h = 0
    for i in range(n):
        k = rank[i]
        if k == 0:
            h = 0
            continue
        j = sa[k - 1]
        while i + h < n and j + h < n and s[i + h] == s[j + h]:
            h += 1
        lcp[k - 1] = h
        if h > 0:
            h -= 1

    best = [0] * (n + 1)
    stack = []
    for i in range(n):
        v = lcp[i]
        start = i
        while stack and stack[-1][1] >= v:
            start, h = stack.pop()
            if h > best[i - start + 1]:
                best[i - start + 1] = h
        stack.append((start, v))

    best[1] = n
    for k in range(n - 1, 0, -1):
        best[k] = max(best[k], best[k + 1])
    return sum(best)


if __name__ == "__main__":
    print(solve())
