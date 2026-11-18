# Problem 765: https://projecteuler.net/problem=765

from fractions import Fraction
from math import comb


def solve():
    rounds = 1000
    remaining = 2**rounds // 10**12
    weight = 0
    for losses in range(rounds + 1):
        count = min(remaining, comb(rounds, losses))
        weight += count * 3**(rounds - losses) * 2**losses
        remaining -= count
        if remaining == 0:
            break

    probability = Fraction(weight, 5**rounds)
    return f"{probability:.10f}"


if __name__ == "__main__":
    print(solve())
