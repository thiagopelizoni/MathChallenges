# Problem 371: https://projecteuler.net/problem=371

from decimal import Decimal, getcontext


PAIRS = 499
TOTAL = Decimal(1000)


def expected_plates():
    getcontext().prec = 50
    with_500 = [Decimal(0)] * (PAIRS + 1)
    without_500 = [Decimal(0)] * (PAIRS + 1)

    for a in range(PAIRS, -1, -1):
        den = TOTAL - a - 1
        new = 2 * (PAIRS - a)
        if a < PAIRS:
            with_500[a] = (TOTAL + new * with_500[a + 1]) / den
            without_500[a] = (TOTAL + new * without_500[a + 1] + with_500[a]) / den
        else:
            with_500[a] = TOTAL / den
            without_500[a] = (TOTAL + with_500[a]) / den

    return without_500[0]


def solve():
    return f"{expected_plates():.8f}"


if __name__ == "__main__":
    print(solve())
