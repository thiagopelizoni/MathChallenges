# Problem 647: https://projecteuler.net/problem=647

from math import isqrt


def solve(limit=10**12):
    root = isqrt(limit)
    total = 0
    t = 1
    while (2 * t + 1)**2 <= limit and (t - 2)**2 * (t + 1) <= 2 * limit:
        m = (root - 1) // (2 * t)
        cap = 2 * limit // (t - 2)**2
        m = min(m, (isqrt(1 + 4 * t * cap) - 1) // (2 * t))

        s1 = m * (m + 1) // 2
        s2 = m * (m + 1) * (2 * m + 1) // 6
        total += m + (t + 2)**2 * (t * s2 + s1) // 2
        t += 2
    return total


if __name__ == "__main__":
    print(solve())
