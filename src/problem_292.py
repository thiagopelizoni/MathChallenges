# Problem 292: https://projecteuler.net/problem=292

from math import gcd, isqrt


LIM = 120
SIDE = 2 * LIM + 1
AREA = SIDE * SIDE


def pack(x, y, p):
    return p * AREA + (x + LIM) * SIDE + (y + LIM)


def groups(n):
    d = {}
    bad = 0

    for x in range(-n, n + 1):
        x2 = x * x
        for y in range(-n, n + 1):
            if x == 0 and y == 0:
                continue

            l = isqrt(x2 + y * y)
            if l * l != x2 + y * y or l > n:
                continue

            if 2 * l <= n:
                bad += 1

            g = gcd(abs(x), abs(y))
            d.setdefault((x // g, y // g), []).append(
                (l, l * AREA + x * SIDE + y)
            )

    return [sorted(d[k]) for k in sorted(d)], bad // 2


def count(n):
    gs, bad = groups(n)
    dp = {pack(0, 0, 0): 1}

    for g in gs:
        nxt = dp.copy()
        get = nxt.get
        for k, ways in dp.items():
            left = n - k // AREA
            for l, delta in g:
                if l > left:
                    break
                nk = k + delta
                nxt[nk] = get(nk, 0) + ways
        dp = nxt

    return sum(dp.get(pack(0, 0, p), 0) for p in range(n + 1)) - 1 - bad


def solve():
    return count(LIM)


if __name__ == "__main__":
    print(solve())
