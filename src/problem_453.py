# Problem 453: https://projecteuler.net/problem=453

from functools import cache
from math import comb, isqrt


MOD = 135_707_531


def power_sum(n, k):
    if n <= 0:
        return 0
    if k == 0:
        return n
    if k == 1:
        return n * (n + 1) // 2
    if k == 2:
        return n * (n + 1) * (2 * n + 1) // 6
    if k == 3:
        return n * n * (n + 1) * (n + 1) // 4
    return (
        n
        * (n + 1)
        * (2 * n + 1)
        * (3 * n * n + 3 * n - 1)
        // 30
    )


def quadrilaterals(m, n):
    points = (m + 1) * (n + 1)

    @cache
    def coprime_sum(u, v, a, b):
        if u <= 0 or v <= 0:
            return 0

        root = isqrt(u)
        upper = min(v, u // root)
        result = power_sum(u, a) * power_sum(v, b)

        for k in range(2, upper + 1):
            result -= (
                coprime_sum(u // k, v // k, a, b)
                * k ** (a + b)
            )

        for k in range(1, root):
            x = v // (u // (k + 1) + 1)
            y = v // (u // k)
            if x == y:
                result -= coprime_sum(k, x, a, b) * (
                    power_sum(u // k, a + b)
                    - power_sum(u // (k + 1), a + b)
                )
                continue

            low = max(u // (k + 1), v // (x + 1))
            high = min(u // k, v // x)
            if high > low:
                result -= coprime_sum(k, x, a, b) * (
                    power_sum(high, a + b)
                    - power_sum(low, a + b)
                )

            if y:
                low = max(u // (k + 1), v // (y + 1))
                high = min(u // k, v // y)
                if high > low:
                    result -= coprime_sum(k, y, a, b) * (
                        power_sum(high, a + b)
                        - power_sum(low, a + b)
                    )
        return result

    def gcd_sum(a, b, c):
        if c == 0:
            return power_sum(m, a) * power_sum(n, b)

        root = isqrt(m)
        upper = min(n, m // root)
        result = 0
        for k in range(1, upper + 1):
            result += (
                coprime_sum(m // k, n // k, a, b)
                * k ** (a + b + c)
            )

        for k in range(1, root):
            x = n // (m // (k + 1) + 1)
            y = n // (m // k)
            if x == y:
                result += coprime_sum(k, x, a, b) * (
                    power_sum(m // k, a + b + c)
                    - power_sum(m // (k + 1), a + b + c)
                )
                continue

            low = max(m // (k + 1), n // (x + 1))
            high = min(m // k, n // x)
            if high > low:
                result += coprime_sum(k, x, a, b) * (
                    power_sum(high, a + b + c)
                    - power_sum(low, a + b + c)
                )

            if y:
                low = max(m // (k + 1), n // (y + 1))
                high = min(m // k, n // y)
                if high > low:
                    result += coprime_sum(k, y, a, b) * (
                        power_sum(high, a + b + c)
                        - power_sum(low, a + b + c)
                    )
        return result

    def moment(a, b, c):
        result = gcd_sum(a, b, c)
        if a == 0:
            result += power_sum(n, b + c)
        if b == 0:
            result += power_sum(m, a + c)
        if a + b + c == 0:
            result += 1
        return result

    needed = (
        (0, 0, 1), (0, 1, 1), (1, 0, 1), (1, 1, 1),
        (0, 0, 2), (0, 1, 2), (1, 0, 2), (1, 1, 2),
        (0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 0),
        (3, 3, 0), (3, 2, 0), (2, 3, 0), (2, 2, 0),
        (3, 1, 0), (2, 1, 0), (3, 0, 0), (2, 0, 0),
        (1, 3, 0), (1, 2, 0), (0, 3, 0), (0, 2, 0),
    )
    values = {key: moment(*key) for key in needed}

    s = (
        (values[0, 1, 2] - 11 * values[2, 3, 0]
         - values[2, 1, 0] - values[0, 3, 0]) * (m + 1)
        + (values[1, 0, 2] - 11 * values[3, 2, 0]
           - values[3, 0, 0] - values[1, 2, 0]) * (n + 1)
        - (values[1, 1, 2] - 11 * values[3, 3, 0]
           - values[3, 1, 0] - values[1, 3, 0])
        - (values[0, 0, 2] - 11 * values[2, 2, 0]
           - values[2, 0, 0] - values[0, 2, 0])
        * (m + 1) * (n + 1)
    )

    collinear3 = (
        2 * (
            (values[0, 1, 0] - values[0, 1, 1]) * (m + 1)
            + (values[1, 0, 0] - values[1, 0, 1]) * (n + 1)
            - (values[0, 0, 0] - values[0, 0, 1])
            * (m + 1) * (n + 1)
            - values[1, 1, 0] + values[1, 1, 1]
        )
        + values[0, 2, 0]
        - (n + 2) * values[0, 1, 0]
        + (n + 1) * values[0, 0, 0]
        + values[2, 0, 0]
        - (m + 2) * values[1, 0, 0]
        + (m + 1) * values[0, 0, 0]
    )

    twice_collinear4 = (
        (4 * values[0, 0, 0] - 6 * values[0, 0, 1]
         + 2 * values[0, 0, 2]) * (m + 1) * (n + 1)
        + 4 * values[1, 1, 0] - 6 * values[1, 1, 1]
        + 2 * values[1, 1, 2]
        - (4 * values[1, 0, 0] - 6 * values[1, 0, 1]
           + 2 * values[1, 0, 2]) * (n + 1)
        - (4 * values[0, 1, 0] - 6 * values[0, 1, 1]
           + 2 * values[0, 1, 2]) * (m + 1)
        + values[0, 3, 0] - (n + 4) * values[0, 2, 0]
        + (3 * n + 5) * values[0, 1, 0]
        - 2 * (n + 1) * values[0, 0, 0]
        + values[3, 0, 0] - (m + 4) * values[2, 0, 0]
        + (3 * m + 5) * values[1, 0, 0]
        - 2 * (m + 1) * values[0, 0, 0]
    )

    return (
        comb(points, 4)
        - comb(points, 3)
        + s // 3
        + (7 - 2 * points) * collinear3
        + 7 * twice_collinear4 // 2
    )


def solve():
    return quadrilaterals(12_345, 6_789) % MOD


if __name__ == "__main__":
    print(solve())
