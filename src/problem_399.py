# Problem 399: https://projecteuler.net/problem=399

from math import floor, log10, sqrt

from sympy import factorint, primerange


TARGET = 100_000_000
LIMIT = TARGET * 4 // 3


def fib_mod_pair(n, mod):
    if n == 0:
        return 0, 1

    a, b = fib_mod_pair(n // 2, mod)
    c = a * (2 * b - a) % mod
    d = (a * a + b * b) % mod
    if n % 2:
        return d, (c + d) % mod
    return c, d


def rank(p):
    if p == 2:
        return 3
    if p == 5:
        return 5

    n = p - 1 if p % 5 in (1, 4) else p + 1
    for q in factorint(n):
        while n % q == 0 and fib_mod_pair(n // q, p)[0] == 0:
            n //= q
    return n


def prime_bound(limit):
    a, b = 1, 1
    z = 2
    best = 2

    while True:
        a, b = b, a + b
        z += 1
        best = max(best, min(b, limit // z))
        if b >= limit // z:
            return best


def squarefree_index():
    bad = bytearray(LIMIT + 1)
    for p in primerange(2, prime_bound(LIMIT) + 1):
        step = p * rank(p)
        if step <= LIMIT:
            bad[step::step] = b"\1" * (LIMIT // step)

    remaining = TARGET
    block = 1_000_000
    for start in range(1, LIMIT + 1, block):
        chunk = bad[start : min(start + block, LIMIT + 1)]
        good = chunk.count(0)
        if remaining > good:
            remaining -= good
            continue

        for offset, value in enumerate(chunk):
            if value == 0:
                remaining -= 1
                if remaining == 0:
                    return start + offset


def solve():
    n = squarefree_index()
    last = fib_mod_pair(n, 10**16)[0]

    phi = (1 + sqrt(5)) / 2
    x = n * log10(phi) - log10(sqrt(5))
    exponent = floor(x)
    mantissa = 10 ** (x - exponent)
    return f"{last:016d},{mantissa:.1f}e{exponent}"


if __name__ == "__main__":
    print(solve())
