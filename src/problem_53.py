# Problem 53: https://projecteuler.net/problem=53
from math import comb

def solve():
    lim = 10**6
    return sum(comb(n, r) > lim for n in range(1, 101) for r in range(n + 1))

if __name__ == "__main__":
    print(solve())