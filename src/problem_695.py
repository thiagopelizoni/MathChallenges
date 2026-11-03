# Problem 695: https://projecteuler.net/problem=695

from sympy import Rational, integrate, sqrt, symbols


def solve():
    u = symbols("u", positive=True)
    r = (3 - sqrt(5)) / 2
    f = (1 - 2 * u) / (1 - u)
    g = (1 - u) / (2 - u)

    a = u * f + (1 - u) * (g - f - (g**2 - f**2) / 2)
    a += (u**2 - g**2) / 2
    b = (1 - u) * (g - g**2 / 2) + (u**2 - g**2) / 2

    median = 2 * (
        r**3 / 3
        + integrate(a, (u, r, Rational(1, 2)))
        + integrate(b, (u, Rational(1, 2), 1))
    )
    mean = (Rational(5, 12) + 2 * median) / 12
    return f"{mean.evalf(20):.10f}"


if __name__ == "__main__":
    print(solve())
