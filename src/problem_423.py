# Problem 423: https://projecteuler.net/problem=423

from sympy import sieve


MOD = 1_000_000_007
N = 50_000_000


def solve():
    primes = iter(sieve.primerange(2, N + 1))
    next_prime = int(next(primes, N + 1))
    count = term = 1
    prime_count = 0
    total = 6

    for n in range(1, N):
        if n + 1 == next_prime:
            inv = pow(prime_count + 1, -1, MOD)
            count = (
                6 * count + term * (n - 1 - prime_count) * inv
            ) % MOD
            term = term * n * inv % MOD
            prime_count += 1
            next_prime = int(next(primes, N + 1))
        else:
            count = (6 * count - term) % MOD
            term = term * 5 * n * pow(n - prime_count, -1, MOD) % MOD
        total = (total + 6 * count) % MOD

    return total


if __name__ == "__main__":
    print(solve())
