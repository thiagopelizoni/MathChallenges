# Problem 307: https://projecteuler.net/problem=307

from decimal import Decimal, getcontext


K = 20_000
N = 1_000_000
ROUND = Decimal("0.0000000001")


def no_triple(k, n):
    nd = Decimal(n)
    term = Decimal(1)

    for i in range(k):
        term *= Decimal(n - i) / nd

    total = term
    for j in range(k // 2):
        num = (k - 2 * j) * (k - 2 * j - 1)
        den = 2 * (j + 1) * (n - k + j + 1)
        term *= Decimal(num) / Decimal(den)
        total += term

    return total


def solve():
    getcontext().prec = 50
    return f"{(Decimal(1) - no_triple(K, N)).quantize(ROUND)}"


if __name__ == "__main__":
    print(solve())
