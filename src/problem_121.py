# Problem 121: https://projecteuler.net/problem=121

from math import factorial


def solve():
    turns = 15
    dp = [1] + [0] * turns

    for red in range(1, turns + 1):
        nxt = [0] * (turns + 1)
        for blue, ways in enumerate(dp):
            nxt[blue] += ways * red
            if blue < turns:
                nxt[blue + 1] += ways
        dp = nxt

    return factorial(turns + 1) // sum(dp[turns // 2 + 1 :])


if __name__ == "__main__":
    print(solve())
