# Problem 77: https://projecteuler.net/problem=77

import gmpy2

def solve():
    limit = 200
    primes = [p for p in range(2, limit + 1) if gmpy2.is_prime(p)]

    ways = [1] + [0] * limit
    for p in primes:
        for i in range(p, limit + 1):
            ways[i] += ways[i - p]

    for i in range(2, limit + 1):
        if ways[i] > 5000:
            return i

if __name__ == "__main__":
    print(solve())
