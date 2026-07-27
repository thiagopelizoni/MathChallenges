# Problem 457: https://projecteuler.net/problem=457

from sympy import sieve, sqrt_mod


LIMIT = 10_000_000
QUADRATIC_RESIDUES_MODULO_13 = {1, 3, 4, 9, 10, 12}


def smallest_root_modulo_prime_square(prime):
    if prime == 13 or prime % 13 not in QUADRATIC_RESIDUES_MODULO_13:
        return 0

    square_root = int(sqrt_mod(13, prime))
    correction = (
        (13 - square_root * square_root)
        // prime
        * pow(2 * square_root, -1, prime)
        % prime
    )
    square_root += correction * prime

    modulus = prime * prime
    inverse_two = (modulus + 1) // 2
    roots = (
        (3 + square_root) * inverse_two % modulus,
        (3 - square_root) * inverse_two % modulus,
    )
    return min(root for root in roots if root)


def solve():
    return sum(
        smallest_root_modulo_prime_square(prime)
        for prime in sieve.primerange(3, LIMIT + 1)
    )


if __name__ == "__main__":
    print(solve())
