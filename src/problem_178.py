# Problem 178: https://projecteuler.net/problem=178
from collections import defaultdict

FULL = (1 << 10) - 1


def solve():
    dp = {(d, 1 << d): 1 for d in range(1, 10)}
    total = 0

    for _ in range(1, 41):
        total += sum(cnt for (_, mask), cnt in dp.items() if mask == FULL)
        nxt = defaultdict(int)
        for (d, mask), cnt in dp.items():
            for e in (d - 1, d + 1):
                if 0 <= e <= 9:
                    nxt[e, mask | (1 << e)] += cnt
        dp = nxt

    return total


if __name__ == "__main__":
    print(solve())
