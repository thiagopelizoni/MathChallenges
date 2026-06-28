# Problem 341: https://projecteuler.net/problem=341

from array import array
from bisect import bisect_left


N = 10**6


def golomb_table(limit):
    g = array("I", [0, 1])
    h = array("Q", [0, 1])
    w = array("Q", [0, 1])
    n = 2

    while w[-1] < limit:
        v = 1 + g[n - g[g[n - 1]]]
        g.append(v)
        h.append(h[-1] + v)
        w.append(w[-1] + n * v)
        n += 1

    return h, w


def golomb(n, h, w):
    k = bisect_left(w, n)
    q, r = divmod(n - w[k - 1], k)
    return h[k - 1] + q + (1 if r else 0)


def solve():
    h, w = golomb_table((N - 1) ** 3)
    return sum(golomb(n**3, h, w) for n in range(1, N))


if __name__ == "__main__":
    print(solve())
