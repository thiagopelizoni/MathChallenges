# Problem 739: https://projecteuler.net/problem=739


def solve(n=10**8):
    mod = 1_000_000_007
    if n == 1:
        return 1
    if n == 2:
        return 3

    a, b = 3, 14
    s, fact = -4, 2
    for m in range(3, n):
        a, b = b, (4 * m * b + m * (m - 1) * a + (9 * m - 12) * s) % mod
        s = s * (4 * m - 6) % mod
        fact = fact * m % mod

    return b * pow(fact, -1, mod) % mod


if __name__ == "__main__":
    print(solve())
