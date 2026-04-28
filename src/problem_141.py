# Problem 141: https://projecteuler.net/problem=141

from math import gcd, isqrt


def solve():
    lim = 10**12
    squares = set()

    for a in range(2, 10_000):
        a3 = a * a * a
        if a3 >= lim:
            break

        for b in range(1, a):
            if gcd(a, b) != 1:
                continue

            c = 1
            while True:
                n = c * c * a3 * b + c * b * b
                if n >= lim:
                    break

                s = isqrt(n)
                if s * s == n:
                    squares.add(n)
                c += 1

    return sum(squares)


if __name__ == "__main__":
    print(solve())
