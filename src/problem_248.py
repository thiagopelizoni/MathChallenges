# Problem 248: https://projecteuler.net/problem=248
from functools import cache
from math import factorial

from sympy import divisors, isprime


TARGET = factorial(13)
INDEX = 150000


def prime_powers():
    opts = []
    for p in sorted(d + 1 for d in divisors(TARGET) if isprime(d + 1)):
        cur = []
        n = p
        phi = p - 1
        while TARGET % phi == 0:
            cur.append((n, phi))
            n *= p
            phi *= p
        opts.append((p, tuple(cur)))
    return tuple(opts)


POSSIBLE = prime_powers()


@cache
def build(start, rem):
    if rem == 1:
        return (1,)

    ans = []
    for i in range(start, len(POSSIBLE)):
        p, powers = POSSIBLE[i]
        if rem % (p - 1):
            continue
        for n, phi in powers:
            if rem % phi == 0:
                ans.extend(n * k for k in build(i + 1, rem // phi))
    return tuple(ans)


def solve():
    return sorted(build(0, TARGET))[INDEX - 1]


if __name__ == "__main__":
    print(solve())
