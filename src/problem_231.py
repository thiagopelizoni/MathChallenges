# Problem 231: https://projecteuler.net/problem=231
from sympy import primerange


N = 20_000_000
K = 15_000_000


def vp_fact(n, p):
    s = 0
    while n:
        n //= p
        s += n
    return s


def solve():
    total = 0
    for p in primerange(1, N + 1):
        e = vp_fact(N, p) - vp_fact(K, p) - vp_fact(N - K, p)
        total += p * e
    return total


if __name__ == "__main__":
    print(solve())
