# Problem 309: https://projecteuler.net/problem=309

from collections import defaultdict
from math import gcd, isqrt


LIM = 1_000_000


def heights_by_width(lim):
    h = defaultdict(list)

    for m in range(2, isqrt(lim - 1) + 2):
        for n in range(1, m):
            c = m * m + n * n
            if c >= lim:
                break
            if (m + n) % 2 == 0 or gcd(m, n) != 1:
                continue

            a = m * m - n * n
            b = 2 * m * n
            k = 1

            while k * c < lim:
                h[k * a].append(k * b)
                h[k * b].append(k * a)
                k += 1

    return h


def count(lim):
    total = 0

    for hs in heights_by_width(lim).values():
        hs.sort()
        for i, a in enumerate(hs):
            for b in hs[i + 1 :]:
                if a * b % (a + b) == 0:
                    total += 1

    return total


def solve():
    return count(LIM)


if __name__ == "__main__":
    print(solve())
