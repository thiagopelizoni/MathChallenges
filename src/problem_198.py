# Problem 198: https://projecteuler.net/problem=198
from math import isqrt


def count(limit, width):
    bound = limit // 2
    root = isqrt(bound)
    stop = root + (root * (root + 1) <= bound)
    stack = list(range(width, stop))
    a = root
    total = 0

    while stack:
        b = stack[-1]
        if a * b > bound:
            a = stack.pop()
        else:
            total += 1
            stack.append(a + b)

    return total + bound - width // 2


def solve():
    return count(100_000_000, 100)


if __name__ == "__main__":
    print(solve())
