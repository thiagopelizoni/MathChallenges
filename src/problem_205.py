# Problem 205: https://projecteuler.net/problem=205
from collections import Counter


def rolls(dice, sides):
    counts = Counter({0: 1})

    for _ in range(dice):
        nxt = Counter()
        for total, n in counts.items():
            for face in range(1, sides + 1):
                nxt[total + face] += n
        counts = nxt

    return counts


def solve():
    peter = rolls(9, 4)
    colin = rolls(6, 6)
    wins = sum(
        pn * cn
        for ps, pn in peter.items()
        for cs, cn in colin.items()
        if ps > cs
    )
    return f"{wins / (4**9 * 6**6):.7f}"


if __name__ == "__main__":
    print(solve())
