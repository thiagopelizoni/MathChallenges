# Problem 799: https://projecteuler.net/problem=799

from functools import cache

import numpy as np
from sympy import factorint, integer_nthroot, primerange, sqrt_mod
from sympy.solvers.diophantine.diophantine import prime_as_sum_of_two_squares


@cache
def gaussian_choices(p, exponent):
    x, y = prime_as_sum_of_two_squares(p)
    z = complex(x, y)
    powers = [1]
    for _ in range(exponent):
        powers.append(powers[-1] * z)
    return [powers[k] * powers[exponent - k].conjugate() for k in range(exponent + 1)]


def representations(n):
    odd_part = ((6 * n - 1) ** 2 + 1) // 2
    points = [1 + 1j]
    for p, exponent in factorint(odd_part).items():
        choices = gaussian_choices(p, exponent)
        points = [z * w for z in points for w in choices]

    count = sum(int(abs(z.real)) % 6 == 5 and int(abs(z.imag)) % 6 == 5 for z in points)
    return (count + 1) // 2


def solve():
    target = 100
    start = 1
    while True:
        stop = 2 * start
        x = 6 * np.arange(start, stop) - 1
        remainder = (x * x + 1) // 2
        limit = integer_nthroot(int(remainder[-1]), 3)[0]
        divisors = np.ones_like(remainder)

        for p in primerange(5, limit + 1):
            if p % 4 != 1:
                continue
            root = sqrt_mod(-1, p)
            inverse = pow(6, -1, p)
            for r in (root, -root):
                first = ((r + 1) * inverse - start) % p
                values = remainder[first::p]
                values //= p
                divisors[first::p] *= 2
                indices = first + p * np.flatnonzero(values % p == 0)
                exponent = 2
                while indices.size:
                    remainder[indices] //= p
                    divisors[indices] //= exponent
                    divisors[indices] *= exponent + 1
                    indices = indices[remainder[indices] % p == 0]
                    exponent += 1

        divisors[remainder > 1] *= 2
        divisors[remainder >= (limit + 1) ** 2] *= 2
        for offset in np.flatnonzero(divisors >= 2 * target + 1):
            n = start + int(offset)
            if representations(n) > target:
                return n * (3 * n - 1) // 2
        start = stop


if __name__ == "__main__":
    print(solve())
