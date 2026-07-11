# Problem 382: https://projecteuler.net/problem=382

import numpy as np


MOD = 10**9
INITIAL = (1, 2, 4, 6, 11, 20)


def solve(n=10**18):
    if n <= len(INITIAL):
        prefix = sum(INITIAL[:n])
    else:
        matrix = np.zeros((12, 12), dtype=object)
        matrix[0, 2] = 2
        matrix[0, 3] = 1
        matrix[0, 5] = -1
        matrix[0, 9] = 5
        matrix[0, 11] = 1
        matrix[1:6, :5] = np.eye(5, dtype=object)
        matrix[6, 6] = 2
        matrix[7:10, 6:9] = np.eye(3, dtype=object)
        matrix[10, 10] = 1
        matrix[10] += matrix[0]
        matrix[11, 11] = 1

        state = np.array(
            [20, 11, 6, 4, 2, 1, 32, 16, 8, 4, sum(INITIAL), 1],
            dtype=object,
        )
        power = np.eye(12, dtype=object)
        exponent = n - 6
        while exponent:
            if exponent % 2:
                power = np.remainder(power @ matrix, MOD)
            matrix = np.remainder(matrix @ matrix, MOD)
            exponent //= 2

        prefix = int(np.remainder(power @ state, MOD)[10])

    return (pow(2, n, MOD) - 1 - prefix) % MOD


if __name__ == "__main__":
    print(solve())
