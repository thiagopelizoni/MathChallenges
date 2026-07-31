# Problem 482: https://projecteuler.net/problem=482

from bisect import bisect_right
from collections import defaultdict
from math import gcd, isqrt


def triangle_sum(limit):
    max_radius = limit // 10
    semiperimeter = limit // 2
    max_hypotenuse = isqrt(
        max_radius * max_radius + semiperimeter * semiperimeter
    )
    legs = defaultdict(list)

    for m in range(2, isqrt(max_hypotenuse) + 1):
        for n in range(1, m):
            if gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            a = m * m - n * n
            b = 2 * m * n
            hypotenuse = m * m + n * n
            if hypotenuse > max_hypotenuse:
                continue

            for radius, tangent in ((a, b), (b, a)):
                scales = min(
                    max_radius // radius,
                    semiperimeter // tangent,
                )
                for scale in range(1, scales + 1):
                    legs[scale * radius].append(scale * tangent)

    total = 0
    for radius, tangents in legs.items():
        tangents.sort()
        radius_squared = radius * radius

        for i, x in enumerate(tangents):
            if 3 * x > semiperimeter:
                break
            ix = isqrt(radius_squared + x * x)
            first = max(i, bisect_right(tangents, radius_squared // x))
            last = bisect_right(
                tangents,
                min(
                    (semiperimeter - x) // 2,
                    radius * (radius + ix) // x,
                ),
            )

            for j in range(first, last):
                y = tangents[j]
                denominator = x * y - radius_squared
                numerator = radius_squared * (x + y)
                if numerator % denominator:
                    continue
                z = numerator // denominator
                if x + y + z > semiperimeter:
                    continue
                total += (
                    2 * (x + y + z)
                    + ix
                    + isqrt(radius_squared + y * y)
                    + isqrt(radius_squared + z * z)
                )

    return total


def solve():
    return triangle_sum(10**7)


if __name__ == "__main__":
    print(solve())
