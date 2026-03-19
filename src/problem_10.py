# Problem 10: https://projecteuler.net/problem=10
from sympy import primerange

def solve():
    return sum(primerange(2, 2_000_000))

if __name__ == "__main__":
    print(solve())