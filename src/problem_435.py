# Problem 435: https://projecteuler.net/problem=435

from sympy.polys.domains import ZZ
from sympy.polys.galoistools import gf_pow_mod


MOD = 1_307_674_368_000


def polynomial_value(n, x):
    if x == 0:
        return 0
    d = x * x + x - 1
    modulus = MOD * d
    fn, previous = map(
        int, gf_pow_mod([1, 0], n, [1, -1, -1], modulus, ZZ)
    )
    next_fn = (fn + previous) % modulus
    numerator = (
        next_fn * pow(x, n + 1, modulus)
        + fn * pow(x, n + 2, modulus)
        - x
    ) % modulus
    return numerator // d


def solve():
    n = 10**15
    return sum(polynomial_value(n, x) for x in range(101)) % MOD


if __name__ == "__main__":
    print(solve())
