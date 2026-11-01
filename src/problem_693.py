# Problem 693: https://projecteuler.net/problem=693

import numpy as np

def g(x):
    a = np.arange(2, x, dtype=np.int64)
    z = x
    while a.size > 1:
        a = np.unique(a * a % z)
        a = a[a > 1]
        z += 1
    if a.size:
        y = int(a[0])
        while y > 1:
            y = y * y % z
            z += 1
    return z - x + 1

def solve(n=3000000):
    best = 1
    stack = [(2, n)]
    while stack:
        a, b = stack.pop()
        v = g(b)
        best = max(best, v)
        if b - a + v <= best:
            continue
        m = (a + b) // 2
        if m + 1 < b:
            stack.append((m + 1, b - 1))
        stack.append((a, m))
    return best

if __name__ == "__main__":
    print(solve())
