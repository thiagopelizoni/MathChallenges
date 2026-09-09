# Problem 601: https://projecteuler.net/problem=601

from math import lcm


def solve():
    total = 0
    multiple = 1
    for s in range(1, 31 + 1):
        next_multiple = lcm(multiple, s + 1)
        limit = 4**s - 2
        total += limit // multiple - limit // next_multiple
        multiple = next_multiple
    return total


if __name__ == "__main__":
    print(solve())
