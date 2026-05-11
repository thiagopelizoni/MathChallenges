# Problem 194: https://projecteuler.net/problem=194
from math import comb


def solve():
    a, b, c = 25, 75, 1984
    mod = 100_000_000

    na = c**5 - 9 * c**4 + 34 * c**3 - 69 * c**2 + 77 * c - 38
    nb = (c - 2) ** 3 * (c * c - 2 * c + 3)

    return (
        comb(a + b, a)
        * c
        * (c - 1)
        * pow(na, a, mod)
        * pow(nb, b, mod)
        % mod
    )


if __name__ == "__main__":
    print(solve())
