# Problem 722: https://projecteuler.net/problem=722

from decimal import Decimal

from sympy import Rational, factorial, log, zeta


def solve():
    k = 15
    places = 12
    q = 1 - Rational(1, 2**25)
    t = -log(q)
    value = factorial(k) * zeta(k + 1) / t ** (k + 1)
    value = Decimal(str(value.evalf(2 * (places + 1))))
    return f"{value:.{places}e}".replace("e+", "e")


if __name__ == "__main__":
    print(solve())
