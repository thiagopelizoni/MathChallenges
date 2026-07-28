# Problem 462: https://projecteuler.net/problem=462

from decimal import Decimal
from math import factorial, prod


LIMIT = 10**18


def count_permutations(limit):
    rows = []
    power_of_three = 1
    while power_of_three <= limit:
        length = 0
        value = power_of_three
        while value <= limit:
            length += 1
            value *= 2
        rows.append(length)
        power_of_three *= 3

    columns = [
        sum(length > column for length in rows)
        for column in range(rows[0])
    ]
    hooks = [
        length - column + columns[column] - row - 1
        for row, length in enumerate(rows)
        for column in range(length)
    ]
    return factorial(sum(rows)) // prod(hooks)


def solve():
    result = format(Decimal(count_permutations(LIMIT)), ".10E").lower()
    return result.replace("e+", "e")


if __name__ == "__main__":
    print(solve())
