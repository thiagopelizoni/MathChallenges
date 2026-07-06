# Problem 365: https://projecteuler.net/problem=365

from itertools import combinations

from sympy import sieve
from sympy.ntheory.residue_ntheory import binomial_mod


N = 10**18
K = 10**9


def binomial_residues(primes):
    return {p: int(binomial_mod(N, K, p)) for p in primes}


def modular_inverses(primes):
    return {(p, q): pow(p, -1, q) for p in primes for q in primes if p != q}


def crt_value(p, q, r, residues, inverses):
    ap = residues[p]
    aq = residues[q]
    ar = residues[r]

    t = (aq - ap) * inverses[p, q] % q
    x = ap + p * t
    u = (ar - x) * (inverses[p, r] * inverses[q, r] % r) % r
    return x + p * q * u


def solve():
    primes = tuple(sieve.primerange(1001, 5000))
    residues = binomial_residues(primes)
    inverses = modular_inverses(primes)
    return sum(crt_value(p, q, r, residues, inverses) for p, q, r in combinations(primes, 3))


if __name__ == "__main__":
    print(solve())
