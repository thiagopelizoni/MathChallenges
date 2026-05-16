# Problem 219: https://projecteuler.net/problem=219
from collections import defaultdict


def total_cost(n):
    cnt = defaultdict(int)
    cnt[0] = 1
    leaves = 1
    cost = 0

    while leaves < n:
        while cnt[cost] == 0:
            cost += 1

        k = min(cnt[cost], n - leaves)
        cnt[cost] -= k
        cnt[cost + 1] += k
        cnt[cost + 4] += k
        leaves += k

    return sum(c * k for c, k in cnt.items())


def solve():
    return total_cost(1_000_000_000)


if __name__ == "__main__":
    print(solve())
