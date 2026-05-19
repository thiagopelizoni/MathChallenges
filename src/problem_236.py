# Problem 236: https://projecteuler.net/problem=236
from math import gcd


A = (5248, 1312, 2624, 5760, 3936)
B = (640, 1888, 3776, 3776, 5664)
TA = sum(A)
TB = sum(B)


def candidates():
    out = set()
    a0, b0 = A[0], B[0]
    for a in range(1, a0 + 1):
        lo = a * b0 // a0 + 1
        for b in range(lo, b0 + 1):
            u = b * a0
            v = a * b0
            g = gcd(u, v)
            out.add((u // g, v // g))
    return out


def parameters(u, v):
    cs = []
    ts = []
    for a, b in zip(A, B):
        num = u * b
        den = v * a
        g = gcd(num, den)
        num //= g
        den //= g
        t = min(a // den, b // num)
        if t == 0:
            return None
        cs.append(v * TB * den - u * TA * num)
        ts.append(t)
    return cs, ts


def feasible(u, v):
    data = parameters(u, v)
    if data is None:
        return False

    cs, ts = data
    smax = ts[1] + ts[2] + ts[4]
    for t0 in range(1, ts[0] + 1):
        c0 = cs[0] * t0
        for t3 in range(1, ts[3] + 1):
            rem = -(c0 + cs[3] * t3)
            if rem % cs[1] == 0 and 3 <= rem // cs[1] <= smax:
                return True
    return False


def solve():
    best = (0, 1)
    for u, v in candidates():
        if u * best[1] > best[0] * v and feasible(u, v):
            best = (u, v)
    return f"{best[0]}/{best[1]}"


if __name__ == "__main__":
    print(solve())
