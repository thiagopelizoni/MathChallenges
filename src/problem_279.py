# Problem 279: https://projecteuler.net/problem=279

from math import gcd


LIMIT = 10**8


def count_90():
    total = 0
    m = 2
    while 2 * m * (m + 1) <= LIMIT:
        for n in range(1, m):
            p = 2 * m * (m + n)
            if p > LIMIT:
                break
            if (m + n) % 2 and gcd(m, n) == 1:
                total += LIMIT // p
        m += 1
    return total


def count_60():
    total = LIMIT // 3
    v = 2
    while v * (v + 1) <= LIMIT:
        for u in range(1, v):
            if gcd(u, v) != 1:
                continue

            p = 3 * v * (u + v)
            if (v - u) % 3 == 0:
                p //= 3
            if p <= LIMIT:
                total += LIMIT // p
        v += 1
    return total


def count_120():
    total = 0
    v = 2
    while v * (v + v // 2 + 1) <= LIMIT:
        for u in range(v // 2 + 1, v):
            if (u + v) % 3 and gcd(u, v) == 1:
                total += LIMIT // (v * (u + v))
        v += 1
    return total


def solve():
    return count_60() + count_90() + count_120()


if __name__ == "__main__":
    print(solve())
