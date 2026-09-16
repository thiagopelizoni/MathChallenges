# Problem 618: https://projecteuler.net/problem=618

import numpy as np
from sympy import primerange


def prime_sums(n, mod):
    dp = np.zeros(n + 1, dtype=np.int64)
    dp[0] = 1
    for p in primerange(2, n + 1):
        step = p
        weight = p
        while step <= n:
            dp[step:] = (dp[step:] + weight * dp[:-step]) % mod
            step *= 2
            weight = weight * weight % mod
    return dp


def solve():
    fib = [1, 1]
    while len(fib) < 24:
        fib.append(fib[-1] + fib[-2])
    mod = 10**9
    dp = prime_sums(fib[-1], mod)
    return f"{sum(int(dp[n]) for n in fib[1:]) % mod:09d}"


if __name__ == "__main__":
    print(solve())
