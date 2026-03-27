# Problem 58: https://projecteuler.net/problem=58
from sympy import isprime

def solve():
    primes = 0
    total = 1
    side = 1
    while True:
        side += 2
        step = side - 1
        sq = side * side
        primes += isprime(sq - step)
        primes += isprime(sq - 2 * step)
        primes += isprime(sq - 3 * step)
        total += 4
        if primes * 10 < total:
            return side

if __name__ == "__main__":
    print(solve())
