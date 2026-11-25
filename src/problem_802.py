# Problem 802: https://projecteuler.net/problem=802

from functools import cache


@cache
def period_sum(n, mod):
    total = pow(2, n, mod)
    k = 2
    while k <= n:
        q = n // k
        end = n // q
        total -= (end - k + 1) * period_sum(q, mod)
        k = end + 1
    return total % mod


def solve():
    return period_sum(10**7, 1_020_340_567)


if __name__ == "__main__":
    print(solve())
