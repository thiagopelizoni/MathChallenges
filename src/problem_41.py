# Problem 41: https://projecteuler.net/problem=41
from gmpy2 import is_prime
from itertools import permutations

def solve():
    for p in permutations("7654321"):
        n = int("".join(p))
        if is_prime(n):
            return n

if __name__ == "__main__":
    print(solve())