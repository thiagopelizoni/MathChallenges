# Problem 547: https://projecteuler.net/problem=547

from math import asinh, fsum, hypot


def primitive(x, y):
    x = abs(x)
    y = abs(y)
    r = hypot(x, y)
    if x == 0 or y == 0:
        return -r**5 / 60
    return (
        (x**4 * y * asinh(y / x) + x * y**4 * asinh(x / y)) / 24
        + r * (3 * x * x * y * y - x**4 - y**4) / 60
    )


def solve():
    n = 40
    table = [[primitive(x, y) for y in range(n + 1)] for x in range(n + 1)]

    def rect_integral(a, b):
        total = 0.0
        for x1, sx1 in ((a[0], -1), (a[2], 1)):
            for x2, sx2 in ((b[0], -1), (b[2], 1)):
                for y1, sy1 in ((a[1], -1), (a[3], 1)):
                    for y2, sy2 in ((b[1], -1), (b[3], 1)):
                        sign = sx1 * sx2 * sy1 * sy2
                        total += sign * table[abs(x1 - x2)][abs(y1 - y2)]
        return total

    square = (0, 0, n, n)
    whole = rect_integral(square, square)
    values = []

    for w in range(1, n - 1):
        for h in range(1, n - 1):
            inner = rect_integral((0, 0, w, h), (0, 0, w, h))
            area = n * n - w * h
            for x in range(1, n - w):
                for y in range(1, n - h):
                    hole = (x, y, x + w, y + h)
                    cross = rect_integral(square, hole)
                    values.append((whole - 2 * cross + inner) / (area * area))

    return f"{fsum(values):.4f}"


if __name__ == "__main__":
    print(solve())
