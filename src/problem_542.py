# Problem 542: https://projecteuler.net/problem=542

from functools import cache
from math import log2

from sympy import integer_nthroot


@cache
def best_sum(k):
    tmax = int(log2(k))
    while 2 ** (tmax + 1) <= k:
        tmax += 1
    while 2**tmax > k:
        tmax -= 1

    best = 0
    for t in range(tmax, 1, -1):
        pmax = int(integer_nthroot(k, t)[0])
        bound = min(t + 1, pmax) * k
        if bound <= best:
            if pmax >= t + 1:
                break
            continue

        for p in range(2, pmax + 1):
            pt = p**t
            span = p * pt - (p - 1) ** (t + 1)
            value = k // pt * span
            if value > best:
                best = value

    return best


def alternating(a, b):
    length = b - a + 1
    if length % 2 == 0:
        return 0
    return 1 if a % 2 == 0 else -1


def total(n):
    ans = 0
    k = 4

    while k <= n:
        value = best_sum(k)
        step = 1
        high = min(n, k + step)
        while high < n and best_sum(high) == value:
            step *= 2
            high = min(n, k + step)

        if high == n and best_sum(high) == value:
            ans += value * alternating(k, n)
            break

        low = k + 1
        while low < high:
            mid = (low + high) // 2
            if best_sum(mid) == value:
                low = mid + 1
            else:
                high = mid

        ans += value * alternating(k, low - 1)
        k = low

    return ans


def solve():
    return total(10**17)


if __name__ == "__main__":
    print(solve())
