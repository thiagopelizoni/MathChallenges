# Problem 792: https://projecteuler.net/problem=792

from gmpy2 import mpq, remove
from sympy.ntheory import multiplicity_in_factorial


def u(n):
    m = n + 1
    twos = m - multiplicity_in_factorial(2, m)
    term = mpq(2**twos)
    tail = term
    k = m
    while True:
        v = remove(tail.numerator, 2)[1]
        if v <= k - m:
            return m + v
        term *= mpq(-4 * (2 * k + 1), k + 1)
        tail += term
        k += 1


def solve():
    return sum(u(n**3) for n in range(1, 10**4 + 1))


if __name__ == "__main__":
    print(solve())
