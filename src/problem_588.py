# Problem 588: https://projecteuler.net/problem=588

from functools import cache

from numpy import convolve


P = (1, 1, 1, 1, 1)


def trim(a):
    while a and a[-1] == 0:
        a = a[:-1]
    return a


@cache
def q(n, a):
    if not a:
        return 0
    if n == 0:
        return sum(a)

    if n % 2:
        a = tuple(int(v % 2) for v in convolve(a, P))

    m = n // 2
    return q(m, trim(a[::2])) + q(m, trim(a[1::2]))


def solve():
    return sum(q(10**k, (1,)) for k in range(1, 18 + 1))


if __name__ == "__main__":
    print(solve())
