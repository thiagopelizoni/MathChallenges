# Problem 452: https://projecteuler.net/problem=452

from functools import cache
from math import comb, isqrt

from sympy import nextprime, primepi, sieve


N = 10**9
MOD = 1_234_567_891


@cache
def prime_count(n):
    return int(primepi(n))


def count_tuples(n):
    sentinel = int(nextprime(isqrt(n)))
    primes = list(sieve.primerange(2, sentinel + 1))
    weights = [1]
    power = 2
    while power <= n:
        e = len(weights)
        weights.append(comb(n + e - 1, e) % MOD)
        power *= 2

    @cache
    def total(limit, index):
        p0 = primes[index]
        if limit < 2 or p0 > limit:
            return 1
        if p0 * p0 > limit:
            count = prime_count(limit) - prime_count(p0 - 1)
            return (1 + count * weights[1]) % MOD

        root = isqrt(limit)
        count = prime_count(limit) - prime_count(root)
        result = (1 + count * weights[1]) % MOD

        i = index
        while primes[i] <= root:
            p = primes[i]
            prime_power = p
            e = 1
            while prime_power <= limit:
                result += (
                    weights[e]
                    * total(limit // prime_power, i + 1)
                )
                result %= MOD
                prime_power *= p
                e += 1
            i += 1
        return result

    return total(n, 0)


def solve():
    return count_tuples(N)


if __name__ == "__main__":
    print(solve())
