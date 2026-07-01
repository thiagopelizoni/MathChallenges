# Problem 351: https://projecteuler.net/problem=351

from sympy import sieve


N = 100_000_000


def hidden_points(n):
    visible = sum(sieve.totientrange(1, n + 1))
    total_on_sixth = n * (n + 1) // 2
    return 6 * (total_on_sixth - visible)


def solve():
    return hidden_points(N)


if __name__ == "__main__":
    print(solve())
