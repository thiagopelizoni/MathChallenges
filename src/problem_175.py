# Problem 175: https://projecteuler.net/problem=175
from math import gcd


def shortened_binary_expansion(p, q):
    g = gcd(p, q)
    p //= g
    q //= g

    cf = []
    while q:
        a, p, q = p // q, q, p % q
        cf.append(a)

    if (len(cf) - 1) % 2 == 0:
        cf[-1] -= 1
        cf.append(1)

    return ",".join(map(str, reversed(cf[1:])))


def solve():
    return shortened_binary_expansion(123_456_789, 987_654_321)


if __name__ == "__main__":
    print(solve())
