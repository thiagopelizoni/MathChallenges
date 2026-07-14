# Problem 393: https://projecteuler.net/problem=393
from collections import defaultdict
from itertools import permutations


def count_migrations(n):
    empty = (0,) * n
    dp = {(empty, 0): 1}

    for row in range(n):
        for col in range(n):
            nxt = defaultdict(int)
            for (above, left), count in dp.items():
                if above[col] and above[col] == left:
                    continue

                incoming = {above[col], left} - {0}
                missing = tuple({1, 2} - incoming)
                available = []
                if col + 1 < n:
                    available.append("right")
                if row + 1 < n:
                    available.append("down")

                for positions in permutations(available, len(missing)):
                    outgoing = dict(zip(positions, missing))
                    below = outgoing.get("down", 0)
                    right = outgoing.get("right", 0)
                    frontier = above[:col] + (below,) + above[col + 1 :]
                    nxt[(frontier, right)] += count
            dp = nxt

    return dp.get((empty, 0), 0)


def solve():
    return count_migrations(10)


if __name__ == "__main__":
    print(solve())
