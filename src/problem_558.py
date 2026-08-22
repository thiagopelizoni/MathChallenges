# Problem 558: https://projecteuler.net/problem=558
import numpy as np


MOD = 1_000_000_007
MOD_INV = pow(2**64, -1, MOD)
ROOT = np.longdouble("1.4655712318767680266567312252199391080255775684723")
ROUNDING = 16 * np.finfo(np.longdouble).eps


def norm64(a, b, c):
    a = a.view(np.uint64)
    b = b.view(np.uint64)
    c = c.view(np.uint64)
    value = a * a * a
    value += a * a * b
    value += a * a * c
    value -= 3 * a * b * c
    value -= 2 * a * c * c
    value += b * b * b
    value += b * b * c
    value += c * c * c
    return value


def norm_int(a, b, c):
    value = a**3
    value += a * a * b
    value += a * a * c
    value -= 3 * a * b * c
    value -= 2 * a * c * c
    value += b**3
    value += b * b * c
    value += c**3
    return value


def norm_mod(a, b, c):
    a = a % MOD
    b = b % MOD
    c = c % MOD
    aa = a * a % MOD
    bb = b * b % MOD
    cc = c * c % MOD
    value = aa * a % MOD
    value = (value + aa * b) % MOD
    value = (value + aa * c) % MOD
    value = (value - 3 * (a * b % MOD) * c) % MOD
    value = (value - 2 * a * cc) % MOD
    value = (value + bb * b) % MOD
    value = (value + bb * c) % MOD
    value = (value + cc * c) % MOD
    return value


def nonnegative(a, b, c, exponent):
    if exponent > 4:
        ar = a.astype(np.longdouble)
        br = b.astype(np.longdouble)
        cr = c.astype(np.longdouble)
        value = ar + br * ROOT + cr * ROOT * ROOT
        error = ROUNDING * (np.abs(ar) + np.abs(br) * ROOT + np.abs(cr) * ROOT * ROOT)
        take = value > error
        uncertain = np.flatnonzero(np.abs(value) <= error)
        for i in uncertain:
            ai = int(a[i])
            bi = int(b[i])
            ci = int(c[i])
            take[i] = norm_int(ai, bi, ci) >= 0
        return take

    low = norm64(a, b, c)
    if exponent < -49:
        return low.view(np.int64) >= 0

    other = norm_mod(a, b, c)
    low_mod = (low % np.uint64(MOD)).astype(np.int64)
    high = ((other - low_mod) % MOD) * MOD_INV % MOD
    return high < MOD // 2


def solve(limit=5_000_000):
    powers = {0: (1, 0, 0), 1: (0, 1, 0), 2: (0, 0, 1)}
    for k in range(81):
        p0 = powers[k]
        p2 = powers[k + 2]
        powers[k + 3] = (p2[0] + p0[0], p2[1] + p0[1], p2[2] + p0[2])
    for k in range(-1, -201, -1):
        p2 = powers[k + 2]
        p3 = powers[k + 3]
        powers[k] = (p3[0] - p2[0], p3[1] - p2[1], p3[2] - p2[2])

    total = 0
    for start in range(1, limit + 1, 100_000):
        stop = min(start + 100_000, limit + 1)
        values = np.arange(start, stop, dtype=np.int64)
        a = values * values
        b = np.zeros(stop - start, dtype=np.int64)
        c = np.zeros(stop - start, dtype=np.int64)
        weight = np.zeros(stop - start, dtype=np.int16)

        for k in range(80, -201, -1):
            pa, pb, pc = powers[k]
            da = a - pa
            db = b - pb
            dc = c - pc
            take = nonnegative(da, db, dc, k)
            a[take] = da[take]
            b[take] = db[take]
            c[take] = dc[take]
            weight += take
            if k < -100 and not np.any(a) and not np.any(b) and not np.any(c):
                break

        total += int(weight.sum())

    return total


if __name__ == "__main__":
    print(solve())
