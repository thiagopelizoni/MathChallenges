# Problem 683: https://projecteuler.net/problem=683
import numpy as np


def G(n):
    total = 0.0
    for m in range(2, n + 1):
        a = np.eye(m - 1)
        for d in range(1, m):
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    e = (d + j - i) % m
                    if e:
                        a[d - 1, e - 1] -= 1 / 9
        t = np.linalg.solve(a, np.ones(m - 1))
        s2 = np.linalg.solve(a, 2 * t - 1)
        total += s2.sum() / m
    return total


def solve():
    mant, exp = f"{G(500):.8e}".split("e")
    return f"{mant}e{int(exp)}"


if __name__ == "__main__":
    print(solve())
