# Problem 152: https://projecteuler.net/problem=152

from collections import Counter
from fractions import Fraction
from math import lcm


def primes_upto(n):
    primes = []
    for k in range(2, n + 1):
        if all(k % p for p in primes if p * p <= k):
            primes.append(k)
    return primes


def candidates():
    nums = set(range(2, 81))

    for p in reversed(primes_upto(80)):
        if p == 2:
            continue

        group = sorted(n for n in nums if n % p == 0)
        allowed = set()
        for mask in range(1 << len(group)):
            s = Fraction(0)
            chosen = []
            for i, n in enumerate(group):
                if mask >> i & 1:
                    s += Fraction(1, n * n)
                    chosen.append(n)
            if s.denominator % p != 0:
                allowed.update(chosen)

        nums.difference_update(set(group) - allowed)

    return sorted(nums)


def subset_counts(values):
    counts = Counter({0: 1})
    for v in values:
        counts += Counter({s + v: c for s, c in counts.items()})
    return counts


def solve():
    nums = candidates()
    den = 1
    for n in nums:
        den = lcm(den, n * n)

    terms = [den // (n * n) for n in nums]
    mid = len(terms) // 2
    left = subset_counts(terms[:mid])

    total = 0
    target = den // 2
    right_sums = [0]
    for v in terms[mid:]:
        right_sums += [s + v for s in right_sums]

    for s in right_sums:
        total += left[target - s]

    return total


if __name__ == "__main__":
    print(solve())
