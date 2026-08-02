# Problem 490: https://projecteuler.net/problem=490

import numpy as np


L = 10**14
MOD = 10**9
INITIAL = (1, 1, 1, 2, 6, 14, 28, 56)
COEFFICIENTS = (2, -1, 2, 1, 1, 0, -1, -1)


def transition():
    matrix = np.zeros((8, 8), dtype=np.int64)
    matrix[0] = np.remainder(COEFFICIENTS, MOD)
    matrix[np.arange(1, 8), np.arange(7)] = 1
    return matrix


def transform(matrix, tensor):
    tensor = np.einsum(
        "ip,pjk->ijk", matrix, tensor, optimize=True
    ) % MOD
    tensor = np.einsum(
        "jq,iqk->ijk", matrix, tensor, optimize=True
    ) % MOD
    return np.einsum(
        "kr,ijr->ijk", matrix, tensor, optimize=True
    ) % MOD


def cube_sum(length):
    if length <= 7:
        return sum(value**3 for value in INITIAL[:length]) % MOD

    matrix = transition()
    state = np.array(INITIAL[::-1], dtype=np.int64)
    tensor = np.einsum("i,j,k->ijk", state, state, state) % MOD
    powers = []
    sums = []
    size = 1
    remaining = length - 7
    while size <= remaining:
        powers.append(matrix)
        sums.append(tensor)
        tensor = (tensor + transform(matrix, tensor)) % MOD
        matrix = matrix @ matrix % MOD
        size *= 2

    product = np.identity(8, dtype=np.int64)
    total = np.zeros((8, 8, 8), dtype=np.int64)
    index = 0
    while remaining:
        if remaining % 2:
            total = (total + transform(product, sums[index])) % MOD
            product = product @ powers[index] % MOD
        remaining //= 2
        index += 1

    prefix = sum(value**3 for value in INITIAL[:7])
    return (prefix + int(total[0, 0, 0])) % MOD


def solve():
    return cube_sum(L)


if __name__ == "__main__":
    print(solve())
