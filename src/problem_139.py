# Problem 139: https://projecteuler.net/problem=139

from math import gcd, isqrt


def solve():
    lim = 100_000_000
    total = 0

    for m in range(2, isqrt(lim // 2) + 2):
        for n in range(1 + m % 2, m, 2):
            if gcd(m, n) != 1:
                continue

            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            p = a + b + c

            if p >= lim:
                break
            if c % abs(a - b) == 0:
                total += (lim - 1) // p

    return total


if __name__ == "__main__":
    print(solve())
