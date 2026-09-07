# Problem 598: https://projecteuler.net/problem=598

from collections import defaultdict
from fractions import Fraction
from math import factorial, gcd, prod

from sympy import factorint, primerange


def solve(n=factorial(100)):
    exponents = sorted(factorint(n).values(), reverse=True)
    dp = {Fraction(1): 1}
    for i, e in enumerate(exponents):
        next_e = exponents[i + 1] if i + 1 < len(exponents) else 0
        forbidden = prod(primerange(next_e + 2, e + 2))
        ratios = [Fraction(k + 1, e - k + 1) for k in range(e + 1)]
        new = defaultdict(int)
        for ratio, count in dp.items():
            for step in ratios:
                r = ratio * step
                if gcd(r.numerator * r.denominator, forbidden) == 1:
                    new[r] += count
        dp = new

    diagonal = all(e % 2 == 0 for e in exponents)
    return (dp.get(1, 0) + diagonal) // 2


if __name__ == "__main__":
    print(solve())
