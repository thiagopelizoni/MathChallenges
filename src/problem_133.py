# Problem 133: https://projecteuler.net/problem=133

from sympy import n_order, primerange


def never_divides(p):
    if p in (2, 3, 5):
        return True

    order = n_order(10, p)
    while order % 2 == 0:
        order //= 2
    while order % 5 == 0:
        order //= 5

    return order != 1


def solve():
    return sum(p for p in primerange(2, 100_000) if never_divides(p))


if __name__ == "__main__":
    print(solve())
