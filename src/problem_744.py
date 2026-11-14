# Problem 744: https://projecteuler.net/problem=744

from decimal import Decimal


def solve():
    n = 10**11
    p = Decimal("0.4999")
    q = 1 - p
    ans = 1 - Decimal(n) / (q * (2 * n + 1))
    return f"{ans:.10f}"


if __name__ == "__main__":
    print(solve())
