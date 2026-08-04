# Problem 499: https://projecteuler.net/problem=499

from math import expm1, fsum

from scipy.optimize import brentq


FEE = 15
CAPITAL = 10**9


def equation(t, fee):
    power = 1.0
    weight = 0.5
    terms = []
    for _ in range(100):
        terms.append(weight * expm1(power * t))
        power *= 2.0
        weight *= 0.5
    return expm1(fee * t) - fsum(terms)


def survival_probability(fee, capital):
    high = -1e-12
    while equation(high, fee) <= 0:
        high *= 0.5
    low = 2 * high
    while equation(low, fee) > 0:
        low *= 2
    root = brentq(
        equation, low, high, args=(fee,), xtol=1e-20, rtol=1e-15
    )
    return -expm1(root * (capital - fee + 1))


def solve():
    return f"{survival_probability(FEE, CAPITAL):.7f}"


if __name__ == "__main__":
    print(solve())
