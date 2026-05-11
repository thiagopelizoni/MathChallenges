# Problem 192: https://projecteuler.net/problem=192
from math import isqrt


def closer_den(n, p1, q1, p2, q2):
    if p1 * q2 < p2 * q1:
        low = (p1, q1)
        high = (p2, q2)
    else:
        low = (p2, q2)
        high = (p1, q1)

    mid_num = low[0] * high[1] + high[0] * low[1]
    mid_den = 2 * low[1] * high[1]
    return low[1] if n * mid_den * mid_den < mid_num * mid_num else high[1]


def best_denominator(n, bound):
    a0 = isqrt(n)
    m = 0
    d = 1
    a = a0
    p0, p1 = 0, 1
    q0, q1 = 1, 0

    while True:
        p = a * p1 + p0
        q = a * q1 + q0
        if q > bound:
            t = (bound - q0) // q1
            if t <= 0:
                return q1
            return closer_den(n, p1, q1, t * p1 + p0, t * q1 + q0)

        p0, p1 = p1, p
        q0, q1 = q1, q
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d


def solve():
    total = 0
    bound = 10**12

    for n in range(2, 100_001):
        r = isqrt(n)
        if r * r != n:
            total += best_denominator(n, bound)

    return total


if __name__ == "__main__":
    print(solve())
