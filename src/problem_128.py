# Problem 128: https://projecteuler.net/problem=128

from itertools import count

from sympy import isprime


def solve():
    vals = [1]

    for r in count(1):
        if isprime(6 * r - 1) and isprime(6 * r + 1) and isprime(12 * r + 5):
            vals.append(3 * r * (r - 1) + 2)
            if len(vals) == 2000:
                return vals[-1]

        if (
            r > 1
            and isprime(6 * r - 1)
            and isprime(6 * r + 5)
            and isprime(12 * r - 7)
        ):
            vals.append(3 * r * (r + 1) + 1)
            if len(vals) == 2000:
                return vals[-1]


if __name__ == "__main__":
    print(solve())
