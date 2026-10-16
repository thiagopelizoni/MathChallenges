# Problem 671: https://projecteuler.net/problem=671

import numpy as np


def solve():
    k = 10
    n = 10004003002001
    mod = 1000004321

    v_cols = [0, 1, 2]
    h_cols = [(0, 1), (1, 0), (0, 2), (2, 0), (1, 2), (2, 1), (2, 3)]
    states = [("V", c) for c in v_cols]
    for rt in range(3):
        for rb in range(3):
            for ct, cb in h_cols:
                states.append(("H", rt, rb, ct, cb))

    idx = {s: i for i, s in enumerate(states)}
    sz = len(states)
    mat = np.zeros((sz, sz), dtype=object)

    def add_h(i, rt, rb, ct, cb, w=1):
        if ct >= 2 and cb >= 2:
            pair = (2, 3)
        else:
            pair = (ct if ct < 2 else 2, cb if cb < 2 else 2)
        mat[i, idx[("H", rt, rb, pair[0], pair[1])]] += w

    for s in states:
        i = idx[s]
        if s[0] == "V":
            _, c = s
            m = 2 if c < 2 else 3
            for c2 in range(m + 1):
                if c2 != c:
                    w = 1 if c2 < m else (k - m)
                    mat[i, idx[("V", c2 if c2 < 2 else 2)]] += w
            for ct in range(m + 1):
                if ct == c:
                    continue
                wt = 1 if ct < m else (k - m)
                m2 = max(m, ct + 1)
                for cb in range(m2 + 1):
                    if cb == c or cb == ct:
                        continue
                    wb = 1 if cb < m2 else (k - m2)
                    for lt in (1, 2, 3):
                        for lb in (1, 2, 3):
                            add_h(i, lt - 1, lb - 1, ct, cb, wt * wb)
        else:
            _, rt, rb, ct, cb = s
            m = max(2, ct + 1, cb + 1)
            if rt == 0 and rb == 0:
                for c2 in range(m + 1):
                    if c2 != ct and c2 != cb:
                        w = 1 if c2 < m else (k - m)
                        mat[i, idx[("V", c2 if c2 < 2 else 2)]] += w
            elif rt > 0 and rb > 0:
                add_h(i, rt - 1, rb - 1, ct, cb, 1)
            elif rt == 0 and rb > 0:
                for ct2 in range(m + 1):
                    if ct2 != ct and ct2 != cb:
                        w = 1 if ct2 < m else (k - m)
                        for lt in (1, 2, 3):
                            add_h(i, lt - 1, rb - 1, ct2, cb, w)
            elif rt > 0 and rb == 0:
                for cb2 in range(m + 1):
                    if cb2 != cb and cb2 != ct:
                        w = 1 if cb2 < m else (k - m)
                        for lb in (1, 2, 3):
                            add_h(i, rt - 1, lb - 1, ct, cb2, w)

    res = np.eye(sz, dtype=object)
    base = mat % mod
    e = n
    while e > 0:
        if e % 2 == 1:
            res = (res @ base) % mod
        base = (base @ base) % mod
        e //= 2

    total = k * res[idx[("V", 0)], idx[("V", 0)]]
    for rt in range(3):
        for rb in range(3):
            u = idx[("H", rt, rb, 0, 1)]
            total += k * (k - 1) * res[u, u]

    return (total % mod) * pow(n, -1, mod) % mod


if __name__ == "__main__":
    print(solve())
