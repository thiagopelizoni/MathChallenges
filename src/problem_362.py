# Problem 362: https://projecteuler.net/problem=362

from bisect import bisect_right
from collections import defaultdict
from functools import lru_cache
from itertools import combinations, product
from math import isqrt, prod

from sympy import integer_nthroot, sieve
from sympy.utilities.iterables import partitions


N = 10_000_000_000
SMALL_LIMIT = 1_000_000
PHI_X = 100_000
PHI_A = 100

PRIMES = tuple(sieve.primerange(2, SMALL_LIMIT + 1))
COUNT_PRIMES = tuple(p for p in PRIMES if p <= isqrt(N))
BASE_PRIMES = tuple(sieve.primerange(2, 200))


def prime_prefix():
    prefix = [0] * (SMALL_LIMIT + 1)
    pos = 0
    for n in range(1, SMALL_LIMIT + 1):
        prefix[n] = prefix[n - 1]
        if pos < len(PRIMES) and PRIMES[pos] == n:
            prefix[n] += 1
            pos += 1
    return tuple(prefix)


def phi_rows():
    rows = [[0] * PHI_X for _ in range(PHI_A)]
    for x in range(PHI_X):
        rows[0][x] = x

    for a in range(1, PHI_A):
        p = PRIMES[a - 1]
        prev = rows[a - 1]
        row = rows[a]
        for x in range(PHI_X):
            row[x] = prev[x] - prev[x // p]
    return tuple(tuple(row) for row in rows)


PI_SMALL = prime_prefix()
PHI_ROWS = phi_rows()


def iroot(n, k):
    return int(integer_nthroot(n, k)[0])


@lru_cache(maxsize=None)
def phi(x, a):
    if a == 0:
        return x
    if a < PHI_A and x < PHI_X:
        return PHI_ROWS[a][x]
    return phi(x, a - 1) - phi(x // PRIMES[a - 1], a - 1)


@lru_cache(maxsize=None)
def prime_count(x):
    if x <= SMALL_LIMIT:
        return PI_SMALL[x]

    a = prime_count(iroot(x, 4))
    b = prime_count(isqrt(x))
    c = prime_count(iroot(x, 3))
    total = phi(x, a) + ((b + a - 2) * (b - a + 1)) // 2

    for i in range(a, b):
        w = x // PRIMES[i]
        total -= prime_count(w)
        if i < c:
            lim = prime_count(isqrt(w))
            for j in range(i, lim):
                total -= prime_count(w // PRIMES[j]) - j
    return total


@lru_cache(maxsize=None)
def squarefree_factorizations(exps):
    target = tuple(sorted(exps, reverse=True))
    states = tuple(product(*(range(e + 1) for e in target)))
    subsets = tuple(s for s in product((0, 1), repeat=len(target)) if any(s))
    dp = {(0,) * len(target): 1}

    for subset in subsets:
        for state in states:
            ways = dp.get(state, 0)
            if not ways:
                continue

            nxt = tuple(state[i] + subset[i] for i in range(len(target)))
            if all(nxt[i] <= target[i] for i in range(len(target))):
                dp[nxt] = dp.get(nxt, 0) + ways

    return dp[target]


def max_omega(limit):
    total = 0
    n = 1
    while n * 2 <= limit:
        n *= 2
        total += 1
    return total


def exponent_patterns(limit):
    out = set()
    for total in range(1, max_omega(limit) + 1):
        for part in partitions(total):
            exps = []
            for exp, count in part.items():
                exps.extend([exp] * count)

            exps = tuple(sorted(exps, reverse=True))
            least = prod(p**e for p, e in zip(BASE_PRIMES, exps))
            if least <= limit:
                out.add(exps)
    return out


@lru_cache(maxsize=None)
def squarefree_count(limit, count, min_prime):
    if count == 0:
        return 1
    if count == 1:
        return prime_count(limit) - prime_count(min_prime)

    total = 0
    start = bisect_right(COUNT_PRIMES, min_prime)
    for p in COUNT_PRIMES[start:]:
        if p**count > limit:
            break
        total += squarefree_count(limit // p, count - 1, p)
    return total


@lru_cache(maxsize=None)
def squarefree_count_excluding(limit, count, excluded):
    excluded = tuple(excluded)
    if not excluded:
        return squarefree_count(limit, count, 1)

    total = 0
    for size in range(min(count, len(excluded)) + 1):
        sign = -1 if size % 2 else 1
        for fixed in combinations(excluded, size):
            fixed_product = prod(fixed) if fixed else 1
            if fixed_product <= limit:
                total += sign * squarefree_count_excluding(
                    limit // fixed_product,
                    count - size,
                    tuple(sorted(fixed)),
                )
    return total


def grouped_patterns():
    groups = defaultdict(dict)
    for exps in exponent_patterns(N):
        high = tuple(e for e in exps if e > 1)
        ones = len(exps) - len(high)
        groups[high][ones] = squarefree_factorizations(exps)
    return groups


def count_group(high, coeffs):
    high = tuple(high)
    coeffs = tuple(sorted(coeffs.items()))

    @lru_cache(maxsize=None)
    def rec(pos, limit, chosen):
        if pos == len(high):
            return sum(
                coef * squarefree_count_excluding(
                    limit,
                    ones,
                    tuple(sorted(chosen)),
                )
                for ones, coef in coeffs
            )

        e = high[pos]
        min_prime = chosen[-1] if pos > 0 and high[pos - 1] == e else 1
        max_p = iroot(limit, e)
        total = 0
        chosen_set = set(chosen)
        start = bisect_right(COUNT_PRIMES, min_prime)

        for p in COUNT_PRIMES[start:]:
            if p > max_p:
                break
            if p in chosen_set:
                continue
            total += rec(pos + 1, limit // (p**e), chosen + (p,))
        return total

    return rec(0, N, ())


def solve():
    return sum(count_group(high, coeffs) for high, coeffs in grouped_patterns().items())


if __name__ == "__main__":
    print(solve())
