# Problem 752: https://projecteuler.net/problem=752

import numpy as np
from sympy import factorint, primerange


def power(n, mod):
    a, b = 1, 0
    c, d = 1, 1
    while n:
        n, r = divmod(n, 2)
        if r:
            a, b = (a * c + 7 * b * d) % mod, (a * d + b * c) % mod
        c, d = (c * c + 7 * d * d) % mod, (2 * c * d) % mod
    return a, b


def solve(limit=10**6):
    orders = np.ones(limit + 1, dtype=np.int64)
    orders[::2] = 0
    orders[::3] = 0
    for p in primerange(5, limit + 1):
        if p == 7:
            order = 7
        else:
            order = p * p - 1
            factors = set(factorint(p - 1)).union(factorint(p + 1))
            for q in factors:
                while order % q == 0 and power(order // q, p) == (1, 0):
                    order //= q
        m = p
        while m <= limit:
            if power(order, m) != (1, 0):
                order *= p
            np.lcm(orders[m::m], order, out=orders[m::m])
            m *= p
    return int(orders[2:].sum())


if __name__ == "__main__":
    print(solve())
