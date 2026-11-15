# Problem 750: https://projecteuler.net/problem=750

import numpy as np


def solve(n=976):
    pos = [0] * n
    card = 1
    for i in range(n):
        card = 3 * card % (n + 1)
        pos[card - 1] = i

    pos = np.array(pos, dtype=np.int64)
    dp = np.zeros((n, n), dtype=np.int64)

    for width in range(1, n):
        for i in range(n - width):
            j = i + width
            dp[i, j] = np.min(
                dp[i, i:j] + dp[i + 1:j + 1, j] + np.abs(pos[i:j] - pos[j])
            )

    return int(dp[0, n - 1])


if __name__ == "__main__":
    print(solve())
