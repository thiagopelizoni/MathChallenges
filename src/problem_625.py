# Problem 625: https://projecteuler.net/problem=625

from itertools import chain

import numpy as np
from sympy import integer_nthroot, sieve


def solve(n=10**11):
    mod = 998244353
    cutoff = int(integer_nthroot(n * n, 3)[0])
    prefix = np.fromiter(
        chain([0], sieve.totientrange(1, cutoff + 1)),
        dtype=np.int64,
        count=cutoff + 1,
    )
    np.cumsum(prefix, out=prefix)
    prefix %= mod
    memo = {}

    def phi_sum(x):
        if x <= cutoff:
            return int(prefix[x])
        if x in memo:
            return memo[x]
        total = x * (x + 1) // 2
        left = 2
        while left <= x:
            q = x // left
            right = x // q
            total -= (right - left + 1) * phi_sum(q)
            left = right + 1
        memo[x] = total % mod
        return memo[x]

    total = 0
    left = 1
    while left <= n:
        q = n // left
        right = n // q
        weight = (left + right) * (right - left + 1) // 2
        total += weight * phi_sum(q)
        left = right + 1
    return total % mod


if __name__ == "__main__":
    print(solve())
