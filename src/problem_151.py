# Problem 151: https://projecteuler.net/problem=151

from functools import cache


@cache
def expected(state):
    sheets = sum(state)
    remaining = 8 * state[0] + 4 * state[1] + 2 * state[2] + state[3]
    if remaining == 0:
        return 0.0

    total = 1.0 if sheets == 1 and remaining > 1 else 0.0
    for i, count in enumerate(state):
        if count == 0:
            continue

        nxt = list(state)
        nxt[i] -= 1
        for j in range(i + 1, 4):
            nxt[j] += 1
        total += count / sheets * expected(tuple(nxt))

    return total


def solve():
    return f"{expected((1, 1, 1, 1)):.6f}"


if __name__ == "__main__":
    print(solve())
