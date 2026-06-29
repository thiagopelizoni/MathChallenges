# Problem 344: https://projecteuler.net/problem=344

from math import comb

from sympy.ntheory.modular import crt


N = 1_000_000
C = 100
P = 1_000_003
Q = 1_000_033


def digits(n):
    out = []

    while n:
        n, r = divmod(n, 2)
        out.append(r)

    return out or [0]


def choices(active, passive, mod):
    out = [0] * (active + passive + 1)

    for x in range(0, active + 1, 2):
        a = comb(active, x)
        for y in range(passive + 1):
            s = x + y
            out[s] = (out[s] + a * comb(passive, y)) % mod

    return [(s, v) for s, v in enumerate(out) if v]


def count(total, active, passive, mod):
    terms = choices(active, passive, mod)
    dp = {0: 1}

    for d in digits(total):
        nxt = {}
        for carry, val in dp.items():
            for s, ways in terms:
                z = carry + s
                if z % 2 == d:
                    nc = (z - d) // 2
                    nxt[nc] = (nxt.get(nc, 0) + val * ways) % mod
        dp = nxt

    return dp.get(0, 0)


def losing(n, c, mod):
    coins = c + 1
    empty = n - coins
    active = (coins + 1) // 2
    passive = coins - active + 1
    second = count(empty, active, passive, mod)
    other = count(empty + 1, active, passive, mod) - count(
        empty + 1, active - 1, passive, mod
    )

    return (second + (coins - 2) * other) % mod


def w(n, c, mod):
    coins = c + 1
    return (coins * (comb(n, coins) % mod) - losing(n, c, mod)) % mod


def solve():
    return int(crt([P, Q], [w(N, C, P), w(N, C, Q)])[0])


if __name__ == "__main__":
    print(solve())
