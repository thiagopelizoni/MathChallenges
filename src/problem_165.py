# Problem 165: https://projecteuler.net/problem=165
from math import gcd

DEN_BITS = 20
PAIR_BITS = 50


def segments():
    s = 290797
    t = []
    for _ in range(20_000):
        s = s * s % 50_515_093
        t.append(s % 500)

    out = []
    for i in range(0, len(t), 4):
        x1, y1, x2, y2 = t[i:i + 4]
        out.append((
            x1,
            y1,
            x2 - x1,
            y2 - y1,
            min(x1, x2),
            max(x1, x2),
            min(y1, y2),
            max(y1, y2),
        ))
    return out


def point_key(x, y, dx, dy, den, t):
    xn = x * den + dx * t
    yn = y * den + dy * t
    gx = gcd(xn, den)
    gy = gcd(yn, den)
    return (
        ((((xn // gx) << DEN_BITS) | (den // gx)) << PAIR_BITS)
        | ((yn // gy) << DEN_BITS)
        | (den // gy)
    )


def solve():
    segs = segments()
    points = set()

    for i in range(len(segs) - 1):
        x1, y1, dx1, dy1, minx1, maxx1, miny1, maxy1 = segs[i]
        for j in range(i + 1, len(segs)):
            x3, y3, dx2, dy2, minx2, maxx2, miny2, maxy2 = segs[j]
            if maxx1 < minx2 or maxx2 < minx1 or maxy1 < miny2 or maxy2 < miny1:
                continue

            den = dx1 * dy2 - dy1 * dx2
            if den == 0:
                continue

            qx = x3 - x1
            qy = y3 - y1
            t = qx * dy2 - qy * dx2
            u = qx * dy1 - qy * dx1
            if den < 0:
                den = -den
                t = -t
                u = -u

            if 0 < t < den and 0 < u < den:
                points.add(point_key(x1, y1, dx1, dy1, den, t))

    return len(points)


if __name__ == "__main__":
    print(solve())
