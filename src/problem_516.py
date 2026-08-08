# Problem 516: https://projecteuler.net/problem=516

from bisect import bisect_right
from itertools import accumulate

from sympy import isprime

LIMIT = 10**12
MODULUS = 2**32


def solve(limit=LIMIT):
    smooth = [1]
    for p in (2, 3, 5):
        previous = smooth
        smooth = []
        power = 1
        while power <= limit:
            for n in previous:
                value = power * n
                if value > limit:
                    break
                smooth.append(value)
            power *= p
        smooth.sort()

    prefix = [0, *accumulate(smooth)]
    primes = [n + 1 for n in smooth if n >= 6 and isprime(n + 1)]

    def subtotal(start, product):
        total = product * prefix[bisect_right(smooth, limit // product)]
        for i in range(start, len(primes)):
            value = product * primes[i]
            if value > limit:
                break
            total += subtotal(i + 1, value)
        return total

    return subtotal(0, 1) % MODULUS


if __name__ == "__main__":
    print(solve())
