# Problem 329: https://projecteuler.net/problem=329

from fractions import Fraction


SQUARES = 500
PATTERN = "PPPPNNPPPNPPNPN"


def prime_sieve(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for p in range(2, int(n**0.5) + 1):
        if prime[p]:
            prime[p * p : n + 1 : p] = [False] * (((n - p * p) // p) + 1)

    return prime


def solve():
    prime = prime_sieve(SQUARES)
    dp = [Fraction(0) for _ in range(SQUARES + 1)]

    for i in range(1, SQUARES + 1):
        dp[i] = Fraction(1, SQUARES)

    for j, ch in enumerate(PATTERN):
        for i in range(1, SQUARES + 1):
            ok = (ch == "P") == prime[i]
            dp[i] *= Fraction(2 if ok else 1, 3)

        if j + 1 == len(PATTERN):
            break

        ndp = [Fraction(0) for _ in range(SQUARES + 1)]
        ndp[2] += dp[1]
        ndp[SQUARES - 1] += dp[SQUARES]

        for i in range(2, SQUARES):
            ndp[i - 1] += dp[i] / 2
            ndp[i + 1] += dp[i] / 2

        dp = ndp

    ans = sum(dp)
    return f"{ans.numerator}/{ans.denominator}"


if __name__ == "__main__":
    print(solve())
