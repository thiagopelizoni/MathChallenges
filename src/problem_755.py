# Problem 755: https://projecteuler.net/problem=755

from bisect import bisect_right
from functools import cache
from itertools import accumulate


def solve(n=10**13):
    fib = [1, 2]
    while fib[-1] <= n:
        fib.append(fib[-1] + fib[-2])
    sums = [0, *accumulate(fib)]

    @cache
    def count(n):
        if n < 0:
            return 0
        if n == 0:
            return 1
        i = bisect_right(fib, n) - 1
        return 2**i - count(sums[i] - n - 1) + count(n - fib[i])

    return count(n)


if __name__ == "__main__":
    print(solve())
