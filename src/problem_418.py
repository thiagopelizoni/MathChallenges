# Problem 418: https://projecteuler.net/problem=418

from bisect import bisect_left, bisect_right
from math import factorial, isqrt, log

from sympy import factorint, integer_nthroot


BEAM = 1_000


def divisors(factors):
    values = [1]
    for p, e in factors:
        previous = values
        values = []
        power = 1
        for _ in range(e + 1):
            values.extend(value * power for value in previous)
            power *= p
    return sorted(values)


def split_factors(factors):
    left = []
    right = []
    left_count = right_count = 1
    for factor in sorted(factors, key=lambda item: item[1], reverse=True):
        if left_count <= right_count:
            left.append(factor)
            left_count *= factor[1] + 1
        else:
            right.append(factor)
            right_count *= factor[1] + 1
    return left, right


def divisors_in_interval(factors, lo, hi):
    left, right = split_factors(factors)
    a = divisors(left)
    b = divisors(right)
    values = []
    for x in a:
        begin = bisect_left(b, (lo + x - 1) // x)
        end = bisect_right(b, hi // x)
        values.extend(x * y for y in b[begin:end])
    return sorted(values)


def largest_divisor_in_interval(n, lo, hi):
    left, right = split_factors(list(factorint(n).items()))
    a = divisors(left)
    b = divisors(right)
    best = 0
    for x in a:
        begin = bisect_left(b, (lo + x - 1) // x)
        end = bisect_right(b, hi // x)
        if begin < end:
            best = max(best, x * b[end - 1])
    return best


def initial_triple(factors):
    states = {(1, 1, 1)}
    for p, e in reversed(factors):
        powers = [p**i for i in range(e + 1)]
        nxt = set()
        for a, b, c in states:
            for i in range(e + 1):
                for j in range(e - i + 1):
                    triple = a * powers[i], b * powers[j], c * powers[e - i - j]
                    nxt.add(tuple(sorted(triple)))
        states = set(
            sorted(nxt, key=lambda triple: log(triple[2]) - log(triple[0]))[:BEAM]
        )
    return min(states, key=lambda triple: triple[2] / triple[0])


def factor_sum(n):
    factors = list(factorint(n).items())
    best_a, best_b, best_c = initial_triple(factors)
    upper = integer_nthroot(n, 3)[0]
    lower = integer_nthroot(n * best_a**2 // best_c**2, 3)[0]
    while (lower + 1) ** 3 * best_c**2 <= n * best_a**2:
        lower += 1
    while lower**3 * best_c**2 > n * best_a**2:
        lower -= 1

    candidates = divisors_in_interval(factors, lower + 1, upper)
    for a in reversed(candidates):
        if a**3 * best_c**2 <= n * best_a**2:
            break
        remaining = n // a
        lo = max(a, n * best_a // (best_c * a**2) + 1)
        b = largest_divisor_in_interval(remaining, lo, isqrt(remaining))
        if b:
            c = remaining // b
            if c * best_a < best_c * a:
                best_a, best_b, best_c = a, b, c

    return best_a + best_b + best_c


def solve():
    return factor_sum(factorial(43))


if __name__ == "__main__":
    print(solve())
