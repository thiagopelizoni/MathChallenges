# Problem 182: https://projecteuler.net/problem=182
from math import gcd


def solve():
    p, q = 1009, 3643
    phi = (p - 1) * (q - 1)
    best = None
    total = 0

    for e in range(2, phi):
        if gcd(e, phi) != 1:
            continue
        fixed = (gcd(e - 1, p - 1) + 1) * (gcd(e - 1, q - 1) + 1)
        if best is None or fixed < best:
            best = fixed
            total = e
        elif fixed == best:
            total += e

    return total


if __name__ == "__main__":
    print(solve())
