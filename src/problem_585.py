# Problem 585: https://projecteuler.net/problem=585
from bisect import bisect_right
from collections import Counter
from math import gcd, isqrt

from sympy import divisors


def pair_counts(queries, coprime=False):
    grouped = {}
    for d, m in queries:
        grouped.setdefault(d, set()).add(m)

    counts = {}
    for d, limits in grouped.items():
        top = max(limits)
        sums = []
        zmax = isqrt(top * top // (4 * d))
        for z in range(1, zmax + 1):
            p = d * z * z
            for a in divisors(p):
                if a * a > p:
                    break
                b = p // a
                if not coprime or gcd(a, b) == 1:
                    sums.extend((a + b,) * (1 if a == b else 2))
        sums.sort()
        for m in limits:
            counts[d, m] = bisect_right(sums, m)
    return counts


def solve():
    n = 5_000_000
    bnd = isqrt(n)

    phi = list(range(n // 2 + 1))
    for p in range(2, len(phi)):
        if phi[p] == p:
            for k in range(p, len(phi), p):
                phi[k] -= phi[k] // p

    kernels = list(range(bnd * bnd // 4 + 2))
    for p in range(2, len(kernels)):
        if kernels[p] == p:
            square = p * p
            for k in range(square, len(kernels), square):
                while kernels[k] % square == 0:
                    kernels[k] //= square

    raw = 0
    for s in range(2, n // 2 + 1):
        m = n // s
        raw += phi[s] * m * (m - 1) // 2

    square_products = Counter({2: 1})
    for r in range(1, isqrt(n // 2) + 1):
        for q in range(1, r):
            if gcd(r, q) == 1:
                square_products[r * r + q * q] += 2

    square_queries = {(1, n)}
    square_queries.update((1, n // s) for s in range(2, n // 2 + 1))
    square_counts = pair_counts(square_queries)

    first_square = sum(c * (n // s) * (n // s - 1) // 2 for s, c in square_products.items() if s <= n // 2)
    second_square = sum(phi[s] * square_counts[1, n // s] for s in range(2, n // 2 + 1))
    both_square = sum(c * square_counts[1, n // s] for s, c in square_products.items() if s <= n // 2)

    left = Counter()
    for s in range(2, bnd + 1):
        for u in range(1, s):
            if gcd(u, s) == 1:
                left[kernels[u * (s - u)], n // s] += 1
    left_counts = pair_counts(left)
    equal_classes = sum(c * left_counts[d, m] for (d, m), c in left.items())

    right = Counter()
    for t in range(2, bnd + 1):
        for a in range(1, t):
            right[kernels[a * (t - a)], n // t] += 1
    right_queries = set(right)
    right_queries.update((d, bnd) for d, m in right)
    right_counts = pair_counts(right_queries, True)
    equal_classes += sum(c * (right_counts[d, m] - right_counts[d, bnd]) for (d, m), c in right.items())

    four_roots = (raw - first_square - second_square + 2 * both_square - equal_classes) // 8
    all_pairs = (n - 1) * (n - 1) // 4
    same_class_pairs = (square_counts[1, n] - n // 2) // 2
    return all_pairs - same_class_pairs + four_roots


if __name__ == "__main__":
    print(solve())
