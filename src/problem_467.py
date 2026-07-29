# Problem 467: https://projecteuler.net/problem=467

import numpy as np
from sympy import composite, prime, sieve


N = 10_000
MOD = 1_000_000_007


def digital_root_sequences(n):
    prime_limit = int(prime(n))
    primes = np.fromiter(
        (1 + (p - 1) % 9 for p in sieve.primerange(2, prime_limit + 1)),
        dtype=np.uint8,
        count=n,
    )

    composite_limit = int(composite(n))
    prime_set = set(sieve.primerange(2, composite_limit + 1))
    composites = np.fromiter(
        (
            1 + (x - 1) % 9
            for x in range(4, composite_limit + 1)
            if x not in prime_set
        ),
        dtype=np.uint8,
        count=n,
    )
    return primes, composites


def smallest_superinteger_mod(a, b):
    rows = len(a)
    columns = len(b)
    lcs = np.zeros((rows + 1, columns + 1), dtype=np.uint16)

    for i in range(rows - 1, -1, -1):
        candidates = np.maximum(
            lcs[i + 1, :-1],
            lcs[i + 1, 1:] + (b == a[i]),
        )
        np.maximum.accumulate(
            candidates[::-1],
            out=lcs[i, :-1][::-1],
        )

    i = 0
    j = 0
    result = 0
    while i < rows or j < columns:
        if i == rows:
            digit = b[j]
            j += 1
        elif j == columns:
            digit = a[i]
            i += 1
        elif a[i] == b[j]:
            digit = a[i]
            i += 1
            j += 1
        elif lcs[i + 1, j] > lcs[i, j + 1]:
            digit = a[i]
            i += 1
        elif lcs[i + 1, j] < lcs[i, j + 1]:
            digit = b[j]
            j += 1
        elif a[i] < b[j]:
            digit = a[i]
            i += 1
        else:
            digit = b[j]
            j += 1
        result = (10 * result + int(digit)) % MOD

    return result


def solve():
    return smallest_superinteger_mod(*digital_root_sequences(N))


if __name__ == "__main__":
    print(solve())
