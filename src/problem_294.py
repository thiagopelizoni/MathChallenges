# Problem 294: https://projecteuler.net/problem=294


MOD = 10**9
N = 11**12
S = 23
R = 23


def unit(w):
    a = [[0] * R for _ in range(S + 1)]
    for d in range(10):
        a[d][d * w % R] += 1
    return a


def mul(a, b):
    c = [[0] * R for _ in range(S + 1)]

    for i, ai in enumerate(a):
        for j, bj in enumerate(b[: S + 1 - i]):
            row = c[i + j]
            for r, x in enumerate(ai):
                if not x:
                    continue
                for s, y in enumerate(bj):
                    if y:
                        k = (r + s) % R
                        row[k] = (row[k] + x * y) % MOD

    return c


def prod(ws):
    a = [[0] * R for _ in range(S + 1)]
    a[0][0] = 1
    for w in ws:
        a = mul(a, unit(w))
    return a


def power(a, n):
    r = [[0] * R for _ in range(S + 1)]
    r[0][0] = 1

    while n:
        if n % 2:
            r = mul(r, a)
        n //= 2
        if n:
            a = mul(a, a)

    return r


def solve():
    ws = []
    w = 1
    for _ in range(22):
        ws.append(w)
        w = w * 10 % R

    q, r = divmod(N, 22)
    return mul(power(prod(ws), q), prod(ws[:r]))[S][0]


if __name__ == "__main__":
    print(solve())
