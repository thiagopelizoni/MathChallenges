# Problem 221: https://projecteuler.net/problem=221
from math import isqrt


TARGET = 150_000


def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p * p:n + 1:p] = b"\x00" * ((n - p * p) // p + 1)
    return [p for p in range(n + 1) if sieve[p]]


def divisors(n, primes):
    ds = [1]
    m = n
    for p in primes:
        if p * p > m:
            break
        if m % p == 0:
            base = ds[:]
            q = 1
            while m % p == 0:
                m //= p
                q *= p
                ds.extend(d * q for d in base)
    if m > 1:
        ds.extend(d * m for d in ds[:])
    return ds


def solve():
    primes = primes_upto(100_000)
    values = set()
    bound = None
    n = 1

    while bound is None or 4 * n**3 <= bound:
        m = n * n + 1
        for d in divisors(m, primes):
            if d * d <= m:
                values.add(n * (n + d) * (n + m // d))

        if n % 10_000 == 0 and len(values) >= TARGET:
            bound = sorted(values)[TARGET - 1]
        n += 1

    return sorted(values)[TARGET - 1]


if __name__ == "__main__":
    print(solve())
