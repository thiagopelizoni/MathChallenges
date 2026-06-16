# Problem 311: https://projecteuler.net/problem=311

from functools import lru_cache
from math import isqrt


N = 10_000_000_000


def primes_1mod4(n):
    if n < 5:
        return []

    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"

    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = b"\x00" * ((n - p * p) // p + 1)

    return [p for p in range(5, n + 1, 4) if sieve[p]]


def z_prefix(lim, ps):
    good = bytearray(b"\x01") * (lim + 1)
    good[0] = 0

    for n in range(2, lim + 1, 2):
        good[n] = 0

    for p in ps:
        if p > lim:
            break
        for n in range(p, lim + 1, p):
            good[n] = 0

    pref = [0] * (lim + 1)
    total = 0
    for n in range(1, lim + 1):
        total += good[n]
        pref[n] = total

    return pref


def p0(d):
    return d * (d - 2) * (d - 4) // 48


def psq(d):
    return (d - 1) * (d - 3) * (d - 5) // 48


def ptw(d):
    return (d - 1) * (d - 3) * (d + 1) // 48


def count(n):
    x = n // 4
    ps = primes_1mod4(x // 25)
    pref = z_prefix(isqrt(x), ps)

    @lru_cache(maxsize=None)
    def b_counts(y):
        total = sq = tw = 0
        q = 1
        odd = False

        while q <= y:
            c = pref[isqrt(y // q)]
            total += c
            if odd:
                tw += c
            else:
                sq += c
            q *= 2
            odd = not odd

        return total, sq, tw

    def contribution(d, square, y):
        if square:
            a = psq(d)
            b = ptw(d)
            if a == 0 and b == 0:
                return 0
            total, sq, tw = b_counts(y)
            return a * sq + b * tw

        a = p0(d)
        if a == 0:
            return 0
        total, sq, tw = b_counts(y)
        return a * total

    ans = contribution(1, True, x)

    def search(i, a, d, square):
        nonlocal ans

        for j in range(i, len(ps)):
            p = ps[j]
            val = a * p
            if val > x:
                break

            e = 1
            while val <= x:
                nd = d * (e + 1)
                nsq = square and e % 2 == 0
                ans += contribution(nd, nsq, x // val)

                if val * p <= x:
                    search(j + 1, val, nd, nsq)

                e += 1
                val *= p

    search(0, 1, 1, True)
    return ans


def solve():
    return count(N)


if __name__ == "__main__":
    print(solve())
