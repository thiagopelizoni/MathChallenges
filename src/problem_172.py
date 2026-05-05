# Problem 172: https://projecteuler.net/problem=172
from itertools import product
from math import factorial, prod


def solve():
    fact = [factorial(n) for n in range(19)]
    total = 0

    for counts in product(range(4), repeat=10):
        if sum(counts) == 18:
            total += (18 - counts[0]) * fact[17] // prod(fact[c] for c in counts)

    return total


if __name__ == "__main__":
    print(solve())
