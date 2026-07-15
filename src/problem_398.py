# Problem 398: https://projecteuler.net/problem=398

from decimal import Decimal, localcontext
from math import comb


def solve():
    n = 10**7
    m = 100
    r = m - 1
    total = comb(n - 1, r)

    numerator = m * sum(
        comb(n - r * k + r - 1, r) for k in range(1, (n - 1) // r + 1)
    )
    numerator -= r * sum(
        comb(n - m * k + r, r) for k in range(1, n // m + 1)
    )

    with localcontext() as ctx:
        ctx.prec = 20
        return f"{Decimal(numerator) / Decimal(total):.5f}"


if __name__ == "__main__":
    print(solve())
