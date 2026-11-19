# Problem 771: https://projecteuler.net/problem=771
from math import isqrt

from sympy import sieve


def triangle(n):
    return n * (n + 1) // 2 if n > 0 else 0


def solve(limit=10**18):
    small = 8

    def extend(a, b, length):
        if a >= 5 and b == a + 1:
            return max(0, limit - b + 1 - max(0, 5 - length))
        total = int(length >= 5)
        lo = max(b + 1, (b*b - 2 + a - 1) // a)
        hi = min(limit, (b*b + 2) // a)
        for c in range(lo, hi + 1):
            total += extend(b, c, length + 1)
        return total

    total = triangle(limit - small - 3)
    for b in range(2, min(small, limit) + 1):
        for a in range(1, b):
            total += extend(a, b, 2)

    root = isqrt(isqrt(limit))
    for p, phi in enumerate(sieve.totientrange(2, root + 1), 2):
        power = p**4
        while power <= limit:
            scales = limit // power
            total += phi * scales - min(scales, small // p)
            power *= p

    for seed in range(2, root + 2):
        for k in range(seed - 1, seed + 2):
            for sign in (-1, 1):
                deviation = seed * (seed - k) + sign
                if not 1 <= abs(deviation) <= 2:
                    continue
                if sign == 1 and k <= 2:
                    continue
                a, b = 1, seed
                pairs = 0
                while b <= limit:
                    if b > small:
                        pairs += 1
                    a, b = b, k*b - sign*a
                total += triangle(pairs - 3)

    return total % 1_000_000_007


if __name__ == "__main__":
    print(solve())
