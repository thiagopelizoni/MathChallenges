# Problem 249: https://projecteuler.net/problem=249
import numpy as np
from sympy import primerange


MOD = 10**16
LIMIT = 5000


def solve():
    primes = list(primerange(LIMIT))
    total = sum(primes)
    dp = np.zeros(total + 1, dtype=np.uint64)
    dp[0] = 1

    s = 0
    for p in primes:
        dp[p : s + p + 1] = (dp[p : s + p + 1] + dp[: s + 1]) % MOD
        s += p

    return sum(int(dp[p]) for p in primerange(total + 1)) % MOD


if __name__ == "__main__":
    print(solve())
