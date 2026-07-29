# Problem 468: https://projecteuler.net/problem=468

from array import array
from bisect import bisect_left

import numpy as np
from sympy import sieve


N = 11_111_111
MOD = 1_000_000_993


def prime_tables(n):
    primes = np.fromiter(sieve.primerange(2, n + 1), dtype=np.int32)
    smallest = np.zeros(n + 1, dtype=np.int32)
    for value in primes:
        p = int(value)
        if p * p > n:
            break
        entries = smallest[p * p :: p]
        missing = entries == 0
        entries[missing] = p
    smallest[primes] = primes

    indices = np.full(n + 1, -1, dtype=np.int32)
    indices[primes] = np.arange(len(primes), dtype=np.int32)
    inverses = [pow(int(p), MOD - 2, MOD) for p in primes]
    return primes, smallest, indices, inverses


def weighted_tree(primes, n):
    frequencies = [n // int(p) for p in primes]
    prefix = [0]
    for frequency in frequencies:
        prefix.append(prefix[-1] + frequency)

    left = array("i", [-1])
    right = array("i", [-1])
    parent = array("i", [-1])
    leaves = array("i", [0]) * len(primes)
    products = [1]
    weighted = [0]
    stack = [(0, len(primes), 0)]

    while stack:
        lo, hi, node = stack.pop()
        if hi - lo == 1:
            leaves[lo] = node
            next_prime = int(primes[lo + 1]) if lo + 1 < len(primes) else n + 1
            weighted[node] = next_prime - int(primes[lo])
            continue

        target = (prefix[lo] + prefix[hi]) // 2
        middle = bisect_left(prefix, target, lo + 1, hi)
        if middle == hi:
            middle -= 1

        left_child = len(left)
        right_child = left_child + 1
        left[node] = left_child
        right[node] = right_child
        left.extend((-1, -1))
        right.extend((-1, -1))
        parent.extend((node, node))
        products.extend((1, 1))
        weighted.extend((0, 0))
        stack.append((lo, middle, left_child))
        stack.append((middle, hi, right_child))

    for node in range(len(left) - 1, -1, -1):
        if left[node] >= 0:
            a = left[node]
            b = right[node]
            weighted[node] = (weighted[a] + products[a] * weighted[b]) % MOD

    return left, right, parent, leaves, products, weighted


def binomial_row_sum(n):
    primes, smallest, indices, inverses = prime_tables(n)
    left, right, parent, leaves, products, weighted = weighted_tree(primes, n)

    def update(prime_index, multiplier):
        node = leaves[prime_index]
        products[node] = products[node] * multiplier % MOD
        weighted[node] = weighted[node] * multiplier % MOD
        node = parent[node]
        while node >= 0:
            a = left[node]
            b = right[node]
            first = products[a]
            products[node] = first * products[b] % MOD
            weighted[node] = (weighted[a] + first * weighted[b]) % MOD
            node = parent[node]

    def apply(value, divide=False):
        while value > 1:
            p = int(smallest[value])
            exponent = 0
            power = 1
            while value % p == 0:
                value //= p
                exponent += 1
                power *= p
            prime_index = int(indices[p])
            multiplier = (
                pow(inverses[prime_index], exponent, MOD)
                if divide
                else power
            )
            update(prime_index, multiplier)

    total = 0
    middle = n // 2
    for r in range(middle + 1):
        multiplicity = 1 if n % 2 == 0 and r == middle else 2
        total = (total + multiplicity * (1 + weighted[0])) % MOD
        if r < middle:
            apply(n - r)
            apply(r + 1, divide=True)
    return total


def solve():
    return binomial_row_sum(N)


if __name__ == "__main__":
    print(solve())
