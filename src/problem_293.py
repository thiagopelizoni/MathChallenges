# Problem 293: https://projecteuler.net/problem=293

from math import isqrt


LIM = 10**9


def prime_list(n):
    s = bytearray(b"\x01") * (n + 1)
    s[:2] = b"\x00\x00"

    for p in range(2, isqrt(n) + 1):
        if s[p]:
            s[p * p:n + 1:p] = b"\x00" * ((n - p * p) // p + 1)

    return [p for p in range(n + 1) if s[p]]


primes = prime_list(100_000)


def is_prime(n):
    for p in primes:
        if p * p > n:
            return n > 1
        if n % p == 0:
            return n == p

    return True


def admissible(i, n, xs):
    if i == len(primes):
        return

    n *= primes[i]
    while n < LIM:
        xs.append(n)
        admissible(i + 1, n, xs)
        n *= primes[i]


def fortunate(n):
    m = 3
    while not is_prime(n + m):
        m += 2
    return m


def solve():
    xs = []
    admissible(0, 1, xs)
    return sum({fortunate(n) for n in xs})


if __name__ == "__main__":
    print(solve())
