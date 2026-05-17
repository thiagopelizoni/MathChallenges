# Problem 227: https://projecteuler.net/problem=227
import numpy as np


PLAYERS = 100


def solve():
    m = PLAYERS // 2
    a = np.eye(m)
    b = np.ones(m)
    moves = [(-2, 1 / 36), (-1, 2 / 9), (0, 1 / 2), (1, 2 / 9), (2, 1 / 36)]

    for k in range(1, m + 1):
        i = k - 1
        for d, p in moves:
            j = (k + d) % PLAYERS
            j = min(j, PLAYERS - j)
            if j:
                a[i, j - 1] -= p

    expected = np.linalg.solve(a, b)[m - 1]
    return f"{expected:.6f}"


if __name__ == "__main__":
    print(solve())
