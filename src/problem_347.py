# Problem 347: https://projecteuler.net/problem=347

from sympy import sieve


N = 10_000_000


def largest(p, q, n):
    best = 0
    pp = p

    while pp * q <= n:
        qq = q
        while pp * qq <= n:
            best = max(best, pp * qq)
            qq *= q
        pp *= p

    return best


def solve():
    primes = list(sieve.primerange(2, N // 2 + 1))
    total = 0

    for i, p in enumerate(primes):
        if p * p > N:
            break

        for j in range(i + 1, len(primes)):
            q = primes[j]
            if p * q > N:
                break
            total += largest(p, q, N)

    return total


if __name__ == "__main__":
    print(solve())
