# Problem 645: https://projecteuler.net/problem=645

from math import fsum


def solve(days=10000):
    harmonic = fsum(1 / k for k in range(1, days + 1))
    term = 1.0
    terms = [term]

    for k in range(1, days // 2):
        term *= (
            k
            * (days - 2 * k)
            * (days - 2 * k - 1)
            / ((k + 1) * (days - k) * (days - k - 1))
        )
        terms.append(term)

    return f"{days * (harmonic - fsum(terms)):.4f}"


if __name__ == "__main__":
    print(solve())
