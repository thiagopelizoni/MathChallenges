# Problem 643: https://projecteuler.net/problem=643

from functools import cache

import numpy as np
from sympy import integer_nthroot, sieve


def solve(n=10**11):
    mod = 1_000_000_007
    limit = int(integer_nthroot((n // 2) ** 2, 3)[0])
    prefix = np.zeros(limit + 1, dtype=np.int64)
    prefix[1:] = np.fromiter(sieve.totientrange(1, limit + 1), dtype=np.int64)
    np.cumsum(prefix, out=prefix)
    prefix %= mod

    @cache
    def total(x):
        if x <= limit:
            return int(prefix[x])
        result = x * (x + 1) // 2
        left = 2
        while left <= x:
            q = x // left
            right = x // q
            result -= (right - left + 1) * total(q)
            left = right + 1
        return result % mod

    result = 0
    n //= 2
    while n >= 2:
        result += total(n) - 1
        n //= 2
    return result % mod


if __name__ == "__main__":
    print(solve())
