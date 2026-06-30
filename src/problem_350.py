# Problem 350: https://projecteuler.net/problem=350

from sympy import factorint


G = 10**6
L = 10**12
N = 10**18
MOD = 101**4
EXP_WAYS = [
    0,
    *[
        (pow(e + 1, N, MOD) - 2 * pow(e, N, MOD) + pow(e - 1, N, MOD))
        % MOD
        for e in range(1, 20)
    ],
]


def h(r):
    ans = 1

    for e in factorint(r).values():
        ans = ans * EXP_WAYS[e] % MOD

    return ans


def solve():
    total = 0

    for r in range(1, L // G + 1):
        total = (total + (L // r - G + 1) * h(r)) % MOD

    return total


if __name__ == "__main__":
    print(solve())
