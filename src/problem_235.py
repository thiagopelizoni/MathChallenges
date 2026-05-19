# Problem 235: https://projecteuler.net/problem=235
from decimal import Decimal, ROUND_HALF_UP, getcontext


N = 5000
TARGET = Decimal("-600000000000")


def partial_sum(r):
    rn = r**N
    a = (rn - 1) / (r - 1)
    b = (1 - (N + 1) * rn + N * rn * r) / ((1 - r) ** 2)
    return Decimal(900) * a - Decimal(3) * b


def solve():
    getcontext().prec = 60
    lo = Decimal(1)
    hi = Decimal("1.01")

    for _ in range(160):
        mid = (lo + hi) / 2
        if partial_sum(mid) > TARGET:
            lo = mid
        else:
            hi = mid

    r = (lo + hi) / 2
    return str(r.quantize(Decimal("0.000000000001"), rounding=ROUND_HALF_UP))


if __name__ == "__main__":
    print(solve())
