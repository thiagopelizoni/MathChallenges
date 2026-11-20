# Problem 775: https://projecteuler.net/problem=775

from math import isqrt


def half_perimeter_sum(n):
    k = isqrt(n)
    rest = n - k * k
    first = min(rest, k)
    total = k * (8 * k * k + 3 * k + 1) // 6
    return total + (2 * k + 1) * first + (2 * k + 2) * (rest - first)


def saved_paper(n):
    half_area = 0
    k = 1
    while k**3 <= n:
        for a, b in ((k, k), (k + 1, k), (k + 1, k + 1)):
            face = a * b
            m = min(face, n - k * face + 1)
            if m <= 0:
                break
            half_area += m * (face + k * (a + b)) + half_perimeter_sum(m - 1)
        k += 1
    return 3 * n * (n + 1) - 2 * half_area


def solve():
    return saved_paper(10**16) % 1_000_000_007


if __name__ == "__main__":
    print(solve())
