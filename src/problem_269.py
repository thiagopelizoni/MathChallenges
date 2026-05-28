# Problem 269: https://projecteuler.net/problem=269

from functools import cache
from itertools import combinations


LIMIT = 10**16
ROOTS = range(1, 10)


def factor_poly(roots):
    q = [1]
    for r in roots:
        nxt = [0] * (len(q) + 1)
        for i, c in enumerate(q):
            nxt[i] += c * r
            nxt[i + 1] += c
        q = nxt
    return tuple(q)


def count_divisible(roots, max_degree):
    q = factor_poly(roots)
    s = len(q) - 1
    q0 = q[0]
    if q0 > 9 or s > max_degree:
        return 0

    total = 0
    for t in range(max_degree - s + 1):

        @cache
        def dp(i, state):
            if i == t + 1:
                for k in range(1, s + 1):
                    c = sum(
                        q[j] * state[j - k]
                        for j in range(k, s + 1)
                        if j - k < len(state)
                    )
                    if not ((1 if k == s else 0) <= c <= 9):
                        return 0
                return 1

            known = sum(q[j] * state[j - 1] for j in range(1, min(s, i) + 1))
            ans = 0
            for digit in range(1 if i == 0 else 0, 10):
                v = digit - known
                if v % q0 == 0:
                    ans += dp(i + 1, (v // q0,) + state[: s - 1])
            return ans

        total += dp(0, ())

    return total


def solve():
    total = LIMIT // 10

    for k in range(1, len(ROOTS) + 1):
        sign = 1 if k % 2 else -1
        for roots in combinations(ROOTS, k):
            total += sign * count_divisible(roots, 15)

    return total


if __name__ == "__main__":
    print(solve())
