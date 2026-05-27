# Problem 262: https://projecteuler.net/problem=262

from math import exp, hypot

from scipy.optimize import minimize_scalar, root


L = 1600.0
A = (200.0, 200.0)
B = (1400.0, 1400.0)


def h_grad(x, y):
    p = 5000 - 0.005 * (x * x + y * y + x * y) + 12.5 * (x + y)
    q = 1e-6 * (x * x + y * y) - 0.0015 * (x + y) + 0.7
    e = exp(-abs(q))
    s = 1.0 if q >= 0 else -1.0
    px = 12.5 - 0.01 * x - 0.005 * y
    py = 12.5 - 0.01 * y - 0.005 * x
    qx = 2e-6 * x - 0.0015
    qy = 2e-6 * y - 0.0015

    return p * e, e * (px - p * s * qx), e * (py - p * s * qy)


def h(x, y):
    return h_grad(x, y)[0]


def critical_level():
    res = minimize_scalar(lambda y: -h(0.0, y), bounds=(0.0, L), method="bounded")
    return -res.fun


def segment_clear(origin, point, f):
    ox, oy = origin
    px, py = point

    for i in range(1, 1000):
        t = i / 1000
        x = ox + t * (px - ox)
        y = oy + t * (py - oy)
        if h(x, y) > f + 1e-6:
            return False

    return True


def tangent_points(origin, f):
    ox, oy = origin

    def eq(z):
        x, y = z
        v, hx, hy = h_grad(x, y)
        return v - f, hx * (ox - x) + hy * (oy - y)

    points = []
    for sx in range(0, 1601, 80):
        for sy in range(0, 1601, 80):
            if abs(h(sx, sy) - f) > 800:
                continue
            sol = root(eq, (sx, sy))
            if not sol.success:
                continue
            x, y = map(float, sol.x)
            err = max(abs(v) for v in eq((x, y)))
            if not (-1e-6 <= x <= L + 1e-6 and -1e-6 <= y <= L + 1e-6):
                continue
            if err < 1e-4 and all(hypot(x - u, y - v) > 1e-3 for u, v in points):
                points.append((x, y))

    return [p for p in points if segment_clear(origin, p, f)]


def project(x, y, f):
    for _ in range(4):
        v, hx, hy = h_grad(x, y)
        d = hx * hx + hy * hy
        x -= (v - f) * hx / d
        y -= (v - f) * hy / d

    return x, y


def tangent_unit(x, y, direction):
    _, hx, hy = h_grad(x, y)
    n = hypot(hx, hy)
    return -direction * hy / n, direction * hx / n


def rk4_step(x, y, ds, direction, f):
    def tangent(xx, yy):
        return tangent_unit(xx, yy, direction)

    k1x, k1y = tangent(x, y)
    k2x, k2y = tangent(x + 0.5 * ds * k1x, y + 0.5 * ds * k1y)
    k3x, k3y = tangent(x + 0.5 * ds * k2x, y + 0.5 * ds * k2y)
    k4x, k4y = tangent(x + ds * k3x, y + ds * k3y)

    x += ds * (k1x + 2 * k2x + 2 * k3x + k4x) / 6
    y += ds * (k1y + 2 * k2y + 2 * k3y + k4y) / 6

    return project(x, y, f)


def arc_length(start, target, direction, f):
    x, y = project(*start, f)
    length = 0.0
    step = 0.5

    while length < 10_000:
        d = hypot(x - target[0], y - target[1])
        if d < 1e-8:
            return length

        ds = min(step, max(1e-9, d * 0.5))
        nx, ny = rk4_step(x, y, ds, direction, f)
        if d < 1.0 and hypot(nx - target[0], ny - target[1]) > d:
            step *= 0.5
            continue

        x, y = nx, ny
        length += ds

    return float("inf")


def solve():
    f = critical_level()
    ta = tangent_points(A, f)
    tb = tangent_points(B, f)
    best = float("inf")

    for p in ta:
        for q in tb:
            arc = min(arc_length(p, q, 1.0, f), arc_length(p, q, -1.0, f))
            best = min(best, hypot(p[0] - A[0], p[1] - A[1]) + arc + hypot(q[0] - B[0], q[1] - B[1]))

    return f"{best:.3f}"


if __name__ == "__main__":
    print(solve())
