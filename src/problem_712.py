# Problem 712: https://projecteuler.net/problem=712

from math import isqrt

import numpy as np
from sympy import sieve


def solve(n=10**12):
    mod = 1_000_000_007
    r = isqrt(n)
    primes = list(sieve.primerange(2, r + 1))
    indices = np.arange(1, r + 1, dtype=np.int64)
    values = n // indices
    small = np.arange(r + 1, dtype=np.int64) - 1
    small[0] = 0
    large = values - 1

    for count, p in enumerate(primes):
        end = min(r, n // (p * p))
        split = min(end, n // (p * (r + 1)))
        large[:split] -= large[indices[:split] * p - 1] - count
        large[split:end] -= small[values[split:end] // p] - count
        if p * p <= r:
            x = np.arange(p * p, r + 1)
            small[p * p:] -= small[x // p] - count

    total = 0
    for p in primes:
        power = p
        while power <= n:
            a = n // power
            total += a * (n - a)
            power *= p

    end = n // (r + 1)
    for a in range(1, end + 1):
        upper = int(large[a - 1])
        lower = int(large[a]) if a < end else int(small[r])
        total += (upper - lower) * a * (n - a)

    return 2 * total % mod


if __name__ == "__main__":
    print(solve())
