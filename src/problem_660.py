# Problem 660: https://projecteuler.net/problem=660

from itertools import chain
from math import gcd, isqrt


def pandigital(a, b, c, base):
    seen = [False] * base
    for value in (a, b, c):
        while value:
            value, digit = divmod(value, base)
            if seen[digit]:
                return False
            seen[digit] = True
    return all(seen)


def triangles(base):
    powers = [base**i for i in range(base + 1)]
    target = base * (base - 1) // 2

    for x in range(1, base // 3 + 1):
        for y in range(x, (base - x) // 2 + 1):
            z = base - x - y
            if z > y + 1:
                continue
            a_max, b_max, c_max = powers[x] - 1, powers[y] - 1, powers[z] - 1
            bound = min((a_max + 1) // 2, isqrt(2 * b_max), isqrt(c_max))

            for m in range(2, bound + 1):
                square = m * m
                low = 1 if square <= b_max else isqrt(square - b_max - 1) + 1
                high = min(m - 1, isqrt(square + b_max) - m)
                high = min(high, (isqrt(4 * c_max - 3 * square) - m) // 2)
                left = min(high, isqrt(square + a_max) - m)
                right = 1 if square <= a_max else isqrt(square - a_max - 1) + 1
                right = max(low, left + 1, right)

                for r in chain(range(low, left + 1), range(right, high + 1)):
                    if (m - r) % 3 == 0 or gcd(m, r) != 1:
                        continue
                    a, b = sorted((square - r * r, 2 * m * r + r * r))
                    c = square + m * r + r * r
                    first = max((powers[x - 1] + a - 1) // a,
                                (powers[y - 1] + b - 1) // b,
                                (powers[z - 1] + c - 1) // c)
                    last = min(a_max // a, b_max // b, c_max // c)
                    if first > last:
                        continue
                    perimeter = a + b + c
                    g = gcd(perimeter, base - 1)
                    if target % g:
                        continue
                    step = (base - 1) // g
                    residue = target // g * pow(perimeter // g, -1, step) % step
                    first += (residue - first) % step

                    for scale in range(first, last + 1, step):
                        aa, bb, cc = scale * a, scale * b, scale * c
                        if pandigital(aa, bb, cc, base):
                            yield aa, bb, cc


def solve():
    return sum(c for base in range(9, 19) for a, b, c in triangles(base))


if __name__ == "__main__":
    print(solve())
