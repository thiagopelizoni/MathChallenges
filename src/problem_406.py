# Problem 406: https://projecteuler.net/problem=406

from decimal import Decimal, getcontext
from heapq import heappop, heappush
from math import comb

from sympy import fibonacci


N = 10**12
getcontext().prec = 50


def optimal_cost(n, a, b):
    heap = [(Decimal(0), 0, 0)]
    seen = {(0, 0)}
    total = 0

    while True:
        cost, i, j = heappop(heap)
        total += comb(i + j, i)
        if total >= n:
            return cost

        for x, y, value in ((i + 1, j, cost + a), (i, j + 1, cost + b)):
            if (x, y) not in seen:
                seen.add((x, y))
                heappush(heap, (value, x, y))


def solve():
    total = sum(
        optimal_cost(N, Decimal(k).sqrt(), Decimal(int(fibonacci(k))).sqrt())
        for k in range(1, 31)
    )
    return f"{total:.8f}"


if __name__ == "__main__":
    print(solve())
