# Problem 764: https://projecteuler.net/problem=764

from math import gcd, isqrt


def fourth_root(n):
    return isqrt(isqrt(n))


def solve(limit=10**16):
    total = 0
    for a in range(1, fourth_root(limit) + 1, 2):
        u = a**4
        for b in range(a + 2, fourth_root(2 * limit - u) + 1, 2):
            if gcd(a, b) == 1:
                v = b**4
                x = (v - u) // 8
                z = (u + v) // 2
                total += x + a * b + z

    for a in range(1, fourth_root(limit // 4) + 1, 2):
        u = a**4
        for b in range(1, fourth_root((limit // 4 - u) // 4) + 1):
            if gcd(a, b) == 1:
                v = 4 * b**4
                x = abs(v - u)
                z = 4 * (u + v)
                total += x + 4 * a * b + z

    return total % 10**9


if __name__ == "__main__":
    print(solve())
