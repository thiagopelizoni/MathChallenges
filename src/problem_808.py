# Problem 808: https://projecteuler.net/problem=808
from math import isqrt

from sympy import isprime, sieve


def solve():
    total = 0
    count = 0
    for p in sieve:
        square = p * p
        reverse = int(str(square)[::-1])
        if reverse == square:
            continue
        root = isqrt(reverse)
        if root * root == reverse and isprime(root):
            total += square
            count += 1
            if count == 50:
                return total


if __name__ == "__main__":
    print(solve())
