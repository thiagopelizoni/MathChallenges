# Problem 473: https://projecteuler.net/problem=473

from bisect import bisect_right
from collections import defaultdict
from itertools import accumulate

from sympy import fibonacci


def phigital_terms():
    fib = [int(fibonacci(i)) for i in range(50)]
    terms = []
    for e in range(1, 48):
        if e % 2:
            terms.append((-fib[e - 1], fib[e - 1] + fib[e + 2]))
        else:
            terms.append((fib[e + 2], fib[e - 1] - fib[e + 2]))
    return terms


def subset_sums(terms):
    sums = []

    def visit(i, previous, a, b, first):
        if i == len(terms):
            sums.append((a, b, first, previous))
            return
        visit(i + 1, False, a, b, first)
        if not previous:
            da, db = terms[i]
            visit(i + 1, True, a + da, b + db, first or i == 0)

    visit(0, False, 0, 0, False)
    return sums


def palindromic_sum(limit):
    terms = phigital_terms()
    left = subset_sums(terms[:24])
    right = subset_sums(terms[24:])
    groups = defaultdict(list)

    for a, b, first, _ in right:
        groups[a, first].append(b)

    indexes = {}
    for key, values in groups.items():
        values.sort()
        indexes[key] = values, list(accumulate(values, initial=0))

    total = 1
    for a, b, _, last in left:
        for first in (False, True):
            if last and first:
                continue
            item = indexes.get((-a, first))
            if item is None:
                continue
            values, prefix = item
            i = bisect_right(values, limit - b)
            total += i * b + prefix[i]
    return total


def solve():
    return palindromic_sum(10**10)


if __name__ == "__main__":
    print(solve())
