# Problem 794: https://projecteuler.net/problem=794

from decimal import Decimal
from functools import cache
from math import inf, lcm


def solve():
    n = 17
    scale = lcm(*range(1, n + 1))
    partitions = [()]
    for k in range(1, n + 1):
        width = scale // k
        partitions.append(tuple((a, a + width) for a in range(0, scale, width)))

    @cache
    def minimum(points):
        if len(points) == 1:
            return points[0][0]

        bins = partitions[len(points) - 1]
        best = inf
        for i, (lower, _) in enumerate(points):
            rest = points[:i] + points[i + 1:]
            clipped = []
            for (a, b), (left, right) in zip(rest, bins):
                lo, hi = max(a, left), min(b, right)
                if lo >= hi:
                    break
                clipped.append((lo, hi))
            else:
                best = min(best, lower + minimum(tuple(clipped)))
        return best

    total = minimum(partitions[n])
    return f"{Decimal(total) / scale:.12f}"


if __name__ == "__main__":
    print(solve())
