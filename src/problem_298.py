# Problem 298: https://projecteuler.net/problem=298

from collections import defaultdict


TURNS = 50
VALUES = 10
SIZE = 5


def canon(l, r):
    mp = {}
    nl = []
    for x in l:
        if x not in mp:
            mp[x] = len(mp)
        nl.append(mp[x])

    nr = []
    for x in r:
        if x not in mp:
            mp[x] = len(mp)
        nr.append(mp[x])

    return tuple(nl), tuple(nr)


def larry(mem, x):
    mem = list(mem)
    hit = x in mem
    if hit:
        mem.remove(x)
    elif len(mem) == SIZE:
        mem.pop(0)
    mem.append(x)
    return tuple(mem), hit


def robin(mem, x):
    mem = list(mem)
    hit = x in mem
    if not hit:
        if len(mem) == SIZE:
            mem.pop(0)
        mem.append(x)
    return tuple(mem), hit


def solve():
    dp = {((), (), 0): 1}

    for _ in range(TURNS):
        nd = defaultdict(int)
        for (l, r, d), cnt in dp.items():
            n = len(set(l).union(r))

            for x in range(n):
                nl, lh = larry(l, x)
                nr, rh = robin(r, x)
                nl, nr = canon(nl, nr)
                nd[(nl, nr, d + int(lh) - int(rh))] += cnt

            if n < VALUES:
                nl, _ = larry(l, n)
                nr, _ = robin(r, n)
                nl, nr = canon(nl, nr)
                nd[(nl, nr, d)] += cnt * (VALUES - n)

        dp = nd

    num = 0
    for (_, _, d), cnt in dp.items():
        num += abs(d) * cnt

    den = VALUES**TURNS
    ans = (2 * num * 10**8 + den) // (2 * den)
    return f"{ans // 10**8}.{ans % 10**8:08d}"


if __name__ == "__main__":
    print(solve())
