# Problem 318: https://projecteuler.net/problem=318

from math import ceil, log10, sqrt


LIM = 2011
NINES = 2011


def solve():
    total = 0

    for p in range(1, LIM // 2 + 1):
        sp = sqrt(p)

        for q in range(p + 1, LIM - p + 1):
            d = q - p

            if d * d < 2 * (p + q) - 1:
                g = (sqrt(q) - sp) ** 2
                total += ceil(-NINES / log10(g))

    return total


if __name__ == "__main__":
    print(solve())
