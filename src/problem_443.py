# Problem 443: https://projecteuler.net/problem=443

from math import gcd

from sympy import factorint


N = 10**15


def solve():
    n = 4
    value = 13
    while n < N:
        primes = factorint(value - n - 1)
        next_n = min((n // p + 1) * p for p in primes)
        if next_n > N:
            return value + N - n
        value += next_n - n - 1
        value += gcd(next_n, value)
        n = next_n
    return value


if __name__ == "__main__":
    print(solve())
