# Problem 503: https://projecteuler.net/problem=503

from decimal import Decimal, localcontext


N = 10**6


def expected_score(n):
    with localcontext() as context:
        context.prec = 40
        score = Decimal(n + 1) / 2
        for i in range(n - 1, 0, -1):
            cutoff = min(i, int(score * (i + 1) / (n + 1)))
            stopped = Decimal(n + 1) * cutoff * (cutoff + 1) / (2 * (i + 1))
            score = (stopped + (i - cutoff) * score) / i
        return +score


def solve():
    return f"{expected_score(N):.10f}"


if __name__ == "__main__":
    print(solve())
