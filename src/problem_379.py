# Problem 379: https://projecteuler.net/problem=379

from bisect import bisect_left
from math import isqrt

from sympy import primerange


def sum_squared_divisors(n):
    root = isqrt(n)
    values = []
    i = 1
    while i <= n:
        q = n // i
        values.append(q)
        i = n // q + 1
    values.reverse()

    large_index = [-1] * (root + 1)
    for index, value in enumerate(values):
        if value > root:
            large_index[n // value] = index

    sums = [value - 1 for value in values]
    primes = list(primerange(2, root + 1))

    for p in primes:
        square = p * p
        previous = sums[p - 2]
        for index in range(len(values) - 1, bisect_left(values, square) - 1, -1):
            quotient = values[index] // p
            subtotal = (
                sums[quotient - 1]
                if quotient <= root
                else sums[large_index[n // quotient]]
            )
            sums[index] -= subtotal - previous

    sums = [3 * value for value in sums]

    for p in reversed(primes):
        square = p * p
        prime_sum = sums[p - 1]
        for index in range(len(values) - 1, bisect_left(values, square) - 1, -1):
            quotient = values[index] // p
            exponent = 1
            while quotient >= p:
                subtotal = (
                    sums[quotient - 1]
                    if quotient <= root
                    else sums[large_index[n // quotient]]
                )
                sums[index] += (2 * exponent + 1) * (subtotal - prime_sum)
                sums[index] += 2 * exponent + 3
                exponent += 1
                quotient //= p

    return sums[-1] + 1


def solve(n=10**12):
    return (sum_squared_divisors(n) + n) // 2


if __name__ == "__main__":
    print(solve())
