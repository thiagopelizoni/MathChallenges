# Problem 736: https://projecteuler.net/problem=736

from itertools import count


def search(x, y, p, q):
    if x == y:
        return x if p + q == 0 else None
    if x * 2**q + p > (y + q) * 2**p:
        return None
    if (x + p) * 2**q < y * 2**p + q:
        return None
    if p:
        result = search(x + 1, 2 * y, p - 1, q)
        if result is not None:
            return result
    if q:
        return search(2 * x, y + 1, p, q - 1)
    return None


def solve():
    for steps in count(2, 2):
        for p in range(steps + 1):
            result = search(45, 90, p, steps - p)
            if result is not None:
                return result


if __name__ == "__main__":
    print(solve())
