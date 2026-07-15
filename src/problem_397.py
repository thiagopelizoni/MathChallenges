# Problem 397: https://projecteuler.net/problem=397

from math import gcd


K = 10**6
X = 10**9


def sum_floor_half(a, n):
    total = a * n * (n + 1) // 2
    odd = a % 2 * ((n + 1) // 2)
    return (total - odd) // 2


def sum_ceil_half(a, n):
    total = a * n * (n + 1) // 2
    odd = a % 2 * ((n + 1) // 2)
    return (total + odd) // 2


def max_scale(limit, coefficient, odd_extra):
    n = limit // coefficient
    if n % 2 and n * coefficient + odd_extra > limit:
        n -= 1
    return n


def endpoint_sum(k, d, e):
    n = K // k
    x = k - d
    y = e - k
    h = x - 2 * max(y, 0)
    if h < 0:
        n = min(n, (2 * X - 1) // -h)
    return n * X + sum_ceil_half(h, n)


def middle_sum(k, d, e):
    n = K // k
    a = k + d
    c = k + e
    span = a + c
    n = min(n, 2 * X // span)
    if n == 0:
        return 0

    small, large = sorted((a, c))
    first = min(
        max_scale(2 * X + 2, 2 * large + small, small % 2),
        max_scale(4 * X + 4, 3 * span, a % 2 + c % 2),
    )
    second = max_scale(2 * X + 2, 2 * small + large, large % 2)

    p = min(n, first)
    total = sum_ceil_half(a, p) + sum_ceil_half(c, p) - p

    q = min(n, second)
    if q > p:
        total += (q - p) * X
        total -= sum_floor_half(large, q) - sum_floor_half(large, p)

    r = max(p, q)
    if n > r:
        total += (n - r) * (2 * X + 1)
        total -= span * (n * (n + 1) // 2 - r * (r + 1) // 2)

    return total


def overlap_sum(k, d, e, numerator, denominator):
    g = gcd(numerator, denominator)
    step = denominator // g
    z = numerator // g
    x = step * (k - d)
    y = step * (e - k)
    p = z - y
    if p <= 0:
        return 0

    h = k - d - 2 * max(e - k, 0)
    coefficient = p - step * h
    n = K // (step * k)
    if coefficient > 0:
        n = min(n, 2 * X // coefficient)
    return n // 2 if (p - x) % 2 else n


def solve():
    endpoint = middle = both_ends = adjacent = 0

    for u in range(1, K + 1, 2):
        for v in range(1, K // u + 1):
            if gcd(u, v) != 1:
                continue

            k = u * v
            for d, e in ((u * u, 2 * v * v), (2 * v * v, u * u)):
                endpoint += endpoint_sum(k, d, e)
                middle += middle_sum(k, d, e)

                denominator = 2 * k - e
                if denominator > 0:
                    both_ends += overlap_sum(k, d, e, k * e, denominator)

                denominator = d - 2 * k
                if denominator > 0:
                    adjacent += overlap_sum(k, d, e, k * d, denominator)

    return 2 * endpoint + middle - both_ends - 2 * adjacent


if __name__ == "__main__":
    print(solve())
