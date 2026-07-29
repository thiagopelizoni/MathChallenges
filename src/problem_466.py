# Problem 466: https://projecteuler.net/problem=466

from math import lcm


ROWS = 64
COLUMNS = 10**16


def count_products(m, n):
    coefficients = {}
    total = 0
    limit = m * n

    for a in range(m, 0, -1):
        updates = {a: 1}
        for q, coefficient in coefficients.items():
            multiple = lcm(q, a)
            if multiple <= limit:
                updates[multiple] = updates.get(multiple, 0) - coefficient

        for q, coefficient in updates.items():
            coefficients[q] = coefficients.get(q, 0) + coefficient
            if coefficients[q] == 0:
                del coefficients[q]

        lower = (a - 1) * n
        upper = a * n
        total += sum(
            coefficient * (upper // q - lower // q)
            for q, coefficient in coefficients.items()
        )

    return total


def solve():
    return count_products(ROWS, COLUMNS)


if __name__ == "__main__":
    print(solve())
