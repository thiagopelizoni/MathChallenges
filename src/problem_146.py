# Problem 146: https://projecteuler.net/problem=146

from sympy import isprime


PRIME_OFFSETS = (1, 3, 7, 9, 13, 27)
GAP_OFFSETS = tuple(a for a in range(5, 27, 2) if a not in PRIME_OFFSETS)
SMALL_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23)


def allowed_residues():
    residues = [0]
    mod = 1

    for p in SMALL_PRIMES:
        next_residues = []
        for r0 in residues:
            for r in range(r0, mod * p, mod):
                if all((r * r + a) % p for a in PRIME_OFFSETS):
                    next_residues.append(r)
        residues = next_residues
        mod *= p

    return mod, residues


def has_prime_pattern(n):
    n2 = n * n
    return (
        all(isprime(n2 + a) for a in PRIME_OFFSETS)
        and not any(isprime(n2 + a) for a in GAP_OFFSETS)
    )


def solve():
    lim = 150_000_000
    mod, residues = allowed_residues()
    total = 0

    for r in residues:
        start = r or mod
        for n in range(start, lim, mod):
            if has_prime_pattern(n):
                total += n

    return total


if __name__ == "__main__":
    print(solve())
