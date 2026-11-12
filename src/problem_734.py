# Problem 734: https://projecteuler.net/problem=734

from sympy import inverse_mobius_transform, mobius_transform, sieve


def solve(n=10**6, k=999983):
    mod = 1_000_000_007
    primes = list(sieve.primerange(n + 1))
    counts = [0] * (n + 1)
    for p in primes:
        counts[p] = 1

    counts = mobius_transform(counts)
    counts = [pow(int(c), k, mod) for c in counts]
    counts = inverse_mobius_transform(counts)
    return int(sum(counts[p] for p in primes) % mod)


if __name__ == "__main__":
    print(solve())
