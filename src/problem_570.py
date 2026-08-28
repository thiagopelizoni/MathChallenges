# Problem 570: https://projecteuler.net/problem=570
from math import gcd


def solve():
    limit = 10**7
    total = 0

    for n in range(3, limit + 1):
        modulus = 7 * n + 3
        residue = (pow(2, 2 * n - 3, modulus) - pow(3, n - 2, modulus)) % modulus
        total += 6 * gcd(residue, modulus)

    return total


if __name__ == "__main__":
    print(solve())
