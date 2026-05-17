# Problem 226: https://projecteuler.net/problem=226
from math import asin, floor, sqrt


R = 0.25
C = 0.25
TERMS = 60


def blancmange(x):
    y = 0.0
    p = 1.0
    t = x
    for _ in range(TERMS):
        y += min(t, 1.0 - t) / p
        t = (2.0 * t) % 1.0
        p *= 2.0
    return y


def s_int(x):
    k = floor(x)
    r = x - k
    if r <= 0.5:
        return k / 4.0 + r * r / 2.0
    return k / 4.0 + r - r * r / 2.0 - 0.25


def blancmange_int(x):
    total = 0.0
    z = x
    p = 1.0
    for _ in range(TERMS):
        total += s_int(z) / (p * p)
        z *= 2.0
        p *= 2.0
    return total


def lower_circle(x):
    return 0.5 - sqrt(R * R - (x - C) ** 2)


def circle_int(x):
    u = x - C
    return x / 2.0 - 0.5 * (u * sqrt(R * R - u * u) + R * R * asin(u / R))


def solve():
    lo, hi = 0.0, 0.25
    for _ in range(80):
        mid = (lo + hi) / 2.0
        if blancmange(mid) > lower_circle(mid):
            hi = mid
        else:
            lo = mid

    x = (lo + hi) / 2.0
    area = blancmange_int(0.5) - blancmange_int(x) - circle_int(0.5) + circle_int(x)
    return f"{area:.8f}"


if __name__ == "__main__":
    print(solve())
