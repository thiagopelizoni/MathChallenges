# Problem 536: https://projecteuler.net/problem=536

from bisect import bisect_right
from math import gcd, isqrt

from sympy import primerange


LIMIT = 10**12


def solve():
    prime_limit = 2 + isqrt(LIMIT + 4)
    primes = list(primerange(3, prime_limit + 1))
    prime_set = set(primes)
    values = {1, 2, 3, 5}

    def search(product, lam, start):
        end = bisect_right(primes, isqrt(LIMIT // product))
        for i in range(start, end):
            p = primes[i]
            n = product * p
            d = p - 1
            new_lam = lam // gcd(lam, d) * d
            g = gcd(n, new_lam)
            if 3 % g:
                continue

            step = new_lam // g
            q = 0 if step == 1 else (-3 // g * pow(n // g, -1, step)) % step
            if q <= p:
                q += (p - q) // step * step + step
            upper = min(LIMIT // n, n + 4, prime_limit)
            while q <= upper:
                if q in prime_set and (n + 3) % (q - 1) == 0:
                    values.add(n * q)
                q += step

            if i + 1 < len(primes) and n <= LIMIT // primes[i + 1] ** 2:
                search(n, new_lam, i + 1)

    search(1, 1, 0)
    return sum(values)


if __name__ == "__main__":
    print(solve())
