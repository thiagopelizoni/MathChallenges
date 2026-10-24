# Problem 684: https://projecteuler.net/problem=684


def S(k, mod):
    q, r = divmod(k, 9)
    p = pow(10, q, mod)
    full = 5 * (p - 1) - 9 * q
    part = (r + 1) * (r + 2) // 2 * p - (r + 1)
    return (full + part) % mod


def solve():
    mod = 1_000_000_007
    a, b = 0, 1
    total = 0
    for _ in range(2, 91):
        a, b = b, a + b
        total += S(b, mod)
    return total % mod


if __name__ == "__main__":
    assert S(20, 10**9) == 1074
    print(solve())
