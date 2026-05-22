# Problem 250: https://projecteuler.net/problem=250
import numpy as np


MOD = 10**16
SIZE = 250
LIMIT = 250250


def solve():
    dp = np.zeros(SIZE, dtype=np.uint64)
    dp[0] = 1

    for n in range(1, LIMIT + 1):
        dp = (dp + np.roll(dp, pow(n, n, SIZE))) % MOD

    return (int(dp[0]) - 1) % MOD


if __name__ == "__main__":
    print(solve())
