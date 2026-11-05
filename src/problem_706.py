# Problem 706: https://projecteuler.net/problem=706

from collections import Counter
from itertools import product
from math import comb


def solve(d=10**5):
    mod = 1_000_000_007
    states = list(product(range(3), repeat=4))
    index = {state: i for i, state in enumerate(states)}
    transitions = []
    for state in states:
        row = []
        for r in range(3):
            s = (state[3] + r) % 3
            counts = list(state[:3])
            counts[s] = (counts[s] + 1) % 3
            row.append(index[tuple(counts) + (s,)])
        transitions.append(row)

    first = Counter(digit % 3 for digit in range(1, 10))
    following = Counter(digit % 3 for digit in range(10))
    dp = [0] * len(states)
    dp[index[(1, 0, 0, 0)]] = 1
    for k in range(d):
        weights = first if k == 0 else following
        nxt = [0] * len(states)
        for i, ways in enumerate(dp):
            if ways:
                for r, weight in weights.items():
                    nxt[transitions[i][r]] += ways * weight
        dp = [ways % mod for ways in nxt]

    return sum(
        ways
        for state, ways in zip(states, dp)
        if sum(comb(c, 2) for c in state[:3]) % 3 == 0
    ) % mod


if __name__ == "__main__":
    print(solve())
