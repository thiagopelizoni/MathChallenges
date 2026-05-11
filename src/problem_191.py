# Problem 191: https://projecteuler.net/problem=191
from collections import defaultdict


def prize_strings(days):
    dp = {(0, 0): 1}

    for _ in range(days):
        nxt = defaultdict(int)
        for (late, absent), cnt in dp.items():
            nxt[late, 0] += cnt
            if late == 0:
                nxt[1, 0] += cnt
            if absent < 2:
                nxt[late, absent + 1] += cnt
        dp = nxt

    return sum(dp.values())


def solve():
    return prize_strings(30)


if __name__ == "__main__":
    print(solve())
