# Problem 324: https://projecteuler.net/problem=324

from itertools import product


MOD = 100_000_007
N = 10**10000
SAMPLES = 100
CELLS = tuple(product(range(3), range(3)))
POS = {cell: i for i, cell in enumerate(CELLS)}
ZERO = (0,) * 9


def transitions_for(state):
    out = {}

    def rec(cur, nxt):
        try:
            i = cur.index(0)
        except ValueError:
            out[nxt] = out.get(nxt, 0) + 1
            return

        cur2 = list(cur)
        cur2[i] = 1
        nxt2 = list(nxt)
        nxt2[i] = 1
        rec(tuple(cur2), tuple(nxt2))

        r, c = CELLS[i]
        for dr, dc in ((1, 0), (0, 1)):
            nb = (r + dr, c + dc)
            if nb in POS:
                j = POS[nb]
                if cur[j] == 0:
                    cur2 = list(cur)
                    cur2[i] = cur2[j] = 1
                    rec(tuple(cur2), nxt)

    rec(state, ZERO)
    return out


def terms(count):
    trans = {s: transitions_for(s) for s in product((0, 1), repeat=9)}
    dp = {ZERO: 1}
    seq = []

    for _ in range(count):
        seq.append(dp.get(ZERO, 0) % MOD)
        ndp = {}
        for s, v in dp.items():
            for t, w in trans[s].items():
                ndp[t] = (ndp.get(t, 0) + v * w) % MOD
        dp = ndp

    return seq


def recurrence(seq):
    c = [1]
    b = [1]
    l = 0
    m = 1
    d0 = 1

    for n in range(len(seq)):
        d = seq[n]
        for i in range(1, l + 1):
            d = (d + c[i] * seq[n - i]) % MOD

        if d == 0:
            m += 1
            continue

        old = c[:]
        coef = d * pow(d0, -1, MOD) % MOD
        if len(c) < len(b) + m:
            c.extend([0] * (len(b) + m - len(c)))

        for j in range(len(b)):
            c[j + m] = (c[j + m] - coef * b[j]) % MOD

        if 2 * l <= n:
            l = n + 1 - l
            b = old
            d0 = d
            m = 1
        else:
            m += 1

    return [(-x) % MOD for x in c[1:]]


def nth(seq, coef, n):
    d = len(coef)
    if n < len(seq):
        return seq[n]

    def combine(a, b):
        tmp = [0] * (2 * d - 1)

        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y:
                        tmp[i + j] = (tmp[i + j] + x * y) % MOD

        for i in range(2 * d - 2, d - 1, -1):
            v = tmp[i]
            if v:
                for j, cj in enumerate(coef, 1):
                    tmp[i - j] = (tmp[i - j] + v * cj) % MOD

        return tmp[:d]

    res = [1] + [0] * (d - 1)
    base = [0] * d
    base[1 if d > 1 else 0] = 1 if d > 1 else coef[0]

    while n:
        if n % 2:
            res = combine(res, base)
        base = combine(base, base)
        n //= 2

    return sum(a * b for a, b in zip(res, seq[:d])) % MOD


def solve():
    seq = terms(SAMPLES)
    return nth(seq, recurrence(seq), N)


if __name__ == "__main__":
    print(solve())
