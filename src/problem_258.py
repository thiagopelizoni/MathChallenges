# Problem 258: https://projecteuler.net/problem=258
import numpy as np


N = 10**18
D = 2000
MOD = 20092010


def mul(a, b):
    c = np.convolve(a, b) % MOD
    hi = c[D:]

    if hi.size:
        c[: hi.size] = (c[: hi.size] + hi) % MOD
        c[1 : hi.size + 1] = (c[1 : hi.size + 1] + hi) % MOD

    return c[:D]


def solve():
    ans = np.zeros(D, dtype=np.int64)
    ans[0] = 1
    x = np.zeros(D, dtype=np.int64)
    x[1] = 1
    n = N

    while n:
        if n & 1:
            ans = mul(ans, x)
        n >>= 1
        if n:
            x = mul(x, x)

    return int(ans.sum() % MOD)


if __name__ == "__main__":
    print(solve())
