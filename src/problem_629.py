# Problem 629: https://projecteuler.net/problem=629

import numpy as np


def grundy(n, k):
    g = [0] * (n + 1)
    reach = []
    for _ in range(k + 1):
        reach.append([set() for _ in range(n + 1)])

    for s in range(1, n + 1):
        moves = set()
        for p in range(2, min(k, s) + 1):
            values = reach[p][s]
            for a in range(1, s - p + 2):
                values.update(g[a] ^ x for x in reach[p - 1][s - a])
            moves.update(values)
        while g[s] in moves:
            g[s] += 1
        reach[1][s].add(g[s])

    return g


def solve(n=200):
    mod = 10**9 + 7
    ans = 0

    for k in range(2, n + 1):
        g = grundy(n, k)
        width = 1
        while width <= max(g):
            width *= 2
        states = np.arange(width)
        dp = np.zeros((n + 1, width), dtype=np.int64)
        dp[0, 0] = 1

        for s in range(1, n + 1):
            order = states ^ g[s]
            for total in range(s, n + 1):
                dp[total] = (dp[total] + dp[total - s, order]) % mod

        wins = int(dp[n, 1:].sum() % mod)
        if g[1:] == list(range(n)):
            ans += (n - k + 1) * wins
            break
        ans += wins

    return ans % mod


if __name__ == "__main__":
    print(solve())
