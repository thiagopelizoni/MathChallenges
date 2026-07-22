# Problem 428: https://projecteuler.net/problem=428

from functools import cache
from math import isqrt

from sympy import primerange


N = 1_000_000_000
COEFFICIENTS = {
    "D": 4,
    "D2": 6,
    "D3": 2,
    "D23": 4,
    "L": 2,
    "L2": 4,
    "E": -1,
    "E2": -2,
    "J": -1,
}
CORRECTIONS = {
    "D": (0, 0),
    "D2": (2, 0),
    "D3": (0, 2),
    "D23": (2, 2),
    "L": (0, 2),
    "L2": (2, 2),
    "E": (0, 3),
    "E2": (2, 3),
}


def solve():
    values = []
    i = 1
    while i <= N:
        value = N // i
        values.append(value)
        i = N // value + 1

    index = {value: i for i, value in enumerate(values)}
    prime_counts = [value - 1 for value in values]
    prime_characters = [0 if value % 3 == 1 else -1 for value in values]
    primes = tuple(primerange(2, isqrt(N) + 1))

    for p in primes:
        count_before = prime_counts[index[p - 1]]
        character_before = prime_characters[index[p - 1]]
        character = 0 if p == 3 else (1 if p % 3 == 1 else -1)
        for j, value in enumerate(values):
            if value < p * p:
                break
            q = index[value // p]
            prime_counts[j] -= prime_counts[q] - count_before
            prime_characters[j] -= character * (
                prime_characters[q] - character_before
            )

    def prime_sum(x, kind):
        count = prime_counts[index[x]]
        character = prime_characters[index[x]]
        if kind == "J":
            return count + 2 * character - (1 if x >= 3 else 0)
        at_two, at_three = CORRECTIONS[kind]
        return (
            3 * count
            - (at_two if x >= 2 else 0)
            - (at_three if x >= 3 else 0)
        )

    def prime_power(kind, p, exponent):
        if kind in ("D2", "D23", "L2", "E2") and p == 2:
            return 1
        if kind in ("D3", "D23") and p == 3:
            return 1
        if kind in ("L", "L2") and p == 3:
            return 2 * exponent - 1
        if kind in ("E", "E2", "J") and p == 3:
            return 0
        if kind == "J" and p % 3 == 2:
            return -1 if exponent % 2 else 1
        return 2 * exponent + 1

    def summatory(kind):
        @cache
        def recurse(x, start):
            if start and x < primes[start - 1]:
                return 1
            lower = primes[start - 1] if start else 1
            total = 1 + prime_sum(x, kind) - prime_sum(lower, kind)
            for j in range(start, len(primes)):
                p = primes[j]
                if p * p > x:
                    break
                total += prime_power(kind, p, 1) * (
                    recurse(x // p, j + 1) - 1
                )
                power = p * p
                exponent = 2
                while power <= x:
                    total += prime_power(kind, p, exponent) * recurse(
                        x // power, j + 1
                    )
                    power *= p
                    exponent += 1
            return total

        return recurse(N, 0)

    return sum(
        coefficient * summatory(kind)
        for kind, coefficient in COEFFICIENTS.items()
    ) // 2


if __name__ == "__main__":
    print(solve())
