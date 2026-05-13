# Problem 203: https://projecteuler.net/problem=203
from math import comb, isqrt

from sympy import primerange


def squarefree(n, squares):
    for q in squares:
        if q > n:
            return True
        if n % q == 0:
            return False
    return True


def solve():
    values = {comb(n, k) for n in range(51) for k in range(n + 1)}
    squares = [p * p for p in primerange(2, isqrt(max(values)) + 1)]
    return sum(n for n in values if squarefree(n, squares))


if __name__ == "__main__":
    print(solve())
