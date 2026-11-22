# Problem 783: https://projecteuler.net/problem=783

from decimal import ROUND_CEILING, ROUND_FLOOR, Context, Decimal, localcontext


def expectation(n, k):
    r = 2 * k
    drawn_pairs = r * (r - 1)
    added_pairs = k * (k - 1)
    black = Decimal(k)
    pairs = Decimal(added_pairs)
    total = Decimal(n * k)

    for size in range(k * (n + 1), k, -k):
        size_pairs = size * (size - 1)
        total += pairs * drawn_pairs / size_pairs

        left = size - r
        black = black * left / size
        pairs = pairs * (left * (left - 1)) / size_pairs + r * black + added_pairs
        black += k

    return total


def solve():
    n, k = 10**6, 10
    with localcontext(Context(rounding=ROUND_FLOOR)):
        lo = round(expectation(n, k))
    with localcontext(Context(rounding=ROUND_CEILING)):
        hi = round(expectation(n, k))
    assert lo == hi
    return lo


if __name__ == "__main__":
    print(solve())
