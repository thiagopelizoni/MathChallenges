# Problem 679: https://projecteuler.net/problem=679

from collections import defaultdict


def solve():
    n = 30
    keywords = ("FREE", "FARE", "AREA", "REEF")
    dp = {("", (0, 0, 0, 0)): 1}

    for _ in range(n):
        nxt = defaultdict(int)
        for (suf, seen), cnt in dp.items():
            for ch in "AEFR":
                w = suf + ch
                if w in keywords:
                    idx = keywords.index(w)
                    if seen[idx]:
                        continue
                    nseen = seen[:idx] + (1,) + seen[idx + 1 :]
                else:
                    nseen = seen
                nxt[(w[-3:], nseen)] += cnt
        dp = nxt

    return sum(cnt for (_, seen), cnt in dp.items() if seen == (1, 1, 1, 1))


if __name__ == "__main__":
    print(solve())
