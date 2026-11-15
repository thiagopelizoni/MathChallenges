# Problem 751: https://projecteuler.net/problem=751

from fractions import Fraction
from math import ceil, floor


def solve():
    places = 24
    scale = 10**places
    states = [(Fraction(2), Fraction(3), 1, 0, 2, "2")]

    while True:
        lower = min(lo for lo, hi, p, q, a, digits in states)
        upper = max(hi for lo, hi, p, q, a, digits in states)
        rounded = floor(lower * scale + Fraction(1, 2))
        if rounded == floor(upper * scale + Fraction(1, 2)):
            whole, decimal = divmod(rounded, scale)
            return f"{whole}.{decimal:0{places}d}"

        following = []
        for lo, hi, p, q, a, digits in states:
            p, q = a * p, a * (q - a + 1)
            for a in range(floor(p * lo + q), ceil(p * hi + q)):
                prefix = digits + str(a)
                denominator = 10 ** (len(prefix) - 1)
                left = max(lo, Fraction(a - q, p), Fraction(int(prefix), denominator))
                right = min(hi, Fraction(a + 1 - q, p), Fraction(int(prefix) + 1, denominator))
                if left < right:
                    following.append((left, right, p, q, a, prefix))
        states = following


if __name__ == "__main__":
    print(solve())
