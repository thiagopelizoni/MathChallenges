# Problem 591: https://projecteuler.net/problem=591

from math import isqrt

from sympy import floor, pi


def min_mod(a, b, m, n):
    a %= m
    b %= m
    reverse = 2 * a > m
    if reverse:
        b = (a * (n - 1) + b) % m
        a = m - a

    value, index = b, 0
    height = (a * (n - 1) + b) // m
    if a and height:
        candidate, level = min_mod(-m, b - m, a, height)
        if candidate < value:
            value = candidate
            index = (m * (level + 1) - b + a - 1) // a

    if reverse:
        index = n - 1 - index
    return value, index


def approximation(d, n):
    scale = 4 * (n + 1) ** 2 * (isqrt(d) + 2)
    while True:
        root = isqrt(d * scale * scale)
        target = int(floor(pi * scale))
        lower = max(-n, -((n * scale - target) // root))
        upper = min(n, (n * scale + target) // root)
        candidates = set()

        if lower <= upper:
            count = upper - lower + 1
            _, index = min_mod(root, lower * root - target, scale, count)
            b = lower + index
            candidates.add((-((b * root - target) // scale), b))

            _, index = min_mod(-root, target - lower * root, scale, count)
            b = lower + index
            candidates.add(((target - b * root) // scale, b))

        for b in (lower - 1, upper + 1):
            if -n <= b <= n:
                a = max(-n, min(n, (target - b * root) // scale))
                candidates.add((a, b))

        bounds = []
        for a, b in candidates:
            error = a * scale + b * root - target
            left = error + min(0, b) - 1
            right = error + max(0, b)
            least = 0 if left <= 0 <= right else min(abs(left), abs(right))
            bounds.append((max(abs(left), abs(right)), least, a, b))

        bounds.sort()
        best = bounds[0]
        if all(best[0] < other[1] for other in bounds[1:]):
            return best[2], best[3]
        scale *= 2


def solve():
    total = 0
    for d in range(2, 100):
        if isqrt(d) ** 2 != d:
            a, _ = approximation(d, 10**13)
            total += abs(a)
    return total


if __name__ == "__main__":
    print(solve())
