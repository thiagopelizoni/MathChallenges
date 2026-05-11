# Problem 195: https://projecteuler.net/problem=195
from math import gcd, isqrt


def scaled_limit(n, g):
    return isqrt((4 * n * n * g * g) // 3)


def count(n):
    lim1 = scaled_limit(n, 1)
    lim3 = scaled_limit(n, 3)
    total = 0

    p = 1
    while p * (p + 1) <= lim3:
        for q in range(p + 1, lim3 // p + 1):
            if gcd(p, q) != 1:
                continue

            pq = p * q
            if p % 3 == q % 3:
                total += lim3 // pq
            elif pq <= lim1:
                total += lim1 // pq

        p += 1

    return total


def solve():
    return count(1_053_779)


if __name__ == "__main__":
    print(solve())
