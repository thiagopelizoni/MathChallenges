# Problem 604: https://projecteuler.net/problem=604

from math import gcd

from sympy.ntheory.generate import Sieve


def solve():
    n = 10**18
    sieve = Sieve()
    used = 0
    points = 1
    lo, hi = 2, 4
    while True:
        for s, phi in enumerate(sieve.totientrange(lo, hi), lo):
            cost = s * phi // 2
            if used + cost > n:
                remaining = n - used
                extra = 2 * remaining // s
                needed = extra // 2 * s
                if extra % 2:
                    a = s // 2
                    while gcd(a, s) != 1:
                        a -= 1
                    needed += s - a
                assert needed <= remaining
                return points + extra
            used += cost
            points += phi
        lo, hi = hi, 2 * hi


if __name__ == "__main__":
    print(solve())
