# Problem 188: https://projecteuler.net/problem=188
from math import lcm


def factor(n):
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        factors[n] = 1
    return factors


def carmichael(n):
    values = []
    for p, a in factor(n).items():
        if p == 2 and a >= 3:
            values.append(2 ** (a - 2))
        else:
            values.append((p - 1) * p ** (a - 1))
    return lcm(*values)


def tower_mod(a, h, mod):
    if mod == 1:
        return 0
    if h == 1:
        return a % mod
    return pow(a, tower_mod(a, h - 1, carmichael(mod)), mod)


def solve():
    return tower_mod(1777, 1855, 10**8)


if __name__ == "__main__":
    print(solve())
