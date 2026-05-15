# Problem 216: https://projecteuler.net/problem=216
from math import isqrt


def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"

    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start:n + 1:p] = b"\x00" * ((n - start) // p + 1)

    return sieve


def sqrt_mod(n, p):
    if p % 4 == 3:
        return pow(n, (p + 1) // 4, p)

    q = p - 1
    s = 0
    while q % 2 == 0:
        s += 1
        q //= 2

    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1

    c = pow(z, q, p)
    x = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s

    while t != 1:
        i = 1
        u = t * t % p
        while u != 1:
            u = u * u % p
            i += 1

        b = pow(c, 1 << (m - i - 1), p)
        x = x * b % p
        t = t * b * b % p
        c = b * b % p
        m = i

    return x


def count(limit):
    pmax = isqrt(2 * limit * limit - 1)
    primes = primes_upto(pmax)
    composite = bytearray(limit + 1)
    composite[0] = composite[1] = 1

    for p in range(3, pmax + 1, 2):
        if not primes[p] or p & 7 not in (1, 7):
            continue

        r = sqrt_mod((p + 1) // 2, p)
        for a in (r, p - r):
            if a > limit:
                continue
            start = a
            if 2 * a * a - 1 == p:
                start += p
            if start <= limit:
                composite[start:limit + 1:p] = b"\x01" * (
                    (limit - start) // p + 1
                )

    return composite.count(0)


def solve():
    return count(50_000_000)


if __name__ == "__main__":
    print(solve())
