# Problem 533: https://projecteuler.net/problem=533

from math import isqrt, log

import numpy as np


N = 20_000_000
MOD = 10**9


def factors(m, spf):
    fac = {}
    while m > 1:
        p = int(spf[m])
        e = 0
        while m % p == 0:
            m //= p
            e += 1
        fac[p] = e
    return fac


def solve():
    spf = np.arange(N + 1, dtype=np.int32)
    for p in range(2, isqrt(N) + 1):
        if spf[p] == p:
            spf[p * p :: p] = np.minimum(spf[p * p :: p], p)

    best = 1
    best_log = 0.0

    for m in range(N // 2 + 1, N):
        fac = factors(m, spf)
        tau = 1
        for e in fac.values():
            tau *= e + 1
        v2 = fac.get(2, 0)
        base = (v2 + 2) * log(2) if v2 else log(2)
        if base + log(m) + tau * log(m + 1) <= best_log:
            continue

        divs = [1]
        for p, e in fac.items():
            divs = [d * p**k for k in range(e + 1) for d in divs]

        lg = base
        extra = []
        for d in divs:
            p = d + 1
            if p < 3 or p > N or spf[p] != p:
                continue
            e = fac.get(p, 0) + 1
            lg += e * log(p)
            extra.append((p, e))

        if lg <= best_log:
            continue

        val = 2 ** (v2 + 2) if v2 else 2
        for p, e in extra:
            val *= p**e
        if val > best:
            best = val
            best_log = lg

    return (best + 1) % MOD


if __name__ == "__main__":
    print(solve())
