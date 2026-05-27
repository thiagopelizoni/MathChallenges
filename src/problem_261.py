# Problem 261: https://projecteuler.net/problem=261

from math import isqrt


def square_parts(lim):
    spf = list(range(lim + 1))
    for p in range(2, isqrt(lim) + 1):
        if spf[p] == p:
            for n in range(p * p, lim + 1, p):
                if spf[n] == n:
                    spf[n] = p

    sf = [0] * (lim + 1)
    sq = [0] * (lim + 1)
    sf[1] = sq[1] = 1

    for n in range(2, lim + 1):
        x = n
        s = q = 1
        while x > 1:
            p = spf[x]
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            if e % 2:
                s *= p
            q *= p ** (e // 2)
        sf[n] = s
        sq[n] = q

    return sf, sq


def pell_unit(d):
    a0 = isqrt(d)
    m = 0
    q = 1
    a = a0
    x0, x = 1, a
    y0, y = 0, 1

    while x * x - d * y * y != 1:
        m = q * a - m
        q = (d - m * m) // q
        a = (a0 + m) // q
        x0, x = x, x0 + a * x
        y0, y = y, y0 + a * y

    return x, y


def solve():
    lim = 10**10
    mlim = (isqrt(2 * lim + 1) - 1) // 2
    sf, sq = square_parts(mlim + 1)
    pivots = set()
    units = {}

    for m in range(1, mlim + 1):
        s = sf[m] * sf[m + 1]
        q = sq[m] * sq[m + 1]
        x1, y1 = units.setdefault(s, pell_unit(s))
        x, y = x1, y1
        xmax = (2 * lim - m) // m

        while x <= xmax:
            if x % 2 and x >= 2 * m + 1:
                num = m * x + q * s * y + m
                if num % 2 == 0:
                    k = num // 2
                    if k <= lim:
                        pivots.add(k)
            x, y = x1 * x + s * y1 * y, x1 * y + y1 * x

    return sum(pivots)


if __name__ == "__main__":
    print(solve())
