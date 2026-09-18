# Problem 621: https://projecteuler.net/problem=621

from math import isqrt

from sympy import factorint, kronecker_symbol


def solve(n=17526 * 10**9):
    d = 8 * n + 3
    factors = factorint(d)
    for p, e in factors.items():
        d //= p ** (2 * (e // 2))

    multiplier = 1
    for p, e in factors.items():
        k = e // 2
        if k:
            chi = int(kronecker_symbol(-d, p))
            multiplier *= 1 + (p - chi) * ((p**k - 1) // (p - 1))

    n = (d - 3) // 8
    total = 0
    for z in range((isqrt(8 * n + 1) - 1) // 2 + 1):
        remainder = n - z * (z + 1) // 2
        ways = 1
        for p, e in factorint(4 * remainder + 1).items():
            if p % 4 == 3:
                if e % 2:
                    ways = 0
                    break
            else:
                ways *= e + 1
        total += ways
    return total * multiplier


if __name__ == "__main__":
    print(solve())
