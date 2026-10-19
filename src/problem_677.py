# Problem 677: https://projecteuler.net/problem=677

import math
import numpy as np


def solve():
    n = 10_000
    mod = 1_000_000_007
    half = n // 2

    dp_u = np.zeros((5, n), dtype=np.int64)
    dp_v = np.zeros((4, n), dtype=np.int64)
    dp_u[0, 0] = 1
    dp_v[0, 0] = 1

    inv_fact = [pow(math.factorial(j), -1, mod) for j in range(5)]

    def multiset_count(c, j):
        res = 1
        for i in range(j):
            res = res * (c + i) % mod
        return res * inv_fact[j] % mod

    v_half = 0
    y_half = 0

    for m in range(1, half + 1):
        r_m = int(dp_u[:4, m - 1].sum()) % mod
        b_m = int(dp_u[:3, m - 1].sum()) % mod
        y_m = int(dp_v[:3, m - 1].sum()) % mod

        u_m = (r_m + b_m + y_m) % mod
        v_m = (r_m + b_m) % mod

        if m == half:
            v_half = v_m
            y_half = y_m

        if m <= (n - 1) // 2:
            cu = [multiset_count(u_m, j) for j in range(5)]
            cv = [multiset_count(v_m, j) for j in range(4)]

            for k in range(4, 0, -1):
                for j in range(1, k + 1):
                    shift = j * m
                    if shift < n:
                        dp_u[k, shift:] = (dp_u[k, shift:] + cu[j] * dp_u[k - j, :-shift]) % mod

            for k in range(3, 0, -1):
                for j in range(1, k + 1):
                    shift = j * m
                    if shift < n:
                        dp_v[k, shift:] = (dp_v[k, shift:] + cv[j] * dp_v[k - j, :-shift]) % mod

    ans = (int(dp_u[:5, n - 1].sum()) + int(dp_u[:4, n - 1].sum()) + int(dp_v[:4, n - 1].sum())) % mod
    if n % 2 == 0:
        bicentroid = (v_half * (v_half + 1) * inv_fact[2] + v_half * y_half) % mod
        ans = (ans + bicentroid) % mod

    return ans


if __name__ == "__main__":
    print(solve())
