# Problem 481: https://projecteuler.net/problem=481

from bisect import bisect_right
from itertools import combinations

import numpy as np
from sympy import fibonacci


def competition(skills):
    n = len(skills)
    wins = {}
    expected = {}

    for chef in range(n):
        alive = (chef,)
        wins[alive] = np.eye(1, n, chef)
        expected[alive] = np.zeros(1)

    for size in range(2, n + 1):
        for alive in combinations(range(n), size):
            success_wins = np.empty((size, n))
            success_expected = np.empty(size)

            for row, current in enumerate(alive):
                best = -1.0
                choice = None
                for victim in alive[row + 1 :] + alive[:row]:
                    reduced = tuple(chef for chef in alive if chef != victim)
                    next_row = bisect_right(reduced, current) % len(reduced)
                    value = wins[reduced][next_row, current]
                    if value > best + 1e-14:
                        best = value
                        choice = reduced, next_row

                reduced, next_row = choice
                success_wins[row] = wins[reduced][next_row]
                success_expected[row] = expected[reduced][next_row]

            matrix = np.eye(size)
            rhs = np.empty((size, n + 1))
            for row, current in enumerate(alive):
                p = skills[current]
                matrix[row, (row + 1) % size] -= 1 - p
                rhs[row, :n] = p * success_wins[row]
                rhs[row, n] = 1 + p * success_expected[row]

            solution = np.linalg.solve(matrix, rhs)
            wins[alive] = solution[:, :n]
            expected[alive] = solution[:, n]

    alive = tuple(range(n))
    return wins[alive][0], expected[alive][0]


def solve():
    denominator = fibonacci(15)
    skills = [float(fibonacci(k) / denominator) for k in range(1, 15)]
    return f"{competition(skills)[1]:.8f}"


if __name__ == "__main__":
    print(solve())
