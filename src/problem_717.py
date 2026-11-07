# Problem 717: https://projecteuler.net/problem=717

from sympy import sieve


def g(p):
    r = pow(2, pow(2, p, p - 1), p)
    k = r * pow(2, -1, p) % p
    m = p * p
    b = pow(2, p, m)
    return (k * b - r) % m // p


def solve(n=10**7):
    return sum(g(p) for p in sieve.primerange(3, n))


if __name__ == "__main__":
    print(solve())
