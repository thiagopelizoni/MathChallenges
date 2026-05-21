# Problem 247: https://projecteuler.net/problem=247
from heapq import heappop, heappush
from itertools import count
from math import comb, sqrt


TARGET = 3


def size(x, y):
    return (sqrt((x - y) * (x - y) + 4) - x - y) / 2


def solve():
    seq = count()
    s = size(1.0, 0.0)
    heap = [(-s, next(seq), 1.0, 0.0, 0, 0)]
    found = 0
    n = 0
    need = comb(2 * TARGET, TARGET)

    while found < need:
        neg, _, x, y, left, below = heappop(heap)
        s = -neg
        n += 1

        if left == below == TARGET:
            found += 1

        heappush(heap, (-size(x + s, y), next(seq), x + s, y, left + 1, below))
        heappush(heap, (-size(x, y + s), next(seq), x, y + s, left, below + 1))

    return n


if __name__ == "__main__":
    print(solve())
