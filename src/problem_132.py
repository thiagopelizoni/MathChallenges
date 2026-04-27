# Problem 132: https://projecteuler.net/problem=132

from sympy import primerange


def solve():
    total = 0
    found = 0

    for p in primerange(2, 1_000_000):
        if p not in (2, 3, 5) and pow(10, 10**9, p) == 1:
            total += p
            found += 1
            if found == 40:
                return total


if __name__ == "__main__":
    print(solve())
