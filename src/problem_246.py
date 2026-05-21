# Problem 246: https://projecteuler.net/problem=246
from math import isqrt


A2 = 7500**2
B2 = 2500**2 * 5
AB = A2 * B2


def wide_angle(x, y):
    x2 = x * x
    y2 = y * y
    e = B2 * x2 + A2 * y2
    if e <= AB:
        return False

    s = (e - AB) * (x2 + y2)
    t = A2 * A2 * y2 + B2 * B2 * x2
    d = s - t
    if d < 0:
        return True

    return 2 * d * d < (s + t) ** 2 - 4 * (e - AB) * (B2 - A2) ** 2 * x2 * y2


def first_outside(x):
    if B2 * x * x > AB:
        return 0

    y = isqrt((AB - B2 * x * x) // A2)
    while B2 * x * x + A2 * y * y <= AB:
        y += 1
    return y


def last_wide(x, y):
    lo = y
    hi = y + 1
    while wide_angle(x, hi):
        hi *= 2

    while lo < hi:
        mid = (lo + hi + 1) // 2
        if wide_angle(x, mid):
            lo = mid
        else:
            hi = mid - 1
    return lo


def solve():
    total = 0
    x = 0

    while True:
        y0 = first_outside(x)
        if not wide_angle(x, y0):
            break

        y1 = last_wide(x, y0)
        n = 2 * (y1 - y0 + 1)
        if y0 == 0:
            n -= 1
        total += n if x == 0 else 2 * n
        x += 1

    return total


if __name__ == "__main__":
    print(solve())
