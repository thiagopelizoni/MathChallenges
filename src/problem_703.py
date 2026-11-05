# Problem 703: https://projecteuler.net/problem=703

from collections import deque

import numpy as np


def solve(n=20):
    mod = 1_001_001_011
    size = 2**n
    x = np.arange(size)
    b1 = x >> (n - 1)
    b2 = (x >> (n - 2)) & 1
    b3 = (x >> (n - 3)) & 1
    nxt = ((x << 1) & (size - 1)) | (b1 & (b2 ^ b3))
    degree = np.bincount(nxt, minlength=size).tolist()
    nxt = nxt.tolist()
    zero = [1] * size
    one = [1] * size
    leaves = deque(v for v in range(size) if degree[v] == 0)

    while leaves:
        v = leaves.popleft()
        w = nxt[v]
        zero[w] = zero[w] * (zero[v] + one[v]) % mod
        one[w] = one[w] * zero[v] % mod
        degree[w] -= 1
        if degree[w] == 0:
            leaves.append(w)

    ans = 1
    for start in range(size):
        if degree[start] == 0:
            continue
        a, b = zero[start], 0
        c, d = 0, one[start]
        degree[start] = 0
        v = nxt[start]
        while v != start:
            a, b = (a + b) * zero[v] % mod, a * one[v] % mod
            c, d = (c + d) * zero[v] % mod, c * one[v] % mod
            degree[v] = 0
            v = nxt[v]
        ans = ans * (a + b + c) % mod
    return ans


if __name__ == "__main__":
    print(solve())
