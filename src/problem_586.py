# Problem 586: https://projecteuler.net/problem=586

from bisect import bisect_right
from math import isqrt, prod

from sympy import factorint, integer_nthroot, nextprime, primerange


def multiplicative_partitions(n, least=2):
    yield (n,)
    for d in range(least, isqrt(n) + 1):
        if n % d == 0:
            for tail in multiplicative_partitions(n // d, d):
                yield (d,) + tail


def first_split_primes(count):
    primes = []
    p = 1
    while len(primes) < count:
        p = nextprime(p)
        if p % 5 in (1, 4):
            primes.append(p)
    return primes


def solve():
    n = 10**15
    r = 40

    patterns = []
    for ways in (2 * r, 2 * r + 1):
        for factors in multiplicative_partitions(ways):
            patterns.append(tuple(sorted((d - 1 for d in factors), reverse=True)))

    first = first_split_primes(max(map(len, patterns)))
    patterns = [
        exponents
        for exponents in patterns
        if prod(p**e for p, e in zip(first, exponents)) <= n
    ]

    max_neutral = max(
        n // prod(p**e for p, e in zip(first, exponents))
        for exponents in patterns
    )
    max_prime = max(
        integer_nthroot(
            n // prod(p**e for p, e in zip(first, exponents[:-1])),
            exponents[-1],
        )[0]
        for exponents in patterns
    )

    primes = [p for p in primerange(2, max_prime + 1) if p % 5 in (1, 4)]
    powers = {e: [p**e for p in primes] for exponents in patterns for e in exponents}

    neutral = []
    for m in range(1, isqrt(max_neutral) + 1):
        if all(p % 5 in (2, 3) for p in factorint(m)):
            h = m * m
            while h <= max_neutral:
                neutral.append(h)
                h *= 5
    neutral.sort()

    def count_pattern(limit, exponents):
        used = []

        def equal_powers(remainder, exponent, count, start):
            prime_powers = powers[exponent]
            end = bisect_right(prime_powers, remainder)
            if count == 1:
                total = max(0, end - start)
                for index in used:
                    if start <= index < end:
                        total -= 1
                return total

            total = 0
            for index in range(start, end):
                if index in used:
                    continue
                smallest_tail = 1
                found = 0
                next_index = index + 1
                while found < count - 1 and next_index < len(primes):
                    if next_index not in used:
                        smallest_tail *= prime_powers[next_index]
                        found += 1
                    next_index += 1
                if found < count - 1 or prime_powers[index] * smallest_tail > remainder:
                    break
                total += equal_powers(
                    remainder // prime_powers[index], exponent, count - 1, index + 1
                )
            return total

        def visit(position, remainder):
            exponent = exponents[position]
            if all(e == exponent for e in exponents[position:]):
                return equal_powers(remainder, exponent, len(exponents) - position, 0)

            total = 0
            prime_powers = powers[exponent]
            for index in range(bisect_right(prime_powers, remainder)):
                if index not in used:
                    used.append(index)
                    total += visit(position + 1, remainder // prime_powers[index])
                    used.pop()
            return total

        return visit(0, limit)

    return sum(
        count_pattern(n // h, exponents)
        for h in neutral
        for exponents in patterns
    )


if __name__ == "__main__":
    print(solve())
