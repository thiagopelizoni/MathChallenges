# Problem 252: https://projecteuler.net/problem=252
from math import atan2


N = 500


def points(n):
    s = 290797
    t = []
    for _ in range(2 * n):
        s = s * s % 50515093
        t.append(s % 2000 - 1000)
    return list(zip(t[::2], t[1::2]))


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def left_masks(ps):
    n = len(ps)
    left = [[0] * n for _ in range(n)]
    for i, a in enumerate(ps):
        for j, b in enumerate(ps):
            if i == j:
                continue
            dx = b[0] - a[0]
            dy = b[1] - a[1]
            m = 0
            for k, p in enumerate(ps):
                if k != i and k != j and dx * (p[1] - a[1]) - dy * (p[0] - a[0]) > 0:
                    m |= 1 << k
            left[i][j] = m
    return left


def solve():
    ps = points(N)
    left = left_masks(ps)
    ans = 0

    for r in sorted(range(N), key=lambda i: ps[i]):
        cand = [i for i in range(N) if ps[i] > ps[r]]
        cand.sort(key=lambda i: atan2(ps[i][1] - ps[r][1], ps[i][0] - ps[r][0]))
        m = len(cand)
        dp = [[0] * m for _ in range(m)]

        for b in range(m):
            kb = cand[b]
            for a in range(b):
                ka = cand[a]
                area = cross(ps[r], ps[ka], ps[kb])
                if area <= 0 or left[r][ka] & left[ka][kb] & left[kb][r]:
                    continue

                best = area
                for h in range(a):
                    v = dp[h][a]
                    if v and cross(ps[cand[h]], ps[ka], ps[kb]) > 0:
                        best = max(best, v + area)

                dp[a][b] = best
                ans = max(ans, best)

    return f"{ans / 2:.1f}"


if __name__ == "__main__":
    print(solve())
