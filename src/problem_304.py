# Problem 304: https://projecteuler.net/problem=304

from itertools import islice

from sympy import factorint, fibonacci, primerange
from sympy.ntheory.modular import crt


START = 10**14
COUNT = 100_000
MOD = 1_234_567_891_011
SPAN = 5_000_000


def primes_after(n, cnt):
    high = n + SPAN

    while True:
        ps = list(islice(primerange(n + 1, high), cnt))
        if len(ps) == cnt:
            return ps
        high += SPAN


def pisano_period(m):
    a, b = 0, 1

    for k in range(1, 6 * m + 1):
        a, b = b, (a + b) % m
        if a == 0 and b == 1:
            return k


def fib_state(n):
    mods = [p**e for p, e in factorint(MOD).items()]
    periods = [pisano_period(m) for m in mods]
    f0 = [fibonacci(n % pi) % m for m, pi in zip(mods, periods)]
    f1 = [fibonacci((n + 1) % pi) % m for m, pi in zip(mods, periods)]

    return int(crt(mods, f0)[0] % MOD), int(crt(mods, f1)[0] % MOD)


def solve():
    ps = primes_after(START, COUNT)
    it = iter(ps)
    p = next(it)
    f, g = fib_state(START)
    total = 0

    for k in range(START + 1, ps[-1] + 1):
        f, g = g, (f + g) % MOD

        if k == p:
            total = (total + f) % MOD
            p = next(it, None)
            if p is None:
                break

    return total


if __name__ == "__main__":
    print(solve())
