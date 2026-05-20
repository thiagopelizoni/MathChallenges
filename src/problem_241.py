# Problem 241: https://projecteuler.net/problem=241
from fractions import Fraction
from functools import cache

from sympy import factorint, nextprime


LIMIT = 10**18


@cache
def smallest_prime_factor(n):
    return min(factorint(n))


def quotient_bound(lim):
    n = 1
    r = Fraction(1, 1)
    p = 2

    while n * p <= lim:
        n *= p
        r *= Fraction(p, p - 1)
        p = nextprime(p)

    return int(2 * r)


def collect(n, rem, used, ans):
    if n > LIMIT or rem < 1:
        return
    if rem == 1:
        ans.add(n)
        return
    if rem.denominator == 1:
        return

    p = smallest_prime_factor(rem.denominator)
    if p in used:
        return

    ppow = 1
    sig = 1
    while n * ppow * p <= LIMIT:
        ppow *= p
        sig += ppow
        f = Fraction(sig, ppow)
        if f > rem:
            break
        collect(n * ppow, rem / f, used + (p,), ans)


def solve():
    ans = set()
    for q in range(3, quotient_bound(LIMIT) + 1, 2):
        collect(1, Fraction(q, 2), (), ans)
    return sum(ans)


if __name__ == "__main__":
    print(solve())
