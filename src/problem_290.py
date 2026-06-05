# Problem 290: https://projecteuler.net/problem=290

from collections import defaultdict


def digit_sum(n):
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total


def count(digits, multiplier):
    dp = {(0, 0): 1}

    for _ in range(digits):
        nxt = defaultdict(int)
        for (carry, diff), ways in dp.items():
            for a in range(10):
                x = multiplier * a + carry
                b = x % 10
                nxt[(x // 10, diff + a - b)] += ways
        dp = nxt

    return sum(ways for (carry, diff), ways in dp.items() if diff == digit_sum(carry))


def solve():
    return count(18, 137)


if __name__ == "__main__":
    print(solve())
