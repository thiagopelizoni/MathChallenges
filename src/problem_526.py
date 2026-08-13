# Problem 526: https://projecteuler.net/problem=526

from gmpy2 import is_prime
from sympy import factorint, primerange
from sympy.ntheory.modular import crt

import numpy as np


N = 10**16
POS = (0, 1, 2, 3, 5, 6, 7, 8)


def upper(n):
    return (
        n
        + (n + 1) // 6
        + (n + 2)
        + (n + 3) // 4
        + (n + 4) // 105
        + (n + 5) // 2
        + (n + 6)
        + (n + 7) // 24
        + (n + 8)
    )


def solve():
    residues = [int(crt([24, 5, 7], [a, 1, 3])[0]) for a in (17, 23)]
    mod = 840
    for p in primerange(11, 30):
        lifted = []
        for r0 in residues:
            for r in range(r0, mod * p, mod):
                if all((r + i) % p for i in POS):
                    lifted.append(r)
        residues = lifted
        mod *= p

    residues = np.array(residues, dtype=np.int64)
    top = N - (N - residues) % mod
    primes = list(primerange(31, 250))
    tables = []
    for p in primes:
        good = np.ones(p, dtype=bool)
        for i in POS:
            good[(-i) % p] = False
        tables.append(good)

    best = 0
    lo = 2
    step = 0
    width = np.int64(mod)

    while True:
        cand = top - step * width
        step += 1
        cand = cand[cand >= lo]
        if cand.size == 0:
            break
        keep = np.ones(cand.size, dtype=bool)
        for p, good in zip(primes, tables):
            keep = np.logical_and(keep, good[cand % p])
        for n in map(int, cand[keep]):
            d = (6, 4, 2, 24) if n % 24 == 17 else (24, 2, 4, 6)
            qs = (
                n,
                (n + 1) // d[0],
                n + 2,
                (n + 3) // d[1],
                (n + 5) // d[2],
                n + 6,
                (n + 7) // d[3],
                n + 8,
            )
            if all(is_prime(q) for q in qs):
                val = sum(qs) + max(factorint(n + 4))
                if val > best:
                    best = val
                    a, b = 2, N
                    while a < b:
                        mid = (a + b) // 2
                        if upper(mid) > best:
                            b = mid
                        else:
                            a = mid + 1
                    lo = a

    return best


if __name__ == "__main__":
    print(solve())
