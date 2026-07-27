# Problem 459: https://projecteuler.net/problem=459

from functools import cache
from math import isqrt

import numpy as np


N = 1_000_000
NIM_LIMIT = 1024


def nim_sum(a, b):
    result = 0
    place = 1
    while a or b:
        a, x = divmod(a, 2)
        b, y = divmod(b, 2)
        result += (x + y) % 2 * place
        place *= 2
    return result


def nim_sum_table():
    values = np.arange(NIM_LIMIT, dtype=np.int16)
    table = np.zeros((NIM_LIMIT, NIM_LIMIT), dtype=np.int16)
    place = 1
    while place < NIM_LIMIT:
        digits = values // place % 2
        table += (digits[:, None] + digits[None, :]) % 2 * place
        place *= 2
    return table


@cache
def nim_product(a, b):
    if not a or not b:
        return 0
    if a == 1:
        return b
    if b == 1:
        return a

    field = 2
    while field * field <= max(a, b):
        field *= field
    ah, al = divmod(a, field)
    bh, bl = divmod(b, field)
    ac = nim_product(ah, bh)
    high = nim_sum(nim_sum(ac, nim_product(ah, bl)), nim_product(al, bh))
    low = nim_sum(nim_product(ac, field // 2), nim_product(al, bl))
    return high * field + low


def coin_game(n, lengths, addition):
    prefix = np.zeros(n + 1, dtype=np.int16)
    seen = np.zeros(NIM_LIMIT, dtype=np.bool_)
    count = 0

    for position in range(1, n + 1):
        while count < len(lengths) and lengths[count] <= position:
            count += 1
        previous = prefix[position - 1]
        options = addition[
            previous,
            prefix[position - lengths[:count]],
        ]
        seen[options] = True
        grundy = 0
        while seen[grundy]:
            grundy += 1
        seen[options] = False
        prefix[position] = addition[previous, grundy]

    frequencies = np.zeros(NIM_LIMIT, dtype=np.int64)
    for length in lengths:
        values = addition[prefix[length:], prefix[:-length]]
        frequencies += np.bincount(values, minlength=NIM_LIMIT)
    return int(prefix[n]), frequencies


def solve(n=N):
    addition = nim_sum_table()

    roots = np.arange(1, isqrt(n) + 1, dtype=np.int32)
    squares = roots * roots
    index = (isqrt(8 * n + 1) - 1) // 2
    roots = np.arange(1, index + 1, dtype=np.int32)
    triangles = roots * (roots + 1) // 2

    width, width_frequencies = coin_game(n, squares, addition)
    height, height_frequencies = coin_game(n, triangles, addition)
    board = nim_product(width, height)

    total = 0
    widths = np.flatnonzero(width_frequencies)
    heights = np.flatnonzero(height_frequencies)
    for x in widths:
        for y in heights:
            if nim_product(int(x), int(y)) == board:
                total += int(width_frequencies[x]) * int(height_frequencies[y])
    return total


if __name__ == "__main__":
    print(solve())
