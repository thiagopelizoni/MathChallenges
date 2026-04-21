# Problem 91: https://projecteuler.net/problem=91

from math import gcd


def solve():
    n = 50
    total = n * n

    for x in range(n + 1):
        for y in range(n + 1):
            if x == y == 0:
                continue

            g = gcd(x, y)
            dx = y // g
            dy = x // g

            total += min((n - x) // dx if dx else n, y // dy if dy else n)
            total += min(x // dx if dx else n, (n - y) // dy if dy else n)

    return total


if __name__ == "__main__":
    print(solve())
