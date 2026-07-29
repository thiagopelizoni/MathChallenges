# Problem 465: https://projecteuler.net/problem=465

import numpy as np
from sympy import sieve


N = 7**13
MOD = 1_000_000_007
SIEVE_LIMIT = 20_000_000


def totient_sums(n):
    limit = min(n, SIEVE_LIMIT)
    prefix = np.empty(limit + 1, dtype=np.int64)
    prefix[0] = 0
    prefix[1:] = np.fromiter(
        sieve.totientrange(1, limit + 1),
        dtype=np.int64,
        count=limit,
    )
    np.cumsum(prefix, out=prefix)

    large = {}
    for i in range(n // (limit + 1), 0, -1):
        x = n // i
        total = x * (x + 1) // 2
        left = 2
        while left <= x:
            q = x // left
            right = x // q
            subtotal = int(prefix[q]) if q <= limit else large[q]
            total -= (right - left + 1) * subtotal
            left = right + 1
        large[x] = total
    return prefix, large


def count_polygons(n):
    prefix, large = totient_sums(n)

    def totient_sum(x):
        return int(prefix[x]) if x < len(prefix) else large[x]

    h = 1
    qsum = 0
    left = 1
    while left <= n:
        quotient = n // left
        right = n // quotient
        count = totient_sum(right) - totient_sum(left - 1)
        h = h * pow(quotient + 1, 4 * count % (MOD - 1), MOD) % MOD
        qsum = (qsum + 4 * (count % MOD) * pow(quotient, 2, MOD)) % MOD
        left = right + 1

    w = 2 * n * (n + 1) % MOD
    return (h * (h - 2 * w) + qsum - 1) % MOD


def solve():
    return count_polygons(N)


if __name__ == "__main__":
    print(solve())
