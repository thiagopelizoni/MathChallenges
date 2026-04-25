# Problem 118: https://projecteuler.net/problem=118

from collections import Counter
from functools import cache
from itertools import combinations, permutations

from sympy import isprime


DIGITS = "123456789"
FULL = (1 << 9) - 1


def prime_counts():
    counts = Counter()

    for r in range(1, 10):
        for digits in combinations(DIGITS, r):
            if r > 1 and sum(map(int, digits)) % 3 == 0:
                continue

            mask = sum(1 << (int(d) - 1) for d in digits)
            for p in permutations(digits):
                if r > 1 and p[-1] in "24568":
                    continue

                if isprime(int("".join(p))):
                    counts[mask] += 1

    return counts


def solve():
    counts = prime_counts()

    @cache
    def count(mask):
        if mask == 0:
            return 1

        bit = mask & -mask
        total = 0
        sub = mask
        while sub:
            if sub & bit:
                total += counts[sub] * count(mask ^ sub)
            sub = (sub - 1) & mask

        return total

    return count(FULL)


if __name__ == "__main__":
    print(solve())
