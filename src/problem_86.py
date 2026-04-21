# Problem 86: https://projecteuler.net/problem=86

from math import isqrt


def solve():
    target = 1_000_000
    total = 0
    m = 0

    while total <= target:
        m += 1
        for s in range(2, 2 * m + 1):
            r = isqrt(s * s + m * m)
            if r * r == s * s + m * m:
                lo = max(1, s - m)
                hi = s // 2
                if lo <= hi:
                    total += hi - lo + 1

    return m


if __name__ == "__main__":
    print(solve())
