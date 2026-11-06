# Problem 708: https://projecteuler.net/problem=708

from math import isqrt

import numpy as np
from sympy import divisor_count, integer_nthroot, sieve


def solve(n=10**14):
    lim = int(integer_nthroot(n, 3)[0])
    counts = np.fromiter((divisor_count(k) for k in range(1, lim + 1)), dtype=np.int64)
    sums = [0] + np.cumsum(counts).tolist()
    primes = list(sieve.primerange(2, isqrt(n) + 1))
    divisors = np.arange(1, isqrt(n) + 1, dtype=np.int64)

    def visit(x, start):
        if x <= lim:
            total = sums[x]
        else:
            r = isqrt(x)
            total = 2 * int(np.sum(x // divisors[:r])) - r * r

        for i in range(start, len(primes)):
            p = primes[i]
            power = p * p
            if power > x:
                break
            weight = 1
            while power <= x:
                total += weight * visit(x // power, i + 1)
                power *= p
                weight *= 2
        return total

    return visit(n, 0)


if __name__ == "__main__":
    print(solve())
