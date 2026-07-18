# Problem 411: https://projecteuler.net/problem=411

from array import array
from bisect import bisect_right
from math import lcm

import numpy as np
from sympy import factorint, n_order


BASE = 32
BLOCKS = 100_000
CHUNK = 1_000_000


def orbit_size(n):
    factors = factorint(n)
    e2 = factors.get(2, 0)
    e3 = factors.get(3, 0)
    preperiod = max(e2, e3)
    m2 = n // 2**e2
    m3 = n // 3**e3
    order2 = 1 if m2 == 1 else int(n_order(2, m2))
    order3 = 1 if m3 == 1 else int(n_order(3, m3))
    return min(2 * n + 1, preperiod + lcm(order2, order3))


def station_keys(n):
    length = orbit_size(n)
    blocks = (length + BASE - 1) // BASE
    local2 = np.array([pow(2, j, n) for j in range(BASE)], dtype=np.int64)
    local3 = np.array([pow(3, j, n) for j in range(BASE)], dtype=np.int64)
    starts2 = np.empty(blocks, dtype=np.int64)
    starts3 = np.empty(blocks, dtype=np.int64)
    value2 = value3 = 1 % n
    step2 = pow(2, BASE, n)
    step3 = pow(3, BASE, n)

    for i in range(blocks):
        starts2[i] = value2
        starts3[i] = value3
        value2 = value2 * step2 % n
        value3 = value3 * step3 % n

    keys = np.empty(length, dtype=np.uint64)
    offset = 0
    for begin in range(0, blocks, BLOCKS):
        end = min(begin + BLOCKS, blocks)
        x = starts2[begin:end, None] * local2 % n
        y = starts3[begin:end, None] * local3 % n
        values = (x * n + y).ravel()
        take = min(len(values), length - offset)
        keys[offset : offset + take] = values[:take]
        offset += take

    keys.sort()
    return keys


def station_path(n):
    keys = station_keys(n)
    tails = array("I")

    for begin in range(0, len(keys), CHUNK):
        y = (keys[begin : begin + CHUNK] % n).astype(np.uint32)
        for value in y:
            pos = bisect_right(tails, value)
            if pos == len(tails):
                tails.append(value)
            else:
                tails[pos] = value

    return len(tails)


def solve():
    return sum(station_path(k**5) for k in range(1, 31))


if __name__ == "__main__":
    print(solve())
