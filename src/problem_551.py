# Problem 551: https://projecteuler.net/problem=551

from functools import cache


TARGET = 10**15


def digit_sum(n):
    return sum(map(int, str(n)))


@cache
def cross(length, prefix, start):
    if length == 0:
        if start:
            return 0, start
        return 1, prefix

    base = 10 ** (length - 1)
    steps = 0
    value = start

    while value < 10 * base:
        digit, low = divmod(value, base)
        used, end = cross(length - 1, prefix + digit, low)
        steps += used
        value = digit * base + end

    return steps, value


def solve():
    value = 1
    remaining = TARGET - 1
    length = 18

    while remaining:
        base = 10**length
        high, low = divmod(value, base)
        used, end = cross(length, digit_sum(high), low)

        if used <= remaining:
            value = high * base + end
            remaining -= used
        else:
            length -= 1

    return value


if __name__ == "__main__":
    print(solve())
