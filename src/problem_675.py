# Problem 675: https://projecteuler.net/problem=675

import math
import numpy as np
from sympy import sieve


def solve():
    n = 10_000_000
    mod = 1_000_000_087
    s = math.isqrt(n)

    sieve.extend(n)
    primes = np.array(sieve._list, dtype=np.int64)
    primes = primes[primes <= n]

    cols = (n + s - 1) // s
    size = s * cols

    num = np.ones(size + 1, dtype=np.int64)
    den = np.ones(size + 1, dtype=np.int64)

    small_primes = primes[primes <= s]
    large_primes = primes[primes > s]

    for p in small_primes:
        p = int(p)
        m = n // p
        k = np.arange(1, m + 1, dtype=np.int64)
        e = k.copy()
        q = p
        while q <= m:
            e += k // q
            q *= p
        u = (2 * e + 1) % mod
        num[p : n + 1 : p] = num[p : n + 1 : p] * u % mod
        den[2 * p : n + 1 : p] = den[2 * p : n + 1 : p] * u[:-1] % mod

    for k in range(1, n // (s + 1) + 1):
        cnt = int(np.searchsorted(large_primes, n // k, side="right"))
        if cnt == 0:
            break
        w = (2 * k + 1) * pow(2 * k - 1, -1, mod) % mod
        idx = k * large_primes[:cnt]
        num[idx] = num[idx] * w % mod

    d_mat = den[1:].reshape(s, cols)
    n_mat = num[1:].reshape(s, cols)

    pref = np.empty_like(d_mat)
    pref[:, 0] = d_mat[:, 0]
    for j in range(1, cols):
        pref[:, j] = pref[:, j - 1] * d_mat[:, j] % mod

    inv_end = np.array([pow(int(x), -1, mod) for x in pref[:, -1]], dtype=np.int64)
    for j in range(cols - 1, 0, -1):
        inv_d = inv_end * pref[:, j - 1] % mod
        inv_end = inv_end * d_mat[:, j] % mod
        n_mat[:, j] = n_mat[:, j] * inv_d % mod
    n_mat[:, 0] = n_mat[:, 0] * inv_end % mod

    if size > n:
        n_mat.ravel()[n:] = 0

    cur = np.ones(s, dtype=np.int64)
    block_sum = np.zeros(s, dtype=np.int64)
    for j in range(cols):
        cur = cur * n_mat[:, j] % mod
        block_sum = (block_sum + cur) % mod

    ans = 0
    prod = 1
    for b in range(s):
        ans = (ans + prod * int(block_sum[b])) % mod
        prod = prod * int(cur[b]) % mod

    return (ans - 1) % mod


if __name__ == "__main__":
    print(solve())
