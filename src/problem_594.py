# Problem 594: https://projecteuler.net/problem=594

from collections import defaultdict
from itertools import combinations_with_replacement, product


def paths(h, b):
    a = len(h)
    edges = defaultdict(list)
    for i in range(a + 1):
        for k in range(a + 1):
            low = 0 if i == 0 or k == 0 else b - h[i - 1][k - 1]
            high = b if i == a or k == a else b - h[i][k]
            for j in range(low, high):
                edges[i, j, k].append((i, j + 1, k))

            if i < a:
                low = 0 if k == 0 else b - h[i][k - 1]
                high = b if k == a else b - h[i][k]
                for j in range(low, high + 1):
                    edges[i, j, k].append((i + 1, j, k))

            if k < a:
                low = 0 if i == 0 else b - h[i - 1][k]
                high = b if i == a else b - h[i][k]
                for j in range(low, high + 1):
                    edges[i, j, k].append((i, j, k + 1))

    dp = {((0, 0, 0),) * b: 1}
    for _ in range(2 * a + b):
        nxt = defaultdict(int)
        for vertices, count in dp.items():
            for step in product(*(edges[v] for v in vertices)):
                if all(u[0] - u[2] <= v[0] - v[2] for u, v in zip(step, step[1:])):
                    nxt[step] += count
        dp = nxt
    return dp[((a, b, a),) * b]


def solve(a=4, b=2):
    rows = [row[::-1] for row in combinations_with_replacement(range(b + 1), a)]

    def visit(h):
        if len(h) == a:
            return paths(h, b)
        total = 0
        for row in rows:
            if not h or all(x <= y for x, y in zip(row, h[-1])):
                total += visit(h + [row])
        return total

    return visit([])


if __name__ == "__main__":
    print(solve())
