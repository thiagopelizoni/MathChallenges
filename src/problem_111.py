# Problem 111: https://projecteuler.net/problem=111

from itertools import combinations, product

from sympy import isprime


N = 10
DIGITS = "0123456789"


def sum_primes(d, k):
    repeated = str(d)
    choices = [c for c in DIGITS if c != repeated]
    total = 0

    for positions in combinations(range(N), k):
        for repl in product(choices, repeat=k):
            digits = [repeated] * N
            for i, c in zip(positions, repl):
                digits[i] = c
            if digits[0] != "0" and digits[-1] in "1379":
                n = int("".join(digits))
                if isprime(n):
                    total += n

    return total


def solve():
    ans = 0
    for d in range(10):
        for k in range(1, N + 1):
            s = sum_primes(d, k)
            if s:
                ans += s
                break
    return ans


if __name__ == "__main__":
    print(solve())
