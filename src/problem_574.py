# Problem 574: https://projecteuler.net/problem=574
from math import isqrt

from sympy import primerange


def solve():
    limit = 3800
    small_primes = list(primerange(2, isqrt(limit) + 1))
    modulus = 1
    residues = [0]
    next_prime = 0
    total = 0

    for p in primerange(2, limit):
        while next_prime < len(small_primes) and small_primes[next_prime] ** 2 < p:
            r = small_primes[next_prime]
            inverse = pow(modulus, -1, r)
            old_modulus = modulus
            modulus *= r
            extended = []

            for x in residues:
                extended.append(x + (-x * inverse % r) * old_modulus)
                extended.append(x + ((1 - x) * inverse % r) * old_modulus)

            residues = extended
            next_prime += 1

        low = (p + 1) // 2
        best = None

        for x in residues:
            a = p * x % modulus
            if a < low:
                a += (low - a + modulus - 1) // modulus * modulus
            if a % p == 0:
                a += modulus
            if best is None or a < best:
                best = a

        total += best

    return total


if __name__ == "__main__":
    print(solve())
