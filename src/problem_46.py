# Problem 46: https://projecteuler.net/problem=46
from gmpy2 import is_prime
from math import isqrt

def solve():
    primes = [2, 3]
    n = 5

    while True:
        if is_prime(n):
            primes.append(n)
            n += 2
            continue

        ok = False
        for p in primes:
            if p >= n:
                break
            d = n - p
            if d % 2 == 0:
                r = isqrt(d // 2)
                if 2 * r * r == d:
                    ok = True
                    break

        if not ok:
            return n

        n += 2

if __name__ == "__main__":
    print(solve())