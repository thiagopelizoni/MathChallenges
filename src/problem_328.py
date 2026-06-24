# Problem 328: https://projecteuler.net/problem=328

from bisect import bisect_left
from functools import cache


N = 200_000

GAPS = []
x = 1
while x < 2 * N:
    GAPS.append(x)
    x = 2 * x + 1


@cache
def complete_coeff(length):
    if length <= 0:
        return 0, 0
    if length == 1:
        return 1, 0
    if length == 2:
        return 1, 1

    t = GAPS[bisect_left(GAPS, length) - 1]
    d = min(t, length - (t - 1) // 2)

    ml, cl = complete_coeff(d - 1)
    mr, cr = complete_coeff(length - d - 1)
    cr += mr * (d + 1)

    if ml > mr or (ml == mr and cl >= cr):
        m, c = ml, cl
    else:
        m, c = mr, cr

    return m + 1, c + d


def complete_cost(lo, hi):
    m, c = complete_coeff(hi - lo)
    return m * lo + c


def solve():
    c = [0] * (N + 1)
    for n, v in enumerate((0, 0, 1, 2, 4, 6, 8)):
        c[n] = v

    dist = 3
    deltas = [0]
    p = 4
    while p <= N:
        deltas.append(p)
        p *= 2

    total = sum(c[1:7])
    width = 2

    for n in range(7, N + 1):
        if dist > 4**width:
            width += 1

        best = None
        best_dist = None

        for delta in deltas[:width]:
            k = n - dist - delta
            if not 0 < k < n:
                continue

            right = complete_cost(k + 1, n)
            cost = k + max(c[k - 1], right)

            if best is None or cost < best:
                best = cost
                best_dist = dist + delta

        c[n] = best
        dist = best_dist
        total += best

    return total


if __name__ == "__main__":
    print(solve())
