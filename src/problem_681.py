# Problem 681: https://projecteuler.net/problem=681
from math import gcd, isqrt
from sympy import divisors, integer_nthroot
from sympy.ntheory.factor_ import core


def tally(X, Y, k, qs):
    e = X - Y
    a = X + Y
    s = 0
    for r, Z, W in qs:
        L = k // r
        if L == 0:
            break
        b = Z + W
        if Z * e >= Y * b or e >= b * L:
            continue
        h = 1
        while True:
            lo = (h * Z + Y - 1) // Y
            hi = L // h
            if lo > hi:
                break
            if e:
                hi = min(hi, (h * b - 1) // e)
            if a % 2:
                lo += (lo + h * b) % 2
                hi -= (hi + h * b) % 2
                step = 2
            elif h * b % 2:
                h += 1
                continue
            else:
                step = 1
            if lo <= hi:
                t = (hi - lo) // step + 1
                s += t * h * b + a * (lo + hi) * t // 2
            h += 1
    return s


def solve(n=1_000_000):
    nn = n * n
    m = integer_nthroot(nn, 3)[0]
    sq = [0] + [core(v) for v in range(1, m + 1)]

    small = {}
    W = 1
    while W ** 4 <= nn:
        Z = W
        while Z ** 3 * W <= nn and Z * W <= n:
            if gcd(Z, W) == 1:
                c = sq[Z] * sq[W]
                small.setdefault(c, []).append((isqrt(Z * W // c), Z, W))
            Z += 1
        W += 1

    ans = 0
    for c, qs in small.items():
        qs.sort()
        for c1 in divisors(c):
            c2 = c // c1
            B = 1
            while c * (c2 * B * B) ** 2 <= nn:
                Y = c2 * B * B
                A = isqrt((Y - 1) // c1) + 1
                while True:
                    X = c1 * A * A
                    if X >= 3 * Y or c * A * B * qs[0][0] > n or Y * Y * (X - Y + 1) > 2 * nn:
                        break
                    if gcd(X, Y) == 1:
                        ans += tally(X, Y, n // (c * A * B), qs)
                    A += 1
                B += 1
    return ans


if __name__ == "__main__":
    print(solve())
