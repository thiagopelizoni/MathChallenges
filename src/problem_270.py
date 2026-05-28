# Problem 270: https://projecteuler.net/problem=270

from functools import cache


N = 30
MOD = 10**8


def boundary_masks(n):
    masks = []
    for i in range(4 * n):
        side, offset = divmod(i, n)
        if offset == 0:
            masks.append((1 << side) | (1 << ((side - 1) % 4)))
        else:
            masks.append(1 << side)
    return masks


def solve():
    masks = boundary_masks(N)

    def cut(a, b):
        return masks[a] & masks[b] == 0

    @cache
    def dp(i, j):
        if j <= i + 1:
            return 1

        total = 0
        for k in range(i + 1, j):
            if (k == i + 1 or cut(i, k)) and (k == j - 1 or cut(k, j)):
                total = (total + dp(i, k) * dp(k, j)) % MOD
        return total

    return dp(0, 4 * N - 1)


if __name__ == "__main__":
    print(solve())
