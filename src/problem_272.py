# Problem 272: https://projecteuler.net/problem=272

from bisect import bisect_left, bisect_right
from math import isqrt, prod


LIMIT = 10**11
SPECIAL_MIN = [7, 13, 19, 31, 37]
MAX_SPECIAL_PRIME = LIMIT // (9 * prod(SPECIAL_MIN[:3]))
NEUTRAL_LIMIT = LIMIT // (9 * prod(SPECIAL_MIN[:4]))


def primes_1_mod_3(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"

    i = 2
    while i * i <= n:
        if sieve[i]:
            start = i * i
            sieve[start : n + 1 : i] = b"\x00" * ((n - start) // i + 1)
        i += 1

    return [i for i in range(n + 1) if sieve[i] and i % 3 == 1]


def neutral_prefix(n):
    spf = [0] * (n + 1)
    for i in range(2, n + 1):
        if spf[i] == 0:
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i

    ok = bytearray(n + 1)
    ok[1] = 1
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        if i > 1:
            p = spf[i]
            ok[i] = ok[i // p] and p % 3 == 2
        prefix[i] = prefix[i - 1] + i * ok[i]

    return prefix


def min_products(primes, kmax):
    mins = [[1] * (len(primes) + 1)]
    for r in range(1, kmax + 1):
        row = [LIMIT + 1] * (len(primes) + 1)
        prev = mins[-1]
        for i in range(len(primes) - r + 1):
            v = primes[i] * prev[i + 1]
            row[i] = v if v <= LIMIT else LIMIT + 1
        mins.append(row)
    return mins


def solve():
    primes = primes_1_mod_3(MAX_SPECIAL_PRIME)
    neutral = neutral_prefix(NEUTRAL_LIMIT)
    neutral_with_3 = [neutral[i] + 3 * neutral[i // 3] for i in range(NEUTRAL_LIMIT + 1)]
    prime_sum = [0]
    mins = min_products(primes, 5)

    for p in primes:
        prime_sum.append(prime_sum[-1] + p)

    def tail_sum(start, m, prefix):
        top = LIMIT // m
        end = bisect_right(primes, top)
        if start >= end:
            return 0

        total = 0
        lo = primes[start]
        while lo <= top:
            y = top // lo
            hi = min(top, top // y)
            a = bisect_left(primes, lo, start, end)
            b = bisect_right(primes, hi, a, end)
            total += (prime_sum[b] - prime_sum[a]) * prefix[y]
            lo = hi + 1

        for p in primes[start : bisect_right(primes, isqrt(top), start, end)]:
            q = p * p
            while q <= top:
                total += q * prefix[top // q]
                q *= p

        return m * total

    def search(start, r, m, prefix):
        if r == 1:
            return tail_sum(start, m, prefix)

        total = 0
        for i in range(start, len(primes) - r + 1):
            p = primes[i]
            t = mins[r - 1][i + 1]
            if m * p * t > LIMIT:
                break

            q = p
            while m * q * t <= LIMIT:
                total += search(i + 1, r - 1, m * q, prefix)
                q *= p
        return total

    total = search(0, 5, 1, neutral_with_3)

    q = 9
    while q * prod(SPECIAL_MIN[:4]) <= LIMIT:
        total += search(0, 4, q, neutral)
        q *= 3

    return total


if __name__ == "__main__":
    print(solve())
