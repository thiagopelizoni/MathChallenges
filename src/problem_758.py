# Problem 758: https://projecteuler.net/problem=758

from itertools import combinations

from sympy import primerange


def pourings(m, n, mod):
    x, y = 1, 1
    while m > 1:
        k, r = divmod(n, m)
        a = pow(2, m, mod) - 1
        z = pow(2, r, mod)
        if a:
            q = (pow(2, n, mod) - z) * pow(a, -1, mod) % mod
        else:
            q = k * z % mod
        x, y = y, (x + q * y) % mod
        n, m = m, r
    return (2 * y - 2) % mod


def solve():
    mod = 1_000_000_007
    exponents = [p**5 for p in primerange(1000)]
    total = 0
    for m, n in combinations(exponents, 2):
        total += pourings(m, n, mod)
    return total % mod


if __name__ == "__main__":
    print(solve())
