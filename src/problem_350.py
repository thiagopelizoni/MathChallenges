# Problem 350: https://projecteuler.net/problem=350

from sympy import factorint


G = 10**6
L = 10**12
N = 10**18
MOD = 101**4
MAX_EXPONENT = 19


def valuation_patterns(e):
    all_patterns = pow(e + 1, N, MOD)
    without_zero = pow(e, N, MOD)
    without_top = pow(e, N, MOD)
    without_zero_or_top = pow(e - 1, N, MOD)
    return (all_patterns - without_zero - without_top + without_zero_or_top) % MOD


WAYS_BY_EXPONENT = [
    0,
    *[valuation_patterns(e) for e in range(1, MAX_EXPONENT + 1)],
]


def h(r):
    ans = 1

    for e in factorint(r).values():
        ans = ans * WAYS_BY_EXPONENT[e] % MOD

    return ans


def solve():
    total = 0

    for r in range(1, L // G + 1):
        total = (total + (L // r - G + 1) * h(r)) % MOD

    return total


if __name__ == "__main__":
    print(solve())
