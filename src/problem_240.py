# Problem 240: https://projecteuler.net/problem=240
from collections import defaultdict
from math import comb


def count(dice, sides, top, target):
    dp = {(0, 0, 0): 1}

    for face in range(sides, 0, -1):
        ndp = defaultdict(int)
        for (used, got, s), ways in dp.items():
            for c in range(dice - used + 1):
                take = min(c, top - got)
                ns = s + take * face
                if ns <= target:
                    ndp[(used + c, got + take, ns)] += ways * comb(used + c, c)
        dp = ndp

    return dp[(dice, top, target)]


def solve():
    return count(20, 12, 10, 70)


if __name__ == "__main__":
    print(solve())
