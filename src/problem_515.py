# Problem 515: https://projecteuler.net/problem=515

from sympy import primerange

A = 10**9
B = 10**5
K = 10**5


def solve():
    return sum(pow(K - 1, -1, p) for p in primerange(A, A + B))


if __name__ == "__main__":
    print(solve())
