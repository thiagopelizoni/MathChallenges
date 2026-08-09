# Problem 519: https://projecteuler.net/problem=519

import numpy as np

N = 20_000
MOD = 10**9
BASE = 32_768


def divide(num, den):
    size = len(num)
    d = np.asarray(den, dtype=np.int64)
    dlo = (d % BASE).astype(float)
    dhi = (d // BASE).astype(float)
    dsum = dlo + dhi

    out = np.zeros(size, dtype=np.int64)
    olo = np.zeros(size)
    ohi = np.zeros(size)
    osum = np.zeros(size)
    out[0] = num[0]
    olo[0] = out[0] % BASE
    ohi[0] = out[0] // BASE
    osum[0] = olo[0] + ohi[0]

    for n in range(1, size):
        ll = int(np.dot(dlo[1 : n + 1], olo[n - 1 :: -1]))
        hh = int(np.dot(dhi[1 : n + 1], ohi[n - 1 :: -1]))
        both = int(np.dot(dsum[1 : n + 1], osum[n - 1 :: -1]))
        cross = both - ll - hh
        value = (int(num[n]) - ll - cross * BASE - hh * BASE * BASE) % MOD
        out[n] = value
        olo[n] = value % BASE
        ohi[n] = value // BASE
        osum[n] = olo[n] + ohi[n]
    return out


def solve(limit=N):
    part = [0] * (limit + 1)
    part[0] = 1
    num = [0] * (limit + 1)
    den = [0] * (limit + 1)

    m = 0
    while m * (m + 1) <= limit or m * (m + 2) <= limit:
        sign = 1 if m % 2 == 0 else -1
        a = m * (m + 2)
        b = m * (m + 1)
        if a <= limit:
            for i in range(limit - a + 1):
                num[i + a] = (num[i + a] + sign * part[i]) % MOD
        if b <= limit:
            for i in range(limit - b + 1):
                den[i + b] = (den[i + b] + sign * part[i]) % MOD
        m += 1
        for i in range(m, limit + 1):
            part[i] = (part[i] + part[i - m]) % MOD

    f = divide(num, den)
    a = 2 * f % MOD
    a[0] = (a[0] - 1) % MOD

    num = np.zeros(limit + 1, dtype=np.int64)
    num[1:] = a[:-1]
    den = np.zeros(limit + 1, dtype=np.int64)
    den[0] = 1
    den[1:] = -2 * a[:-1] % MOD
    t = divide(num, den)
    return int(3 * t[limit] % MOD)


if __name__ == "__main__":
    print(solve())
