# Problem 263: https://projecteuler.net/problem=263

from gmpy2 import is_prime
from sympy import primerange


PRIME_OFFSETS = (-9, -3, 3, 9)
GAP_OFFSETS = (-7, -5, -1, 1, 5, 7)
PRACTICAL_OFFSETS = (-8, -4, 0, 4, 8)
WHEEL_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23)
FACTOR_PRIMES = list(primerange(2, 100_000))


def candidate_residues():
    residues = [0]
    mod = 1

    for p in WHEEL_PRIMES:
        nxt = []
        for r in residues:
            for a in range(p):
                n = r + mod * a
                if all((n + o) % p for o in PRIME_OFFSETS):
                    nxt.append(n % (mod * p))
        residues = nxt
        mod *= p

    return sorted(residues), mod


def practical(n):
    reach = 1
    x = n

    for p in FACTOR_PRIMES:
        if p * p > x:
            break
        if x % p:
            continue

        pp = 1
        while x % p == 0:
            x //= p
            pp *= p

        if p > reach + 1:
            return False
        reach *= (pp * p - 1) // (p - 1)

    if x > 1:
        if x > reach + 1:
            return False
        reach *= x + 1

    return True


def engineer(n):
    return (
        all(is_prime(n + o) for o in PRIME_OFFSETS)
        and not any(is_prime(n + o) for o in GAP_OFFSETS)
        and all(practical(n + o) for o in PRACTICAL_OFFSETS)
    )


def solve():
    residues, mod = candidate_residues()
    found = []
    base = 0

    while len(found) < 4:
        for r in residues:
            n = base + r
            if n >= 10 and engineer(n):
                found.append(n)
                if len(found) == 4:
                    break
        base += mod

    return sum(found)


if __name__ == "__main__":
    print(solve())
