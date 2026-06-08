# Problem 295: https://projecteuler.net/problem=295

from math import gcd, isqrt, sqrt


N = 100_000


def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = egcd(b, a % b)
    return g, y, x - a // b * y


def interval(u, v, ax, ay, r2, x0, y0):
    s = u * u + v * v
    dx = x0 - ax
    dy = y0 - ay
    a = s
    b = 2 * (u * dx + v * dy)
    c = dx * dx + dy * dy - r2
    d = b * b - 4 * a * c
    if d <= 0:
        return None

    h = isqrt(d)
    q = 2 * a
    return -((b + h) // q), (-b + h - 1) // q


def has_point(u, v, m, k, p, q):
    s = u * u + v * v
    ax = (u - m * v) // 2
    ay = (v + m * u) // 2
    bx = (u + m * v) // 2
    by = (v - m * u) // 2
    r2 = s * (1 + m * m) // 4
    x0 = -k * q
    y0 = k * p

    ia = interval(u, v, ax, ay, r2, x0, y0)
    if ia is None:
        return False
    ib = interval(u, v, bx, by, r2, x0, y0)
    if ib is None:
        return False

    return max(ia[0], ib[0]) <= min(ia[1], ib[1])


def min_m(u, v, mmax):
    g, p, q = egcd(u, v)
    if g != 1:
        return None

    s = u * u + v * v
    m = 1
    while m <= mmax:
        kmax = int(s // (2 * (sqrt(1 + m * m) + m)))
        for k in range(1, kmax + 1):
            if has_point(u, v, m, k, p, q):
                break
        else:
            return m
        m += 2

    return None


def add(d, r2, s):
    old = d.get(r2)
    if old is None:
        d[r2] = (s,)
    elif s not in old:
        d[r2] = tuple(sorted(old + (s,)))


def intersects(a, b):
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            return True
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return False


def solve():
    reps = {}
    lim = 4 * N

    for u in range(1, isqrt(lim) + 1, 2):
        u2 = u * u
        for v in range(1, isqrt(lim - u2) + 1, 2):
            if gcd(u, v) == 1:
                s = u2 + v * v
                reps.setdefault(s, []).append((u, v))

    radii = {}
    for s, rs in reps.items():
        mmax = isqrt(4 * N * N // s - 1)
        m0 = None

        for u, v in rs:
            m = min_m(u, v, mmax)
            if m is not None and (m0 is None or m < m0):
                m0 = m

        if m0 is None:
            continue

        for m in range(m0, mmax + 1, 2):
            add(radii, s * (1 + m * m) // 4, s)

    cnt = {}
    for ss in radii.values():
        cnt[ss] = cnt.get(ss, 0) + 1

    total = 0
    items = list(cnt.items())
    for i, (a, ca) in enumerate(items):
        total += ca * (ca + 1) // 2
        for b, cb in items[i + 1 :]:
            if intersects(a, b):
                total += ca * cb

    return total


if __name__ == "__main__":
    print(solve())
