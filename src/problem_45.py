# Problem 45: https://projecteuler.net/problem=45
from math import isqrt

def is_pent(x):
    y = 24 * x + 1
    r = isqrt(y)
    return r * r == y and (r + 1) % 6 == 0

def solve():
    n = 144

    while True:
        h = n * (2 * n - 1)
        if is_pent(h):
            return h
        n += 1

if __name__ == "__main__":
    print(solve())