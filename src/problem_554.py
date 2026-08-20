# Problem 554: https://projecteuler.net/problem=554

import numpy as np
from sympy import fibonacci


MOD = 100_000_007
HALF = (MOD - 1) // 2
CHUNK = 1_000_000


def range_product(start, stop):
    result = 1
    while start < stop:
        end = min(start + CHUNK, stop)
        values = np.arange(start, end, dtype=np.uint64)
        while len(values) > 1:
            paired = len(values) // 2 * 2
            values[:paired // 2] = values[:paired:2] * values[1:paired:2] % MOD
            if paired < len(values):
                values[paired // 2] = values[-1]
                values = values[:paired // 2 + 1]
            else:
                values = values[:paired // 2]
        result = result * int(values[0]) % MOD
        start = end
    return result


def digits(n):
    result = []
    while n:
        n, digit = divmod(n, MOD)
        result.append(digit)
    return result


def solve():
    numbers = [int(fibonacci(i)) for i in range(2, 91)]
    expansions = [digits(n) for n in numbers]
    needed = set()
    for expansion in expansions:
        if all(digit <= HALF for digit in expansion):
            needed.update(expansion)
    points = sorted(needed.union(2 * digit for digit in needed))

    factorials = {}
    value = 1
    start = 1
    for point in points:
        value = value * range_product(start, point + 1) % MOD
        factorials[point] = value
        start = point + 1

    central = {}
    for digit in needed:
        denominator = factorials[digit] * factorials[digit] % MOD
        central[digit] = factorials[2 * digit] * pow(denominator, -1, MOD) % MOD

    total = 0
    for n, expansion in zip(numbers, expansions):
        if any(digit > HALF for digit in expansion):
            choose = 0
        else:
            choose = 1
            for digit in expansion:
                choose = choose * central[digit] % MOD
        total += 8 * choose - 3 * n * n - 2 * n - 7
    return total % MOD


if __name__ == "__main__":
    print(solve())
