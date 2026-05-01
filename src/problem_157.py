# Problem 157: https://projecteuler.net/problem=157

from math import gcd

from sympy import divisor_count


def solutions(n):
    total = 0
    seen = set()

    for i in range(n + 1):
        for j in range(n + 1):
            x = 2**i * 5**j
            for k in range(n + 1):
                for l in range(n + 1):
                    y = 2**k * 5**l
                    g = gcd(x, y)
                    a, b = x // g, y // g
                    if a > b:
                        a, b = b, a
                    if (a, b) in seen:
                        continue

                    seen.add((a, b))
                    total += divisor_count((a + b) * 10**n // (a * b))

    return total


def solve():
    return sum(solutions(n) for n in range(1, 10))


if __name__ == "__main__":
    print(solve())
