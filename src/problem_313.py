# Problem 313: https://projecteuler.net/problem=313

from sympy import primerange


N = 1_000_000


def count_for_prime(p):
    t = (p * p + 13) // 2
    return 2 * ((t - 2) // 3 - t // 4)


def solve():
    return sum(count_for_prime(p) for p in primerange(2, N))


if __name__ == "__main__":
    print(solve())
