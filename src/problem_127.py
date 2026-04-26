# Problem 127: https://projecteuler.net/problem=127

from math import gcd


def radicals(lim):
    rad = [1] * lim
    for p in range(2, lim):
        if rad[p] == 1:
            for n in range(p, lim, p):
                rad[n] *= p
    return rad


def solve():
    lim = 120_000
    rad = radicals(lim)
    by_rad = sorted((rad[n], n) for n in range(1, lim))
    total = 0

    for c in range(3, lim):
        rc = rad[c]
        for ra, a in by_rad:
            if ra * rc >= c:
                break
            if 2 * a >= c:
                continue

            b = c - a
            if ra * rad[b] * rc < c and gcd(a, b) == 1:
                total += c

    return total


if __name__ == "__main__":
    print(solve())
