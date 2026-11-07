# Problem 719: https://projecteuler.net/problem=719

from math import isqrt


def can_split(n, target):
    if n == target:
        return True
    if n < target:
        return False

    power = 10
    while power <= n:
        left, right = divmod(n, power)
        if right <= target and can_split(left, target - right):
            return True
        power *= 10
    return False


def solve():
    total = 0
    for r in range(2, isqrt(10**12) + 1):
        if r % 9 in (0, 1) and can_split(r * r, r):
            total += r * r
    return total


if __name__ == "__main__":
    print(solve())
