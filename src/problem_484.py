# Problem 484: https://projecteuler.net/problem=484

from math import isqrt

import numpy as np
from sympy import integer_nthroot, sieve


LIMIT = 5 * 10**15
CHUNK_SIZE = 1_000_000
EXCEPTIONAL_PRIMES = (2, 3, 5, 7, 11, 13)


def prime_power_gcd(prime, exponent):
    if exponent == 0:
        return 1
    power = exponent if exponent % prime == 0 else exponent - 1
    return prime**power


def convolution_factor(prime, exponent):
    if exponent == 0:
        return 1
    return prime_power_gcd(prime, exponent) - prime_power_gcd(
        prime, exponent - 1
    )


def generic_factor(prime, exponent):
    if exponent == 0:
        return 1
    return (prime - 1) * prime ** (exponent - 2)


def exact_sum(values, maximum):
    block_size = max(1, int(np.iinfo(np.int64).max) // maximum)
    total = 0
    for start in range(0, values.size, block_size):
        total += int(
            values[start : start + block_size].sum(dtype=np.int64)
        )
    return total


def correction_tables(limit):
    tables = {}
    root = isqrt(limit)
    for prime in EXCEPTIONAL_PRIMES:
        maximum = 0
        power = prime
        while power <= root:
            maximum += 1
            power *= prime
        old = np.array(
            [
                generic_factor(prime, 2 * exponent)
                for exponent in range(maximum + 1)
            ],
            dtype=np.int64,
        )
        even = np.array(
            [
                convolution_factor(prime, 2 * exponent)
                for exponent in range(maximum + 1)
            ],
            dtype=np.int64,
        )
        odd = np.array(
            [
                convolution_factor(prime, 2 * exponent + 3)
                for exponent in range(maximum + 1)
            ],
            dtype=np.int64,
        )
        tables[prime] = old, even, odd
    return tables


def factor_even_segment(low, high, primes):
    numbers = np.arange(low, high + 1, dtype=np.int64)
    remaining = numbers.copy()
    weights = np.ones(numbers.size, dtype=np.int64)
    valuations = {
        prime: np.zeros(numbers.size, dtype=np.uint8)
        for prime in EXCEPTIONAL_PRIMES
    }

    for prime in primes:
        if prime * prime > high and prime not in EXCEPTIONAL_PRIMES:
            break
        power = prime
        while power <= high:
            first = (-low) % power
            if first < numbers.size:
                remaining[first::power] //= prime
                multiplier = prime - 1 if power == prime else prime * prime
                weights[first::power] *= multiplier
                if prime in valuations:
                    valuations[prime][first::power] += 1
            if power > high // prime:
                break
            power *= prime

    mask = remaining > 1
    weights[mask] *= remaining[mask] - 1
    return numbers, weights, valuations


def powerful_groups(limit):
    bound = integer_nthroot(limit, 3)[0]
    mobius = np.fromiter(
        sieve.mobiusrange(1, bound + 1), dtype=np.int8, count=bound
    )
    totients = np.zeros(bound + 1, dtype=np.int64)
    totients[1:] = np.fromiter(
        sieve.totientrange(1, bound + 1), dtype=np.int64, count=bound
    )

    groups = {}
    # In d = a^2 b^3, b is squarefree.  Even b can be omitted because
    # the convolution factor at every odd power of 2 is zero.
    for cube_root in range(1, bound + 1, 2):
        if mobius[cube_root - 1] == 0:
            continue
        state = 1
        for prime in EXCEPTIONAL_PRIMES[1:]:
            if cube_root % prime == 0:
                state *= prime
        quotient = limit // cube_root**3
        groups.setdefault(state, []).append(
            (cube_root, quotient, isqrt(quotient))
        )
    return groups, totients


def summatory_gcd(limit):
    # For n = product(p^e), gcd(n, n') = product(p^(e - 1 + [p divides e])).
    # Its convolution with the Moebius function vanishes outside powerful
    # numbers, which have the unique form a^2 b^3 for squarefree b.
    root = isqrt(limit)
    prime_limit = max(isqrt(root), EXCEPTIONAL_PRIMES[-1])
    primes = tuple(sieve.primerange(2, prime_limit + 1))
    groups, totients = powerful_groups(limit)
    tables = correction_tables(limit)
    total = 0

    for low in range(1, root + 1, CHUNK_SIZE):
        high = min(root, low + CHUNK_SIZE - 1)
        numbers, even_weights, valuations = factor_even_segment(
            low, high, primes
        )
        squares = numbers * numbers

        for state, entries in groups.items():
            active_count = 0
            for _, _, maximum in entries:
                if maximum < low:
                    break
                active_count += 1
            if active_count == 0:
                continue

            maximum = entries[0][2]
            size = min(high, maximum) - low + 1
            state_weights = even_weights[:size].copy()
            for prime in EXCEPTIONAL_PRIMES:
                values = valuations[prime][:size]
                old, even, odd = tables[prime]
                replacement = odd if state % prime == 0 else even
                state_weights //= old[values]
                state_weights *= replacement[values]

            for index in range(active_count):
                cube_root, quotient, maximum = entries[index]
                size = min(high, maximum) - low + 1
                large_part = cube_root // state
                multiples = quotient // squares[:size]

                if large_part == 1:
                    contribution = state_weights[:size] * multiples
                else:
                    # For primes above 13 the convolution factor is generic.
                    # If c = gcd(a, b), changing p^(2v) into p^(2v+3)
                    # multiplies the weight by b*phi(b)*c^2/phi(c).
                    common = np.gcd(numbers[:size], large_part)
                    contribution = state_weights[:size] // totients[common]
                    contribution *= common
                    contribution *= common
                    contribution *= large_part * totients[large_part]
                    contribution *= multiples
                total += exact_sum(contribution, limit)

    return total


def solve():
    return summatory_gcd(LIMIT) - 1


if __name__ == "__main__":
    print(solve())
