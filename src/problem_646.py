# Problem 646: https://projecteuler.net/problem=646

from bisect import bisect_right
from itertools import accumulate
from math import factorial

from sympy import factorint


def signed_products(factors):
    values = [1]
    for p, e in factors:
        expanded = []
        q = 1
        for _ in range(e + 1):
            expanded.extend(d * q for d in values)
            q *= -p
        values = expanded
    return values


def solve(n=70, low=10**20, high=10**60, mod=1_000_000_007):
    groups = [[], []]
    sizes = [1, 1]
    factors = factorint(factorial(n))
    for p, e in sorted(factors.items(), key=lambda item: -item[1]):
        i = sizes.index(min(sizes))
        groups[i].append((p, e))
        sizes[i] *= e + 1

    i = sizes.index(min(sizes))
    values = signed_products(groups[i])
    values.sort(key=abs)
    keys = list(map(abs, values))
    sums = list(accumulate((d % mod for d in values), lambda a, b: (a + b) % mod, initial=0))
    del values

    total = 0
    for d in signed_products(groups[1 - i]):
        x = abs(d)
        left = bisect_right(keys, (low - 1) // x)
        right = bisect_right(keys, high // x)
        total = (total + d * (sums[right] - sums[left])) % mod
    return total


if __name__ == "__main__":
    print(solve())
