# Problem 340: https://projecteuler.net/problem=340

A = 21**7
B = 7**21
C = 12**7
MOD = 10**9


def s(a, b, c):
    q, r = divmod(b, a)
    floors = a * q * (q - 1) // 2 + q * (r + 1)
    return b * (b + 1) // 2 + 4 * (a - c) * (b + 1) + (4 * a - 3 * c) * floors


def solve():
    return s(A, B, C) % MOD


if __name__ == "__main__":
    print(solve())
