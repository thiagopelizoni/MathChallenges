# Problem 622: https://projecteuler.net/problem=622

from sympy import divisors, n_order


def solve():
    shuffles = 60
    total = 0
    for d in divisors(2**shuffles - 1):
        if d > 1 and n_order(2, d) == shuffles:
            total += d + 1
    return total


if __name__ == "__main__":
    print(solve())
