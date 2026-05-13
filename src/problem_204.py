# Problem 204: https://projecteuler.net/problem=204
from sympy import primerange


def count(limit, kind):
    primes = list(primerange(2, kind + 1))

    def dfs(i, n):
        if i == len(primes):
            return 1

        total = 0
        p = primes[i]
        while n <= limit:
            total += dfs(i + 1, n)
            n *= p
        return total

    return dfs(0, 1)


def solve():
    return count(1_000_000_000, 100)


if __name__ == "__main__":
    print(solve())
