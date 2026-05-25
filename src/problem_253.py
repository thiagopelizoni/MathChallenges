# Problem 253: https://projecteuler.net/problem=253
from bisect import bisect_left
from collections import defaultdict
from decimal import Decimal, getcontext
from math import factorial


N = 40


def ins(t, x):
    if not x:
        return t
    i = bisect_left(t, x)
    return t[:i] + (x,) + t[i:]


def repl(t, i, x=0):
    return ins(t[:i] + t[i + 1 :], x)


def add(dst, vals, k):
    for m, v in vals:
        dst[m] += v * k


def add_birth(dst, vals, k, s):
    for m, v in vals:
        dst[m if m >= s else s] += v * k


def solve():
    lim = (N + 1) // 2
    dp = defaultdict(lambda: [0] * (lim + 1))

    for i in range(N):
        edges = tuple(x for x in sorted((i, N - 1 - i)) if x)
        dp[(edges, ())][1] += 1

    for _ in range(1, N):
        ndp = defaultdict(lambda: [0] * (lim + 1))

        for (edges, gaps), counts in dp.items():
            vals = [(m, v) for m, v in enumerate(counts) if v]
            s = len(gaps) + 2

            if len(edges) == 2 and edges[0] == edges[1]:
                eruns = ((0, edges[0], 2),)
            else:
                eruns = tuple((i, x, 1) for i, x in enumerate(edges))

            for i, l, c in eruns:
                add(ndp[(repl(edges, i, l - 1), gaps)], vals, c)
                for x in range(2, l + 1):
                    add_birth(ndp[(repl(edges, i, l - x), ins(gaps, x - 1))], vals, c, s)

            i = 0
            while i < len(gaps):
                l = gaps[i]
                j = i + 1
                while j < len(gaps) and gaps[j] == l:
                    j += 1

                c = j - i
                if l == 1:
                    add(ndp[(edges, repl(gaps, i))], vals, c)
                else:
                    add(ndp[(edges, repl(gaps, i, l - 1))], vals, 2 * c)
                    base = repl(gaps, i)
                    for x in range(2, l):
                        add_birth(ndp[(edges, ins(ins(base, x - 1), l - x))], vals, c, s)

                i = j

        dp = ndp

    total = sum(m * c for m, c in enumerate(dp[((), ())]))
    getcontext().prec = 40
    return f"{Decimal(total) / Decimal(factorial(N)):.6f}"


if __name__ == "__main__":
    print(solve())
