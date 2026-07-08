# Problem 372: https://projecteuler.net/problem=372

from math import isqrt


M = 2_000_000
N = 1_000_000_000


def floor_surd_mul(n, d, a, b):
    return (isqrt(n * n * d) + n * a) // b


def beatty(n, d):
    s = isqrt(d)
    if s * s == d:
        return s * n * (n + 1) // 2

    def rec(n, a, b):
        if n <= 0:
            return 0

        q = (s + a) // b
        a -= q * b
        total = q * n * (n + 1) // 2
        m = floor_surd_mul(n, d, a, b)
        if m:
            total += n * m - rec(m, -a, (d - a * a) // b)
        return total

    return rec(n, 0, 1)


def below(d, m, n):
    s = isqrt(d)
    u = min(n, isqrt((n * n) // d))
    if u <= m:
        return (n - m) * (n - m)

    section = beatty(u, d) - beatty(m, d)
    if s * s == d:
        section -= u - m
    return (n - u) * (n - m) + section - m * (u - m)


def count(m, n):
    q = (n * n) // ((m + 1) * (m + 1))
    dmax = q if q % 2 == 0 else q + 1
    total = 0

    for d in range(1, dmax + 1):
        if d % 2 == 0:
            total += below(d, m, n)
        else:
            total -= below(d, m, n)

    return total


def solve():
    return count(M, N)


if __name__ == "__main__":
    print(solve())
