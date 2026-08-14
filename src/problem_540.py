# Problem 540: https://projecteuler.net/problem=540

import math
from functools import cache
import numpy as np


def solve():
    N = 3141592653589793
    M = math.isqrt(N - 1)
    M0 = math.isqrt(N // 2)
    max_d = M // 2

    limit = max_d
    mu = np.ones(limit + 1, dtype=np.int8)
    is_p = np.ones(limit + 1, dtype=bool)
    is_p[:2] = False
    for i in range(2, int(math.isqrt(limit)) + 1):
        if is_p[i]:
            is_p[i * 2 :: i] = False
            mu[i * i :: i * i] = 0

    primes = np.nonzero(is_p)[0]
    for p in primes:
        mu[p::p] *= -1

    M_arr = np.zeros(limit + 1, dtype=np.int64)
    M_arr[1:] = np.cumsum(mu[1:])
    M_list = M_arr.tolist()

    PRE_LIMIT = 2_000_000
    phi = np.arange(PRE_LIMIT + 1, dtype=np.int64)
    for i in range(2, PRE_LIMIT + 1):
        if phi[i] == i:
            phi[i::i] -= phi[i::i] // i
    Phi_small = np.cumsum(phi)

    @cache
    def Phi(x):
        if x <= PRE_LIMIT:
            return int(Phi_small[x])
        ans = x * (x + 1) // 2
        l = 2
        while l <= x:
            v = x // l
            r = x // v
            ans -= (r - l + 1) * Phi(v)
            l = r + 1
        return ans

    def E(x):
        ans = 0
        while x > 0:
            x //= 2
            ans += Phi(x)
        return ans

    totient_part = (E(M0) + Phi(M0) - 1) // 2

    D = 40000
    d_part = 0
    for d in range(1, D + 1):
        mud = int(mu[d])
        if mud == 0:
            continue
        k_start = M0 // d + 1
        k_end = M // d
        if k_end < k_start:
            continue
        k_arr = np.arange(k_start, k_end + 1, dtype=np.int64)
        m_arr = k_arr * d
        Lm_arr = np.sqrt(N - m_arr * m_arr).astype(np.int64)
        if d % 2 == 1:
            evens = (k_arr % 2 == 0)
            terms = np.where(evens, Lm_arr // d, Lm_arr // (2 * d))
            d_part += mud * int(np.sum(terms))
        else:
            d_part += mud * int(np.sum(Lm_arr // d))

    def get_M_odd(x):
        ans = 0
        while x > 0:
            ans += M_list[x]
            x //= 2
        return ans

    def get_M_even(x):
        ans = 0
        x //= 2
        while x > 0:
            ans -= M_list[x]
            x //= 2
        return ans

    k_part = 0
    max_k = M // D
    for k in range(2, max_k + 1):
        d_min = max(D, M0 // k)
        d_max = M // k
        if d_min >= d_max:
            continue
        if k % 2 == 0:
            for u in range(1, k):
                lim = int(math.isqrt(N // (k * k + u * u)))
                top = min(d_max, lim)
                if top > d_min:
                    k_part += M_list[top] - M_list[d_min]
        else:
            for u in range(1, k):
                lim = int(math.isqrt(N // (k * k + u * u)))
                top = min(d_max, lim)
                if top > d_min:
                    k_part += get_M_even(top) - get_M_even(d_min)
            for u in range(1, (k - 1) // 2 + 1):
                lim = int(math.isqrt(N // (k * k + 4 * u * u)))
                top = min(d_max, lim)
                if top > d_min:
                    k_part += get_M_odd(top) - get_M_odd(d_min)

    return totient_part + d_part + k_part


if __name__ == "__main__":
    print(solve())
