# Problem 458: https://projecteuler.net/problem=458

import numpy as np


N = 10**12
MODULUS = 10**9
STATES = 6


def multiply(a, b):
    return np.matmul(a, b) % MODULUS


def matrix_power(matrix, exponent):
    result = np.identity(STATES, dtype=np.int64)
    while exponent:
        exponent, odd = divmod(exponent, 2)
        if odd:
            result = multiply(result, matrix)
        matrix = multiply(matrix, matrix)
    return result


def solve():
    transition = np.zeros((STATES, STATES), dtype=np.int64)
    for distinct in range(1, STATES + 1):
        transition[:distinct, distinct - 1] = 1
        if distinct < STATES:
            transition[distinct, distinct - 1] = 7 - distinct

    initial = np.zeros(STATES, dtype=np.int64)
    initial[0] = 7
    counts = multiply(matrix_power(transition, N - 1), initial)
    return int(np.sum(counts) % MODULUS)


if __name__ == "__main__":
    print(solve())
