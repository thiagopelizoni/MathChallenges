# Problem 417: https://projecteuler.net/problem=417

from bisect import bisect_right
from math import isqrt

import numpy as np


N = 100_000_000


def prime_orders(n):
    root = isqrt(n)
    spf = np.zeros(n + 1, dtype=np.uint32)
    for p in range(2, root + 1):
        if spf[p] == 0:
            segment = spf[p * p :: p]
            unset = segment == 0
            segment[unset] = p

    primes = np.flatnonzero(spf[2:] == 0) + 2
    orders = np.empty(primes.size, dtype=np.uint32)
    for i, value in enumerate(primes):
        p = int(value)
        if p == 2 or p == 5:
            orders[i] = 1
            continue

        x = p - 1
        factors = []
        while x > 1:
            q = int(spf[x]) or x
            factors.append(q)
            while x % q == 0:
                x //= q

        order = p - 1
        for q in factors:
            while order % q == 0 and pow(10, order // q, p) == 1:
                order //= q
        orders[i] = order

    return primes, orders


def recurring_orders(n, primes, p_orders):
    root = isqrt(n)
    split = bisect_right(primes, root)
    orders = np.ones(n + 1, dtype=np.uint32)

    for value, base_order in zip(primes[:split], p_orders[:split]):
        p = int(value)
        if p == 2 or p == 5:
            continue
        power = p
        order = int(base_order)
        while power <= n:
            segment = orders[power::power]
            np.lcm(segment, order, out=segment)
            if power > n // p:
                break
            power *= p
            if pow(10, order, power) != 1:
                order *= p

    large_primes = primes[split:]
    large_orders = p_orders[split:]
    for k in range(1, root + 1):
        if k % 2 == 0 or k % 5 == 0:
            continue
        end = bisect_right(large_primes, n // k)
        indices = large_primes[:end] * k
        orders[indices] = np.lcm(orders[k], large_orders[:end])

    orders[::2] = 0
    orders[::5] = 0
    orders[1] = 0
    return orders


def smooth_numbers(n):
    values = []
    a = 1
    while a <= n:
        b = a
        while b <= n:
            values.append(b)
            b *= 5
        a *= 2
    return values


def solve():
    primes, p_orders = prime_orders(N)
    orders = recurring_orders(N, primes, p_orders)
    smooth = smooth_numbers(N)
    cuts = sorted(N // q for q in smooth)
    prefix = {}
    total = 0
    previous = -1
    for cut in cuts:
        total += int(np.sum(orders[previous + 1 : cut + 1], dtype=np.uint64))
        prefix[cut] = total
        previous = cut
    return sum(prefix[N // q] for q in smooth)


if __name__ == "__main__":
    print(solve())
