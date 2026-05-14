# Problem 208: https://projecteuler.net/problem=208
from functools import cache


def walks(n):
    target = n // 5

    @cache
    def dp(step, h, c0, c1, c2, c3):
        counts = [c0, c1, c2, c3]
        c4 = step - sum(counts)
        if c4 > target or any(c > target for c in counts):
            return 0
        if step == n:
            return c0 == c1 == c2 == c3 == c4 == target

        total = 0
        for turn in (-1, 1):
            j = h if turn == -1 else (h + 1) % 5
            nxt = counts[:]
            if j < 4:
                nxt[j] += 1
            total += dp(step + 1, (h + turn) % 5, *nxt)

        return total

    return dp(0, 0, 0, 0, 0, 0)


def solve():
    return walks(70)


if __name__ == "__main__":
    print(solve())
