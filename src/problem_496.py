# Problem 496: https://projecteuler.net/problem=496

from math import isqrt

from sympy import factorint


LIMIT = 10**9


def squarefree_coefficients(n):
    coefficients = [(1, 1)]
    for p in factorint(n):
        coefficients += [
            (d * p, -coefficient * p) for d, coefficient in coefficients
        ]
    return coefficients


def coprime_prefix_sum(coefficients, n):
    return sum(
        coefficient * (n // d) * (n // d + 1) // 2
        for d, coefficient in coefficients
    )


def sum_sides(limit):
    total = 0
    for p in range(2, isqrt(limit) + 1):
        high = min(2 * p - 1, limit // p)
        if high <= p:
            continue

        coefficients = squarefree_coefficients(p)
        m = limit // p
        q = p + 1
        while q <= high:
            multiples = m // q
            end = min(high, m // multiples)
            q_sum = coprime_prefix_sum(
                coefficients, end
            ) - coprime_prefix_sum(coefficients, q - 1)
            total += p * q_sum * multiples * (multiples + 1) // 2
            q = end + 1
    return total


def solve():
    return sum_sides(LIMIT)


if __name__ == "__main__":
    print(solve())
