# Problem 741: https://projecteuler.net/problem=741


def fixed_counts(n, mod):
    f, f1 = 1, 0
    d, d1, d2, d3 = 1, 0, 0, 0
    for k in range(1, n + 1):
        f, f1 = (k * (k - 1) * f + k * (k - 1) ** 2 // 2 * f1) % mod, f
        d, d1, d2, d3 = (
            2 * (k - 1) * d
            + (k - 1) * (3 - k) * d1
            - (k - 1) * (k - 2) * (k - 3) // 2 * d3
        ) % mod, d, d1, d2

    m = n // 2
    h, h1 = 1, 0
    q, q1, q2 = 1, 0, 0
    v = 1
    for k in range(1, m + 1):
        h, h1 = (k * (4 * k - 3) * h + 4 * k * (k - 1) ** 2 * h1) % mod, h
        q, q1, q2 = (
            (2 * k - 1) * q
            - (k - 1) * q1
            + 2 * (k - 1) * (k - 2) * q2
        ) % mod, q, q1
        v = k * (2 * k - 1) * v % mod

    if n % 2:
        h = (m * h + m * m * h1) % mod
        q = v = 0
    return f, h, q, v, d


def solve():
    mod = 1_000_000_007
    total = 0
    for n in (7**7, 8**8):
        f, h, q, v, d = fixed_counts(n, mod)
        total += f + h + 2 * (q + v + d)
    return total * pow(8, -1, mod) % mod


if __name__ == "__main__":
    print(solve())
