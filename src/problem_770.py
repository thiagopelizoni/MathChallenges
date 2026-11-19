# Problem 770: https://projecteuler.net/problem=770

from bisect import bisect_left

from mpmath import binomial, mpf, power


def guaranteed_gold(n):
    middle = binomial(2 * n, n) / power(4, n)
    return 2 / (1 + middle)


def solve():
    target = mpf("1.9999")
    high = 1
    while guaranteed_gold(high) < target:
        high *= 2
    return bisect_left(range(high + 1), target, key=guaranteed_gold)


if __name__ == "__main__":
    print(solve())
