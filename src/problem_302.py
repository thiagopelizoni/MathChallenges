# Problem 302: https://projecteuler.net/problem=302

from bisect import bisect_right
from math import gcd, isqrt


LIM = 10**18


def icbrt(n):
    x = int(n ** (1 / 3))
    while (x + 1) ** 3 <= n:
        x += 1
    while x**3 > n:
        x -= 1
    return x


def prime_data(n):
    spf = list(range(n + 1))
    primes = []

    for i in range(2, n + 1):
        if spf[i] == i:
            primes.append(i)
            if i * i <= n:
                for j in range(i * i, n + 1, i):
                    if spf[j] == j:
                        spf[j] = i

    return primes, spf


def factor(n, spf):
    f = []
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        f.append((p, e))
    return tuple(f)


def solve():
    pmax = icbrt((LIM - 1) // 4) + 2
    primes, spf = prime_data(pmax)
    fac = {p: factor(p - 1, spf) for p in primes}

    exp = {}
    ones = set()
    ans = 0

    def put(q, a, changes):
        old = exp.get(q, 0)
        if old == 1:
            ones.remove(q)
        new = old + a
        exp[q] = new
        if new == 1:
            ones.add(q)
        changes.append((q, old))

    def apply(p, e):
        changes = []
        put(p, e - 1, changes)
        for q, a in fac[p]:
            put(q, a, changes)
        return changes

    def undo(changes):
        for q, old in reversed(changes):
            cur = exp[q]
            if cur == 1:
                ones.remove(q)
            if old:
                exp[q] = old
                if old == 1:
                    ones.add(q)
            else:
                del exp[q]

    def phi_gcd():
        g = 0
        for e in exp.values():
            g = gcd(g, e) if g else e
            if g == 1:
                return 1
        return g

    def search(maxi, n, depth, g):
        nonlocal ans

        if depth >= 2 and g == 1 and not ones and phi_gcd() == 1:
            ans += 1

        fit = bisect_right(primes, isqrt((LIM - 1) // n), 0, maxi)
        if fit == 0:
            return

        if ones:
            d = max(ones)
            top = primes[fit - 1]
            if top < d:
                return
            if top == d:
                p = top
                e = 2
                pe = p * p
                while n * pe < LIM:
                    changes = apply(p, e)
                    search(fit - 1, n * pe, depth + 1, gcd(g, e))
                    undo(changes)
                    pe *= p
                    e += 1
                return

        for idx in range(fit - 1, -1, -1):
            p = primes[idx]
            e = 2
            pe = p * p
            while n * pe < LIM:
                changes = apply(p, e)
                search(idx, n * pe, depth + 1, gcd(g, e))
                undo(changes)
                pe *= p
                e += 1

    for idx, p in enumerate(primes):
        e = 3
        pe = p**3
        while pe * 4 < LIM:
            changes = apply(p, e)
            search(idx, pe, 1, e)
            undo(changes)
            pe *= p
            e += 1

    return ans


if __name__ == "__main__":
    print(solve())
