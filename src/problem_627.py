# Problem 627: https://projecteuler.net/problem=627

from collections import Counter
from itertools import combinations
from math import comb

from scipy.spatial import Delaunay
from sympy import Matrix, factorint, primerange


def solve(m=30, n=10001):
    mod = 10**9 + 7
    primes = list(primerange(1, m + 1))
    isolated = {p for p in primes if 2 * p > m}
    primes = [p for p in primes if p not in isolated]
    points = []
    for i in range(1, m + 1):
        if i not in isolated:
            factors = factorint(i)
            points.append([factors.get(p, 0) for p in primes])

    faces = set()
    for simplex in Delaunay(points).simplices:
        simplex = sorted(simplex)
        base = points[simplex[0]]
        edges = []
        for i in simplex[1:]:
            edges.append([a - b for a, b in zip(points[i], base)])
        assert abs(Matrix(edges).det()) == 1
        for size in range(len(simplex) + 1):
            faces.update(combinations(simplex, size))

    counts = Counter(map(len, faces))
    r = len(isolated)
    total = sum(count * comb(n + r - 1, size + r - 1)
                for size, count in counts.items())
    return total % mod


if __name__ == "__main__":
    print(solve())
