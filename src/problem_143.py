# Problem 143: https://projecteuler.net/problem=143

from math import isqrt


def solve():
    lim = 120_000
    pairs = [set() for _ in range(lim + 1)]

    for m in range(2, isqrt(2 * lim) + 2):
        for n in range(1, m):
            a = m * m - n * n
            b = 2 * m * n + n * n
            s = a + b
            if s > lim:
                continue

            for k in range(1, lim // s + 1):
                x, y = k * a, k * b
                pairs[x].add(y)
                pairs[y].add(x)

    totals = set()
    for p in range(1, lim + 1):
        for q in pairs[p]:
            if q <= p:
                continue
            for r in pairs[p].intersection(pairs[q]):
                if r > q and p + q + r <= lim:
                    totals.add(p + q + r)

    return sum(totals)


if __name__ == "__main__":
    print(solve())
