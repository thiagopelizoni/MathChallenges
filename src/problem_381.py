# Problem 381: https://projecteuler.net/problem=381

from sympy import primerange


def solve(limit=10**8):
    return sum(
        (p * ((3 * p) % 8) - 3) // 8
        for p in primerange(5, limit)
    )


if __name__ == "__main__":
    print(solve())
