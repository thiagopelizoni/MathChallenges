# Problem 540: https://projecteuler.net/problem=540

from math import isqrt

import numpy as np


def solve():
    n = 3141592653589793
    m1 = isqrt(n)
    m0 = isqrt(n // 2)

    prime = np.ones(m0 + 1, dtype=bool)
    prime[:2] = False
    for i in range(2, isqrt(m0) + 1):
        if prime[i]:
            prime[i * i :: i] = False

    phi = np.arange(m0 + 1, dtype=np.int64)
    for p in np.nonzero(prime)[0]:
        phi[p::p] -= phi[p::p] // p

    ans = int(phi[2:].sum() + phi[2::2].sum()) // 2

    lim = m1 // 2
    mu = np.ones(lim + 1, dtype=np.int8)
    for i in range(2, isqrt(lim) + 1):
        if prime[i]:
            mu[i * i :: i * i] = 0
    for p in np.nonzero(prime[: lim + 1])[0]:
        mu[p::p] *= -1

    cutoff = 20000
    for d in range(1, cutoff + 1):
        s = int(mu[d])
        if s == 0:
            continue
        a = m0 // d + 1
        b = m1 // d
        if a > b:
            continue
        k = np.arange(a, b + 1, dtype=np.int64)
        rem = n - (k * d) * (k * d)
        L = np.sqrt(rem).astype(np.int64)
        L -= L * L > rem
        L += (L + 1) * (L + 1) <= rem
        if d % 2 == 0:
            ans += s * int((L // d).sum())
        else:
            ans += s * int((L[k % 2 == 0] // d).sum())
            ans += s * int((L[k % 2 == 1] // (2 * d)).sum())

    for d in range(cutoff + 1, lim + 1):
        s = int(mu[d])
        if s == 0:
            continue
        a = m0 // d + 1
        b = m1 // d
        dd = d * d
        for k in range(a, b + 1):
            L = isqrt(n - dd * k * k)
            if d % 2 == 1 and k % 2 == 1:
                ans += s * (L // (2 * d))
            else:
                ans += s * (L // d)

    return ans


if __name__ == "__main__":
    print(solve())
