# Problem 526: https://projecteuler.net/problem=526

from sympy import factorint

START = 9_997_194_587_108_081


def solve():
    total = 0
    for n in range(START, START + 9):
        total += max(factorint(n))
    return total


if __name__ == "__main__":
    print(solve())
