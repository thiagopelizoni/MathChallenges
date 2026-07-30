# Problem 474: https://projecteuler.net/problem=474

import numpy as np
from sympy import primerange, primitive_root


def add_mod(a, b, mod):
    result = a + b
    np.subtract(result, mod, out=result, where=result >= mod)
    return result


def geometric_sum(values, shift, length, mod, order):
    if length == 1:
        return values
    if length % 2 == 0:
        half = geometric_sum(values, shift, length // 2, mod, order)
        offset = (shift[0] * (length // 2) % 2, shift[1] * (length // 2) % order)
        return add_mod(half, np.roll(half, offset, axis=(0, 1)), mod)
    shorter = geometric_sum(values, shift, length - 1, mod, order)
    offset = (shift[0] * (length - 1) % 2, shift[1] * (length - 1) % order)
    return add_mod(shorter, np.roll(values, offset, axis=(0, 1)), mod)


def solve():
    n = 10**6
    mod = 10**16 + 61
    q = 3125
    order = 2500
    root = primitive_root(q)
    logs = {}
    value = 1
    for k in range(order):
        logs[value] = k
        value = value * root % q

    dp = np.zeros((2, order), dtype=np.int64)
    dp[0, 0] = 1
    for p in primerange(3, n + 1):
        if p == 5:
            continue
        exponent = 0
        quotient = n
        while quotient:
            quotient //= p
            exponent += quotient
        shift = (p % 4 // 2, logs[p % q])
        dp = geometric_sum(dp, shift, exponent + 1, mod, order)

    target = 65432 // 8
    return int(dp[target % 4 // 2, logs[target % q]])


if __name__ == "__main__":
    print(solve())
