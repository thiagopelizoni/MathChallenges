# Problem 746: https://projecteuler.net/problem=746

from itertools import accumulate


def solve(n=2021):
    mod = 1_000_000_007
    fac = list(accumulate(range(1, 4 * n + 1), lambda a, b: a * b % mod, initial=1))
    inv = list(accumulate(range(4 * n, 0, -1), lambda a, b: a * b % mod,
                          initial=pow(fac[-1], -1, mod)))
    inv.reverse()
    powers = [pow(-4, k, mod) for k in range(n + 1)]
    ans = 0
    for m in range(2, n + 1):
        total = 0
        for k in range(m + 1):
            term = fac[m] * inv[k] * inv[m - k] % mod
            term = term * (8 * m) * powers[k] % mod
            term = term * fac[4 * m - 3 * k - 1] % mod
            term = term * fac[2 * (m - k)] ** 2 % mod
            term = term * inv[4 * (m - k)] % mod
            total = (total + term) % mod
        ans = (ans + total) % mod
    return ans


if __name__ == "__main__":
    print(solve())
