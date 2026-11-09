# Problem 727: https://projecteuler.net/problem=727

from itertools import combinations
from math import fsum, gcd, hypot, sqrt


def solve():
    distances = []
    for a, b, c in combinations(range(1, 100 + 1), 3):
        if gcd(a, b, c) != 1:
            continue
        t = sqrt(a * b * c * (a + b + c))
        x = ((a + c) ** 2 + (a + b) ** 2 - (b + c) ** 2) / (2 * (a + b))
        y = 2 * t / (a + b)
        r = a * b * c / (a * b + a * c + b * c + 2 * t)
        u = (a - b) / (a + b)
        v = (a - c - x * u) / y
        distances.append(r * hypot(u, v))
    return f"{fsum(distances) / len(distances):.8f}"


if __name__ == "__main__":
    print(solve())
