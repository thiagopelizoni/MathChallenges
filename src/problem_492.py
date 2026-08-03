# Problem 492: https://projecteuler.net/problem=492

from gmpy2 import lucasv_mod
from sympy import primerange


X = 10**9
Y = 10**7
N = 10**15


def a_mod(p, n):
    character = 1 if pow(13, (p - 1) // 2, p) == 1 else -1
    exponent = pow(2, n - 1, p - character)
    transformed = int(lucasv_mod(11, 1, exponent, p))
    return (transformed - 5) * pow(6, -1, p) % p


def solve():
    return sum(a_mod(p, N) for p in primerange(X, X + Y + 1))


if __name__ == "__main__":
    print(solve())
