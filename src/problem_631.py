# Problem 631: https://projecteuler.net/problem=631

from collections import defaultdict


def solve(n=10**18, m=40):
    mod = 1_000_000_007
    limit = min(n, m + 2)
    dp = {(0, 0, 0): 1}
    ans = 1
    total = 1

    for size in range(limit):
        nxt = defaultdict(int)
        for (inv, boundary, suffix), count in dp.items():
            for i in range(boundary, min(size, m - inv) + 1):
                if i < suffix:
                    key = (inv + i, i + 1, suffix + 1)
                else:
                    key = (inv + i, boundary, i)
                nxt[key] = (nxt[key] + count) % mod
        dp = nxt
        total = sum(dp.values()) % mod
        ans += total

    return (ans + (n - limit) * total) % mod


if __name__ == "__main__":
    print(solve())
