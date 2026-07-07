# Problem 367: https://projecteuler.net/problem=367

from collections import Counter
from itertools import combinations, permutations
from math import factorial

from sympy import Matrix, Rational
from sympy.combinatorics import Permutation
from sympy.utilities.iterables import partitions


N = 11


def partition_tuples(n):
    out = []
    for part in partitions(n):
        items = []
        for length, count in part.items():
            items.extend([length] * count)
        out.append(tuple(sorted(items, reverse=True)))
    return sorted(out, reverse=True)


def representative(part):
    n = sum(part)
    p = list(range(n))
    start = 0
    for length in part:
        cycle = list(range(start, start + length))
        for a, b in zip(cycle, cycle[1:] + cycle[:1]):
            p[a] = b
        start += length
    return tuple(p)


def cycle_type(p):
    structure = Permutation(p).cycle_structure
    items = []
    for length, count in structure.items():
        items.extend([length] * count)
    return tuple(sorted(items, reverse=True))


def class_size(part):
    counts = Counter(part)
    den = 1
    for length, count in counts.items():
        den *= length**count * factorial(count)
    return factorial(sum(part)) // den


def shuffled(p, positions, order):
    q = list(p)
    values = [p[i] for i in positions]
    for i, src in zip(positions, order):
        q[i] = values[src]
    return tuple(q)


def transition_counts(part, ops):
    rep = representative(part)
    counts = Counter()
    for positions, order in ops:
        counts[cycle_type(shuffled(rep, positions, order))] += 1
    return counts


def expected_average(n):
    parts = partition_tuples(n)
    identity = (1,) * n
    unknown = [part for part in parts if part != identity]
    indexes = {part: i for i, part in enumerate(unknown)}
    ops = [
        (positions, order)
        for positions in combinations(range(n), 3)
        for order in permutations(range(3))
    ]
    den = len(ops)

    rows = []
    rhs = []
    for part in unknown:
        row = [Rational(0) for _ in unknown]
        row[indexes[part]] = Rational(1)
        for nxt, count in transition_counts(part, ops).items():
            if nxt != identity:
                row[indexes[nxt]] -= Rational(count, den)
        rows.append(row)
        rhs.append(Rational(1))

    solution = Matrix(rows).LUsolve(Matrix(rhs))
    total = Rational(0)
    for part in unknown:
        total += class_size(part) * solution[indexes[part]]
    return total / factorial(n)


def solve():
    return int(expected_average(N) + Rational(1, 2))


if __name__ == "__main__":
    print(solve())
