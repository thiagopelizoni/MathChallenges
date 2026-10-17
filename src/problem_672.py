# Problem 672: https://projecteuler.net/problem=672


def solve():
    mod = 1117117717
    k = 10**9
    b = (7**10 - 1) // 11

    digits = []
    x = b
    for _ in range(10):
        digits.append(x % 7)
        x //= 7
    digits.reverse()

    fb = 0
    sb = 0
    m = 0
    for d in digits:
        fb = 7 * fb + 21 * m + d * sb + d * (d - 1) // 2
        sb += d
        m = 7 * m + d

    p7 = pow(7, k, mod)
    n_mod = (p7 - 1) * pow(11, -1, mod) % mod
    rep = (p7 - 1) * pow(7**10 - 1, -1, mod) % mod

    fn = (3 * (k - 10) * n_mod + fb * rep) % mod
    ans = (6 * (k - 1) * n_mod - (pow(7, k - 1, mod) - 1) - fn) % mod
    return ans


if __name__ == "__main__":
    print(solve())
