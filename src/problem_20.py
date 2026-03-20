# Problem 20: https://projecteuler.net/problem=20
from math import factorial

def solve():
    return sum(map(int, str(factorial(100))))

if __name__ == "__main__":
    print(solve())