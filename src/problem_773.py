# Problem 773: https://projecteuler.net/problem=773

from itertools import count, islice
from math import comb, prod

from sympy import isprime


def solve(k=97):
    primes = list(islice((p for p in count(7, 10) if isprime(p)), k))
    total = 5 * prod(p - 1 for p in primes)
    for j in range(k + 1):
        r = pow(7, 1 - j, 10)
        total += (-1) ** j * comb(k, j) * (r - 5)
    return prod(primes) * total % 1_000_000_007


if __name__ == "__main__":
    print(solve())
