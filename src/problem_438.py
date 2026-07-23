# Problem 438: https://projecteuler.net/problem=438

from math import comb, factorial


N = 7


def precompute_terms(n):
    shifted_powers = {}
    for x in range(1, 2 * n + 2):
        for power in range(n + 1):
            shifted_powers[x, power] = [
                comb(power, e) * x ** (power - e) * (-1) ** e
                for e in range(n + 1)
            ]

    terms = [
        [[None] * (n + 1) for _ in range(k + 2)]
        for k in range(n + 1)
    ]
    multipliers = [[0] * (k + 2) for k in range(n + 1)]

    for k in range(1, n + 1):
        difference = n - k
        weights = [
            (-1) ** (difference - j) * comb(difference, j)
            for j in range(difference + 1)
        ]
        for m in range(1, k + 2):
            sign = (-1) ** (k + 1 - m)
            multipliers[k][m] = sign * factorial(difference)
            for i in range(k + 1):
                terms[k][m][i] = [
                    sign
                    * sum(
                        weight * shifted_powers[m + j, n - i][e]
                        for j, weight in enumerate(weights)
                    )
                    for e in range(n + 1)
                ]

    return terms, multipliers


def first_nonzero_sign(polynomial):
    for value in polynomial[1:]:
        if value:
            return 1 if value > 0 else -1
    return 0


def coefficient_bound(multiplier, polynomial):
    constant = polynomial[0]
    if multiplier > 0:
        numerator = -constant
        if numerator % multiplier:
            return "lower", numerator // multiplier + 1
        value = numerator // multiplier
        return "lower", value if first_nonzero_sign(polynomial) > 0 else value + 1

    denominator = -multiplier
    if constant % denominator:
        return "upper", constant // denominator
    value = constant // denominator
    return "upper", value if first_nonzero_sign(polynomial) > 0 else value - 1


def sum_absolute_range(lower, upper):
    if upper < 0:
        return -(lower + upper) * (upper - lower + 1) // 2
    if lower > 0:
        return (lower + upper) * (upper - lower + 1) // 2
    return (-lower) * (-lower + 1) // 2 + upper * (upper + 1) // 2


def enumerate_polynomials(n):
    terms, multipliers = precompute_terms(n)
    constants = [[None] * (k + 2) for k in range(n + 1)]
    for k in range(1, n + 1):
        for m in range(1, k + 2):
            constants[k][m] = terms[k][m][0].copy()
    count = 0
    total = 0

    def apply(i, value):
        if value == 0:
            return
        for k in range(i + 1, n + 1):
            for m in range(1, k + 2):
                polynomial = terms[k][m][i]
                current = constants[k][m]
                for e in range(n + 1):
                    current[e] += value * polynomial[e]

    def bounds(k):
        lower = -(10**30)
        upper = 10**30
        for m in range(1, k + 2):
            kind, value = coefficient_bound(
                multipliers[k][m], constants[k][m]
            )
            if kind == "lower":
                lower = max(lower, value)
            else:
                upper = min(upper, value)
        return lower, upper

    def search(k, prefix):
        nonlocal count, total
        lower, upper = bounds(k)
        if lower > upper:
            return
        if k == n:
            amount = upper - lower + 1
            count += amount
            total += amount * prefix + sum_absolute_range(lower, upper)
            return
        for coefficient in range(lower, upper + 1):
            apply(k, coefficient)
            search(k + 1, prefix + abs(coefficient))
            apply(k, -coefficient)

    search(1, 0)
    return count, total


def solve():
    return enumerate_polynomials(N)[1]


if __name__ == "__main__":
    print(solve())
