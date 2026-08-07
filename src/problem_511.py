# Problem 511: https://projecteuler.net/problem=511

import numpy as np
from sympy import divisors


def mul(a, b, m):
    n = len(a)
    R = 10**5
    a = [int(x) for x in a]
    b = [int(x) for x in b]
    al = np.array([x % R for x in a], dtype=float)
    ah = np.array([x // R for x in a], dtype=float)
    bl = np.array([x % R for x in b], dtype=float)
    bh = np.array([x // R for x in b], dtype=float)

    def conv(u, v):
        w = np.fft.ifft(np.fft.fft(u) * np.fft.fft(v)).real
        return [int(round(x)) for x in w]

    ll = conv(al, bl)
    lh = conv(al, bh)
    hl = conv(ah, bl)
    hh = conv(ah, bh)

    out = [0] * n
    for i in range(n):
        out[i] = (ll[i] + R * (lh[i] + hl[i]) + R * R * hh[i]) % m
    return out


def solve():
    n, k, mod = 1234567898765, 4321, 10**9

    f = [0] * k
    for d in divisors(n):
        f[d % k] += 1

    res = [0] * k
    res[0] = 1
    e = n
    while e:
        if e % 2:
            res = mul(res, f, mod)
        f = mul(f, f, mod)
        e //= 2

    return res[(-n) % k]


if __name__ == "__main__":
    print(solve())
