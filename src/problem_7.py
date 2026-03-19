# Problem 7: https://projecteuler.net/problem=7
from gmpy2 import next_prime


def solve():
    p = 1
    for _ in range(10_001):
        p = next_prime(p)
    return int(p)


if __name__ == "__main__":
    print(solve())