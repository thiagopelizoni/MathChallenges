# Problem 200: https://projecteuler.net/problem=200
from math import isqrt

from sympy import isprime, primerange


DIGITS = "0123456789"


def prime_proof(n):
    s = str(n)
    for i, old in enumerate(s):
        for d in DIGITS:
            if d == old or i == 0 and d == "0":
                continue
            if isprime(int(s[:i] + d + s[i + 1:])):
                return False
    return True


def squbes(limit, needle):
    primes = list(primerange(2, isqrt(limit // 8) + 2))
    found = set()

    for q in primes:
        q3 = q**3
        if 4 * q3 > limit:
            break

        for p in primes:
            n = p * p * q3
            if n > limit:
                break
            if p != q and needle in str(n):
                found.add(n)

    return sorted(found)


def solve():
    limit = 100_000_000
    while True:
        found = [n for n in squbes(limit, "200") if prime_proof(n)]
        if len(found) >= 200:
            return found[199]
        limit *= 2


if __name__ == "__main__":
    print(solve())
