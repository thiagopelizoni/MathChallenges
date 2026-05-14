# Problem 209: https://projecteuler.net/problem=209
from math import prod


def step(x):
    a = (x >> 5) & 1
    b = (x >> 4) & 1
    c = (x >> 3) & 1
    return ((x & 31) << 1) | (a ^ (b & c))


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def solve():
    seen = set()
    lengths = []

    for x in range(64):
        if x in seen:
            continue
        n = 0
        while x not in seen:
            seen.add(x)
            n += 1
            x = step(x)
        lengths.append(n)

    return prod(lucas(n) for n in lengths)


if __name__ == "__main__":
    print(solve())
