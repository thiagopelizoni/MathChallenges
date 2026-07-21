# Problem 425: https://projecteuler.net/problem=425

import numpy as np
from sympy import sieve


N = 10_000_000


def find(parent, i):
    while parent[i] != i:
        parent[i] = parent[parent[i]]
        i = int(parent[i])
    return i


def union(parent, sizes, i, j):
    a = find(parent, i)
    b = find(parent, j)
    if a == b:
        return
    if sizes[a] < sizes[b]:
        a, b = b, a
    parent[b] = a
    sizes[a] += sizes[b]


def solve():
    primes = np.fromiter(sieve.primerange(2, N + 1), dtype=np.int64)
    index = np.full(N + 1, -1, dtype=np.int32)
    index[primes] = np.arange(len(primes), dtype=np.int32)
    parent = np.arange(len(primes), dtype=np.int32)
    sizes = np.ones(len(primes), dtype=np.int32)
    total = 0

    for i, value in enumerate(primes):
        p = int(value)
        place = 1
        while place <= p:
            digit = p // place % 10
            start = 1 if place * 10 > p else 0
            base = p - digit * place
            for replacement in range(start, digit):
                j = int(index[base + replacement * place])
                if j >= 0:
                    union(parent, sizes, i, j)
            place *= 10

        highest = place // 10
        if p >= 10:
            q = p % highest
            if q >= highest // 10:
                j = int(index[q])
                if j >= 0:
                    union(parent, sizes, i, j)

        if find(parent, i) != find(parent, 0):
            total += p
    return total


if __name__ == "__main__":
    print(solve())
