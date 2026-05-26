# Problem 257: https://projecteuler.net/problem=257
from math import gcd, isqrt


N = 100_000_000


def solve():
    ans = N // 3

    x = 1
    while (2 * x + 1) * (3 * x + 1) // 2 <= N:
        for y in range(x + 1, isqrt(2 * x * x) + 1):
            if gcd(x, y) == 1:
                p = (x + y) * (2 * x + y)
                if y % 2 == 0:
                    p //= 2
                if p <= N:
                    ans += N // p
        x += 1

    x = 1
    while (2 * x + 1) * (4 * x + 1) // 6 <= N:
        for y in range(x + 1, isqrt(3 * x * x) + 1):
            if gcd(x, y) == 1:
                g1 = 2 // gcd(2, x + y)
                g2 = 2 * y // gcd(2 * y, x * (3 * x + y))
                g = g1 // gcd(g1, g2) * g2
                p = g * (x + y) * (3 * x + y) // (2 * y)
                if p <= N:
                    ans += N // p
        x += 1

    return ans


if __name__ == "__main__":
    print(solve())
