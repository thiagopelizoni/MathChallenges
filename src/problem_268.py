# Problem 268: https://projecteuler.net/problem=268

from math import comb

from sympy import primerange


LIMIT = 10**16
PRIMES = list(primerange(2, 100))


def solve():
    top = LIMIT - 1
    coeff = [0] * (len(PRIMES) + 1)
    for k in range(4, len(coeff)):
        coeff[k] = (-1 if (k - 4) % 2 else 1) * comb(k - 1, 3)

    total = 0

    def search(start, prod, k):
        nonlocal total

        if k >= 4:
            total += coeff[k] * (top // prod)

        for i in range(start, len(PRIMES)):
            p = PRIMES[i]
            if prod * p > top:
                break
            search(i + 1, prod * p, k + 1)

    search(0, 1, 0)
    return total


if __name__ == "__main__":
    print(solve())
