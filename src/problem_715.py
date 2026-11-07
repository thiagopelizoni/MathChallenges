# Problem 715: https://projecteuler.net/problem=715

from math import isqrt
from itertools import chain

import numpy as np
from sympy import integer_nthroot, sieve


def solve(n=10**12):
    mod = 1_000_000_007
    lim = int(integer_nthroot(n * n, 3)[0])
    h = np.fromiter(chain((0,), sieve.mobiusrange(1, lim + 1)), dtype=np.int64)
    h[::2] = 0
    h[3::4] *= -1
    np.cumsum(h, out=h)
    memo = {}

    def total(x):
        if x <= lim:
            return int(h[x])
        if x in memo:
            return memo[x]
        r = isqrt(x)
        end = min(r, x // (lim + 1))
        ans = 1
        for k in range(3, end + 1, 2):
            ans -= (1 if k % 4 == 1 else -1) * total(x // k)
        start = max(3, end + 1)
        start += (start + 1) % 2
        k = np.arange(start, r + 1, 2, dtype=np.int64)
        signs = 2 - k % 4
        ans -= int(np.dot(signs, h[x // k]))
        q = np.arange(1, x // (r + 1) + 1, dtype=np.int64)
        upper = (x // q + 1) // 2 % 2
        lower = (np.maximum(r, x // (q + 1)) + 1) // 2 % 2
        ans -= int(np.dot(h[q], upper - lower))
        memo[x] = ans
        return ans

    r = isqrt(n)
    ans = 0
    for d in range(1, r + 1):
        m = n // d
        s = m * (m + 1) // 2 % mod
        ans = (ans + int(h[d] - h[d - 1]) * s * s) % mod
    for q in range(1, n // (r + 1) + 1):
        upper = total(n // q)
        lower = total(max(r, n // (q + 1)))
        s = q * (q + 1) // 2 % mod
        ans = (ans + s * s * (upper - lower)) % mod
    return ans


if __name__ == "__main__":
    print(solve())
