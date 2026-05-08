# Problem 187: https://projecteuler.net/problem=187
from array import array
from bisect import bisect_right
from math import isqrt


def primes_upto(n):
    sieve = bytearray(b"\x01") * (n // 2 + 1)
    sieve[0] = 0

    for i in range(1, isqrt(n) // 2 + 1):
        if sieve[i]:
            p = 2 * i + 1
            start = p * p // 2
            sieve[start::p] = b"\x00" * ((len(sieve) - 1 - start) // p + 1)

    primes = array("I", [2])
    primes.extend(2 * i + 1 for i in range(1, len(sieve)) if sieve[i])
    return primes


def solve():
    limit = 100_000_000
    primes = primes_upto((limit - 1) // 2)
    total = 0

    for i, p in enumerate(primes):
        if p * p >= limit:
            break
        total += bisect_right(primes, (limit - 1) // p) - i

    return total


if __name__ == "__main__":
    print(solve())
