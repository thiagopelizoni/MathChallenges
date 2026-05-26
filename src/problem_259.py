# Problem 259: https://projecteuler.net/problem=259
from math import gcd


DIGITS = "123456789"


def frac(n, d):
    if d < 0:
        n = -n
        d = -d
    if n == 0:
        return 0, 1
    g = gcd(abs(n), d)
    return n // g, d // g


def solve():
    dp = {}
    m = len(DIGITS)

    for length in range(1, m + 1):
        for i in range(m - length + 1):
            j = i + length
            s = {(int(DIGITS[i:j]), 1)}

            for k in range(i + 1, j):
                for an, ad in dp[i, k]:
                    for bn, bd in dp[k, j]:
                        s.add(frac(an * bd + bn * ad, ad * bd))
                        s.add(frac(an * bd - bn * ad, ad * bd))
                        s.add(frac(an * bn, ad * bd))
                        if bn:
                            s.add(frac(an * bd, ad * bn))

            dp[i, j] = s

    return sum(n for n, d in dp[0, m] if d == 1 and n > 0)


if __name__ == "__main__":
    print(solve())
