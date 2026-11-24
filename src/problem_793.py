# Problem 793: https://projecteuler.net/problem=793
from bisect import bisect_left
from math import comb


def solve(n=1_000_003):
    values = [290797]
    for _ in range(1, n):
        values.append(values[-1] ** 2 % 50515093)
    values.sort()

    def count_pairs(limit):
        j = n - 1
        total = 0
        for i, x in enumerate(values):
            while j > i and x * values[j] > limit:
                j -= 1
            if j <= i:
                break
            total += j - i
        return total

    rank = comb(n, 2) // 2 + 1
    bounds = range(values[0] * values[1], values[-2] * values[-1] + 1)
    return bounds[bisect_left(bounds, rank, key=count_pairs)]


if __name__ == "__main__":
    print(solve())
