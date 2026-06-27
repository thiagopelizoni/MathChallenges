# Problem 339: https://projecteuler.net/problem=339

from math import exp, lgamma, log


N = 10_000


def central_binomial_probability(n):
    return exp(lgamma(2 * n - 1) - 2 * lgamma(n) - (2 * n - 2) * log(2))


def expected(n):
    a = 1.0
    if n == 1:
        return a

    for k in range(2, n + 1):
        prev = a
        c = central_binomial_probability(k)
        a = prev + (2 * k - 1 - prev) * (2 * c / (1 + c))

    c = central_binomial_probability(n)
    return (prev + a + (2 * n - a) * ((2 * n - 1) * c / n)) / 2


def solve():
    return f"{expected(N):.6f}"


if __name__ == "__main__":
    print(solve())
