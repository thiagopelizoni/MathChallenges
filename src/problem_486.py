# Problem 486: https://projecteuler.net/problem=486
from bisect import bisect_right
from math import gcd, lcm

from sympy import n_order

M = 87654321
L = 10**18
PERIOD = [32, 32, 32, 34, 36, 34]
PREF = [0]
for x in PERIOD:
    PREF.append(PREF[-1] + x)


def crt_pair(a1, m1, a2, m2):
    g = gcd(m1, m2)
    if (a2 - a1) % g != 0:
        return None
    mod = m2 // g
    t = ((a2 - a1) // g * pow(m1 // g, -1, mod)) % mod
    return (a1 + m1 * t) % (m1 // g * m2), m1 // g * m2


def residues(r, p):
    ord64 = n_order(64, p)
    T = lcm(ord64, p)
    C = (86 + PREF[r]) % p
    A = pow(2, r + 7, p)
    log = {}
    pw = 1
    for e in range(ord64):
        log[pw] = e
        pw = pw * 64 % p
    invA = pow(A, -1, p)
    out = []
    for b in range(p):
        rhs = (C + 200 * b) * invA % p
        if rhs not in log:
            continue
        k0 = (log[rhs] - b) % ord64
        out.append((b + p * k0) % T)
    return out, T


def residues9(r):
    C = (86 + PREF[r]) % 9
    A = pow(2, r + 7, 9)
    return [q for q in range(9) if (A - 200 * q - C) % 9 == 0]


def arithmetic_progressions(r):
    c = residues9(r)[0]
    s1, T1 = residues(r, 1997)
    s2, T2 = residues(r, 4877)
    g = gcd(T1, T2)
    buckets = {}
    for b in s2:
        buckets.setdefault(b % g, []).append(b)
    ys = []
    Tfull = None
    for a in s1:
        for b in buckets.get(a % g, ()):
            pair = crt_pair(a, T1, b, T2)
            if pair is None:
                continue
            x, T12 = pair
            triple = crt_pair(x, T12, c, 9)
            if triple is None:
                continue
            y, Tfull = triple
            ys.append(y)
    return sorted(set(ys)), Tfull


def count_q(ys, Tfull, qmax):
    if qmax < 0 or not ys:
        return 0
    if qmax < Tfull:
        return bisect_right(ys, qmax)
    k, r = divmod(qmax, Tfull)
    i = bisect_right(ys, r)
    return len(ys) * k + i


def D(limit):
    total = 0
    if limit >= 5 and (pow(2, 6) - 2 - 54) % M == 0:
        total += 1
    for r in range(6):
        ys, Tfull = arithmetic_progressions(r)
        total += count_q(ys, Tfull, (limit - 6 - r) // 6)
    return total


def solve():
    return D(L)


if __name__ == "__main__":
    print(solve())
