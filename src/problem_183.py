# Problem 183: https://projecteuler.net/problem=183
from math import e, gcd, log


def best_k(n):
    a = int(n / e)
    b = a + 1
    return b if b * log(n / b) > a * log(n / a) else a


def terminates(n):
    k = best_k(n)
    den = k // gcd(n, k)

    while den % 2 == 0:
        den //= 2
    while den % 5 == 0:
        den //= 5

    return den == 1


def solve():
    return sum(-n if terminates(n) else n for n in range(5, 10_001))


if __name__ == "__main__":
    print(solve())
