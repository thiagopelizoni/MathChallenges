# Problem 223: https://projecteuler.net/problem=223
from array import array
from math import isqrt


LIMIT = 25_000_000


def ceil_sqrt(n):
    r = isqrt(n)
    return r if r * r == n else r + 1


def spf_upto(n):
    spf = array("I", range(n + 1))
    for i in range(4, n + 1, 2):
        spf[i] = 2
    for p in range(3, isqrt(n) + 1, 2):
        if spf[p] == p:
            for q in range(p * p, n + 1, 2 * p):
                if spf[q] == q:
                    spf[q] = p
    return spf


def factor(n, spf):
    fs = []
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        fs.append((p, e))
    return fs


def roots_prime_power(p, e):
    q = p**e
    if p != 2:
        return [1, q - 1], q
    if e == 1:
        return [1], 2
    if e == 2:
        return [1, 3], 4
    h = 1 << (e - 1)
    return [1, q - 1, 1 + h, h - 1], q


def extend_roots(roots, mod, rs, q):
    inv = pow(mod, -1, q)
    out = []
    for r in roots:
        for s in rs:
            out.append((r + mod * (((s - r) * inv) % q)) % (mod * q))
    return out, mod * q


def roots_from_factors(fs, mod=1):
    roots = [0]
    for p, e in fs:
        rs, q = roots_prime_power(p, e)
        roots, mod = extend_roots(roots, mod, rs, q)
    return roots, mod


def upper_a(u):
    r = isqrt(u * u + 4 * LIMIT * u + 4)
    a = (r - u) // 2
    while a * a + u * a - 1 > LIMIT * u:
        a -= 1
    while (a + 1) * (a + 1) + u * (a + 1) - 1 <= LIMIT * u:
        a += 1
    return a


def solve():
    umax = 0
    while True:
        u = umax + 1
        a = u + ceil_sqrt(2 * u * u + 1)
        if 3 * a + u > LIMIT:
            break
        umax = u

    spf = spf_upto(2 * umax)
    total = (LIMIT - 1) // 2

    for u in range(1, umax + 1):
        lo = u + ceil_sqrt(2 * u * u + 1)
        hi = upper_a(u)
        if lo > hi:
            continue

        if u % 2:
            roots, mod = roots_from_factors(factor(u, spf), mod=2)
        else:
            roots, mod = roots_from_factors(factor(2 * u, spf))

        for r in roots:
            first = r if r else mod
            if first < lo:
                first += ((lo - first + mod - 1) // mod) * mod
            if first <= hi:
                total += (hi - first) // mod + 1

    return total


if __name__ == "__main__":
    print(solve())
