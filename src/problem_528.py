# Problem 528: https://projecteuler.net/problem=528

from itertools import combinations
from math import comb


MOD = 1_000_000_007


def constrained_sums(n, k, b):
    limits = [b**m + 1 for m in range(1, k + 1) if b**m < n]
    total = 0
    for r in range(len(limits) + 1):
        sign = -1 if r % 2 else 1
        for chosen in combinations(limits, r):
            remaining = n - sum(chosen)
            if remaining >= 0:
                total += sign * comb(remaining + k, k)
    return total % MOD


def solve():
    return sum(constrained_sums(10**k, k, k) for k in range(10, 16)) % MOD


if __name__ == "__main__":
    print(solve())
