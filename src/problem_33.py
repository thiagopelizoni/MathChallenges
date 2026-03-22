# Problem 33: https://projecteuler.net/problem=33
from math import gcd

def solve():
    num = 1
    den = 1

    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                n = 10 * a + b
                d = 10 * b + c
                if n >= d:
                    continue
                if n * c == d * a:
                    num *= n
                    den *= d

    return den // gcd(num, den)

if __name__ == "__main__":
    print(solve())