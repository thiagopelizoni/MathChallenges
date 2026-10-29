# Problem 690: https://projecteuler.net/problem=690
from sympy.functions.combinatorial.numbers import partition


def mul(a, b, n, mod):
    c = [0] * (n + 1)
    for i in range(n + 1):
        if a[i]:
            for j in range(n + 1 - i):
                c[i + j] = (c[i + j] + a[i] * b[j]) % mod
    return c


def solve(n=2019, mod=10**9 + 7):
    p = [int(partition(m)) % mod for m in range(n + 1)]
    q = [(x - 1) % mod for x in p]

    a = [1] + [0] * n
    for k in range(1, n + 1):
        a[k] = sum(p[m] * a[k - 1 - m] for m in range(k)) % mod

    r = mul(q, a, n, mod)
    qqa = mul(q, r, n, mod)
    r2 = [0] * (n + 1)
    for i in range(n // 2 + 1):
        r2[2 * i] = r[i]
    pr2 = mul(p, r2, n, mod)

    inv2 = pow(2, -1, mod)
    lob = [0] * (n + 1)
    for k in range(1, n + 1):
        t = 1
        if k >= 2:
            t += p[k - 1] - (k - 1)
        if k >= 4:
            t += (k - 2) // 2
        if k >= 2:
            pal = r2[k - 2]
            if k >= 3:
                pal += pr2[k - 3]
            t += (qqa[k - 2] + pal) * inv2
        lob[k] = t % mod

    c = [0] * (n + 1)
    for d in range(1, n + 1):
        for k in range(d, n + 1, d):
            c[k] = (c[k] + d * lob[d]) % mod

    f = [1] + [0] * n
    for m in range(1, n + 1):
        s = sum(c[k] * f[m - k] for k in range(1, m + 1))
        f[m] = s * pow(m, -1, mod) % mod
    return f[n]


if __name__ == "__main__":
    print(solve())
