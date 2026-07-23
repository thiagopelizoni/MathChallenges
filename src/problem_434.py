# Problem 434: https://projecteuler.net/problem=434

from math import comb


MOD = 1_000_000_033


def rigid_counts(n):
    choose = [[comb(i, j) % MOD for j in range(i + 1)] for i in range(n + 1)]
    powers = [pow(2, k, MOD) for k in range(n * n + 1)]
    connected = [[0] * (n + 1) for _ in range(n + 1)]
    connected[1][0] = 1

    for m in range(1, n + 1):
        row = connected[m]
        for k in range(1, n + 1):
            disconnected = 0
            for i in range(1, m + 1):
                last = k - 1 if i == m else k
                subtotal = 0
                for j in range(last + 1):
                    subtotal += (
                        choose[k][j]
                        * connected[i][j]
                        * powers[(m - i) * (k - j)]
                    ) % MOD
                disconnected += choose[m - 1][i - 1] * (subtotal % MOD)
            row[k] = (powers[m * k] - disconnected) % MOD
    return connected


def solve():
    counts = rigid_counts(100)
    return sum(sum(row[1:]) for row in counts[1:]) % MOD


if __name__ == "__main__":
    print(solve())
