# Problem 634: https://projecteuler.net/problem=634

from math import isqrt

from sympy import integer_nthroot, primepi, sieve


def solve(n=9 * 10**18):
    lim = integer_nthroot(n // 4, 3)[0]
    total = 0
    for b, mu in enumerate(sieve.mobiusrange(2, lim + 1), 2):
        if mu:
            total += isqrt(n // b**3) - 1

    root = isqrt(n)
    lim = integer_nthroot(root, 3)[0]
    cube_free = sum(
        mu * (root // d**3)
        for d, mu in enumerate(sieve.mobiusrange(1, lim + 1), 1)
    )
    return total + root - cube_free - int(primepi(lim))


if __name__ == "__main__":
    print(solve())
