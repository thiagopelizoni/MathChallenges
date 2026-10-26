# Problem 687: https://projecteuler.net/problem=687
from math import comb, factorial

from sympy import Poly, Rational, isprime, symbols


def solve():
    ranks, suits = 13, 4
    n = ranks * suits
    x = symbols("x")
    f = Poly(0, x)
    for b in range(1, suits + 1):
        f += Poly((-1) ** (suits - b) * comb(suits - 1, b - 1) * Rational(1, factorial(b)) * x**b, x)

    total = Rational(factorial(n), factorial(suits) ** ranks)
    p = []
    for t in range(ranks + 1):
        rest = n - suits * t
        cnt = 0
        for (k,), c in (f**t).terms():
            cnt += c * factorial(k + rest)
        p.append(cnt / factorial(suits) ** (ranks - t) / total)

    assert ranks * p[1] == Rational(4324, 425)

    ans = 0
    for m in range(ranks + 1):
        if isprime(m):
            for j in range(ranks - m + 1):
                ans += comb(ranks, m) * (-1) ** j * comb(ranks - m, j) * p[m + j]
    return f"{float(ans):.10f}"


if __name__ == "__main__":
    print(solve())
