# Problem 508: https://projecteuler.net/problem=508

from functools import cache


MOD = 1_000_000_007
L = 10**15
DIRECT_LIMIT = 256


def digit_weight(a, b):
    total = 0
    while a or b:
        digit = (a + b) % 2
        a -= digit
        total += digit
        a, b = (b - a) // 2, -(a + b) // 2
    return total


def rectangle_points(x0, x1, y0, y1):
    if x0 > x1 or y0 > y1:
        return 0
    return (x1 - x0 + 1) * (y1 - y0 + 1)


def diamond_points(u0, u1, v0, v1):
    if u0 > u1 or v0 > v1:
        return 0
    even_u = u1 // 2 - (u0 - 1) // 2
    even_v = v1 // 2 - (v0 - 1) // 2
    odd_u = u1 - u0 + 1 - even_u
    odd_v = v1 - v0 + 1 - even_v
    return even_u * even_v + odd_u * odd_v


def ceil_half(n):
    return -((-n) // 2)


@cache
def rectangle_sum(x0, x1, y0, y1):
    points = rectangle_points(x0, x1, y0, y1)
    if points <= DIRECT_LIMIT:
        return sum(
            digit_weight(a, b)
            for a in range(x0, x1 + 1)
            for b in range(y0, y1 + 1)
        ) % MOD

    zero = (-x1, -x0, y0, y1)
    one = (1 - x1, 1 - x0, y0, y1)
    return (
        diamond_sum(*zero) + diamond_sum(*one) + diamond_points(*one)
    ) % MOD


@cache
def diamond_sum(u0, u1, v0, v1):
    points = diamond_points(u0, u1, v0, v1)
    if points <= DIRECT_LIMIT:
        total = 0
        for u in range(u0, u1 + 1):
            start = v0 + (u - v0) % 2
            for v in range(start, v1 + 1, 2):
                total += digit_weight((u + v) // 2, (u - v) // 2)
        return total % MOD

    zero = (
        ceil_half(-v1),
        (-v0) // 2,
        ceil_half(-u1),
        (-u0) // 2,
    )
    one = (
        ceil_half(1 - v1),
        (1 - v0) // 2,
        ceil_half(1 - u1),
        (1 - u0) // 2,
    )
    return (
        rectangle_sum(*zero) + rectangle_sum(*one) + rectangle_points(*one)
    ) % MOD


def summatory(limit):
    return rectangle_sum(-limit, limit, -limit, limit)


def solve():
    return summatory(L)


if __name__ == "__main__":
    print(solve())
