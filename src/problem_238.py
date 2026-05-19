# Problem 238: https://projecteuler.net/problem=238
import numpy as np


LIMIT = 2_000_000_000_000_000
MOD = 20_300_713
S0 = 14_025_256


def digits():
    seen = set()
    parts = []
    s = S0
    while s not in seen:
        seen.add(s)
        parts.append(str(s))
        s = s * s % MOD
    w = "".join(parts)
    return np.fromiter((int(c) for c in w), dtype=np.int16, count=len(w))


def first_positions(pref, total):
    sums = np.unique(pref[:-1])
    p = np.zeros(total, dtype=np.uint32)
    p[0] = 1
    covered = 1
    last = -1

    for i, x in enumerate(pref[:-1]):
        x = int(x)
        if x == last:
            continue
        last = x

        cut = np.searchsorted(sums, x)
        for r in (sums[cut:] - x, sums[:cut] + total - x):
            free = p[r] == 0
            if free.any():
                p[r[free]] = i + 1
                covered += int(free.sum())
        if covered == total:
            return p

    return p


def solve():
    d = digits()
    pref = np.empty(len(d) + 1, dtype=np.int64)
    pref[0] = 0
    np.cumsum(d, out=pref[1:])

    total = int(pref[-1])
    p = first_positions(pref, total)
    q, r = divmod(LIMIT, total)
    return q * int(p.sum()) + int(p[1:r + 1].sum())


if __name__ == "__main__":
    print(solve())
