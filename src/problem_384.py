# Problem 384: https://projecteuler.net/problem=384

from sympy import fibonacci


def occurrence_index(t, c):
    if t == 1:
        return 0

    high = 1 << (t.bit_length() - 1)
    remainder = t - high
    if remainder == 0:
        if c <= t // 2:
            return t * t // 4 + occurrence_index(t // 2, c)
        return t * t // 2 + occurrence_index(t, c - t // 2)

    if c > high:
        return high * high + occurrence_index(2 * high - remainder, c - high)
    if c > high - remainder:
        return high * high + occurrence_index(remainder, c + remainder - high)
    if c <= remainder:
        return high * high // 2 + occurrence_index(remainder, c)
    return high * high // 2 + occurrence_index(high - remainder, c)


def solve():
    values = [int(fibonacci(i + 1)) for i in range(46)]
    return sum(
        occurrence_index(values[t], values[t - 1])
        for t in range(2, 46)
    )


if __name__ == "__main__":
    print(solve())
