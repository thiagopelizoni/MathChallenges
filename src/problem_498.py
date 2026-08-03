# Problem 498: https://projecteuler.net/problem=498

from math import comb


N = 10**13
M = 10**12
D = 10**4
MOD = 999_999_937


def binomial_mod(n, k):
    result = 1
    while k:
        n, n_digit = divmod(n, MOD)
        k, k_digit = divmod(k, MOD)
        if k_digit > n_digit:
            return 0
        result = result * comb(n_digit, k_digit) % MOD
    return result


def solve():
    return binomial_mod(N, D) * binomial_mod(N - D - 1, M - D - 1) % MOD


if __name__ == "__main__":
    print(solve())
