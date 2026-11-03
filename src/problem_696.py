# Problem 696: https://projecteuler.net/problem=696
from math import comb

MOD = 10**9 + 7


def step(state, c):
    nxt = set()
    for a, b, u in state:
        r = c - a - b
        if r < 0:
            continue
        for q in range(min(2, r) + 1):
            left = r - q
            if left in (0, 3):
                nxt.add((b, q, u))
            elif left == 2 and u == 0:
                nxt.add((b, q, 1))
    return frozenset(nxt)


def w(n, s, t):
    top = 3 * t + 2
    run = {}
    cur = {frozenset([(0, 0, 0)]): {0: 1}}
    for L in range(1, top + 1):
        new = {}
        for state, sums in cur.items():
            for c in range(1, 5):
                ns = step(state, c)
                if not ns:
                    continue
                d = new.setdefault(ns, {})
                for tot, v in sums.items():
                    if tot + c <= top:
                        d[tot + c] = d.get(tot + c, 0) + v
        cur = new
        for state, sums in cur.items():
            if (0, 0, 0) in state or (0, 0, 1) in state:
                for tot, v in sums.items():
                    if tot % 3 != 1:
                        run[L, tot] = run.get((L, tot), 0) + v

    g = {}
    layer = {(0, 0, 0): 1}
    for m in range(1, t + 2):
        nl = {}
        for (S, tot, p), v in layer.items():
            for (L, x), r in run.items():
                q = p + (x % 3 == 2)
                if q > 1 or tot + x > top or S + L > n:
                    continue
                key = (S + L, tot + x, q)
                nl[key] = (nl.get(key, 0) + v * r) % MOD
        layer = nl
        for (S, tot, p), v in layer.items():
            g[m, S, tot, p] = v

    A = [0] * (t + 1)
    B = [0] * (t + 1)
    A[0] = 1
    for (m, S, tot, p), v in g.items():
        ways = comb(n - S + 1, m) % MOD * v % MOD
        if p:
            B[tot // 3] = (B[tot // 3] + ways) % MOD
        else:
            A[tot // 3] = (A[tot // 3] + ways) % MOD

    a = A[:]
    a[0] = 0
    power = [1] + [0] * t
    total = [0] * (t + 1)
    for j in range(t + 1):
        cf = comb(s - 1, j) % MOD
        for i in range(t + 1):
            total[i] = (total[i] + cf * power[i]) % MOD
        nxt = [0] * (t + 1)
        for i in range(t + 1):
            if power[i]:
                for k in range(1, t + 1 - i):
                    nxt[i + k] = (nxt[i + k] + power[i] * a[k]) % MOD
        power = nxt

    res = 0
    for k in range(t + 1):
        res += B[k] * total[t - k]
    return s * res % MOD


def solve():
    return w(10**8, 10**8, 30)


if __name__ == "__main__":
    print(solve())
