# Problem 164: https://projecteuler.net/problem=164
from collections import defaultdict


def solve():
    dp = {(0, d): 1 for d in range(1, 10)}

    for _ in range(19):
        nxt = defaultdict(int)
        for (a, b), cnt in dp.items():
            for c in range(10 - a - b):
                nxt[b, c] += cnt
        dp = nxt

    return sum(dp.values())


if __name__ == "__main__":
    print(solve())
