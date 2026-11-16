# Problem 756: https://projecteuler.net/problem=756
from decimal import Decimal, localcontext

from sympy import sieve


def solve():
    n, m = 12345678, 12345
    places = 6
    with localcontext() as ctx:
        ctx.prec = 4 * len(str(n)) + 2 * places
        eps = Decimal(10) ** (-2 * places)
        w = Decimal(1)
        weights = []
        k = 0
        while n * n * w >= eps:
            k += 1
            w = w * (n - m - k + 1) / (n - k + 1)
            weights.append(w)

        total = sum(w * int(phi) for w, phi in
                    zip(weights, sieve.totientrange(1, k + 1)))
        lo = f"{total - 2 * eps:.{places}f}"
        hi = f"{total + 2 * eps:.{places}f}"
        assert lo == hi
        return lo


if __name__ == "__main__":
    print(solve())
