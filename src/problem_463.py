# Problem 463: https://projecteuler.net/problem=463

from functools import cache


N = 3**37
MODULUS = 10**9


@cache
def f(n):
    if n == 1:
        return 1
    if n == 3:
        return 3

    q, r = divmod(n, 2)
    if r == 0:
        return f(q)

    q, r = divmod(n, 4)
    if r == 1:
        return (2 * f(2 * q + 1) - f(q)) % MODULUS
    return (3 * f(2 * q + 1) - 2 * f(q)) % MODULUS


@cache
def odd_sum(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    q, r = divmod(n, 2)
    result = 5 * odd_sum(q) - 3 * summatory(q - 1) - 1
    if r:
        result += 2 * f(2 * q + 1) - f(q)
    return result % MODULUS


@cache
def summatory(n):
    if n == 0:
        return 0

    q, r = divmod(n, 2)
    result = summatory(q) + odd_sum(q)
    if r:
        result += f(n)
    return result % MODULUS


def solve():
    return summatory(N)


if __name__ == "__main__":
    print(solve())
