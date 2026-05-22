# Problem 251: https://projecteuler.net/problem=251
from math import isqrt

import numpy as np
from sympy import primerange


LIMIT = 110_000_000


def n_limit():
    lo = 1
    hi = LIMIT // 3
    while lo < hi:
        n = (lo + hi + 1) // 2
        r = LIMIT - (3 * n - 1)
        m = n * n * (8 * n - 3)
        b = 2 * r // 3
        if b > 0 and b * b * (r - b) >= m:
            lo = n
        else:
            hi = n - 1
    return lo


NMAX = n_limit()
MMAX = 8 * NMAX - 3


def factor_table():
    spf = np.zeros(NMAX + 1, dtype=np.uint32)
    for p in primerange(2, isqrt(NMAX) + 1):
        spf[p * p :: p] = p
    return spf


def square_part():
    sq = np.ones(NMAX + 1, dtype=np.uint32)
    for p in primerange(3, isqrt(MMAX) + 1):
        q = p * p
        while q <= MMAX:
            r = (3 * pow(8, -1, q)) % q
            if r <= NMAX:
                sq[r::q] *= p
            q *= p * p
    return sq


SPF = factor_table()
SQ = square_part()


def add_factor(fs, p, e):
    for i, (q, k) in enumerate(fs):
        if q == p:
            fs[i] = (q, k + e)
            return
    fs.append((p, e))


def factors(n):
    fs = []
    while n > 1:
        p = int(SPF[n]) or n
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        fs.append((p, e))
    return fs


def divisors(fs):
    ds = [1]
    for p, e in fs:
        base = ds[:]
        pp = 1
        for _ in range(e):
            pp *= p
            ds += [d * pp for d in base]
    return ds


def interval(m, r, top):
    peak = min(top, 2 * r // 3)
    if peak <= 0 or peak * peak * (r - peak) < m:
        return 1, 0

    lo = 1
    hi = peak
    while lo < hi:
        mid = (lo + hi) // 2
        if mid * mid * (r - mid) >= m:
            hi = mid
        else:
            lo = mid + 1
    a = lo

    if top <= 2 * r // 3:
        return a, top

    lo = 2 * r // 3
    hi = top
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid < r and mid * mid * (r - mid) >= m:
            lo = mid
        else:
            hi = mid - 1
    return a, lo


def solve():
    total = 0
    for n in range(1, NMAX + 1):
        r = LIMIT - (3 * n - 1)
        m = n * n * (8 * n - 3)
        fs = factors(n)
        s = int(SQ[n])
        if s > 1:
            for p, e in factors(s):
                add_factor(fs, p, e)

        lo, hi = interval(m, r, n * s)
        if lo <= hi:
            total += sum(lo <= d <= hi for d in divisors(fs))
    return total


if __name__ == "__main__":
    print(solve())
