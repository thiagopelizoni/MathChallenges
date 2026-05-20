# Problem 239: https://projecteuler.net/problem=239
from decimal import Decimal, getcontext
from math import comb, factorial


def solve():
    getcontext().prec = 60
    total = sum((-1) ** j * comb(22, j) * factorial(97 - j) for j in range(23))
    p = Decimal(comb(25, 3) * total) / Decimal(factorial(100))
    return f"{p:.12f}"


if __name__ == "__main__":
    print(solve())
