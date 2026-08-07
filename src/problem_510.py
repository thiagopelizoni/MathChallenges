# Problem 510: https://projecteuler.net/problem=510

from math import gcd, isqrt


N = 10**9


def summatory(limit):
    root = isqrt(limit)
    total = 0
    b = 1

    while b * (b + 1) <= root:
        max_a = min(b, root // b - b)
        for a in range(1, max_a + 1):
            if gcd(a, b) != 1:
                continue

            c = a + b
            multiples = limit // (b * b * c * c)
            radii_sum = (a * a + b * b) * c * c + a * a * b * b
            total += radii_sum * multiples * (multiples + 1) // 2

        b += 1

    return total


def solve():
    return summatory(N)


if __name__ == "__main__":
    print(solve())
