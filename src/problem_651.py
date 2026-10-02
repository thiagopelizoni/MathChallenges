# Problem 651: https://projecteuler.net/problem=651

from collections import Counter
from math import comb, gcd

from sympy import divisors, totient


MOD = 1_000_000_007


def cycle_types(n):
    types = []
    for d in divisors(n):
        types.append(([(d, n // d)], int(totient(d))))
    if n % 2:
        types.append(([(1, 1), (2, (n - 1) // 2)], n))
    else:
        types.append(([(1, 2), (2, (n - 2) // 2)], n // 2))
        types.append(([(2, n // 2)], n // 2))
    return types


def count_patterns(m, a, b):
    counts = Counter()
    rows = cycle_types(a)
    columns = cycle_types(b)
    for x, u in rows:
        for y, v in columns:
            cycles = sum(cx * cy * gcd(dx, dy) for dx, cx in x for dy, cy in y)
            counts[cycles] += u * v

    coefficients = [(-1) ** (m - j) * comb(m, j) for j in range(m + 1)]
    total = 0
    for cycles, weight in counts.items():
        if cycles < m:
            continue
        onto = sum(coefficient * pow(j, cycles, MOD) for j, coefficient in enumerate(coefficients))
        total = (total + weight * onto) % MOD
    return total * pow(4 * a * b, -1, MOD) % MOD


def solve():
    fib = [0, 1]
    for i in range(2, 41):
        fib.append(fib[i - 1] + fib[i - 2])
    return sum(count_patterns(i, fib[i - 1], fib[i]) for i in range(4, 41)) % MOD


if __name__ == "__main__":
    print(solve())
