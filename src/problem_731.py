# Problem 731: https://projecteuler.net/problem=731

from fractions import Fraction


def solve(n=10**16):
    digits = 10
    m = n + digits - 1
    mod = 10**digits
    total = Fraction(0)
    q = 3
    while q <= m:
        total += Fraction(pow(10, m - q, q * mod), q)
        q *= 3
    ans = total.numerator // total.denominator % mod
    return f"{ans:0{digits}d}"


if __name__ == "__main__":
    print(solve())
