# Problem 299: https://projecteuler.net/problem=299

from math import gcd, isqrt


LIM = 100_000_000


def incenter(lim):
    total = 0
    mmax = isqrt(lim) + 2

    for m in range(2, mmax + 1):
        m2 = m * m
        for n in range(1, m):
            s = m2 + 2 * m * n - n * n
            if s >= lim:
                break
            if (m + n) % 2 and gcd(m, n) == 1:
                total += 2 * ((lim - 1) // s)

    return total


def parallel(lim):
    total = 0
    vmax = isqrt(lim // 4) + 2

    for v in range(1, vmax + 1):
        u = 1
        while True:
            b = u * u + 2 * u * v + 2 * v * v
            if 2 * b >= lim:
                break
            if gcd(u, v) == 1:
                total += (lim - 1) // (2 * b)
            u += 2

    return total


def solve():
    return incenter(LIM) + parallel(LIM)


if __name__ == "__main__":
    print(solve())
