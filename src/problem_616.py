# Problem 616: https://projecteuler.net/problem=616

from math import isqrt

from sympy import isprime, primerange


def solve():
    lim = 10**12
    root = isqrt(lim)
    primes = set(primerange(2, root + 1))
    creative = set()

    for a in range(2, root + 1):
        n = a * a
        b = 2
        while n <= lim:
            if a not in primes or not isprime(b):
                creative.add(n)
            n *= a
            b += 1

    creative.discard(16)
    return sum(creative)


if __name__ == "__main__":
    print(solve())
