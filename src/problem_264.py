# Problem 264: https://projecteuler.net/problem=264

from math import gcd, hypot, isqrt


LIMIT = 100_000


def triangles(limit):
    bound = isqrt(limit * limit + 25) // 3 + 10
    found = {}

    for l in range(1, bound + 1):
        qlim = bound // l
        if qlim == 0:
            break

        low = max(0, 3 * l * l - 40 * l - 100)
        kmin = isqrt(low)
        while kmin * kmin < low:
            kmin += 1

        for k in range(kmin, isqrt(3 * l * l - 1) + 1):
            d = 3 * l * l - k * k
            if d <= 0 or d > 40 * l + 100:
                continue

            for a in range(1, min(qlim, 40 * l // d + 2) + 1):
                num = 40 * a * l - 100 - d * a * a
                if num < 0 or num % d:
                    continue

                b2 = num // d
                b = isqrt(b2)
                if b * b != b2 or a * a + b2 > qlim * qlim:
                    continue

                for bb in ((0,) if b == 0 else (b, -b)):
                    if gcd(a, abs(bb)) != 1:
                        continue

                    sx, sy = l * a, l * bb
                    dx, dy = -k * bb, k * a
                    if (sx + dx) % 2 or (sy + dy) % 2:
                        continue

                    va = (5 - sx, -sy)
                    vb = ((sx + dx) // 2, (sy + dy) // 2)
                    vc = ((sx - dx) // 2, (sy - dy) // 2)
                    if len({va, vb, vc}) < 3:
                        continue

                    per = (
                        hypot(va[0] - vb[0], va[1] - vb[1])
                        + hypot(va[0] - vc[0], va[1] - vc[1])
                        + hypot(vb[0] - vc[0], vb[1] - vc[1])
                    )
                    if per <= limit + 1e-12:
                        found[tuple(sorted((va, vb, vc)))] = per

    return found.values()


def solve():
    return f"{sum(triangles(LIMIT)):.4f}"


if __name__ == "__main__":
    print(solve())
