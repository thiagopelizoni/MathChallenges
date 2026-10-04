# Problem 656: https://projecteuler.net/problem=656

from itertools import cycle
from math import isqrt

from sympy import continued_fraction_periodic


def palindrome_sum(beta, count):
    _, period = continued_fraction_periodic(0, 1, beta)
    previous, current = 0, 1
    total = 0

    for index, a in enumerate(cycle(period), 1):
        a = int(a)
        if index % 2:
            take = min(a, count)
            total += take * previous + current * take * (take + 1) // 2
            count -= take
            if count == 0:
                return total
        previous, current = current, previous + a * current


def solve():
    total = 0
    for beta in range(2, 1001):
        if isqrt(beta) ** 2 != beta:
            total += palindrome_sum(beta, 100)
    return total % 10**15


if __name__ == "__main__":
    print(solve())
