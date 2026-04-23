# Problem 109: https://projecteuler.net/problem=109

from bisect import bisect_left
from itertools import combinations_with_replacement


def solve():
    scores = [
        *range(1, 21),
        *(2 * n for n in range(1, 21)),
        *(3 * n for n in range(1, 21)),
        25,
        50,
    ]
    doubles = [*(2 * n for n in range(1, 21)), 50]
    totals = [0, *scores, *(a + b for a, b in combinations_with_replacement(scores, 2))]
    totals.sort()
    return sum(bisect_left(totals, 100 - d) for d in doubles)


if __name__ == "__main__":
    print(solve())
