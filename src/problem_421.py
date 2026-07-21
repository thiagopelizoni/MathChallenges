# Problem 421: https://projecteuler.net/problem=421

from math import gcd

from sympy import sieve


N = 10**11
M = 10**8


def root_of_unity(p, order):
    exponent = (p - 1) // order
    a = 2
    while True:
        z = pow(a, exponent, p)
        if z != 1 and (
            order != 15 or (pow(z, 3, p) != 1 and pow(z, 5, p) != 1)
        ):
            return z
        a += 1


def solve():
    total = 0
    for p in sieve.primerange(2, M + 1):
        p = int(p)
        order = gcd(15, p - 1)
        q, r = divmod(N, p)

        if order == 1:
            extra = int(p - 1 <= r)
        else:
            z = root_of_unity(p, order)
            u = 1
            extra = 0
            for _ in range(order):
                extra += p - u <= r
                u = u * z % p

        total += p * (order * q + extra)
    return total


if __name__ == "__main__":
    print(solve())
