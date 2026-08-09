# Problem 518: https://projecteuler.net/problem=518

from math import gcd, isqrt

import numpy as np

N = 10**8


def solve(limit=N):
    prime = np.ones(limit, dtype=bool)
    prime[:2] = False
    for p in range(2, isqrt(limit - 1) + 1):
        if prime[p]:
            prime[p * p :: p] = False

    total = 0
    for s in range(2, isqrt(limit) + 1):
        ss = s * s
        for d in range(2, limit // ss + 1, 2):
            c = d * ss - 1
            if not prime[c]:
                continue
            for r in range(1, s):
                if gcd(r, s) != 1:
                    continue
                a = d * r * r - 1
                if prime[a]:
                    b = d * r * s - 1
                    if prime[b]:
                        total += a + b + c

    for s in range(2, isqrt(limit // 3) + 1, 2):
        b = 3 * s - 1
        c = 3 * s * s - 1
        if prime[b] and prime[c]:
            total += 2 + b + c
    return total


if __name__ == "__main__":
    print(solve())
