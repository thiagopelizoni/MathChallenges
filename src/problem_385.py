# Problem 385: https://projecteuler.net/problem=385

from math import gcd, isqrt

from sympy.solvers.diophantine.diophantine import diop_DN


def solve(limit=10**9):
    seen = set()
    pell = {}
    total = 0

    for m in range(-isqrt(468 // 3), isqrt(468 // 3) + 1):
        for n in range(-isqrt(468), isqrt(468) + 1):
            if (m == 0 and n == 0) or gcd(abs(m), abs(n)) != 1:
                continue

            divisor = n * n + 3 * m * m
            if 468 % divisor:
                continue
            k = 468 // divisor
            if k not in pell:
                pell[k] = diop_DN(3, k)

            for initial_s, initial_t in pell[k]:
                s, t = initial_s, initial_t
                while max(abs(s), abs(t)) <= 6 * limit + 10:
                    for signed_s in (s, -s):
                        for signed_t in (t, -t):
                            if signed_s * n % 3:
                                continue

                            a = signed_s * m
                            b = -signed_t * n
                            c = signed_s * n // 3
                            d = signed_t * m
                            if (a + c) % 2 or (b + d) % 2:
                                continue

                            x1, y1 = (a + c) // 2, (b + d) // 2
                            x2, y2 = (c - a) // 2, (d - b) // 2
                            x3, y3 = -c, -d
                            vertices = ((x1, y1), (x2, y2), (x3, y3))
                            inside_bounds = all(
                                abs(coordinate) <= limit
                                for vertex in vertices
                                for coordinate in vertex
                            )
                            if not inside_bounds:
                                continue

                            triangle = tuple(sorted(vertices))
                            if triangle in seen:
                                continue
                            seen.add(triangle)
                            total += divisor * abs(s * t)

                    s, t = 2 * s + 3 * t, s + 2 * t

    return total // 4


if __name__ == "__main__":
    print(solve())
