# Problem 740: https://projecteuler.net/problem=740

import numpy as np


def solve(n=100):
    b, c = np.indices((n + 1, n + 1))
    dp = np.zeros((n + 1, n + 1), dtype=np.longdouble)
    dp[0, n] = 1

    for k in range(n, 1, -1):
        nxt = np.zeros_like(dp)
        for j in range(3):
            p = np.zeros_like(dp)
            if j == 0:
                p = dp * (k - b - c) / k
            elif j == 1:
                p[:-1, :] = dp[1:, :] * b[1:, :] / k
            else:
                p[:, :-1] = dp[:, 1:] * c[:, 1:] / k

            for d in range(2):
                total = 2 * k - j - d
                q = p * (total - b - 2 * c) / total
                q[:-1, :] += p[1:, :] * b[1:, :] / total
                q[1:, :-1] += p[:-1, 1:] * 2 * c[:-1, 1:] / total
                p = q
            nxt += p
        dp = nxt

    return f"{dp[1, 0] + dp[0, 1]:.10f}"


if __name__ == "__main__":
    print(solve())
