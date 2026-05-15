# Problem 213: https://projecteuler.net/problem=213
import numpy as np


def step(p, deg):
    q = np.zeros_like(p)
    q[:-1, :] += p[1:, :] / deg[1:, :]
    q[1:, :] += p[:-1, :] / deg[:-1, :]
    q[:, :-1] += p[:, 1:] / deg[:, 1:]
    q[:, 1:] += p[:, :-1] / deg[:, :-1]
    return q


def solve():
    n = 30
    deg = np.full((n, n), 4.0)
    deg[0, :] -= 1
    deg[-1, :] -= 1
    deg[:, 0] -= 1
    deg[:, -1] -= 1

    empty = np.ones((n, n))
    for i in range(n):
        for j in range(n):
            p = np.zeros((n, n))
            p[i, j] = 1.0
            for _ in range(50):
                p = step(p, deg)
            empty *= 1 - p

    return f"{empty.sum():.6f}"


if __name__ == "__main__":
    print(solve())
