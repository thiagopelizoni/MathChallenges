# Problem 342: https://projecteuler.net/problem=342

from bisect import bisect_right
from math import isqrt

from sympy import factorint, primerange


N = 10**10


def add(pending, factors):
    out = pending.copy()

    for p, e in factors:
        r = (out.get(p, 0) + e) % 3
        if r:
            out[p] = r
        else:
            out.pop(p, None)

    return out


def solve():
    primes = list(primerange(2, isqrt(N) + 1))
    pos = {p: i for i, p in enumerate(primes)}
    factors = {
        p: tuple((q, e % 3) for q, e in factorint(p - 1).items() if e % 3)
        for p in primes
    }

    def search(n, max_pos, pending):
        forced = max(pending, default=0)
        room = (N - 1) // n
        opt_pos = min(max_pos, bisect_right(primes, isqrt(room)))
        lo = pos[forced] + 1 if forced else 0
        total = 0

        for i in range(opt_pos - 1, lo - 1, -1):
            p = primes[i]
            m = n * p * p
            out = add(pending, factors[p])
            while m < N:
                total += search(m, i, out)
                m *= p * p * p

        if forced:
            r = pending[forced]
            e = (2 * (1 - r)) % 3 or 3
            m = n * forced**e
            out = pending.copy()
            out.pop(forced)
            out = add(out, factors[forced])

            while m < N:
                total += search(m, pos[forced], out)
                m *= forced**3
        elif n > 1:
            total += n

        return total

    return search(1, len(primes), {})


if __name__ == "__main__":
    print(solve())
