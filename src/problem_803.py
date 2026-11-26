# Problem 803: https://projecteuler.net/problem=803

from math import gcd
from string import ascii_letters

import numpy as np


A = 25214903917
C = 11
MOD = 2**48
UNIT = 2**16


def matching_states(word):
    digits = [ascii_letters.index(ch) for ch in word]
    radix = gcd(len(ascii_letters), MOD // UNIT)
    low_mod = radix * UNIT
    high_mod = MOD // low_mod
    stride = len(ascii_letters) // radix

    first = (digits[0] % radix) * UNIT
    lows = np.arange(first, first + UNIT, dtype=np.int64)
    states = lows
    for digit in digits[1:]:
        states = (A * states + C) % low_mod
        keep = states // UNIT == digit % radix
        states, lows = states[keep], lows[keep]

    batch = stride * UNIT
    for low in map(int, lows):
        checks = []
        state = low
        for i, digit in enumerate(digits[1:], 1):
            state = (A * state + C) % MOD
            checks.append((pow(A, i, high_mod), state // low_mod, digit // radix))

        for start in range(digits[0] // radix, high_mod, batch):
            high = np.arange(start, min(start + batch, high_mod), stride, dtype=np.int64)
            for mul, add, digit in checks:
                high = high[((mul * high + add) % high_mod) % stride == digit]
            for h in high:
                yield low + low_mod * int(h)


def distance(start, end):
    n = 0
    jump = 1
    mul, add = A, C
    while jump < MOD:
        if (start - end) % (2 * jump):
            start = (mul * start + add) % MOD
            n += jump
        mul, add = mul * mul % MOD, (mul + 1) * add % MOD
        jump *= 2
    return n


def solve():
    (start,) = matching_states("PuzzleOne")
    return min(distance(start, end) for end in matching_states("LuckyText"))


if __name__ == "__main__":
    print(solve())
