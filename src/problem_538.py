# Problem 538: https://projecteuler.net/problem=538

from bisect import bisect_left, insort


def solve():
    xs = []
    cnt = {}
    best = (-1, 0)
    total = 0
    for n in range(1, 3_000_001):
        v = 2 ** (3 * n).bit_count() + 3 ** (2 * n).bit_count() + (n + 1).bit_count()
        if v not in cnt:
            insort(xs, v)
            cnt[v] = 1
        else:
            cnt[v] += 1
        p = bisect_left(xs, v)
        left = [v] * min(cnt[v] - 1, 3)
        i = p - 1
        while len(left) < 3 and i >= 0:
            w = xs[i]
            take = min(cnt[w], 3 - len(left))
            left.extend([w] * take)
            i -= 1
        left.reverse()
        right = []
        i = p + 1
        while len(right) < 3 and i < len(xs):
            w = xs[i]
            take = min(cnt[w], 3 - len(right))
            right.extend([w] * take)
            i += 1
        around = left + [v] + right
        for j in range(len(around) - 3):
            a, b, c, d = around[j : j + 4]
            if d >= a + b + c:
                continue
            per = a + b + c + d
            prod = (per - 2 * a) * (per - 2 * b) * (per - 2 * c) * (per - 2 * d)
            cand = (prod, per)
            if cand > best:
                best = cand
        if n >= 4:
            total += best[1]
    return total


if __name__ == "__main__":
    print(solve())
