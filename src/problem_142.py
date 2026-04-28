# Problem 142: https://projecteuler.net/problem=142

from collections import defaultdict
from math import isqrt


def search(lim):
    sq = [n * n for n in range(1, isqrt(lim) + 1)]
    squares = set(sq)
    by_x = defaultdict(list)

    for i, a in enumerate(sq):
        for b in sq[i + 1:]:
            if (a + b) % 2:
                continue

            x = (a + b) // 2
            if x >= lim:
                break
            by_x[x].append((b - a) // 2)

    best = None
    for x, vals in by_x.items():
        vals.sort(reverse=True)
        for i, y in enumerate(vals):
            for z in vals[i + 1:]:
                if y + z in squares and y - z in squares:
                    s = x + y + z
                    if best is None or s < best:
                        best = s

    return best


def solve():
    lim = 4096
    while True:
        best = search(lim)
        if best is not None and best < lim:
            return best
        lim *= 2


if __name__ == "__main__":
    print(solve())
