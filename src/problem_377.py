# Problem 377: https://projecteuler.net/problem=377

import numpy as np


MOD = 10**9
ORDER = 9


def solve():
    matrix = np.zeros((2 * ORDER, 2 * ORDER), dtype=object)
    matrix[0, :ORDER] = 10
    matrix[0, ORDER:] = np.arange(1, ORDER + 1, dtype=object)
    matrix[1:ORDER, : ORDER - 1] = np.eye(ORDER - 1, dtype=object)
    matrix[ORDER, ORDER:] = 1
    matrix[ORDER + 1 :, ORDER : -1] = np.eye(ORDER - 1, dtype=object)

    power = matrix
    total = 0
    for _ in range(17):
        square = np.remainder(power @ power, MOD)
        fourth = np.remainder(square @ square, MOD)
        eighth = np.remainder(fourth @ fourth, MOD)
        power = np.remainder(np.remainder(eighth @ fourth, MOD) @ power, MOD)
        total = (total + power[0, ORDER]) % MOD

    return int(total)


if __name__ == "__main__":
    print(solve())
