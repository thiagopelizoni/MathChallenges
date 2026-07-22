# Problem 432: https://projecteuler.net/problem=432

from bisect import bisect_right
from sympy import primefactors, totient


def solve():
    n = 510510
    m = 10**11
    mod = 10**9
    primes_n = primefactors(n)
    phi_n = totient(n)

    smooth = [1]
    for p in primes_n:
        k = len(smooth)
        for i in range(k):
            v = smooth[i]
            while v <= m // p:
                v *= p
                smooth.append(v)
    smooth.sort()

    def smooth_count(x):
        return bisect_right(smooth, x) if x > 0 else 0

    lim = int(m ** (2 / 3))
    mu = [0] * (lim + 1)
    mu[1] = 1
    primes = []
    composite = [False] * (lim + 1)
    for i in range(2, lim + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            ip = i * p
            if ip > lim:
                break
            composite[ip] = True
            if i % p == 0:
                mu[ip] = 0
                break
            mu[ip] = -mu[i]

    for p in primes_n:
        for i in range(p, lim + 1, p):
            mu[i] = 0

    pref = [0] * (lim + 1)
    run = 0
    for i in range(1, lim + 1):
        run += mu[i]
        pref[i] = run

    memo = {}

    def mertens_coprime(x):
        if x <= 0:
            return 0
        if x <= lim:
            return pref[x]
        if x in memo:
            return memo[x]
        total = 0
        d = 2
        while d <= x:
            v = x // d
            d2 = min(x // v, x)
            total += (d2 - d + 1) * mertens_coprime(v)
            d = d2 + 1
        ans = smooth_count(x) - total
        memo[x] = ans
        return ans

    u = 0
    d = 1
    while d <= m:
        q = m // d
        d2 = m // q
        u += (mertens_coprime(d2) - mertens_coprime(d - 1)) * (q * (q + 1) // 2)
        d = d2 + 1

    return (phi_n * u) % mod


if __name__ == "__main__":
    print(solve())
