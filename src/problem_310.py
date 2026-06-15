# Problem 310: https://projecteuler.net/problem=310

from collections import Counter
from math import isqrt


LIM = 100_000


def nim_sum(a, b):
    total = 0
    place = 1

    while a or b:
        if (a % 2 + b % 2) % 2:
            total += place
        a //= 2
        b //= 2
        place *= 2

    return total


def grundy(lim):
    g = [0] * (lim + 1)
    squares = [n * n for n in range(1, isqrt(lim) + 1)]

    for n in range(1, lim + 1):
        seen = set()
        for s in squares:
            if s > n:
                break
            seen.add(g[n - s])

        m = 0
        while m in seen:
            m += 1
        g[n] = m

    return Counter(g)


def count(lim):
    cnt = grundy(lim)
    vals = list(cnt)
    ordered = 0

    for a in vals:
        for b in vals:
            ordered += cnt[a] * cnt[b] * cnt.get(nim_sum(a, b), 0)

    f0 = cnt[0]
    return (ordered + 3 * lim * f0 + 5 * f0) // 6


def solve():
    return count(LIM)


if __name__ == "__main__":
    print(solve())
