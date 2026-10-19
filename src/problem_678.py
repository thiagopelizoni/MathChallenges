# Problem 678: https://projecteuler.net/problem=678

from collections import defaultdict
import math
import numpy as np
from sympy import integer_nthroot


def solve():
    n_lim = 10**18
    limit3 = integer_nthroot(n_lim, 3)[0]

    spf = list(range(limit3 + 1))
    for i in range(2, math.isqrt(limit3) + 1):
        if spf[i] == i:
            for j in range(i * i, limit3 + 1, i):
                if spf[j] == j:
                    spf[j] = i

    gauss_p = {}

    def get_gauss(p):
        if p not in gauss_p:
            for u in range(1, math.isqrt(p) + 1):
                v2 = p - u * u
                v = math.isqrt(v2)
                if v * v == v2:
                    gauss_p[p] = (u, v)
                    break
        return gauss_p[p]

    def g_mul(z1, z2):
        return (z1[0] * z2[0] - z1[1] * z2[1], z1[0] * z2[1] + z1[1] * z2[0])

    def g_pow(z, e):
        res = (1, 0)
        base = z
        while e > 0:
            if e % 2 == 1:
                res = g_mul(res, base)
            base = g_mul(base, base)
            e //= 2
        return res

    total = 0
    by_val = defaultdict(int)
    powers_ge4 = []

    for c in range(2, limit3 + 1):
        x = c
        fac = []
        while x > 1:
            p = spf[x]
            cnt = 0
            while x % p == 0:
                x //= p
                cnt += 1
            fac.append((p, cnt))

        cf = c * c * c
        f = 3
        while cf <= n_lim:
            ok_e2 = True
            prod_e2 = 1
            for p, cnt in fac:
                if p % 4 == 3 and (cnt * f) % 2 == 1:
                    ok_e2 = False
                    break
                if p % 4 == 1:
                    prod_e2 *= cnt * f + 1
            if ok_e2:
                total += prod_e2 // 2

            if f >= 4:
                by_val[cf] += 1
                powers_ge4.append((cf, c, f, fac))

            ok_e4 = True
            has_1mod8 = False
            for p, cnt in fac:
                ef = cnt * f
                if p == 2:
                    if ef % 4 not in (0, 1):
                        ok_e4 = False
                        break
                elif p % 8 != 1:
                    if ef % 4 != 0:
                        ok_e4 = False
                        break
                else:
                    has_1mod8 = True

            if ok_e4 and has_1mod8:
                scale = 1
                states = [(1, 0)]
                for p, cnt in fac:
                    ef = cnt * f
                    if p == 2:
                        scale *= 2 ** (ef // 2)
                        if ef % 2 == 1:
                            states = [g_mul(z, (1, 1)) for z in states]
                    elif p % 4 == 3:
                        scale *= p ** (ef // 2)
                    else:
                        u, v = get_gauss(p)
                        new_states = []
                        for k in range(ef + 1):
                            zf = g_mul(g_pow((u, v), k), g_pow((u, -v), ef - k))
                            for z in states:
                                new_states.append(g_mul(z, zf))
                        states = new_states

                seen_pairs = set()
                for zx, zy in states:
                    x_sq = abs(zx) * scale
                    y_sq = abs(zy) * scale
                    if x_sq > y_sq:
                        x_sq, y_sq = y_sq, x_sq
                    if 0 < x_sq < y_sq and (x_sq, y_sq) not in seen_pairs:
                        seen_pairs.add((x_sq, y_sq))
                        a = math.isqrt(x_sq)
                        if a * a == x_sq:
                            b = math.isqrt(y_sq)
                            if b * b == y_sq:
                                total += 1

            cf *= c
            f += 1

    for n, c, f, fac in powers_ge4:
        if f % 3 == 0:
            continue
        low = integer_nthroot(n, 3)[0]
        high = integer_nthroot(4 * n - 1, 3)[0]

        divs = [1]
        for p, cnt in fac:
            pe = cnt * f
            new_divs = []
            pw = 1
            for _ in range(pe + 1):
                for d in divs:
                    val = d * pw
                    if val <= high:
                        new_divs.append(val)
                pw *= p
            divs = new_divs

        for s in divs:
            if s > low:
                q = n // s
                num = 4 * q - s * s
                if num > 0 and num % 3 == 0:
                    d2 = num // 3
                    d = math.isqrt(d2)
                    if d * d == d2 and (s - d) % 2 == 0 and s > d > 0:
                        total += 1

    ge4_keys = np.array(sorted(by_val.keys()), dtype=np.int64)
    ge4_cnts = np.array([by_val[int(k)] for k in ge4_keys], dtype=np.int64)

    e = 5
    while 1 + 2**e <= n_lim:
        max_b = integer_nthroot(n_lim, e)[0]
        pe_arr = np.array([x**e for x in range(max_b + 1)], dtype=np.int64)
        for b in range(2, max_b + 1):
            be = int(pe_arr[b])
            lim_a = b - 1
            if int(pe_arr[lim_a]) + be > n_lim:
                lim_a = int(np.searchsorted(pe_arr, n_lim - be, side="right")) - 1
            if lim_a < 1:
                continue
            s_arr = pe_arr[1 : lim_a + 1] + be

            pos = np.searchsorted(ge4_keys, s_arr)
            valid = pos < len(ge4_keys)
            if np.any(valid):
                v_pos = pos[valid]
                hit = ge4_keys[v_pos] == s_arr[valid]
                if np.any(hit):
                    total += int(ge4_cnts[v_pos[hit]].sum())

            cr = np.rint(np.cbrt(s_arr)).astype(np.int64)
            matches = np.nonzero(cr * cr * cr == s_arr)[0]
            for idx in matches:
                s_val = int(pe_arr[int(idx) + 1]) + be
                if integer_nthroot(s_val, 3)[1]:
                    total += 1
        e += 1

    return total


if __name__ == "__main__":
    print(solve())
