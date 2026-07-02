# Problem 356: https://projecteuler.net/problem=356

import numpy as np


MOD = 10**8
EXP = 987_654_321


def mat_mul(a, b):
    return (a @ b) % MOD


def mat_pow(a, e):
    out = np.identity(a.shape[0], dtype=np.int64)

    while e:
        if e % 2:
            out = mat_mul(out, a)
        a = mat_mul(a, a)
        e //= 2

    return out


def root_power_sum(n, k):
    a = pow(2, n, MOD)
    if k == 0:
        return 3
    if k == 1:
        return a
    if k == 2:
        return a * a % MOD

    trans = np.array(((a, 0, -n % MOD), (1, 0, 0), (0, 1, 0)), dtype=np.int64)
    init = np.array((a * a % MOD, a, 3), dtype=np.int64)
    p = mat_pow(trans, k - 2)
    return int(p[0] @ init % MOD)


def solve():
    return sum(root_power_sum(n, EXP) - 1 for n in range(1, 31)) % MOD


if __name__ == "__main__":
    print(solve())
