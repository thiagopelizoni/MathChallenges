# Problem 370: https://projecteuler.net/problem=370

from array import array
from math import gcd, isqrt

from sympy import sieve


N = 25_000_000_000_000


def signed_divisor_table(n):
    mu = [0] + list(sieve.mobiusrange(1, n + 1))
    counts = array("I", [0]) * (n + 2)

    for d in range(1, n + 1):
        if mu[d]:
            for k in range(d, n + 1, d):
                counts[k] += 1

    offsets = array("I", [0]) * (n + 2)
    total = 0
    for i in range(1, n + 2):
        offsets[i] = total
        if i <= n:
            total += counts[i]

    terms = array("i", [0]) * total
    cursor = list(offsets)
    for d in range(1, n + 1):
        if mu[d]:
            sd = d if mu[d] > 0 else -d
            for k in range(d, n + 1, d):
                terms[cursor[k]] = sd
                cursor[k] += 1

    return offsets, terms


def coprime_count(terms, start, end, a, b):
    total = 0
    a -= 1
    while start < end:
        d = terms[start]
        if d > 0:
            total += b // d - a // d
        else:
            d = -d
            total -= b // d - a // d
        start += 1
    return total


def count(limit):
    nmax = isqrt(limit // 3)
    threshold = int(limit ** (1 / 3))
    offsets, terms = signed_divisor_table(nmax)
    total = 0

    for n in range(1, nmax + 1):
        nn = n * n
        mmax = (n + isqrt(5 * nn)) // 2
        pmax = (isqrt(4 * limit - 3 * nn) - n) // 2
        if pmax < mmax:
            mmax = pmax
        if mmax < n:
            continue

        if n <= threshold:
            for m in range(n, mmax + 1):
                if gcd(m, n) == 1:
                    total += limit // (m * m + m * n + nn)
            continue

        start, end = offsets[n], offsets[n + 1]
        m = n
        while m <= mmax:
            q = limit // (m * m + m * n + nn)
            mend = (isqrt(4 * (limit // q) - 3 * nn) - n) // 2
            if mend > mmax:
                mend = mmax
            total += q * coprime_count(terms, start, end, m, mend)
            m = mend + 1

    return total


def solve():
    return count(N)


if __name__ == "__main__":
    print(solve())
